"""
Module: 'dht' on micropython-v1.19.1-samd
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'sysname': 'unknown', 'platform': 'samd', 'version': '1.19.1', 'release': '1.19.1', 'port': 'samd', 'family': 'micropython', 'name': 'micropython', 'machine': 'unknown', 'nodename': 'unknown'}
# Stubber: v1.12.2
from typing import Any

def dht_readinto(*args, **kwargs) -> Any:
    ...


class DHT22():
    def humidity(self, *args, **kwargs) -> Any:
        ...

    def temperature(self, *args, **kwargs) -> Any:
        ...

    def measure(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class DHT11():
    def humidity(self, *args, **kwargs) -> Any:
        ...

    def temperature(self, *args, **kwargs) -> Any:
        ...

    def measure(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class DHTBase():
    def measure(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

