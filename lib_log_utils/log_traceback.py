# STDLIB

# noinspection PyUnresolvedReferences
import logging
# noinspection PyUnresolvedReferences
import sys
import traceback
# noinspection PyUnresolvedReferences
from typing import Optional

# OWN
import lib_parameter

# PROJ
try:
    from . import lib_log_utils
    from . import log_handlers
except ImportError:                 # pragma: no cover
    import lib_log_utils            # type: ignore  # pragma: no cover
    import log_handlers             # type: ignore  # pragma: no cover


def log_exception_traceback(s_error: str, log_level: int = logging.ERROR,
                            log_level_exec_info: Optional[int] = None,
                            log_level_traceback: Optional[int] = None) -> str:
    log_level_exec_info = int(lib_parameter.get_default_if_none(log_level_exec_info, log_level))
    log_level_traceback = int(lib_parameter.get_default_if_none(log_level_traceback, log_level_exec_info))

    if s_error and log_level != logging.NOTSET:
        lib_log_utils.log_level(message=s_error, level=log_level)

    if log_level_exec_info != logging.NOTSET:
        exc_info = sys.exc_info()[1]
        exc_info_type = type(exc_info).__name__
        exc_info_msg = exc_info_type + ': ' + str(exc_info)
        lib_log_utils.log_level(message=exc_info_msg, level=log_level_exec_info)

    if log_level_traceback != logging.NOTSET:
        s_traceback = 'Traceback Information : \n' + traceback.format_exc()
        s_traceback = s_traceback.rstrip('\n')
        lib_log_utils.log_level(message=s_traceback, level=log_level_traceback)

    log_handlers.logger_flush_all_handlers()
    return s_error  # to use it as input for re-raising


def print_exception_traceback(s_error: str) -> str:
    exc_info = sys.exc_info()[1]
    exc_info_type = type(exc_info).__name__
    exc_info_msg = exc_info_type + ': ' + str(exc_info)
    print(exc_info_msg)

    s_traceback = 'Traceback Information : \n' + traceback.format_exc()
    s_traceback = s_traceback.rstrip('\n')
    print(s_traceback)
    return s_error  # to use it as input for re-raising


def test_log_util():   # type: ignore
    """
    # >>> import lib_doctest_pycharm
    # >>> lib_doctest_pycharm.setup_doctest_logger_for_pycharm(log_level=logging.DEBUG)
    # >>> test_log_util() # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
    Fehler
    ZeroDivisionError: division by zero
    Traceback Information :
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero

    """
    try:
        xxx = 1 / 0
        return xxx
    except ZeroDivisionError:
        log_exception_traceback('Fehler', log_level=logging.WARNING, log_level_exec_info=logging.INFO, log_level_traceback=logging.INFO)
