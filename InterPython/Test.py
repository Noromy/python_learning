
import logging.config
import sys

logging.config.fileConfig(r'e:\GettingStarted\Python Inter\LoggingC.config')
logger = logging.getLogger('exampleLogger')
logger.debug('Ini pesan debug')
