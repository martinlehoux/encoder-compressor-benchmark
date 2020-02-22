import flynn

from encoder_compressor_benchmark.encoders.base import BaseEncoder


class CBOREncoder(BaseEncoder):
    ext = 'cbor'
    test_size = 4

    def _encode(self, data):
        return flynn.dumps(data)
