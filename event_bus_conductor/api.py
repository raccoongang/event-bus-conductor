from openedx_events.tooling import OpenEdxPublicSignal

from event_bus_conductor.models import DebugConfiguration


def update_debug_configuration(activate=True, events=None):
    """
    Updates (or creates) Conductor configuration.

    - activate (bool) - controls if the configuration must be activated;
    - events (list[str]) - a list of event types to include for tracking;

    Raises:
    - KeyError - for unknown events
    """
    conductor_conf = DebugConfiguration.current()
    conductor_conf.enabled = True

    if events is None:
        # assuming all events:
        events = [event.event_type for event in OpenEdxPublicSignal.all_events()]
    else:
        for event_type in events:
            if not event_type:
                continue

            # validate:
            OpenEdxPublicSignal.get_signal_by_type(event_type)

    # update configuration:
    conductor_conf.config["event_types"] = events

    # activation:
    if not activate:
        conductor_conf.enabled = False

    # Ensure record is update/created:
    conductor_conf.save()

    return conductor_conf
