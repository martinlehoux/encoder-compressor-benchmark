from humanize import naturalsize
import json
from terminaltables import SingleTable

from encoder_compressor_benchmark.select_from_list import (
    ENABLED_ENCODERS,
    ENABLED_COMPRESSORS
)

BANDWIDTH = 1e6
print()


def main():
    with open('base.json', 'r') as f:
        data = json.load(f)

    table_data = [[f'Network: {naturalsize(BANDWIDTH)}/s', 'Encoding phase']]
    for compressor in ENABLED_COMPRESSORS:
        table_data[0].append(compressor.__name__)

    for Encoder in ENABLED_ENCODERS:
        encoder = Encoder()
        head_line = [Encoder.__name__]
        size_line = ['    size']
        time_line = ['    time']
        network_line = ['    network']
        total_time_line = ['    total time']

        encoded_data = encoder.encode(data)
        size_line.append(encoder.size)
        base_network_time = encoder._size / BANDWIDTH
        base_total_time = encoder._time + base_network_time
        time_line.append(f"{encoder.time}")
        network_line.append(f"{base_network_time * 1000:4.0f} ms")
        total_time_line.append(f"{base_total_time * 1000:4.0f} ms")

        for Compressor in ENABLED_COMPRESSORS:
            compressor = Compressor()
            compressor.compress(encoded_data)
            size_line.append("{size}".format(
                size=compressor.size,
                reduction=compressor._size / encoder._size - 1
            ))
            time_line.append("{time:=+5.0f} ms".format(
                time=compressor._time * 1000,
                ratio=compressor._time / encoder._time
            ))
            network_time = compressor._size / BANDWIDTH
            total_time = encoder._time + compressor._time + network_time
            network_line.append("{time:=+5.0f} ms".format(
                time=(network_time - base_network_time) * 1000,
                ratio=network_time / total_time
            ))
            total_time_line.append(f"{total_time * 1000:4.0f} ms")

        table_data.append(head_line)
        table_data.append(size_line)
        table_data.append(time_line)
        table_data.append(network_line)
        table_data.append(total_time_line)

    table = SingleTable(table_data)
    table.justify_columns[0] = 'left'
    for ind in range(1, len(table_data[0])):
        table.justify_columns[ind] = 'right'
    print(table.table)
