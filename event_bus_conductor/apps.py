"""
App configuration for event_bus_conductor.
"""

from __future__ import unicode_literals

import logging

from django.apps import AppConfig

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
        from event_bus_conductor.toggles import EVENT_BUS_CONDUCTOR_ENABLED

        if not EVENT_BUS_CONDUCTOR_ENABLED.is_enabled():
            logger.info("Conductor: ...is sleeping next to the driver (settings.EVENT_BUS_CONDUCTOR_ENABLED)")
            return

        from pprint import pformat
        from openedx_events.tooling import OpenEdxPublicSignal, load_all_signals
        from event_bus_conductor.signals.handlers import record_event

        logger.info("Conductor: Hello everyone! Please, prepare your tickets!")

        # ensure signals are cached:
        load_all_signals()

        all_events = OpenEdxPublicSignal.all_events()
        for event in all_events:
            event.connect(record_event)

        logger.debug(f"Conductor: subscribed to: {pformat(all_events)}")
        return super().ready()
