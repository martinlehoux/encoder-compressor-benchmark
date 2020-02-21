import pytest
from encoder_compressor_benchmark.encoders import (
    BaseEncoder,
    AVAILABLE_ENCODERS
)


@pytest.mark.parametrize("Encoder", AVAILABLE_ENCODERS)
def test_encoders(Encoder: BaseEncoder):
    enc = Encoder()
    assert enc.size == '0 Bytes'
    assert enc._time == 0

    data = [1, 2, 3]
    enc.encode(data)
    assert enc._size == enc.test_size
    assert enc._time > 0
