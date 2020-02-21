import time
from humanize import naturalsize


class BaseEncoder:
    _time: float = 0
    ext: str = ''
    _size: int = 0
    # Used for testing
    test_size: str

    def _encode(self, data: object) -> bytes:
        raise NotImplementedError

    def encode(self, data: object) -> bytes:
        start = time.time()
        encoded_data = self._encode(data)
        end = time.time()
        self._time = end - start
        self._size = len(encoded_data)
        return encoded_data

    @property
    def size(self) -> str:
        return naturalsize(self._size)

    @property
    def time(self) -> str:
        return f"{self._time * 1000:4.0f} ms"
