"""
App configuration for event_bus_conductor.
"""

from __future__ import unicode_literals

from django.apps import AppConfig

EXTENSIONS_APP_NAME = 'event_bus_conductor'


class EventBusConductorPluginConfig(AppConfig):
    """
    Event bus conductor configuration.
    """
    name = EXTENSIONS_APP_NAME
    verbose_name = 'Event bus conductor'

    # Class attribute that configures and enables this app as a Plugin App.
    plugin_app = {
        'url_config': {
            'lms.djangoapp': {
                'namespace': EXTENSIONS_APP_NAME,
                'app_name': EXTENSIONS_APP_NAME,
                'regex': r'^events_inspector/',
                'relative_path': 'urls',
            },
            'cms.djangoapp': {
                'namespace': EXTENSIONS_APP_NAME,
                'app_name': EXTENSIONS_APP_NAME,
                'regex': r'^events_inspector/',
                'relative_path': 'urls',
            }
        },

        'settings_config': {
            'lms.djangoapp': {
                'common': {
                    'relative_path': 'settings.common',
                },
                'test': {
                    'relative_path': 'settings.test',
                },
                'production': {
                    'relative_path': 'settings.production',
                },
            },
            'cms.djangoapp': {
                'common': {
                    'relative_path': 'settings.common',
                },
                'test': {
                    'relative_path': 'settings.test',
                },
                'production': {
                    'relative_path': 'settings.production',
                },
            },
        }
    }

    def ready(self):
        from .signals import connect_signals_to_listened_events  # pylint: disable=unused-import,import-outside-toplevel
