import sys
import logging
import logging.config

import config


def log_formatter():
    fmt = ('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    return logging.Formatter(fmt, style='%')


def console_handler(stream):
    handler = logging.StreamHandler(stream)
    handler.setFormatter(log_formatter())
    return handler


console_handler = console_handler(sys.stderr)


def start_console_logging(console_handler):
    for name in config.LOGGING['loggers']:
        logger = logging.getLogger(name)
        if not logger.propagate:
            logger.addHandler(console_handler)


def setup_logging():
    logging.config.dictConfig(config.LOGGING)

    if config.LOG_TO_CONSOLE:
        start_console_logging(console_handler)
