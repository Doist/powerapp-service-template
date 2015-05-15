# -*- coding: utf-8 -*-
"""
Here is the longer description of your application
"""
from powerapp.core.apps import ServiceAppConfig

# AppConfig is your main config describing your service. Its name is defined
# in the default_app_config variable of `__init__.py` (make sure it's correct),
# and it's also important to inherit this class from `ServiceAppConfig`


class AppConfig(ServiceAppConfig):
    name = '{{ app_name }}'
    verbose_name = 'A name of your application'

    # The URL where users can find more about your application
    url = 'https://example.com'

    # A description of your application
    description = __doc__

    # If you want to use custom models in your service, you're welcome, and if
    # you do so, don't forget to remove this statement.
    #
    # Yet most likely you don't need any modules, as all integration-specific
    # can be conveniently stored in the Integration settings attribute
    models_module = None

    # If your application requires extra settings, such as third-party
    # service secret keys, define them like this.
    #
    #
    # import environ
    # env = environ.Env()
    #
    # ...
    # class AppConfig(ServiceAppConfig):
    #    ...
    #    FOO_CLIENT_ID = env('FOO_CLIENT_ID', default=None)
    #    FOO_CLIENT_SECRET = env('FOO_CLIENT_SECRET', default=None)
    #
    # All attributes with names matching the "uppercase and dashes" pattern,
    # will also be exported to django.conf.settings
    #
    # Read more how env works here: https://github.com/joke2k/django-environ
    #
    # Important! Don't forget to mention these variables in your installation
    # instruction.
