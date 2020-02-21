import time
from humanize import naturalsize


class BaseCompressor:
    _time: float = 0
    ext: str = ''
    _size: int = 0
    # Used for testing
    test_size: str

    def _compress(self, data: bytes) -> bytes:
        raise NotImplementedError

    def compress(self, data: bytes) -> bytes:
        start = time.time()
        compressed_data = self._compress(data)
        end = time.time()
        self._time = end - start
        self._size = len(compressed_data)
        return compressed_data

    @property
    def size(self) -> str:
        return naturalsize(self._size)

    @property
    def time(self) -> str:
        return f"{self._time * 1000:4.0f} ms"
