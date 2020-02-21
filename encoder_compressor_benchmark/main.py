import json

from encoder_compressor_benchmark.select_from_list import (
    ENABLED_ENCODERS,
    ENABLED_COMPRESSORS
)
from encoder_compressor_benchmark.table import print_table

BANDWIDTH = 1e6


def main():
    with open('base.json', 'r') as f:
        data = json.load(f)

    print_table(data, ENABLED_ENCODERS, ENABLED_COMPRESSORS, BANDWIDTH)
