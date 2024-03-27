======================
Event Bus Conductor
======================

Open edX universal plugin for event bus configuration debugging.

Features
--------

Incoming public signals introspection.

Installation
------------

Nothing special.

Supports the following services:

- Platform
    - LMS
    - CMS
- Credentials

Configuration
-------------

Once installed the plugin will be available in the admin interface.
See: `.EVENT BUS CONDUCTOR` section in the very top of admin site.

Create Debug configuration record, add wanted event types (see `openedx-events <https://github.com/openedx/openedx-events>`_) and activate it:

.. code-block:: json

    {
        "event_types": [
            "edx.course.enrollment.activated",
            "edx.course.enrollment.deactivated"
        ]
    }

Usage
-----

When Debug configuration is active, the plugin will log all incoming public signals as Debug Event records.

Each debug event then renders its internals:

- event bus message uuid
- event type
- payload
- metadata
