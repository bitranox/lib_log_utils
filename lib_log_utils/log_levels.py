import logging

SPAM: int = 5
VERBOSE: int = 15
NOTICE: int = 25
SUCCESS: int = 35

# noinspection PyTypeHints
logging.SPAM = SPAM                                     # type: ignore
# noinspection PyTypeHints
logging.VERBOSE = VERBOSE                               # type: ignore
# noinspection PyTypeHints
logging.NOTICE = NOTICE                                 # type: ignore
# noinspection PyTypeHints
logging.SUCCESS = SUCCESS                               # type: ignore

logging._levelToName[logging.SPAM] = 'SPAM'             # type: ignore
logging._levelToName[logging.VERBOSE] = 'VERBOSE'       # type: ignore
logging._levelToName[logging.NOTICE] = 'NOTICE'         # type: ignore
logging._levelToName[logging.SUCCESS] = 'SUCCESS'       # type: ignore

logging._nameToLevel['SPAM'] = logging.SPAM             # type: ignore
logging._nameToLevel['VERBOSE'] = logging.VERBOSE       # type: ignore
logging._nameToLevel['NOTICE'] = logging.NOTICE         # type: ignore
logging._nameToLevel['SUCCESS'] = logging.SUCCESS       # type: ignore
