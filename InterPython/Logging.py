''''
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
'''
import logging
import logging.config

logging.config.fileConfig("Logging.conf") # Load configuration from file
logger = logging.getLogger('sLogger')
logger.info("Log berhasil dimuat!")

#create handlers
logger = logging.getLogger(__name__)
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# level and  the formatters
stream_h.setLevel(logging.WARNING) 
file_h.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',
                               datefmt='%Y-%m-%d %H:%M:%S')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning("This is a warning")
logger.error("This is an error")
