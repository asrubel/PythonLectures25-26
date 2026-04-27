import logging.config
import yaml

with open("config.yaml", 'r') as config_file:
    config = yaml.safe_load(config_file.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)
logger.debug('debug message')
logger.info('info message')
