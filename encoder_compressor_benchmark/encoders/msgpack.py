import msgpack

from .base import BaseEncoder


class MSGPACKEncoder(BaseEncoder):
    ext = 'msgpack'

    def _encode(self, data):
        return msgpack.packb(data)
