from typing import List

from encoder_compressor_benchmark.compressors.base import BaseCompressor
from encoder_compressor_benchmark.compressors.zstd import ZSTDCompressor
from encoder_compressor_benchmark.compressors.gzip import GZIPCompressor
from encoder_compressor_benchmark.compressors.zlib import ZLIBCompressor


AVAILABLE_COMPRESSORS: List[BaseCompressor] = [
    GZIPCompressor,
    ZSTDCompressor,
    ZLIBCompressor
]
