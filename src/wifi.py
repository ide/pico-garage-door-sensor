import network
import rp2


def enable_wifi(country: str = None, ssid: str = None, password: str = None) -> None:
    if country is not None:
        rp2.country(country)

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    # Disable power-saving mode (see https://datasheets.raspberrypi.com/picow/connecting-to-the-internet-with-pico-w.pdf)
    wlan.config(pm=0xA11140)

    # TODO: Back off if the connection fails. Bonus: switch to AP mode when there is a configuration
    # issue.
    wlan.connect(ssid, password)
    # TODO: Periodically monitor the connection, perhaps resetting if we cannot connect for an hour.
    return wlan
