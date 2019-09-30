import logging

# noinspection PyTypeHints
logging.SPAM = 5                                        # type: ignore
# noinspection PyTypeHints
logging.VERBOSE = 15                                    # type: ignore
# noinspection PyTypeHints
logging.NOTICE = 25                                     # type: ignore
# noinspection PyTypeHints
logging.SUCCESS = 35                                    # type: ignore

logging._levelToName[logging.SPAM] = 'SPAM'             # type: ignore
logging._levelToName[logging.VERBOSE] = 'VERBOSE'       # type: ignore
logging._levelToName[logging.NOTICE] = 'NOTICE'         # type: ignore
logging._levelToName[logging.SUCCESS] = 'SUCCESS'       # type: ignore

logging._nameToLevel['SPAM'] = logging.SPAM             # type: ignore
logging._nameToLevel['VERBOSE'] = logging.VERBOSE       # type: ignore
logging._nameToLevel['NOTICE'] = logging.NOTICE         # type: ignore
logging._nameToLevel['SUCCESS'] = logging.SUCCESS       # type: ignore
