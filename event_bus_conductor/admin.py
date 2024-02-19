from django.contrib import admin

from .admin_forms import EventConfigurationAdminForm
from .models import EventConfiguration, Event

@admin.register(EventConfiguration)
class EventConfigurationAdmin(admin.ModelAdmin):
    form = EventConfigurationAdminForm
    list_display = ('id', 'listened_events', 'change_date', 'changed_by', 'enabled',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass
