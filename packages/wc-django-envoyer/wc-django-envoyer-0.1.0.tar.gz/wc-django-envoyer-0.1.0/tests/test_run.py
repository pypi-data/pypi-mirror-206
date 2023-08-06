import pytest

from wcd_envoyer.models import (
    Template, ChannelConfig, TemplateTranslation, Message
)
from wcd_envoyer.shortcuts import send

from .const import CONSOLE_CHANNEL


@pytest.mark.django_db
def test_simple_sender(django_assert_num_queries):
    event = 'unexisting_event'
    template = Template.objects.create(
        channel=CONSOLE_CHANNEL,
        event=event,
        data={
            'content': 'Hi {{username}} {{channel}} {{subject}}!',
            'subject': 'Some',
        },
        is_active=True,
    )
    translation = TemplateTranslation.objects.create(
        entity=template,
        language='ja',
        data={
            'content': '[ja] Hi {{username}} {{channel}} {{subject}}!',
            'subject': '[ja] Some',
        },
    )
    config = ChannelConfig.objects.create(channel=CONSOLE_CHANNEL)

    with django_assert_num_queries(6):
        send(
            event,
            [{'user_id': 1}, {'user_id': 2}],
            {'username': 'Named', 'language': 'ja'},
        )

    assert Message.objects.all().count() == 2
    assert Message.objects.filter(status=Message.Status.SENT).count() == 2


@pytest.mark.django_db
def test_inactive_template(django_assert_num_queries):
    event = 'unexisting_event'
    template = Template.objects.create(
        channel=CONSOLE_CHANNEL, event=event, data={}, is_active=False,
    )
    config = ChannelConfig.objects.create(channel=CONSOLE_CHANNEL)

    with django_assert_num_queries(2):
        send(
            event,
            [{'user_id': 1}, {'user_id': 2}],
            {'username': 'Named'},
        )

    assert Message.objects.all().count() == 0
