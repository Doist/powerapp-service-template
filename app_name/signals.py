# -*- coding: utf-8 -*-
import datetime
from logging import getLogger
from django.dispatch.dispatcher import receiver
from .apps import AppConfig


logger = getLogger(__name__)


# Place your signal handlers here. You can of course use any signal handlers
# of Django or any third-party applications, but most likely it's crucial for
# the service to react on sync-related events.
#
# Soon after users change something in their Todoist accounts, the sync
# procedure start off and launch a number of events. The class
# `powerapp.core.apps.ServiceAppSignals` describes all types of signals which
# sync operation can emit.

@receiver(AppConfig.signals.todoist_task_added)
def on_task_added(sender, user=None, service=None, integration=None, obj=None, **kwargs):
    logger.info('A new task %s was added' % obj['content'])


# You can also add one or more "polling tasks" for your service. They will be
# started periodically, individually for every integration user installs.
# As you can see, the periodic task callback accepts the Integration and
# User instance as its argument

@AppConfig.periodic_task(datetime.timedelta(minutes=1))
def minute_counter(integration, user):
    logger.info('A minute passes')
