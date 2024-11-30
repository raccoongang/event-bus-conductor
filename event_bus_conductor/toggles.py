"""
Event bus conductor feature management.
"""
from edx_toggles.toggles import SettingToggle

EVENT_BUS_CONDUCTOR_ENABLED = SettingToggle('EVENT_BUS_CONDUCTOR_ENABLED', default=False)
