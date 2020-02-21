import pytest
from encoder_compressor_benchmark.compressors import (
    BaseCompressor,
    ENABLED_COMPRESSORS
)


@pytest.mark.parametrize("Compressor", ENABLED_COMPRESSORS)
def test_compressors(Compressor: BaseCompressor):
    comp = Compressor()
    assert comp.size == '0 Bytes'
    assert comp._time == 0

    data = b'[1, 2, 3]'
    comp.compress(data)
    assert comp._size == comp.test_size
    assert comp._time > 0
