import bencode

from encoder_compressor_benchmark.encoders.base import BaseEncoder


class BENCODEEncoder(BaseEncoder):
    ext = 'bencode'
    test_size = 11

    def _encode(self, data):
        return bencode.encode(data)
