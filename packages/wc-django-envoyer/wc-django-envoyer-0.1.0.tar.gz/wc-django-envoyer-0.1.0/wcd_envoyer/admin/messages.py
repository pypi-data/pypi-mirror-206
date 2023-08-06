from django.contrib import admin

from wcd_envoyer.models import Message

from .utils import JsonDataAdminMixin


@admin.register(Message)
class MessageAdmin(JsonDataAdminMixin, admin.ModelAdmin):
    # actions = 'resend',
    list_display = 'channel', 'event', 'status', 'created_at', 'updated_at',
    list_filter = 'channel', 'event', 'status',
    readonly_fields = 'json_data', 'created_at', 'updated_at',
    date_hierarchy = 'created_at'

    # def resend(self, request, qs):
    #     result = sender_service.resend(letters=qs)
    #     if result['sent_count']:
    #         self.message_user(
    #             request=request,
    #             message=(
    #                 pgettext_lazy(
    #                     'wcd_envour',
    #                     'Successuly resent {} letters.'
    #                 )
    #                 .format(result['sent_count'])
    #             ),
    #             level=message_const.SUCCESS
    #         )
    #     if result['error_ids']:
    #         self.message_user(
    #             request=request,
    #             message=(
    #                 pgettext_lazy(
    #                     'wcd_envour',
    #                     'Failed reseding {} letters with id: {}.'
    #                 )
    #                 .format(
    #                     len(result['error_ids']),
    #                     ', '.join([str(pk) for pk in result['error_ids']])
    #                 )
    #             ),
    #             level=message_const.ERROR
    #         )
    # resend.short_description = pgettext_lazy('wcd_envour', 'Resend letters')
