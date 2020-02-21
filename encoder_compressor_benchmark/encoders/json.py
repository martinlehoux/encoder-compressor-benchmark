import json

from encoder_compressor_benchmark.encoders.base import BaseEncoder


class JSONEncoder(BaseEncoder):
    ext = 'json'
    test_size = 9

    def _encode(self, data):
        return json.dumps(data).encode('utf-8')
