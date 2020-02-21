import gzip

from .base import BaseCompressor


class GZIPCompressor(BaseCompressor):
    ext = 'gzip'

    def _compress(self, data):
        return gzip.compress(data)
