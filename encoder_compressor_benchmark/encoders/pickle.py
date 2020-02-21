import pickle

from encoder_compressor_benchmark.encoders.base import BaseEncoder


class PICKLEEncoder(BaseEncoder):
    ext = 'pickle'
    test_size = 14

    def _encode(self, data):
        return pickle.dumps(data)
