# STDLIB
import logging
import logging.handlers
import getpass
import os
import platform
import sys
from types import TracebackType
from typing import Any, Optional, Type

# EXT
import coloredlogs      # type: ignore


class HostnameFilter(logging.Filter):
    hostname = platform.node()

    def filter(self, record: Any) -> bool:
        record.hostname = HostnameFilter.hostname
        return True


def add_file_handler(filename: str,
                     logger: logging.Logger = logging.getLogger(),
                     name: str = '',
                     level: int = logging.INFO,
                     fmt: str = '[{username}@%(hostname)s][%(asctime)s][%(levelname)-8s]: %(message)s',
                     datefmt: str = '%Y-%m-%d %H:%M:%S',
                     remove_existing_handlers: bool = False,
                     mode: str = 'a',
                     encoding: str = 'utf-8',
                     delay: bool = True) -> logging.Handler:
    """
    name: the name of the file handler. if name = '', name = filename

    mode: 'a': Opens a file for appending new information to it. The pointer is placed at the end of the file.
               A new file is created if one with the same name doesn't exist.
          'w': Opens in write-only mode. The pointer is placed at the beginning of the file and this will overwrite
               any existing file with the same name. It will create a new file if one with the same name doesn't exist.
    delay: If delay is true, then file opening is deferred until the first call to emit(). By default, the file grows indefinitely.
    """

    file_handler = logging.FileHandler(filename=filename, mode=mode, encoding=encoding, delay=delay)  # type: logging.Handler
    file_handler = _add_handler(file_handler, logger=logger, name=name, level=level, fmt=fmt,
                                datefmt=datefmt, remove_existing_handlers=remove_existing_handlers)
    return file_handler


def add_stream_handler(logger: logging.Logger = logging.getLogger(),
                       name: str = 'stream_handler',
                       level: int = logging.INFO,
                       fmt: str = '[{username}@%(hostname)s][%(asctime)s][%(levelname)-8s]: %(message)s',
                       datefmt: str = '%Y-%m-%d %H:%M:%S',
                       remove_existing_handlers: bool = True) -> logging.Handler:

    """
    >>> result = add_stream_handler()

    """
    stream_handler = logging.StreamHandler(stream=sys.stderr)  # type: logging.Handler
    stream_handler = _add_handler(stream_handler, logger=logger, name=name, level=level, fmt=fmt,
                                  datefmt=datefmt, remove_existing_handlers=remove_existing_handlers)
    return stream_handler


def add_stream_handler_color(logger: logging.Logger = logging.getLogger(),
                             name: str = 'stream_handler_color',
                             level: int = logging.INFO,
                             fmt: str = '[{username}@%(hostname)s][%(asctime)s][%(levelname)-8s]: %(message)s',
                             datefmt: str = '%Y-%m-%d %H:%M:%S',
                             field_styles: Any = coloredlogs.DEFAULT_FIELD_STYLES,
                             level_styles: Any = coloredlogs.DEFAULT_LEVEL_STYLES,
                             remove_existing_handlers: bool = True) -> logging.Handler:
    """
    # https://coloredlogs.readthedocs.io/en/latest/api.html

    >>> logger=logging.getLogger()
    >>> handler = add_stream_handler_color()
    >>> logger.debug("DEBUG")
    >>> logger.info("INFO")
    >>> logger.warning("WARNING")
    >>> logger.error("ERROR")
    >>> logger.critical("CRITICAL")

    """
    if remove_existing_handlers:
        remove_all_handlers(logger=logger)

    if not exists_handler_with_name(name):
        fmt = override_via_environment(fmt, 'COLOREDLOGS_LOG_FORMAT')
        if hasattr(fmt, 'format'):
            fmt = fmt.format(username=getpass.getuser())
        datefmt = override_via_environment(datefmt, 'COLOREDLOGS_DATE_FORMAT')
        field_styles = override_via_environment(field_styles, 'COLOREDLOGS_FIELD_STYLES')
        level_styles = override_via_environment(level_styles, 'COLOREDLOGS_LEVEL_STYLES')
        coloredlogs.install(logger=logger, level=level, fmt=fmt, datefmt=datefmt, field_styles=field_styles, level_styles=level_styles, isatty=True)
        logger.handlers[-1].name = name
        handler = logger.handlers[-1]
    else:
        handler = get_handler_by_name(name=name)
    return handler


def override_via_environment(original_value: Any, environment_variable: str) -> Any:
    if environment_variable in os.environ:
        return_value = None
    else:
        return_value = original_value
    return return_value


def _add_handler(handler: logging.Handler,
                 logger: logging.Logger = logging.getLogger(),
                 name: str = 'stream_handler',
                 level: int = logging.INFO,
                 fmt: str = '[{username}@%(hostname)s][%(asctime)s][%(levelname)-8s]: %(message)s',
                 datefmt: str = '%Y-%m-%d %H:%M:%S',
                 remove_existing_handlers: bool = True) -> logging.Handler:

    """
    >>> result = add_stream_handler()

    """
    if remove_existing_handlers:
        remove_all_handlers(logger=logger)

    if not exists_handler_with_name(name):
        handler.addFilter(HostnameFilter())
        fmt = fmt.format(username=getpass.getuser())
        formatter = logging.Formatter(fmt, datefmt)
        handler.setFormatter(formatter)
        handler.setLevel(level)
        handler.name = name
        logger.addHandler(handler)
        return handler
    else:
        raise ValueError('Handler "{name}" already exists'.format(name=name))


def get_handler_by_name(name: str) -> logging.Handler:
    """
    >>> import unittest
    >>> logger = add_stream_handler()
    >>> unittest.TestCase().assertIsNotNone(get_handler_by_name, ['console_handler'])
    >>> unittest.TestCase().assertRaises(ValueError, get_handler_by_name, ['unknown_handler'])

    """

    handlers = logging.getLogger().handlers
    for handler in handlers:
        if hasattr(handler, 'name'):
            if handler.name == name:
                return handler
    raise ValueError('Logging Handler "{name}" not found'.format(name=name))


def remove_handler_by_name(name: str) -> None:
    handler = get_handler_by_name(name=name)
    logging.getLogger().removeHandler(handler)


def remove_all_handlers(logger: logging.Logger = logging.getLogger()) -> None:
    handlers = logger.handlers
    for handler in handlers:
        logger.removeHandler(handler)


def exists_handler_with_name(name: str) -> bool:
    handlers = logging.getLogger().handlers
    for handler in handlers:
        if hasattr(handler, 'name'):
            if handler.name == name:
                return True
    return False


def logger_flush_all_handlers() -> None:
    """
    >>> logger_flush_all_handlers()

    """
    flush_logger = logging.getLogger()
    for handler in flush_logger.handlers:
        if hasattr(handler, 'flush'):
            handler.flush()


class SaveLogHandlerFormatter(object):
    """
    """
    '''
    >>> # those tests dont run on pytest
    >>> import lib_doctest_pycharm
    >>> lib_doctest_pycharm.setup_doctest_logger_for_pycharm()
    >>> logger=logging.getLogger()
    >>> logger.info('test')
    test
    >>> handler = get_handler_by_name('doctest_console_handler')

    >>> log_handler_formatter_save = SaveLogHandlerFormatter(handler=handler)
    >>> set_log_handler_formatter_prefix(handler=handler, log_formatter_prefix='test4 prefix: ')
    >>> logger.info('test')
    test4 prefix: test
    >>> log_handler_formatter_save.restore()
    >>> log_handler_formatter_save.close()

    >>> with SaveLogHandlerFormatter(handler=handler):
    ...     set_log_handler_formatter_prefix(handler=handler, log_formatter_prefix='test5 prefix2: ')
    ...     logger.info('test2')
    test5 prefix2: test2

    >>> # teardown
    >>> remove_handler_by_name(name='doctest_console_handler')

    '''

    def __init__(self, handler: logging.Handler):
        self._handler = handler
        self._formatter = None          # type:  Optional[logging.Formatter]
        self.save()

    def __enter__(self) -> 'SaveLogHandlerFormatter':
        return self

    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException], exc_tb: Optional[TracebackType]) -> None:
        self.restore()
        self.close()

    def close(self) -> None:
        del self._handler
        del self._formatter

    def save(self) -> None:
        self._formatter = self._handler.formatter

    def restore(self) -> None:
        self._handler.formatter = self._formatter


def set_log_handler_formatter_prefix(handler: logging.Handler, log_formatter_prefix: str) -> None:
    if handler.formatter:
        if handler.formatter._fmt:
            handler.formatter._fmt = log_formatter_prefix + handler.formatter._fmt
            handler.formatter._style._fmt = log_formatter_prefix + handler.formatter._style._fmt
        else:
            handler.formatter._fmt = log_formatter_prefix + '%(message)s'
            handler.formatter._style._fmt = log_formatter_prefix + '%(message)s'
    else:
        datefmt = '%Y-%m-%d %H:%M:%S'
        formatter = logging.Formatter(log_formatter_prefix + '%(message)s', datefmt)
        handler.setFormatter(formatter)
