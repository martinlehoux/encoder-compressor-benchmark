import yaml

from .base import BaseEncoder


class YAMLEncoder(BaseEncoder):
    ext = 'yml'

    def _encode(self, data):
        return yaml.safe_dump(data).encode('utf-8')
