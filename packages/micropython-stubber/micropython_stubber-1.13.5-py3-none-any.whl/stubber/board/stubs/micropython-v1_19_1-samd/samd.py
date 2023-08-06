"""
Module: 'samd' on micropython-v1.19.1-samd
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'sysname': 'unknown', 'platform': 'samd', 'version': '1.19.1', 'release': '1.19.1', 'port': 'samd', 'family': 'micropython', 'name': 'micropython', 'machine': 'unknown', 'nodename': 'unknown'}
# Stubber: v1.12.2
from typing import Any

def pininfo(*args, **kwargs) -> Any:
    ...


class Flash():
    def ioctl(self, *args, **kwargs) -> Any:
        ...

    def writeblocks(self, *args, **kwargs) -> Any:
        ...

    def readblocks(self, *args, **kwargs) -> Any:
        ...

    def flash_init(self, *args, **kwargs) -> Any:
        ...

    def flash_version(self, *args, **kwargs) -> Any:
        ...

    def flash_size(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

