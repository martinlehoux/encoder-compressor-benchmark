import gzip

from .base import BaseCompressor


class GZIPCompressor(BaseCompressor):
    ext = 'gzip'
    test_size = 29

    def _compress(self, data):
        return gzip.compress(data)
