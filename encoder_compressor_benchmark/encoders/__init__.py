from typing import List

from .base import BaseEncoder
from .json import JSONEncoder
from .msgpack import MSGPACKEncoder
from .yaml import YAMLEncoder


ENABLED_ENCODERS: List[BaseEncoder] = [
    JSONEncoder,
    MSGPACKEncoder,
    YAMLEncoder
]
