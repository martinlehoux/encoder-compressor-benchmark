from typing import List

from .base import BaseCompressor
from .zstd import ZSTDCompressor
from .gzip import GZIPCompressor
from .zlib import ZLIBCompressor


ENABLED_COMPRESSORS: List[BaseCompressor] = [
    GZIPCompressor,
    ZSTDCompressor,
    ZLIBCompressor
]
