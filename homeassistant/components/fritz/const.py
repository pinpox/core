"""Constants for the FRITZ!Box Tools integration."""

from typing import Literal

from homeassistant.backports.enum import StrEnum
from homeassistant.const import Platform


class MeshRoles(StrEnum):
    """Available Mesh roles."""

    NONE = "none"
    MASTER = "master"
    SLAVE = "slave"


DOMAIN = "fritz"

PLATFORMS = [
    Platform.BUTTON,
    Platform.BINARY_SENSOR,
    Platform.DEVICE_TRACKER,
    Platform.SENSOR,
    Platform.SWITCH,
]

DATA_FRITZ = "fritz_data"

DSL_CONNECTION: Literal["dsl"] = "dsl"

DEFAULT_DEVICE_NAME = "Unknown device"
DEFAULT_HOST = "192.168.178.1"
DEFAULT_PORT = 49000
DEFAULT_USERNAME = ""

ERROR_AUTH_INVALID = "invalid_auth"
ERROR_CANNOT_CONNECT = "cannot_connect"
ERROR_UNKNOWN = "unknown_error"

FRITZ_SERVICES = "fritz_services"
SERVICE_REBOOT = "reboot"
SERVICE_RECONNECT = "reconnect"
SERVICE_CLEANUP = "cleanup"

SWITCH_TYPE_DEFLECTION = "CallDeflection"
SWITCH_TYPE_PORTFORWARD = "PortForward"
SWITCH_TYPE_WIFINETWORK = "WiFiNetwork"

UPTIME_DEVIATION = 5
