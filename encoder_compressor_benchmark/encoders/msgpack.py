import msgpack

from .base import BaseEncoder


class MSGPACKEncoder(BaseEncoder):
    ext = 'msgpack'
    test_size = 4

    def _encode(self, data):
        return msgpack.packb(data)
