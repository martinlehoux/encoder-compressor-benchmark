import json

from .base import BaseEncoder


class JSONEncoder(BaseEncoder):
    ext = 'json'

    def _encode(self, data):
        return json.dumps(data).encode('utf-8')
