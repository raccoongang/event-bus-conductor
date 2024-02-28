# Generated by Django 4.2.10 on 2024-02-24 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import event_bus_conductor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="DebugEvent",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        blank=True, help_text="Original message ID.", null=True
                    ),
                ),
                (
                    "etype",
                    models.CharField(
                        help_text="Public event type.",
                        max_length=255,
                        verbose_name="type",
                    ),
                ),
                (
                    "data",
                    models.TextField(
                        help_text="https://docs.openedx.org/projects/openedx-events/en/latest/decisions/0003-events-payload.html"
                    ),
                ),
                (
                    "metadata",
                    models.TextField(
                        help_text="https://open-edx-proposals.readthedocs.io/en/latest/architectural-decisions/oep-0041-arch-async-server-event-messaging.html"
                    ),
                ),
            ],
            options={
                "get_latest_by": "modified",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="DebugConfiguration",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "change_date",
                    models.DateTimeField(auto_now_add=True, verbose_name="Change date"),
                ),
                ("enabled", models.BooleanField(default=False, verbose_name="Enabled")),
                (
                    "config",
                    models.JSONField(
                        default=event_bus_conductor.models.default_configuration,
                        help_text='Use namespaced types, e.g: "org.openedx.learning.student.registration.completed.v1"',
                    ),
                ),
                (
                    "changed_by",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Changed by",
                    ),
                ),
            ],
            options={
                "ordering": ("-change_date",),
                "abstract": False,
            },
        ),
    ]
