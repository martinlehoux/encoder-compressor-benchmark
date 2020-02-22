from typing import List

from encoder_compressor_benchmark.encoders.base import BaseEncoder
from encoder_compressor_benchmark.encoders.json import JSONEncoder
from encoder_compressor_benchmark.encoders.msgpack import MSGPACKEncoder
from encoder_compressor_benchmark.encoders.yaml import YAMLEncoder
from encoder_compressor_benchmark.encoders.ujson import UJSONEncoder
from encoder_compressor_benchmark.encoders.pickle import PICKLEEncoder
from encoder_compressor_benchmark.encoders.marshal import MARSHALEncoder
from encoder_compressor_benchmark.encoders.bson import BSONEncoder


AVAILABLE_ENCODERS: List[BaseEncoder] = [
    JSONEncoder,
    MSGPACKEncoder,
    YAMLEncoder,
    UJSONEncoder,
    PICKLEEncoder,
    MARSHALEncoder,
    BSONEncoder
]
