from config_models.models import ConfigurationModel
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel
from openedx_events.tooling import OpenEdxPublicSignal


def default_configuration():
    return {"event_types": []}


class DebugConfiguration(ConfigurationModel):
    config = models.JSONField(
        default=default_configuration,
        help_text=_('Use namespaced types, e.g: "org.openedx.learning.student.registration.completed.v1"'),
    )

    def __str__(self):
        return f"DebugConfiguration:{self.id}"

    @property
    def types(self):
        """
        Return the list of event types.
        """
        return self.config.get("event_types", [])


class DebugEvent(TimeStampedModel):
    """
    Public event introspection record.
    """

    DEFAULT = _("Couldn't parse.")

    uuid = models.UUIDField(null=True, blank=True, help_text=_("Original message ID."))
    etype = models.CharField(max_length=255, verbose_name="type", help_text=_("Public event type."))
    data = models.TextField(
        help_text="https://docs.openedx.org/projects/openedx-events/en/latest/decisions/0003-events-payload.html",
    )
    metadata = models.TextField(
        help_text="https://open-edx-proposals.readthedocs.io/en/latest/architectural-decisions/oep-0041-arch-async-server-event-messaging.html",
    )

    def __str__(self):
        return f"Debug Event record:{self.id}({self.created})"
