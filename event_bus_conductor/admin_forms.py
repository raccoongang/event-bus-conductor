"""
Django forms for the event bus conductor.
"""

from django import forms
from django.utils.translation import gettext_lazy as _
from openedx_events.tooling import OpenEdxPublicSignal

from .models import DebugConfiguration


class DebugConfigAdminForm(forms.ModelForm):
    class Meta:
        model = DebugConfiguration
        fields = "__all__"

    def clean(self):
        """
        Validate event types.
        """
        cleaned_data = super().clean()

        try:
            for event_type in cleaned_data.get("config", {}).get("event_types", []):
                OpenEdxPublicSignal.get_signal_by_type(event_type)
        except KeyError:
            raise forms.ValidationError(_(f"Invalid event type: {event_type}"))

        return cleaned_data
