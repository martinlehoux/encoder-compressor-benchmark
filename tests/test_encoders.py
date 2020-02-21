import pytest
from encoder_compressor_benchmark.encoders import (
    BaseEncoder,
    JSONEncoder,
    MSGPACKEncoder,
    YAMLEncoder,
)


@pytest.mark.parametrize("Encoder,expected_size", [
    (JSONEncoder, '9 Bytes'),
    (MSGPACKEncoder, '4 Bytes'),
    (YAMLEncoder, '12 Bytes'),
])
def test_encoders(Encoder: BaseEncoder, expected_size: str):
    enc = Encoder()
    assert enc.size == '0 Bytes'
    assert enc._time == 0

    data = [1, 2, 3]
    enc.encode(data)
    assert enc.size == expected_size
    assert enc._time > 0
