import json
from micropython import alloc_emergency_exception_buf, const

from sensor import enable_sensor
from web import web_server
from wifi import enable_wifi

DOOR_SWITCH_GPIO: int = const(22)


def main() -> None:
    # Allocate a small amount of memory to capture stack traces within interrupt handlers
    alloc_emergency_exception_buf(100)

    # Read in the global configuration from the filesystem
    config = load_config()

    # Start listening to the garage door sensor
    enable_sensor(config.get("sensor_pin", DOOR_SWITCH_GPIO))

    # Connect to the configured Wi-Fi network, reconnecting as needed
    wifi_config = config.get("wifi", {})
    enable_wifi(
        country=wifi_config.get("country"),
        ssid=wifi_config.get("ssid"),
        password=wifi_config.get("password"),
    )

    # Start the HTTP server on port 80
    server = web_server()
    server.run(port=80)


def load_config() -> dict:
    with open("config.json") as config_file:
        return json.load(config_file)


main()
