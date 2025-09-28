import logging
import traceback

try:
    a = [1,2,3]
    val = a[4]
except IndexError as e:
    logging.error("IndexError: %s", e)
    logging.error(e, exc_info=True) # Log with traceback (tracking the error specificly)
    logging.error("The error is :%s", traceback.format_exc) # same function as above


# to Track many logs and make it small and make it back up file

from logging.handlers import RotatingFileHandler 

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#roll over after 2KB and keep back up logs app. log 1. log 2. etc
handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5) # 5 file backup
logger.addHandler(handler)

# for i in range(10000):
   #  logger.info("Hello World!")