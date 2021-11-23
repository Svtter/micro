import logging


def obtain_logger():
    logger = logging.getLogger('micro.main')
    logger.setLevel(logging.DEBUG)
    log_formatter = logging.Formatter(fmt=' %(name)s :: %(levelname)-8s :: %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(log_formatter)
    logger.addHandler(handler)
    return logger


logger = obtain_logger()