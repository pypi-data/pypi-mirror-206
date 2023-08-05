"""alphinity"""

__version__ = "0.1.4"

from . import v1 as v1
from .v1 import encode

__all__ = [
    "encode",
    "v1",
]
