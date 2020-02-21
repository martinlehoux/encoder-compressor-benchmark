from typing import List

from encoder_compressor_benchmark.compressors.base import BaseCompressor
from encoder_compressor_benchmark.compressors.zstd import ZSTDCompressor
from encoder_compressor_benchmark.compressors.gzip import GZIPCompressor
from encoder_compressor_benchmark.compressors.zlib import ZLIBCompressor
from encoder_compressor_benchmark.compressors.bz2 import BZIP2Compressor
from encoder_compressor_benchmark.compressors.lzma import LZMACompressor


AVAILABLE_COMPRESSORS: List[BaseCompressor] = [
    GZIPCompressor,
    ZSTDCompressor,
    ZLIBCompressor,
    BZIP2Compressor,
    LZMACompressor,
]
