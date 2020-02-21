from typing import List

from encoder_compressor_benchmark.encoders.base import BaseEncoder
from encoder_compressor_benchmark.encoders.json import JSONEncoder
from encoder_compressor_benchmark.encoders.msgpack import MSGPACKEncoder
from encoder_compressor_benchmark.encoders.yaml import YAMLEncoder


ENABLED_ENCODERS: List[BaseEncoder] = [
    JSONEncoder,
    MSGPACKEncoder,
    YAMLEncoder
]
