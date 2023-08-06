# WebCase message sender

Message sender to different channels.

## Installation

```sh
pip install wc-django-envoyer
```

In `settings.py`:

```python
INSTALLED_APPS += [
  'wcd_envoyer',
]

WCD_ENVOYER = {
  # Channels list, that will be available in admin interface to message
  # create templates.
  'CHANNELS': [
    {
      # Unique channel key.
      'key': 'console',
      'verbose_name': 'Console',
      # Messaging backend class.
      # Console backend here is a simple message printing backend:
      'backend': 'wcd_envoyer.channels.backends.console.ConsoleBackend',
      'options': {
        # Options that backend receives on initialization.
        # Basic ones are:
        # Actual recipients data resolver for a specific case:
        'recipient_resolver': lambda x: x,
        # Form for additional in-admin backend configuration options.
        'config_form_class': 'wcd_envoyer.channels.forms.BaseConfigForm',
        # In-admin form for template config.
        'template_form_class': 'wcd_envoyer.channels.forms.BaseTemplateForm',
        # Custom string template renderer.
        'template_renderer': 'wcd_envoyer.channels.renderers.django_template_renderer',
        # Separate class that is responsible for messages data transformations.
        'messages_maker_class': 'wcd_envoyer.channels.backend.MessagesMaker',
      }
    },
  ],
  'EVENTS': [
    {
      # Unique event key.
      'key': 'something-happened',
      # Event's verbose name that will be displayed in admin.
      'verbose_name': 'Something happened event',
      # List of variables available on template generation.
      'context': [
        (
          # Key
          'when',
          # Verbose name.
          'When',
          # Additional variable description
          'Time when something happened.'
        ),
        # Variable can be defined as a simple string key:
        'what',
        # Or this could be tuple with only 2 parameters
        ('other', 'Other'),
      ],
  }
  ],
  # JSON encoder class for in-lib postgres json fields:
  'JSON_ENCODER': 'django.core.serializers.json.DjangoJSONEncoder',
}
```

Events and Channels can be registered in special auto-importable `envoyer.py` app submodule.

`envoyer.py`
```python
from django.utils.translation import pgettext_lazy

from wcd_envoyer import events, channels


# Events is better to register here. Because it's more related to
# particular app, not project itself.
events.registry.add({
  'key': 'app-event',
  'verbose_name': 'App event',
  'context': ['var1', 'var2'],
})

# But channels is other case. Better describe them in `settings.py`
channels.registry.add({
  'key': 'sms',
  'verbose_name': 'Sms sender',
  'backend': 'app.envoyer.backends.SMSBackend',
})
```

## Usage

Simple shortcut usage is `send` shortcut.

```python
from wcd_envoyer.shortcuts import send, default_sender

send(
  # Event name
  'app-event',
  # Recipients list.
  # Recipient object is a dict with any key-values, from which different
  # backends will get data they need.
  [
    # This recipient will be used only by sms, or phone call backend.
    {'phone': '+0000000000'},
    # This will be user by email sending backend.
    {'email': 'some@email.com'},
    # And both backends will send message to recipient like that.
    {'phone': '+0000000000', 'email': 'some@email.com'},
  ],
  # Data object, what will be used to render Message.
  # It could be dict with any data.
  # For event probably there will be data for event's context.
  {
    'var1': 'data',
    'var2': 'data',
    # If you need to send messages with specific language, you may add it here:
    'language': 'en',
    # And also any other backend-specific options could be passed to context.
    # ...
  },
  # You may additionally limit channels that message will be send.
  channels=['sms'],
  # Or. None - all channels possible.
  channels=None,
  # Optional parameter, with which you may change sender instance, to your
  # custom one.
  sender=default_sender,
)
```
