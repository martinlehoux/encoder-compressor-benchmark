import zlib
from encoder_compressor_benchmark.compressors.base import BaseCompressor


class ZLIBCompressor(BaseCompressor):
    ext = 'zlib'
    test_size = 17

    def _compress(self, data):
        return zlib.compress(data)
