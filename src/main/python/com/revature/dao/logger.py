import logging

def simple_logger():


    #default level is WARNING

    logging.basicConfig(level=logging.DEBUG, filename="main/resources/file1.log")
    logger = logging.getLogger()

    logger.debug("Use it for tracing")
    logger.info("Use it for informational messages")
    logger.warning("Use it for operations that may raise error")
    logger.error("Use it to notify a rasied error")
    logger.critical("Use it to notify of a critical issue (system error)")
    print(logger.level)
