import yaml

from .base import BaseEncoder


class YAMLEncoder(BaseEncoder):
    ext = 'yml'
    test_size = 12

    def _encode(self, data):
        return yaml.safe_dump(data).encode('utf-8')
