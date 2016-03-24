import logging, logging.config
import sys

class Logger:

    __LOGGING = {
        'version': 1,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'stream': sys.stdout,
            }
        },
        'root': {
            'handlers': ['console'],
            'level': 'INFO'
        }
    }

    def __init__(self):
        logging.config.dictConfig(self.__LOGGING)

    def out(self, data):
        logging.info(data)
