from typing import *
from django import forms

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models.query_utils import Q
from django.utils.translation import pgettext_lazy

from wcd_envoyer.channels.backend import BaseMessagingBackend
from wcd_envoyer.channels.forms import BaseTemplateForm
from wcd_envoyer.utils import importable_prop


__all__ = 'EmailTemplateForm', 'EmailBackend',


class EmailTemplateForm(BaseTemplateForm):
    renderable_fields = ['subject', 'content', 'plain_text']

    class Meta(BaseTemplateForm.Meta):
        entangled_fields = {'data': ['subject', 'content', 'plain_text']}

    subject = forms.CharField(
        label=pgettext_lazy('wcd_envoyer', 'Subject'),
    )
    content = forms.CharField(
        label=pgettext_lazy('wcd_envoyer', 'Content'),
        widget=forms.Textarea(),
    )
    plain_text = forms.CharField(
        label=pgettext_lazy('wcd_envoyer', 'Plain text'),
        widget=forms.Textarea(),
        initial='', required=False,
    )


class EmailBackend(BaseMessagingBackend):
    recipient_resolver = importable_prop(lambda x: x.get('email'))
    template_form_class = importable_prop(EmailTemplateForm)

    def get_default_sender(self):
        if 'des' in settings.INSTALLED_APPS:
            from des.models import DynamicEmailConfiguration
            return DynamicEmailConfiguration.get_solo().from_email

        return settings.DEFAULT_FROM_EMAIL

    # def send(self, *, letter: Letter) -> bool:
    #     data = letter.data
    #     message = EmailMultiAlternatives(
    #         subject=data.get('subject'),
    #         body=data.get('plain_text'),
    #         from_email=data.get('sender'),
    #         to=[
    #             item['email']
    #             for item in data.get('recipients', [])
    #             if 'email' in item
    #         ],
    #     )
    #     message.attach_alternative(data.get('content'), "text/html")
    #     message.send()
    #     return True
