import gzip

from encoder_compressor_benchmark.compressors.base import BaseCompressor


class GZIPCompressor(BaseCompressor):
    ext = 'gzip'
    test_size = 29

    def _compress(self, data):
        return gzip.compress(data)
