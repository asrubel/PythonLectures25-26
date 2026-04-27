import logging

logger = logging.getLogger('my_logger')

c_handler = logging.StreamHandler()
c_handler.setLevel(logging.WARNING)
f_handler = logging.FileHandler('file.log')
f_handler.setLevel(logging.ERROR)

c_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_formatter)
f_handler.setFormatter(f_formatter)

logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
