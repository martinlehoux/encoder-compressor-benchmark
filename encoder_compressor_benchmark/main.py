import json

from encoder_compressor_benchmark.select_config import (
    ENABLED_ENCODERS,
    ENABLED_COMPRESSORS,
    BANDWIDTH
)
from encoder_compressor_benchmark.table import print_table


def main():
    with open('base.json', 'r') as f:
        data = json.load(f)

    print_table(data, ENABLED_ENCODERS, ENABLED_COMPRESSORS, BANDWIDTH)
