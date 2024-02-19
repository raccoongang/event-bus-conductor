from django.db import models
from config_models.models import ConfigurationModel
from django.utils.translation import gettext_lazy as _


class EventConfiguration(ConfigurationModel):
    listened_events = models.JSONField(default={'event_types': []})

    @property
    def events_list(self):
        """
        Return the list of event types.
        """
        return self.listened_events.get('event_types', [])


class Event(models.Model):
    data = models.TextField()
