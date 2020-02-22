import bson

from encoder_compressor_benchmark.encoders.base import BaseEncoder


class BSONEncoder(BaseEncoder):
    ext = 'bson'
    test_size = 37

    def _encode(self, data):
        return bson.dumps(dict(data=data))
