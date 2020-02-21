from PyInquirer import prompt

from encoder_compressor_benchmark.encoders import AVAILABLE_ENCODERS
from encoder_compressor_benchmark.compressors import AVAILABLE_COMPRESSORS

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
ENABLED_ENCODERS = list(filter(
    lambda enc: enc.__name__ in answers['enabled_encoders'],
    AVAILABLE_ENCODERS
))
ENABLED_COMPRESSORS = list(filter(
    lambda enc: enc.__name__ in answers['enabled_compressors'],
    AVAILABLE_COMPRESSORS
))
