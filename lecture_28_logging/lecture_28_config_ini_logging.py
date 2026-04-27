import logging.config

logging.config.fileConfig(fname='config.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)
logger.debug('debug message')
logger.info('info message')
