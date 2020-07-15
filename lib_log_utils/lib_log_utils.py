# STDLIB
from typing import Optional, Union

import logging
import logging.handlers
import platform
import subprocess
import sys
import textwrap
from typing import Dict

# OWN
import lib_parameter

# PROJ
# imports for local pytest
try:
    from . import log_handlers
    from . import log_levels
    from . import log_traceback
except ImportError:                 # pragma: no cover
    import log_handlers             # type: ignore # pragma: no cover
    import log_levels               # type: ignore # pragma: no cover
    import log_traceback            # type: ignore # pragma: no cover


def get_number_of_terminal_colors() -> int:
    """
    >>> if platform.system().lower() == 'windows':
    ...     assert get_number_of_terminal_colors() == 256
    ... else:
    ...    assert get_number_of_terminal_colors() == 8 or get_number_of_terminal_colors() == 256

    """
    if platform.system().lower() != 'windows':
        try:
            # my_process = subprocess.run(['tput', 'colors'], check=True, capture_output=True)
            # colors = int(my_process.stdout)
            output = subprocess.check_output(['tput', 'colors'], stderr=subprocess.PIPE)
            colors = int(output)
        except subprocess.CalledProcessError:       # pragma: no cover
            colors = 256                            # pragma: no cover
    else:
        colors = 256
    return colors


class LogSettings(object):
    """ this holds all the Logger Settings - You can overwrite that values as needed from Your module """

    use_colored_stream_handler = False

    # the format of the log message, for instance :
    # fmt = '[{username}@%(hostname)s][%(asctime)s][%(levelname)-8s]: %(message)s'.format(username=getpass.getuser())
    fmt = '%(message)s'
    # that date format
    datefmt = '%Y-%m-%d %H:%M:%S'
    # the banner width
    banner_width = 140
    # if text should be wrapped
    wrap_text = True
    # if console logging should be skipped
    quiet = False
    # if there is no logger set, we set up a new logger with level new_logger_level
    new_logger_level = logging.INFO
    # default log_level of the stream_handler that will be added, 0 = NOTSET = every message will be taken
    stream_handler_log_level = 0
    # the stream the stream_handler should use
    stream = sys.stderr

    field_styles: Dict[str, Dict[str, Union[str, bool]]] = \
        {
            'asctime': {'color': 'green'},
            'hostname': {'color': 'green'},                                   # 'hostname': {'color': 'magenta'},
            'levelname': {'color': 'yellow'},                                 # 'levelname': {'color': 'black', 'bold': True},
            'name': {'color': 'blue'},
            'programname': {'color': 'cyan'}
        }

    level_styles_256: Dict[str, Dict[str, Union[str, bool]]] = \
        {
            'spam': {'color': 'magenta', 'bright': True},                     # level 5   - SPAM
            'debug': {'color': 'blue', 'bright': True},                       # level 10  - DEBUG
            'verbose': {'color': 'yellow', 'bright': True},                   # level 15  - VERBOSE
            'info': {},                                                       # level 20  - INFO
            'notice': {'background': 'magenta', 'bright': True},              # level 25  - NOTICE
            'warning': {'color': 'red', 'bright': True},                      # level 30  - WARNING
            'success': {'color': 'green', 'bright': True},                    # level 35  - SUCCESS
            'error': {'background': 'red', 'bright': True},                   # level 40  - ERROR
            'critical': {'background': 'red'}                                 # level 50  - CRITICAL  # type: Dict[str, Dict[str, Any]]
        }

    level_styles_8: Dict[str, Dict[str, Union[str, bool]]] = \
        {
            'spam': {'color': 'magenta', 'bold': True},                         # level 5   - SPAM
            'debug': {'color': 'blue', 'bold': True},                           # level 10  - DEBUG
            'verbose': {'color': 'yellow', 'bold': True},                       # level 15  - VERBOSE
            'info': {},                                                         # level 20  - INFO
            'notice': {'background': 'magenta', 'bold': True},                  # level 25  - NOTICE
            'warning': {'color': 'red', 'bold': True},                          # level 30  - WARNING
            'success': {'color': 'green', 'bold': True},                        # level 35  - SUCCESS
            'error': {'background': 'red'},                                     # level 40  - ERROR
            'critical': {'background': 'red', 'bold': True}                    # level 50  - CRITICAL  # type: Dict[str, Dict[str, Any]]
        }

    if get_number_of_terminal_colors() == 8:
        level_styles = level_styles_8
    else:
        level_styles = level_styles_256


def banner_spam(message: str,
                banner_width: Optional[int] = None,
                wrap_text: Optional[bool] = None,
                logger: Optional[logging.Logger] = None,
                quiet: Optional[bool] = None,
                ) -> None:
    """ logs a banner SPAM """
    banner_level(message=message, level=log_levels.SPAM, banner_width=banner_width, wrap_text=wrap_text, logger=logger, quiet=quiet)


def banner_debug(message: str,
                 banner_width: Optional[int] = None,
                 wrap_text: Optional[bool] = None,
                 logger: Optional[logging.Logger] = None,
                 quiet: Optional[bool] = None,
                 ) -> None:
    """ logs a banner DEBUG """
    banner_level(message=message, level=logging.DEBUG, banner_width=banner_width, wrap_text=wrap_text, logger=logger, quiet=quiet)


def banner_verbose(message: str,
                   banner_width: Optional[int] = None,
                   wrap_text: Optional[bool] = None,
                   logger: Optional[logging.Logger] = None,
                   quiet: Optional[bool] = None,
                   ) -> None:
    """ logs a banner VERBOSE """
    banner_level(message=message, level=log_levels.VERBOSE, banner_width=banner_width, wrap_text=wrap_text, logger=logger, quiet=quiet)


def banner_info(message: str,
                banner_width: Optional[int] = None,
                wrap_text: Optional[bool] = None,
                logger: Optional[logging.Logger] = None,
                quiet: Optional[bool] = None,
                ) -> None:
    """ logs a banner INFO """
    banner_level(message=message, level=logging.INFO, banner_width=banner_width, wrap_text=wrap_text, logger=logger, quiet=quiet)


def banner_notice(message: str,
                  banner_width: Optional[int] = None,
                  wrap_text: Optional[bool] = None,
                  logger: Optional[logging.Logger] = None,
                  quiet: Optional[bool] = None,
                  ) -> None:
    """ logs a banner NOTICE """
    banner_level(message=message, level=log_levels.NOTICE, banner_width=banner_width, wrap_text=wrap_text, logger=logger, quiet=quiet)


def banner_success(message: str,
                   banner_width: Optional[int] = None,
                   wrap_text: Optional[bool] = None,
                   logger: Optional[logging.Logger] = None,
                   quiet: Optional[bool] = None,
                   ) -> None:
    """ logs a banner SUCCESS """
    banner_level(message=message, level=log_levels.SUCCESS, banner_width=banner_width, wrap_text=wrap_text, logger=logger, quiet=quiet)


def banner_warning(message: str,
                   banner_width: Optional[int] = None,
                   wrap_text: Optional[bool] = None,
                   logger: Optional[logging.Logger] = None,
                   quiet: Optional[bool] = None,
                   ) -> None:
    """ logs a banner WARNING """
    banner_level(message=message, level=logging.WARNING, banner_width=banner_width, wrap_text=wrap_text, logger=logger, quiet=quiet)


def banner_error(message: str,
                 banner_width: Optional[int] = None,
                 wrap_text: Optional[bool] = None,
                 logger: Optional[logging.Logger] = None,
                 quiet: Optional[bool] = None,
                 ) -> None:
    """ logs a banner ERROR """
    banner_level(message=message, level=logging.ERROR, banner_width=banner_width, wrap_text=wrap_text, logger=logger, quiet=quiet)


def banner_critical(message: str,
                    banner_width: Optional[int] = None,
                    wrap_text: Optional[bool] = None,
                    logger: Optional[logging.Logger] = None,
                    quiet: Optional[bool] = None,
                    ) -> None:
    """ logs a banner CRITICAL """
    banner_level(message=message, level=logging.CRITICAL, banner_width=banner_width, wrap_text=wrap_text, logger=logger, quiet=quiet)


def banner_level(message: str,
                 level: Optional[int] = None,
                 banner_width: Optional[int] = None,
                 wrap_text: Optional[bool] = None,
                 logger: Optional[logging.Logger] = None,
                 quiet: Optional[bool] = None,
                 ) -> None:
    """
    logs a banner LEVEL



    Examples
    --------

    >>> LogSettings.use_colored_stream_handler = True
    >>> # noinspection PyUnresolvedReferences
    >>> banner_level('test')
    >>> banner_level('test', logging.SUCCESS, wrap_text=True)  # noqa
    >>> banner_level('test', logging.ERROR, wrap_text=True)
    >>> banner_level('test', logging.ERROR, wrap_text=False)
    >>> banner_level('this is\\none nice piece of ham\\none nice piece of spam\\none more piece of wonderful spam', \
                     logging.ERROR, banner_width=10, wrap_text=True)
    >>> banner_level('this is\\none nice piece of ham\\none nice piece of spam\\none more piece of wonderful spam', \
                     logging.ERROR, banner_width=10, wrap_text=False)
    >>> banner_spam('spam')
    >>> banner_critical('critical')
    >>> banner_debug('debug')
    >>> banner_error('error')
    >>> banner_info('info')
    >>> banner_notice('notice')
    >>> banner_spam('spam')
    >>> banner_success('success')
    >>> banner_verbose('verbose')
    >>> banner_warning('warning')
    """

    quiet = lib_parameter.get_default_if_none(quiet, default=LogSettings.quiet)

    if quiet:
        return

    message = str(message)

    if logger is None:
        logger = logging.getLogger()
        logger.level = LogSettings.new_logger_level
        setup_handler(logger)

    level = lib_parameter.get_default_if_none(level, default=logging.INFO)
    banner_width = lib_parameter.get_default_if_none(banner_width, default=LogSettings.banner_width)
    wrap_text = lib_parameter.get_default_if_none(wrap_text, default=LogSettings.wrap_text)

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


def log_spam(message: str,
             banner_width: Optional[int] = None,
             wrap_text: Optional[bool] = None,
             logger: Optional[logging.Logger] = None,
             quiet: Optional[bool] = None,
             ) -> None:

    log_level(message=message, level=log_levels.SPAM, banner_width=banner_width, wrap_text=wrap_text, logger=logger, quiet=quiet)


def log_debug(message: str,
              banner_width: Optional[int] = None,
              wrap_text: Optional[bool] = None,
              logger: Optional[logging.Logger] = None,
              quiet: Optional[bool] = None,
              ) -> None:
    log_level(message=message, level=logging.DEBUG, banner_width=banner_width, wrap_text=wrap_text, logger=logger, quiet=quiet)


def log_verbose(message: str,
                banner_width: Optional[int] = None,
                wrap_text: Optional[bool] = None,
                logger: Optional[logging.Logger] = None,
                quiet: Optional[bool] = None,
                ) -> None:
    log_level(message=message, level=log_levels.VERBOSE, banner_width=banner_width, wrap_text=wrap_text, logger=logger, quiet=quiet)


def log_info(message: str,
             banner_width: Optional[int] = None,
             wrap_text: Optional[bool] = None,
             logger: Optional[logging.Logger] = None,
             quiet: Optional[bool] = None,
             ) -> None:
    log_level(message=message, level=logging.INFO, banner_width=banner_width, wrap_text=wrap_text, logger=logger, quiet=quiet)


def log_notice(message: str,
               banner_width: Optional[int] = None,
               wrap_text: Optional[bool] = None,
               logger: Optional[logging.Logger] = None,
               quiet: Optional[bool] = None,
               ) -> None:
    log_level(message=message, level=log_levels.NOTICE, banner_width=banner_width, wrap_text=wrap_text, logger=logger, quiet=quiet)


def log_success(message: str,
                banner_width: Optional[int] = None,
                wrap_text: Optional[bool] = None,
                logger: Optional[logging.Logger] = None,
                quiet: Optional[bool] = None,
                ) -> None:
    log_level(message=message, level=log_levels.SUCCESS, banner_width=banner_width, wrap_text=wrap_text, logger=logger, quiet=quiet)


def log_warning(message: str,
                banner_width: Optional[int] = None,
                wrap_text: Optional[bool] = None,
                logger: Optional[logging.Logger] = None,
                quiet: Optional[bool] = None,
                ) -> None:
    log_level(message=message, level=logging.WARNING, banner_width=banner_width, wrap_text=wrap_text, logger=logger, quiet=quiet)


def log_error(message: str,
              banner_width: Optional[int] = None,
              wrap_text: Optional[bool] = None,
              logger: Optional[logging.Logger] = None,
              quiet: Optional[bool] = None,
              ) -> None:
    log_level(message=message, level=logging.ERROR, banner_width=banner_width, wrap_text=wrap_text, logger=logger, quiet=quiet)


def log_critical(message: str,
                 banner_width: Optional[int] = None,
                 wrap_text: Optional[bool] = None,
                 logger: Optional[logging.Logger] = None,
                 quiet: Optional[bool] = None,
                 ) -> None:
    log_level(message=message, level=logging.CRITICAL, banner_width=banner_width, wrap_text=wrap_text, logger=logger, quiet=quiet)


def log_level(message: str,
              level: Optional[int] = None,
              banner_width: Optional[int] = None,
              wrap_text: Optional[bool] = None,
              logger: Optional[logging.Logger] = None,
              quiet: Optional[bool] = None,
              ) -> None:

    """
    >>> log_level('test')
    >>> log_level('test', logging.SUCCESS, wrap_text=True)  # noqa
    >>> log_level('test', logging.ERROR, wrap_text=True)
    >>> log_level('test', logging.ERROR, wrap_text=False)
    >>> log_level('this is\\none nice piece of ham\\none nice piece of spam\\none more piece of wonderful spam', \
                   logging.ERROR, banner_width=10, wrap_text=True)
    >>> log_level('this is\\none nice piece of ham\\none nice piece of spam\\none more piece of wonderful spam', \
                   logging.ERROR, banner_width=10, wrap_text=False)
    >>> log_spam('spam')
    >>> log_critical('critical')
    >>> log_debug('debug')
    >>> log_error('error')
    >>> log_info('info')
    >>> log_notice('notice')
    >>> log_spam('spam')
    >>> log_success('success')
    >>> log_verbose('verbose')
    >>> log_warning('warning')

    """

    quiet = bool(lib_parameter.get_default_if_none(quiet, default=LogSettings.quiet))

    if quiet:
        return

    level = int(lib_parameter.get_default_if_none(level, default=LogSettings.new_logger_level))
    banner_width = int(lib_parameter.get_default_if_none(banner_width, default=LogSettings.banner_width))
    wrap_text = bool(lib_parameter.get_default_if_none(wrap_text, default=LogSettings.wrap_text))

    if logger is None:
        logger = logging.getLogger()
        logger.level = LogSettings.new_logger_level
        setup_handler(logger)

    message = str(message)

    l_message = message.split('\n')
    for line in l_message:
        if wrap_text:
            l_wrapped_lines = textwrap.wrap(line, width=banner_width, tabsize=4, replace_whitespace=False)
            for msg_line in l_wrapped_lines:
                logger.log(level=level, msg=msg_line)
        else:
            msg_line = line.rstrip()
            logger.log(level=level, msg=msg_line)


def colortest(quiet: bool = False) -> None:
    """ test banner colors

    >>> LogSettings.use_colored_stream_handler=True
    >>> LogSettings.new_logger_level = 0
    >>> LogSettings.stream_handler_log_level = 0
    >>> LogSettings.stream = sys.stdout
    >>> colortest()
    ***...***
    >>> colortest(quiet=True)
    >>> # TearDown
    >>> LogSettings.stream = sys.stderr

    """
    if not quiet:
        banner_spam('test level spam')
        banner_debug('test level debug')
        banner_verbose('test level verbose')
        banner_info('test level info')
        banner_notice('test level notice')
        banner_success('test level success')
        banner_warning('test level warning')
        banner_error('test level error')
        banner_critical('test level critical')


def setup_handler(logger: logging.Logger) -> None:
    if LogSettings.use_colored_stream_handler:
        log_handlers.set_stream_handler_color(logger=logger,
                                              level=LogSettings.stream_handler_log_level,
                                              fmt=LogSettings.fmt,
                                              datefmt=LogSettings.datefmt,
                                              field_styles=LogSettings.field_styles,
                                              level_styles=LogSettings.level_styles,
                                              stream=LogSettings.stream,
                                              remove_existing_stream_handlers=False)
    else:
        log_handlers.set_stream_handler(logger=logger,
                                        level=LogSettings.stream_handler_log_level,
                                        fmt=LogSettings.fmt,
                                        datefmt=LogSettings.datefmt,
                                        stream=LogSettings.stream,
                                        remove_existing_stream_handlers=False)
