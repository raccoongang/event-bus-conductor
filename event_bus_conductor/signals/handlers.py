import logging
from pprint import pformat

import attrs

from ..models import DebugConfiguration, DebugEvent

logger = logging.getLogger(__name__)


def record_event(sender, signal, from_event_bus=False, **kwargs):  # pylint: disable=unused-argument
    if not from_event_bus:
        return

    event_uuid = None
    event_type = DebugEvent.DEFAULT
    event_metadata = DebugEvent.DEFAULT
    event_data = DebugEvent.DEFAULT

    try:
        event_metadata = attrs.asdict(kwargs.pop("metadata"))
        event_uuid = event_metadata.get("id")
        event_type = event_metadata.get("event_type")
        event_data = {data_key: attrs.asdict(data) for data_key, data in kwargs.items()}

    except Exception as exc:
        logger.error("Conductor: %s", exc)
    finally:
        DebugEvent.objects.create(
            uuid=event_uuid,
            etype=event_type,
            data=pformat(event_data),
            metadata=pformat(event_metadata),
        )


def handle_configuration_update(new_debug_configuration):
    """
    Update subscriptions if needed.
    """
    current_debug_config = DebugConfiguration.current()

    # nothing has changed:
    if new_debug_configuration.fields_equal(current_debug_config):
        return

    # respect configuration switch:
    if not new_debug_configuration.enabled:
        current_debug_config.disconnect(record_event)
        logger.info("Conductor: All clear! I'm quitting now.")
        return

    # subscribe for currently set events:
    connected_event_types = new_debug_configuration.connect(record_event)
    if connected_event_types:
        logger.info("Conductor: Ok! Now I'm interested in these: %s", connected_event_types)
