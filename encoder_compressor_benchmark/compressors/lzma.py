import lzma

from encoder_compressor_benchmark.compressors.base import BaseCompressor


class LZMACompressor(BaseCompressor):
    ext = 'xz'
    test_size = 68

    def _compress(self, data):
        return lzma.compress(data)
