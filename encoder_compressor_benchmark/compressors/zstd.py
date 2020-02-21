import zstd

from .base import BaseCompressor


class ZSTDCompressor(BaseCompressor):
    ext = 'zstd'

    def _compress(self, data):
        return zstd.compress(data)
