"""
App configuration for event_bus_conductor.
"""

from __future__ import unicode_literals

import logging

from django.apps import AppConfig
from openedx_events.tooling import load_all_signals, OpenEdxPublicSignal

logger = logging.getLogger(__name__)

EXTENSIONS_APP_NAME = "event_bus_conductor"


class EventBusConductorConfig(AppConfig):
    """
    Event bus conductor configuration.
    """

    name = EXTENSIONS_APP_NAME
    verbose_name = ".Event bus conductor"

    # Class attribute that configures and enables this app as a Plugin App.
    plugin_app = {
        "url_config": {
            "lms.djangoapp": {
                "namespace": EXTENSIONS_APP_NAME,
                "app_name": EXTENSIONS_APP_NAME,
                "regex": r"^event-bus-conductor/",
                "relative_path": "urls",
            },
            "cms.djangoapp": {
                "namespace": EXTENSIONS_APP_NAME,
                "app_name": EXTENSIONS_APP_NAME,
                "regex": r"^event-bus-conductor/",
                "relative_path": "urls",
            },
            "credentials.djangoapp": {
                "namespace": EXTENSIONS_APP_NAME,
                "app_name": EXTENSIONS_APP_NAME,
                "regex": r"^event-bus-conductor/",
                "relative_path": "urls",
            },
        },
        "settings_config": {
            "lms.djangoapp": {
                "common": {
                    "relative_path": "settings.common",
                },
                "test": {
                    "relative_path": "settings.test",
                },
                "production": {
                    "relative_path": "settings.production",
                },
            },
            "cms.djangoapp": {
                "common": {
                    "relative_path": "settings.common",
                },
                "test": {
                    "relative_path": "settings.test",
                },
                "production": {
                    "relative_path": "settings.production",
                },
            },
            "credentials.djangoapp": {
                "common": {
                    "relative_path": "settings.common",
                },
                "test": {
                    "relative_path": "settings.test",
                },
                "production": {
                    "relative_path": "settings.production",
                },
            },
        },
    }

    def ready(self):
        from .signals.handlers import record_event
        logger.info("Conductor: Hello everyone! Please, prepare your tickets!")

        # ensure signals are cached:
        load_all_signals()

        for event in OpenEdxPublicSignal.all_events():
            event.connect(record_event)

        return super().ready()
