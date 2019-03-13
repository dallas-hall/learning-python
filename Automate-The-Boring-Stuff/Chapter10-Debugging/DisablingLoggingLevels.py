import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - [%(levelname)s] - %(message)s')
# Disables all logging at and below the specified level.
logging.disable(logging.ERROR)
logging.debug('This is a debug log message.')
logging.info('This is an information log message.')
logging.warning('This is a warning log message.')
logging.error('This is an error log message. Program can continue.')
logging.fatal('This is a fatal error log message. Program cannot continue.')