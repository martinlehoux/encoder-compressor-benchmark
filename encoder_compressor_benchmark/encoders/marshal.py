import marshal

from encoder_compressor_benchmark.encoders.base import BaseEncoder


class MARSHALEncoder(BaseEncoder):
    ext = 'marshal'
    test_size = 20

    def _encode(self, data):
        return marshal.dumps(data)
