from django.contrib import admin

from config_models.admin import ConfigurationModelAdmin

from .admin_forms import DebugConfigAdminForm
from .models import DebugConfiguration, DebugEvent


@admin.register(DebugConfiguration)
class EventConfigurationAdmin(ConfigurationModelAdmin):
    form = DebugConfigAdminForm


@admin.register(DebugEvent)
class DebugEventAdmin(admin.ModelAdmin):
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
