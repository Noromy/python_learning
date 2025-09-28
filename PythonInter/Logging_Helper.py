import logging
logger = logging.getLogger(__name__)
logger.propagate = False # PRevent double logging if root logger is also logging
logger.info("Logging module initialixzed")


