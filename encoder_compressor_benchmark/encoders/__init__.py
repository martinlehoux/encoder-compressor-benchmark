from typing import List

from .base import BaseEncoder
from .json import JSONEncoder
from .msgpack import MSGPACKEncoder


ENABLED_ENCODERS: List[BaseEncoder] = [
    JSONEncoder,
    MSGPACKEncoder
]
