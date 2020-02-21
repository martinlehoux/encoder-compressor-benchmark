import zstd

from encoder_compressor_benchmark.compressors.base import BaseCompressor


class ZSTDCompressor(BaseCompressor):
    ext = 'zstd'
    test_size = 18

    def _compress(self, data):
        return zstd.compress(data)
