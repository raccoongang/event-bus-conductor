from django.core.management import CommandError
from django.core.management.base import BaseCommand


from event_bus_conductor.api import update_debug_configuration


class Command(BaseCommand):
    """
    Creates an event bus conductor configuration.

    Example:
        - python manage.py create_event_bus_conductor_config                                    # inactive, empty events set
        - python manage.py create_event_bus_conductor_config --activate                         # active, empty events set
        - python manage.py create_event_bus_conductor_config --activate --events=event1,event2  # active, with provided event types

    Note: expected event type format: "org.openedx.learning.student.registration.completed.v1" (see: "openedx-events" library).
    """

    help = "Create an event bus conductor configuration"

    def add_arguments(self, parser):
        parser.add_argument("--activate", action="store_true", help="Activate the event bus conductor configuration")
        parser.add_argument("--events", type=str, help="Comma-separated list of events (e.g. event1,event2)")

    def handle(self, *args, **options):
        activate = options["activate"]
        events = options["events"].split(",") if options["events"] else []

        self.stdout.write(self.style.NOTICE("Configuring event bus Conductor..."))

        update_debug_configuration(activate=activate, events=events)

        self.stdout.write(self.style.SUCCESS("...event bus conductor configuration updated successfully."))
