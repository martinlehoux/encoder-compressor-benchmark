import ujson

from encoder_compressor_benchmark.encoders.base import BaseEncoder


class UJSONEncoder(BaseEncoder):
    ext = 'json'
    test_size = 7

    def _encode(self, data):
        return ujson.dumps(data).encode('utf-8')
