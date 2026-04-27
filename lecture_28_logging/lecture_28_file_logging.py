import logging

logging.basicConfig(filename='my.log', filemode='w',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')

name = "My Logger"
logging.error('%s caused error', name)

try:
    c = 5 / 0
except ZeroDivisionError as e:
    logging.error('Division by zero error', exc_info=False)
    logging.exception('ZeroDivisionError')
