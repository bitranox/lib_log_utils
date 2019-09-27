import logging


def setup_log_levels() -> None:
    logging.SPAM = 5
    logging.VERBOSE = 15
    logging.NOTICE = 25
    logging.SUCCESS = 35

    logging._levelToName[logging.SPAM] = 'SPAM'
    logging._levelToName[logging.VERBOSE] = 'VERBOSE'
    logging._levelToName[logging.NOTICE] = 'NOTICE'
    logging._levelToName[logging.SUCCESS] = 'SUCCESS'

    logging._nameToLevel['SPAM'] = logging.SPAM
    logging._nameToLevel['VERBOSE'] = logging.VERBOSE
    logging._nameToLevel['NOTICE'] = logging.NOTICE
    logging._nameToLevel['SUCCESS'] = logging.SUCCESS


setup_log_levels()
