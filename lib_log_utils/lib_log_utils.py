# STDLIB
import logging
import logging.handlers
import getpass
import multiprocessing
import os
import platform
import sys
import textwrap
import traceback
from types import TracebackType
from typing import Any, Dict, Optional, Type

# EXT
import coloredlogs      # type: ignore

# OWN
import lib_cast
import lib_parameter


class HostnameFilter(logging.Filter):
    hostname = platform.node()

    def filter(self, record: Any) -> bool:
        record.hostname = HostnameFilter.hostname
        return True


def setup_console_logger_color(logger: logging.Logger = logging.getLogger(),
                               name: str = 'console_logger',
                               level: int = logging.INFO,
                               fmt: str = '[{username}@%(hostname)s][%(asctime)s][%(levelname)-8s]: %(message)s',
                               datefmt: str = '%Y-%m-%d %H:%M:%S',
                               field_styles: Any = coloredlogs.DEFAULT_FIELD_STYLES,
                               level_styles: Any = coloredlogs.DEFAULT_LEVEL_STYLES) -> logging.Logger:
    """
    # https://coloredlogs.readthedocs.io/en/latest/api.html

    >>> logger=setup_console_logger_color()
    >>> logger.debug("DEBUG")
    >>> logger.info("INFO")
    >>> logger.warning("WARNING")
    >>> logger.error("ERROR")
    >>> logger.critical("CRITICAL")

    """
    remove_all_handlers(logger=logger)
    fmt = fmt.format(username=getpass.getuser())
    os.environ['COLOREDLOGS_LOG_FORMAT'] = fmt
    coloredlogs.install(logger=logger, level=level, fmt=fmt, datefmt=datefmt, field_styles=field_styles, level_styles=level_styles)
    logger.handlers[0].name = name
    return logger


def setup_console_logger(logger: logging.Logger = logging.getLogger(),
                         name: str = 'console_handler',
                         level: int = logging.INFO,
                         fmt: str = '[{username}@%(hostname)s][%(asctime)s][%(levelname)-8s]: %(message)s',
                         datefmt: str = '%Y-%m-%d %H:%M:%S') -> logging.Logger:
    """
    >>> logger = setup_console_logger()

    """
    remove_all_handlers(logger=logger)
    fmt = fmt.format(username=getpass.getuser())
    console_handler = setup_stream_handler(name=name)
    console_handler.addFilter(HostnameFilter())
    console_handler.setLevel(level)
    formatter = logging.Formatter(fmt, datefmt)
    console_handler.setFormatter(formatter)
    logger.setLevel(level)
    return logger


def add_file_handler(filename: str,
                     logger: logging.Logger = logging.getLogger(),
                     name: str = '',
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
    if not name:
        name = filename

    if not exists_handler_with_name(name):
        file_handler = logging.FileHandler(filename=filename, mode=mode, encoding=encoding, delay=delay)   # type: logging.Handler
        file_handler.name = name
        logger.addHandler(file_handler)
    else:
        file_handler = get_handler_by_name(name)
    return file_handler


def banner(level: int, message: str, banner_width: int = 140, wrap_text: bool = True, logger: logging.Logger = logging.getLogger()) -> None:
    """
    >>> banner(logging.ERROR, 'test', wrap_text=True)
    >>> banner(logging.ERROR, 'test', wrap_text=False)
    >>> banner(logging.ERROR, 'das is\\ndas ist\\ndas ist   ein   test\\ndas ist   ein   weiterer test', banner_width=10, wrap_text=True)
    >>> banner(logging.ERROR, 'das is\\ndas ist\\ndas ist   ein   test\\ndas ist   ein   weiterer test', banner_width=10, wrap_text=False)

    """
    sep_line = '*' * banner_width
    l_message = message.split('\n')
    logger.log(level=level, msg=sep_line)  # 140 characters is about the width in travis log screen
    for line in l_message:
        if wrap_text:
            l_wrapped_lines = textwrap.wrap(line, width=banner_width - 2, tabsize=4, replace_whitespace=False, initial_indent='* ', subsequent_indent='* ')
            for wrapped_line in l_wrapped_lines:
                msg_line = wrapped_line + (banner_width - len(wrapped_line) - 1) * ' ' + '*'
                logger.log(level=level, msg=msg_line)
        else:
            line = "* " + line.rstrip()
            if len(line) < banner_width - 1:
                line = line + (banner_width - len(line) - 1) * ' ' + '*'
            logger.log(level=level, msg=line)
    logger.log(level=level, msg=sep_line)


def log_exception_traceback(s_error: str, log_level: int = logging.ERROR,
                            log_level_exec_info: Optional[int] = None,
                            log_level_traceback: Optional[int] = None) -> str:
    logger = logging.getLogger()
    log_level_exec_info = lib_parameter.get_default_if_none(log_level_exec_info, log_level)
    log_level_traceback = lib_parameter.get_default_if_none(log_level_traceback, log_level_exec_info)

    if s_error and log_level != logging.NOTSET:
        logger.log(level=log_level, msg=s_error)

    if log_level_exec_info != logging.NOTSET:
        exc_info = sys.exc_info()[1]
        exc_info_type = lib_cast.get_type_as_string(exc_info)
        exc_info_msg = exc_info_type + ': ' + str(exc_info)
        logger.log(level=log_level_exec_info, msg=exc_info_msg)     # type: ignore

    if log_level_traceback != logging.NOTSET:
        s_traceback = 'Traceback Information : \n' + traceback.format_exc()
        s_traceback = s_traceback.rstrip('\n')
        logger.log(level=log_level_traceback, msg=s_traceback)      # type: ignore
    logger_flush_all_handlers()
    return s_error  # to use it as input for re-raising


def print_exception_traceback(s_error: str) -> str:
    print(s_error)
    exc_info = sys.exc_info()[1]
    exc_info_type = lib_cast.get_type_as_string(exc_info)
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


def setup_stream_handler(name: str = 'console_handler') -> logging.Handler:
    if not exists_handler_with_name(name):
        console_handler = logging.StreamHandler(stream=sys.stdout)      # type: logging.Handler
        console_handler.name = name
        logging.getLogger().addHandler(console_handler)
    else:
        console_handler = get_handler_by_name(name)
    return console_handler


def setup_console_logger_simple(level: int = logging.INFO, name: str = 'console_handler') -> None:
    """
    >>> setup_console_logger_simple()

    """
    console_handler = setup_stream_handler(name=name)
    console_handler.setLevel(level)
    formatter = logging.Formatter('%(message)s')
    console_handler.setFormatter(formatter)


def setup_console_logger_like_yaml_short(level: int = logging.INFO, name: str = 'console_handler') -> None:
    """
    >>> setup_console_logger_like_yaml_short()

    """

    console_handler = setup_stream_handler(name=name)
    console_handler.setLevel(level)
    datefmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter('[%(asctime)s] %(levelname)-8s: %(name)-60s: %(message)s', datefmt)
    console_handler.setFormatter(formatter)
    logging.getLogger().setLevel(level)


def get_handler_by_name(name: str) -> logging.Handler:
    """
    >>> import unittest
    >>> logger = setup_console_logger()
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


class LogAllHandlersFormatterSave(object):
    """
    """
    '''
    >>> # those tests dont run pytest
    >>> import lib_doctest_pycharm
    >>> logger=logging.getLogger()
    >>> lib_doctest_pycharm.setup_doctest_logger_for_pycharm()
    >>> logger.info('test')
    test
    >>> log_all_handlers_formatter_save = LogAllHandlersFormatterSave()
    >>> log_all_handlers_formatter_save.save()
    >>> set_all_log_handlers_formatter_prefix(log_formatter_prefix='test1 prefix: ')
    >>> logger.info('test')
    test1 prefix: test
    >>> log_all_handlers_formatter_save.restore()
    >>> log_all_handlers_formatter_save.close()

    >>> with LogAllHandlersFormatterSave():
    ...     set_all_log_handlers_formatter_prefix(log_formatter_prefix='test2 prefix2: ')
    ...     logger.info('test2')
    test2 prefix2: test2

    >>> # teardown
    >>> remove_handler_by_name(name='doctest_console_handler')

    '''

    def __init__(self) -> None:
        self._hash_formatter_by_handler = dict()        # type: Dict[logging.Handler, Optional[logging.Formatter]]

    def __enter__(self) -> 'LogAllHandlersFormatterSave':
        self.save()
        return self

    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException], exc_tb: Optional[TracebackType]) -> None:
        self.restore()
        self.close()

    def close(self) -> None:
        del self._hash_formatter_by_handler

    def save(self) -> None:
        _logger = logging.getLogger()
        for handler in _logger.handlers:
            self._hash_formatter_by_handler[handler] = handler.formatter

    def restore(self) -> None:
        for handler, old_formatter in self._hash_formatter_by_handler.items():
            handler.formatter = old_formatter


class LogHandlerFormatterSave(object):
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

    >>> log_handler_formatter_save = LogHandlerFormatterSave(handler=handler)
    >>> set_log_handler_formatter_prefix(handler=handler, log_formatter_prefix='test4 prefix: ')
    >>> logger.info('test')
    test4 prefix: test
    >>> log_handler_formatter_save.restore()
    >>> log_handler_formatter_save.close()

    >>> with LogHandlerFormatterSave(handler=handler):
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

    def __enter__(self) -> 'LogHandlerFormatterSave':
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


def set_all_log_handlers_formatter_prefix(log_formatter_prefix: str) -> None:
    _logger = logging.getLogger()
    for handler in _logger.handlers:
        set_log_handler_formatter_prefix(handler, log_formatter_prefix)


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


class RpycQueueHandler(logging.handlers.QueueHandler):
    """ Log Queue handler - fügt einen Prefix (die RPYC Server informationen) der Log Message hinzu
    Que Handler ist allerdings Ressourcenintensiv und funktioniert am Threaded Rpyc Server schlecht,
    die Queue muss immer offen gehalten werden. ---> versuchen wir besser SocketHandler, dann braucht der
    Client auch nur immer EINEN SocketListener, egal mit wievielen Servern er verbunden ist !
    """

    def __init__(self, queue: multiprocessing.Queue, message_prefix: str):  # type: ignore
        self._message_prefix = message_prefix
        super().__init__(queue)

    # noinspection PyTypeHints
    def prepare(self, record: logging.LogRecord) -> logging.LogRecord:
        self.format(record)
        record.msg = self._message_prefix + record.message
        record.args = None                  # type: ignore
        record.exc_info = None
        record.exc_text = None
        return record

    def enqueue(self, record: logging.LogRecord) -> None:
        """ only put the messages from the own connection to the queue (for threaded server) """
        # noinspection PyBroadException
        try:
            self.queue.put_nowait(record)   # type: ignore
        except Exception:  # wenn die queue nicht mehr existiert
            pass
