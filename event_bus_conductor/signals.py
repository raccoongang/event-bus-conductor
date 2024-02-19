from django.db.models.signals import post_save
from django.dispatch import receiver
from openedx_events.tooling import OpenEdxPublicSignal, load_all_signals

from .models import Event, EventConfiguration


def create_debug_model_for_event(sender, signal, **kwargs):  # pylint: disable=unused-argument
    Event.objects.create(data=kwargs)


@receiver(post_save, sender=EventConfiguration)
def connect_signals_to_listened_events(sender, instance, created, **kwargs):
    if instance.enabled:
        load_all_signals()
        for event_type in instance.events_list:
            signal = OpenEdxPublicSignal.get_signal_by_type(event_type)
            signal.connect(create_debug_model_for_event)
