from logging.config import dictConfig
from os.path import join

path = 'path to dir /log'
logging_config = dictConfig({
    'version': 1,
    'formatters': {
        'error': {
            'class': 'logging.Formatter',
            'format':
                '[{asctime}] '
                '{levelname} '
                '{filename} '
                '[LINE:{lineno}] \n'
                '{message} \n',
        },
        'message': {
            'class': 'logging.Formatter',
            'format':
                '[{asctime}] \n'
                '{message} \n',
        },
    },
    'handlers': {
        'adverts': {
            'class': 'logging.FileHandler',
            'filename': str(join(path, 'adverts.log')),
            'level': 'INFO',
            'mode': 'a',
            'formatter': 'message',
        },
        'reports': {
            'class': 'logging.FileHandler',
            'filename': str(join(path, 'reports.log')),
            'level': 'INFO',
            'mode': 'a',
            'formatter': 'message',
        },
        'errors': {
            'class': 'logging.FileHandler',
            'filename': str(join(path, 'errors.log')),
            'level': 'DEBUG',
            'mode': 'a',
            'formatter': 'error',
        },
    },

    'loggers': {
        'errors': {
            'level': 'DEBUG',
            'handlers': ['errors'],
        },
        'adverts': {
            'level': 'INFO',
            'handlers': ['adverts'],
        },
        'reports': {
            'level': 'INFO',
            'handlers': ['reports'],
        }
    },
})
