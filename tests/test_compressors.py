import pytest
from encoder_compressor_benchmark.compressors import (
    BaseCompressor,
    GZIPCompressor,
    ZSTDCompressor,
    ZLIBCompressor,
)


@pytest.mark.parametrize("Compressor,expected_size", [
    (GZIPCompressor, '29 Bytes'),
    (ZSTDCompressor, '18 Bytes'),
    (ZLIBCompressor, '17 Bytes'),
])
def test_compressors(Compressor: BaseCompressor, expected_size: str):
    comp = Compressor()
    assert comp.size == '0 Bytes'
    assert comp._time == 0

    data = b'[1, 2, 3]'
    comp.compress(data)
    assert comp.size == expected_size
    assert comp._time > 0
