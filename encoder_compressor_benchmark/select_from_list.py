from PyInquirer import prompt
from typing import List

from encoder_compressor_benchmark.encoders import (
    AVAILABLE_ENCODERS,
    BaseEncoder
)
from encoder_compressor_benchmark.compressors import (
    AVAILABLE_COMPRESSORS,
    BaseCompressor
)

questions = [
    {
        'type': 'checkbox',
        'name': 'enabled_encoders',
        'message': 'Activate encoders',
        'choices': [{
            'name': Enc.__name__
        } for Enc in AVAILABLE_ENCODERS]
    },
    {
        'type': 'checkbox',
        'name': 'enabled_compressors',
        'message': 'Activate compressors',
        'choices': [{
            'name': Enc.__name__
        } for Enc in AVAILABLE_COMPRESSORS]
    }
]

answers = prompt(questions)
ENABLED_ENCODERS: List[BaseEncoder] = list(filter(
    lambda enc: enc.__name__ in answers['enabled_encoders'],
    AVAILABLE_ENCODERS
))
ENABLED_COMPRESSORS: List[BaseCompressor] = list(filter(
    lambda enc: enc.__name__ in answers['enabled_compressors'],
    AVAILABLE_COMPRESSORS
))
