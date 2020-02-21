import bz2

from encoder_compressor_benchmark.compressors.base import BaseCompressor


class BZIP2Compressor(BaseCompressor):
    ext = 'bz2'
    test_size = 47

    def _compress(self, data):
        return bz2.compress(data)
