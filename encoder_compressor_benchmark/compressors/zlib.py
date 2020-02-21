import zlib
from .base import BaseCompressor


class ZLIBCompressor(BaseCompressor):
    ext = 'zlib'

    def _compress(self, data):
        return zlib.compress(data)
