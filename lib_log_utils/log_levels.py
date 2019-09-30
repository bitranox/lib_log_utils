import logging


def setup_log_levels() -> None:
    logging.SPAM = 5                                        # type: ignore
    logging.VERBOSE = 15                                    # type: ignore
    logging.NOTICE = 25                                     # type: ignore
    logging.SUCCESS = 35                                    # type: ignore

    logging._levelToName[logging.SPAM] = 'SPAM'             # type: ignore
    logging._levelToName[logging.VERBOSE] = 'VERBOSE'       # type: ignore
    logging._levelToName[logging.NOTICE] = 'NOTICE'         # type: ignore
    logging._levelToName[logging.SUCCESS] = 'SUCCESS'       # type: ignore

    logging._nameToLevel['SPAM'] = logging.SPAM             # type: ignore
    logging._nameToLevel['VERBOSE'] = logging.VERBOSE       # type: ignore
    logging._nameToLevel['NOTICE'] = logging.NOTICE         # type: ignore
    logging._nameToLevel['SUCCESS'] = logging.SUCCESS       # type: ignore


setup_log_levels()
