from django.contrib import admin

from config_models.admin import ConfigurationModelAdmin

from event_bus_conductor.admin_forms import DebugConfigAdminForm
from event_bus_conductor.models import DebugConfiguration, DebugEvent
from event_bus_conductor.toggles import EVENT_BUS_CONDUCTOR_ENABLED


class FeatureModelAdmin(admin.ModelAdmin):
    """
    Hide before feature activation.
    """
    def get_model_perms(self, request):
        """
        """
        perms = super().get_model_perms(request)
        if not EVENT_BUS_CONDUCTOR_ENABLED.is_enabled():
            return {key: False for key in perms}
        return perms


@admin.register(DebugConfiguration)
class EventConfigurationAdmin(FeatureModelAdmin, ConfigurationModelAdmin):
    form = DebugConfigAdminForm


@admin.register(DebugEvent)
class DebugEventAdmin(FeatureModelAdmin):
    list_display = [
        "id",
        "uuid",
        "etype",
        "created",
    ]

    list_display_links = [
        "id",
        "uuid",
    ]

    list_filter = [
        "etype",
    ]

    def has_change_permission(self, request, obj=None):
        return False
