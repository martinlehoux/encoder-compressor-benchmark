import pytest
from encoder_compressor_benchmark.encoders import (
    BaseEncoder,
    ENABLED_ENCODERS
)


@pytest.mark.parametrize("Encoder", ENABLED_ENCODERS)
def test_encoders(Encoder: BaseEncoder):
    enc = Encoder()
    assert enc.size == '0 Bytes'
    assert enc._time == 0

    data = [1, 2, 3]
    enc.encode(data)
    assert enc._size == enc.test_size
    assert enc._time > 0
