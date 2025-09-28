import logging
import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
#s = seconds, m = minutes, h = hours, d = days, w0-w6 = weekday (0=Monday)
# midnight = roll over at midnight
handler = TimedRotatingFileHandler('timed_test.log', when='s', interval=5, backupCount=5) # will back up after 5 second max till 5 file
logger.addHandler(handler)

for i in range(6):
    logger.info("Hello World!")
    time.sleep(5)

# For looping backup file after 5 minutes to create a new one