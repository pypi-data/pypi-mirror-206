"""
Module: 'uselect' on micropython-v1.19.1-samd
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'sysname': 'unknown', 'platform': 'samd', 'version': '1.19.1', 'release': '1.19.1', 'port': 'samd', 'family': 'micropython', 'name': 'micropython', 'machine': 'unknown', 'nodename': 'unknown'}
# Stubber: v1.12.2
from typing import Any

POLLOUT = 4 # type: int
POLLIN = 1 # type: int
POLLHUP = 16 # type: int
POLLERR = 8 # type: int
def select(*args, **kwargs) -> Any:
    ...

def poll(*args, **kwargs) -> Any:
    ...

