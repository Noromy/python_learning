import logging
import logging.config

logging.config.fileConfig("E:\GettingStarted\Python Inter\Test.conf")
logger = logging.getLogger()
logger.info("Log berhasil dimuat!")