"""
Module: 'uasyncio.event' on micropython-v1.19.1-samd
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'sysname': 'unknown', 'platform': 'samd', 'version': '1.19.1', 'release': '1.19.1', 'port': 'samd', 'family': 'micropython', 'name': 'micropython', 'machine': 'unknown', 'nodename': 'unknown'}
# Stubber: v1.12.2
from typing import Any


class ThreadSafeFlag():
    def set(self, *args, **kwargs) -> Any:
        ...

    def ioctl(self, *args, **kwargs) -> Any:
        ...

    def clear(self, *args, **kwargs) -> Any:
        ...

    wait : Any ## <class 'generator'> = <generator>
    def __init__(self, *argv, **kwargs) -> None:
        ...


class Event():
    def set(self, *args, **kwargs) -> Any:
        ...

    def is_set(self, *args, **kwargs) -> Any:
        ...

    def clear(self, *args, **kwargs) -> Any:
        ...

    wait : Any ## <class 'generator'> = <generator>
    def __init__(self, *argv, **kwargs) -> None:
        ...

