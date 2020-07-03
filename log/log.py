# import logging
#
# logging.basicConfig(
#     level=logging.DEBUG,
#     filename='logger.log',
#     filemode='a',
#     format='%(asctime)s [%(lineno)d] %(message)s'
# )
#
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error messgae')
# logging.critical('critical message')

import logging

def logger():

    logger = logging.getLogger()

    fh = logging.FileHandler("test.log")
    ch = logging.StreamHandler()

    fm = logging.Formatter("%(asctime)s %(message)")

    fh.setFormatter(fm)
    ch.setFormatter(fm)

    logger.addHandler(fh)
    logger.addHandler(ch)
    logger.setLevel("DEBUG")

    return logger

logger = logger()
logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
logger.critical('critical')