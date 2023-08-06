import json
from collections import OrderedDict

from i18nfield.fields import I18nFormField, I18nTextarea
from i18nfield.strings import LazyI18nString

from pretix.base.models import OrderPayment
from pretix.base.payment import BasePaymentProvider, PaymentException
from pretix.base.templatetags.rich_text import rich_text
from django.utils.translation import ugettext_lazy as _
from django.template.loader import get_template
from django import forms

from paymentsds.mpesa import Client
from random import randint

class MpesaPayment(BasePaymentProvider):
    identifier = 'mpesa'

    ########################################################
    #                   General Settings
    ########################################################
    @property
    def verbose_name(self):
        return str(self.settings.get('method_name', as_type=LazyI18nString) or _('M-Pesa'))

    @property
    def confirm_button_name(self):
        return _('Pagar via M-Pesa')
    
    @property
    def priority(self):
        return 100
    
    ########################################################
    #                Control Panel Settings
    ########################################################
    @property
    def information_text(self):
        return rich_text(self.settings.get('information_text', as_type=LazyI18nString))

    @property
    def payment_pending_text(self):
        return rich_text(self.settings.get('payment_pending_text', as_type=LazyI18nString))

    @property
    def payment_completed_text(self):
        return rich_text(self.settings.get('payment_completed_text', as_type=LazyI18nString))

    @property
    def settings_form_fields(self):
        service_provider_code_field = forms.CharField(
            label = _('Código de Provedor de Serviço M-Pesa'),
            help_text=_('Identificador da entidade fornecido pelo M-Pesa')
        )

        api_key_field = forms.CharField(
            label = _('API Key'),
            help_text=_('API Key fornecido pelo M-Pesa')
        )

        public_key_field = forms.CharField(
            label = _('Public Key'),
            help_text=_('Public Key fornecido pelo M-Pesa')
        )

        info_field = I18nFormField(
            label = _('Payment information text'),
            help_text=_('Shown to the user when selecting a payment method.'),
            widget = I18nTextarea,
        )
        pending_field = I18nFormField(
            label = _('Payment pending text'),
            help_text = _('Shown to the user when viewing a pending payment order.'),
            widget = I18nTextarea,
        )
        completed_field = I18nFormField(
            label = _('Payment completed text'),
            help_text = _('Shown to the user when viewing an order with completed payment.'),
            widget = I18nTextarea,
        )

        settingsList = [
                ('service_provider_code', service_provider_code_field),
                ('api_key', api_key_field),
                ('public_key', public_key_field),
                ('information_text', info_field),
                ('payment_pending_text', pending_field),
                ('payment_completed_text', completed_field)
        ]

        return OrderedDict(list(super().settings_form_fields.items()) + settingsList)

    ########################################################
    #               Checkout process settings
    ########################################################
    def payment_is_valid_session(self, request):
        return all([
            request.session.get('payment_%s_msisdn' % self.identifier, '') != ''
        ])
    
    def order_change_allowed(self, order):
        return True

    
    ########################################################
    #                   General Settings
    ########################################################
    @property
    def payment_form_fields(self):
        # Validate: ensure only valid numbers can be entered
        msisdn_field = ('msisdn',
            forms.CharField(
            label='Número 84/85',
            required=True,
            max_length=9
        ))
        return OrderedDict([
            msisdn_field,
        ])
    
    def payment_form_render(self, request):
        form = self.payment_form(request)
        template = get_template('pretix_mpesamz/checkout_payment_form.html')
        ctx = {
                'request': request, 
                'form': form,
                'information_text': self.information_text,
        }
        return template.render(ctx)
    
    def checkout_confirm_render(self, request):
        template = get_template('pretix_mpesamz/order.html')
        ctx = {
            'information_text': self.information_text,
            'msisdn': request.session.get('payment_%s_msisdn' % self.identifier)
        }
        return template.render(ctx)

    def execute_mpesa_payment(self, payload):
        client = Client(
            api_key = self.settings.get('api_key'),          
            public_key=self.settings.get('public_key'),
            service_provider_code=self.settings.get('service_provider_code')
        )
     
        return client.receive(payload)

        
    def execute_payment(self, request, payment):
        msisdn = request.session.get('payment_%s_msisdn' % self.identifier, '')

        try:
            payment_data = {
                'from': "258" + msisdn,   
                'reference': payment.order.code,      
                'transaction': 'TEST' + str(randint(0, 1000)), 
                'amount': str(int(float(payment.amount)))
            }

            result = self.execute_mpesa_payment(payment_data)

            if result.success:
                success_payload = json.dumps({
                    'code': result.status.code,
                    'msisdn': msisdn,
                    'conversation': result.data['conversation'],
                    'description': result.status.description
                })
                # Displayed in control panel but not on API order response
                payment.info = success_payload

                # Add success payload to a field returned on Order Endpoint
                payment.order.meta_info = success_payload
                payment.order.save(update_fields=['meta_info'])

                payment.save(update_fields=['info'])
                payment.confirm()
            else:
                payment.fail()
            
            return 
        except Exception as e:
            print(repr(e))
    
    def payment_pending_render(self, request, payment) -> str:
        template = get_template('pretix_mpesamz/order.html')
        if payment.info:
            payment_info = json.loads(payment.info)
        else:
            return _("No payment information available.")
        ctx = {
            'information_text': self.payment_pending_text,
            'msisdn': request.session.get('payment_%s_msisdn' % self.identifier, '')
        }
        return template.render(ctx)

    def order_completed_render(self, request, order) -> str:
        template = get_template('pretix_mpesamz/order.html')
        if order.payment_info:
            payment_info = json.loads(order.payment_info)
        else:
            return _("No payment information available.")
        ctx = {
            'information_text': self.payment_completed_text,
            'msisdn': self.msisdn
        }
        return template.render(ctx)

    ########################################################
    #                   Called to display Order 
    #                   info in Control Panel
    ########################################################
    def payment_control_render(self, request, payment) -> str:
        template = get_template('pretix_mpesamz/control.html')
        if payment.info:
            payment_info = json.loads(payment.info)
        else:
            return _("No payment information available.")
        
        ctx = {
            'conversationID': payment_info['conversation'],
            'msisdn': payment_info['msisdn'],
            'description': payment_info['description'],
        }
        return template.render(ctx)