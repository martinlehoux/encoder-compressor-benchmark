import json
from terminaltables import SingleTable

from encoder_compressor_benchmark.select_from_list import (
    ENABLED_ENCODERS,
    ENABLED_COMPRESSORS
)


def main():
    with open('base.json', 'r') as f:
        data = json.load(f)
    print("data loaded")

    table_data = [['', 'Encoding phase']]
    for compressor in ENABLED_COMPRESSORS:
        table_data[0].append(compressor.__name__)

    for Encoder in ENABLED_ENCODERS:
        encoder = Encoder()
        size_line = [f'{Encoder.__name__} - size']
        time_line = [f'{Encoder.__name__} - time']

        encoded_data = encoder.encode(data)
        size_line.append(encoder.size)
        time_line.append(encoder.time)

        for Compressor in ENABLED_COMPRESSORS:
            compressor = Compressor()
            compressor.compress(encoded_data)
            size_line.append("{size} ({ratio:.0%})".format(
                size=compressor.size,
                ratio=compressor._size / encoder._size
            ))
            time_line.append("{time} ({ratio:.0%})".format(
                time=compressor.time,
                ratio=compressor._time / encoder._time
            ))

        table_data.append(size_line)
        table_data.append(time_line)

    print(SingleTable(table_data).table)
