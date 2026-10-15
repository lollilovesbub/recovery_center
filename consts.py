import string

DEBUG = {
    'on': True,
    'sound_test': False,
    'sequencer_tests': {
        'create': False,
        'load': False,
        'interactive': True,
    },
}
STRIP_FILENAME = string.whitespace + '.'