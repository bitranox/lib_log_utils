# STDLIB
import logging
import logging.handlers
import sys
import traceback

# OWN
import lib_cast
import lib_parameter


def log_exception_traceback(s_error: str, log_level: int = logging.ERROR, log_level_exec_info: int = None, log_level_traceback: int = None) -> str:
    logger = logging.getLogger()
    log_level_exec_info = lib_parameter.get_default_if_none(log_level_exec_info, log_level)
    log_level_traceback = lib_parameter.get_default_if_none(log_level_traceback, log_level_exec_info)

    if s_error and log_level > logging.NOTSET:
        logger.log(level=log_level, msg=s_error)

    if log_level_exec_info > logging.NOTSET:
        exc_info = sys.exc_info()[1]
        exc_info_type = lib_cast.get_type_as_string(exc_info)
        exc_info_msg = exc_info_type + ': ' + str(exc_info)
        logger.log(level=log_level_exec_info, msg=exc_info_msg)

    if log_level_traceback > logging.NOTSET:
        s_traceback = 'Traceback Information : \n' + traceback.format_exc()
        s_traceback = s_traceback.rstrip('\n')
        logger.log(level=log_level_traceback, msg=s_traceback)
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


def test_log_util():
    """
    >>> import lib_doctest_pycharm
    >>> lib_doctest_pycharm.setup_doctest_logger_for_pycharm(log_level=logging.DEBUG)
    >>> test_log_util() # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
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


def test_log_util_reraise():
    """
    >>> import lib_doctest_pycharm
    >>> lib_doctest_pycharm.setup_doctest_logger_for_pycharm(log_level=logging.DEBUG)
    >>> test_log_util_reraise()  # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
    ...
    RuntimeError: Fehler

    """
    try:
        xxx = 1 / 0
        return xxx
    except ZeroDivisionError as exc:
        s_error = log_exception_traceback('Fehler', log_level=logging.WARNING, log_level_exec_info=logging.INFO, log_level_traceback=logging.INFO)
        raise RuntimeError(s_error) from exc


def setup_console_logger(level: int = logging.INFO):
    """
    >>> setup_console_logger()

    """
    console = logging.StreamHandler(stream=sys.stdout)
    console.setLevel(level)
    datefmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter('[%(asctime)s] %(levelname)-8s: %(message)s', datefmt)
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)
    logging.getLogger().setLevel(level)


def setup_console_logger_simple(level: int = logging.INFO):
    """
    >>> setup_console_logger()

    """
    console = logging.StreamHandler(stream=sys.stdout)
    console.setLevel(level)
    formatter = logging.Formatter('%(message)s')
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)
    logging.getLogger().setLevel(level)


def setup_console_logger_like_yaml_short(level: int = logging.INFO):
    console = logging.StreamHandler(stream=sys.stdout)
    console.setLevel(level)
    datefmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter('[%(asctime)s] %(levelname)-8s: %(name)-60s: %(message)s', datefmt)
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)
    logging.getLogger().setLevel(level)


def logger_flush_all_handlers():
    flush_logger = logging.getLogger()
    for handler in flush_logger.handlers:
        if hasattr(handler, 'flush'):
            handler.flush()


class LogAllHandlersFormatterSave(object):
    """
    >>> import lib_doctest_pycharm
    >>> logger=logging.getLogger()
    >>> lib_doctest_pycharm.setup_doctest_logger_for_pycharm()
    >>> logger.info('test')
    test
    >>> log_all_handlers_formatter_save = LogAllHandlersFormatterSave()
    >>> log_all_handlers_formatter_save.save()
    >>> set_all_log_handlers_formatter_prefix(log_formatter_prefix='test prefix: ')
    >>> logger.info('test')
    test prefix: test
    >>> log_all_handlers_formatter_save.restore()
    >>> log_all_handlers_formatter_save.close()

    >>> with LogAllHandlersFormatterSave():
    ...     set_all_log_handlers_formatter_prefix(log_formatter_prefix='test prefix2: ')
    ...     logger.info('test2')
    test prefix2: test2

    >>> setup_console_logger()
    >>> with LogAllHandlersFormatterSave():
    ...     set_all_log_handlers_formatter_prefix(log_formatter_prefix='test prefix3: ')
    ...     logger.info('test3')  # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
    test prefix3: test3
    test prefix3: [...] INFO    : test3

    """

    def __init__(self):
        self._hash_formatter_by_handler = dict()

    def __enter__(self):
        self.save()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.restore()
        self.close()

    def close(self):
        del self._hash_formatter_by_handler

    def save(self):
        self.__init__()
        _logger = logging.getLogger()
        for handler in _logger.handlers:
            self._hash_formatter_by_handler[handler] = handler.formatter

    def restore(self):
        for handler, formatter in self._hash_formatter_by_handler.items():
            handler.formatter = formatter


class LogHandlerFormatterSave(object):
    """
    >>> import lib_doctest_pycharm
    >>> logger=logging.getLogger()
    >>> lib_doctest_pycharm.setup_doctest_logger_for_pycharm()
    >>> logger.info('test')
    test
    >>> handler = logger.handlers[0]

    >>> log_handler_formatter_save = LogHandlerFormatterSave(handler=handler)
    >>> set_log_handler_formatter_prefix(handler=handler, log_formatter_prefix='test prefix: ')
    >>> logger.info('test')
    test prefix: test
    >>> log_handler_formatter_save.restore()
    >>> log_handler_formatter_save.close()

    >>> with LogHandlerFormatterSave(handler=handler):
    ...     set_log_handler_formatter_prefix(handler=handler, log_formatter_prefix='test prefix2: ')
    ...     logger.info('test2')
    test prefix2: test2

    >>> setup_console_logger()
    >>> handler = logger.handlers[1]
    >>> with LogHandlerFormatterSave(handler=handler):
    ...     set_log_handler_formatter_prefix(handler=handler, log_formatter_prefix='test prefix3: ')
    ...     logger.info('test3')  # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
    test3
    test prefix3: [...] INFO    : test3

    """

    def __init__(self, handler):
        self._handler = handler
        self._formatter = None
        self.save()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.restore()
        self.close()

    def close(self):
        del self._handler
        del self._formatter

    def save(self):
        self._formatter = self._handler.formatter

    def restore(self):
        self._handler.formatter = self._formatter


def set_all_log_handlers_formatter_prefix(log_formatter_prefix: str):
    _logger = logging.getLogger()
    for handler in _logger.handlers:
        set_log_handler_formatter_prefix(handler, log_formatter_prefix)


def set_log_handler_formatter_prefix(handler, log_formatter_prefix: str):
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

    def __init__(self, queue, message_prefix: str):
        self._message_prefix = message_prefix
        super().__init__(queue)

    def prepare(self, record):
        self.format(record)
        record.msg = self._message_prefix + record.message
        record.args = None
        record.exc_info = None
        return record

    def enqueue(self, record):
        """ only put the messages from the own connection to the queue (for threaded server) """
        # noinspection PyBroadException
        try:
            self.queue.put_nowait(record)
        except Exception:  # wenn die queue nicht mehr existiert
            pass
