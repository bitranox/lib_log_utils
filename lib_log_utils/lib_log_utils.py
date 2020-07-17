# STDLIB
from typing import Optional, Union

import logging
import logging.handlers
import os
import platform
import subprocess
import sys
import textwrap
from typing import Dict

# EXT
import humanfriendly.cli            # type: ignore

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
    tries to detect the number of colors - selects 8 colors for travis automatically

    >>> # test Windows / Linux
    >>> if platform.system().lower() == 'windows':
    ...     assert get_number_of_terminal_colors() > 0
    ... else:
    ...     assert get_number_of_terminal_colors() > 0

    >>> # Test Travis
    >>> if 'TRAVIS' in os.environ:
    ...    assert get_number_of_terminal_colors() > 0
    ...    save_travis_env = os.environ['TRAVIS']
    ...    discard = os.environ.pop('TRAVIS', None)
    ...    assert get_number_of_terminal_colors() > 0
    ...    os.environ['TRAVIS'] = save_travis_env
    ... else:
    ...    os.environ['TRAVIS'] = 'true'
    ...    assert get_number_of_terminal_colors() == 8
    ...    discard = os.environ.pop('TRAVIS', None)



    """
    if 'TRAVIS' in os.environ:
        # note that there will be no colored output on travis, as soon as
        # a secret is in travis.yaml, since then the output is filtered.
        # see also : https://travis-ci.community/t/ansi-colors-in-console-does-not-work-anymore/6608
        if os.environ['TRAVIS'].lower() == 'true':
            colors = 8
            return colors

    if platform.system().lower() != 'windows':
        try:
            # capture_output not under python 3.6 !
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

    use_colored_stream_handler = True

    # the format of the log message, for instance :
    # fmt = '[{username}@%(hostname)s][%(asctime)s][%(levelname)-8s]: %(message)s'.format(username=getpass.getuser())
    fmt = '%(message)s'
    # that date format
    datefmt = '%Y-%m-%d %H:%M:%S'
    # the banner width
    width = 140
    # if text should be wrapped
    wrap = True
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
            'critical': {'background': 'red', 'bold': True}                     # level 50  - CRITICAL  # type: Dict[str, Dict[str, Any]]
        }

    if get_number_of_terminal_colors() == 8:
        level_styles = level_styles_8
    else:
        level_styles = level_styles_256


def banner_spam(message: str,
                width: Optional[int] = None,
                wrap: Optional[bool] = None,
                logger: Optional[logging.Logger] = None,
                quiet: Optional[bool] = None,
                ) -> None:
    """
    logs a banner SPAM

    >>> banner_spam('spam')

    """
    log_level(message=message, level=log_levels.SPAM, width=width, wrap=wrap, logger=logger, quiet=quiet, banner=True)


def banner_debug(message: str,
                 width: Optional[int] = None,
                 wrap: Optional[bool] = None,
                 logger: Optional[logging.Logger] = None,
                 quiet: Optional[bool] = None,
                 ) -> None:
    """
    logs a banner DEBUG

    >>> banner_debug('debug')

    """
    log_level(message=message, level=logging.DEBUG, width=width, wrap=wrap, logger=logger, quiet=quiet, banner=True)


def banner_verbose(message: str,
                   width: Optional[int] = None,
                   wrap: Optional[bool] = None,
                   logger: Optional[logging.Logger] = None,
                   quiet: Optional[bool] = None,
                   ) -> None:
    """
    logs a banner VERBOSE

    >>> banner_verbose('verbose')

    """
    log_level(message=message, level=log_levels.VERBOSE, width=width, wrap=wrap, logger=logger, quiet=quiet, banner=True)


def banner_info(message: str,
                width: Optional[int] = None,
                wrap: Optional[bool] = None,
                logger: Optional[logging.Logger] = None,
                quiet: Optional[bool] = None,
                ) -> None:
    """
    logs a banner INFO

    >>> banner_info('info')

    """
    log_level(message=message, level=logging.INFO, width=width, wrap=wrap, logger=logger, quiet=quiet, banner=True)


def banner_notice(message: str,
                  width: Optional[int] = None,
                  wrap: Optional[bool] = None,
                  logger: Optional[logging.Logger] = None,
                  quiet: Optional[bool] = None,
                  ) -> None:
    """
    logs a banner NOTICE

    >>> banner_notice('notice')

    """
    log_level(message=message, level=log_levels.NOTICE, width=width, wrap=wrap, logger=logger, quiet=quiet, banner=True)


def banner_success(message: str,
                   width: Optional[int] = None,
                   wrap: Optional[bool] = None,
                   logger: Optional[logging.Logger] = None,
                   quiet: Optional[bool] = None,
                   ) -> None:
    """
    logs a banner SUCCESS

    >>> banner_success('success')

    """
    log_level(message=message, level=log_levels.SUCCESS, width=width, wrap=wrap, logger=logger, quiet=quiet, banner=True)


def banner_warning(message: str,
                   width: Optional[int] = None,
                   wrap: Optional[bool] = None,
                   logger: Optional[logging.Logger] = None,
                   quiet: Optional[bool] = None,
                   ) -> None:
    """
    logs a banner WARNING

    >>> banner_warning('warning')

    """
    log_level(message=message, level=logging.WARNING, width=width, wrap=wrap, logger=logger, quiet=quiet, banner=True)


def banner_error(message: str,
                 width: Optional[int] = None,
                 wrap: Optional[bool] = None,
                 logger: Optional[logging.Logger] = None,
                 quiet: Optional[bool] = None,
                 ) -> None:
    """
    logs a banner ERROR

    >>> banner_error('error')

    """
    log_level(message=message, level=logging.ERROR, width=width, wrap=wrap, logger=logger, quiet=quiet, banner=True)


def banner_critical(message: str,
                    width: Optional[int] = None,
                    wrap: Optional[bool] = None,
                    logger: Optional[logging.Logger] = None,
                    quiet: Optional[bool] = None,
                    ) -> None:
    """
    logs a banner CRITICAL

    >>> banner_critical('critical')

    """
    log_level(message=message, level=logging.CRITICAL, width=width, wrap=wrap, logger=logger, quiet=quiet, banner=True)


def log_spam(message: str,
             width: Optional[int] = None,
             wrap: Optional[bool] = None,
             logger: Optional[logging.Logger] = None,
             quiet: Optional[bool] = None,
             ) -> None:
    """
    logs SPAM

    >>> log_spam('spam')

    """
    log_level(message=message, level=log_levels.SPAM, width=width, wrap=wrap, logger=logger, quiet=quiet)


def log_debug(message: str,
              width: Optional[int] = None,
              wrap: Optional[bool] = None,
              logger: Optional[logging.Logger] = None,
              quiet: Optional[bool] = None,
              ) -> None:
    """
    logs DEBUG

    >>> log_debug('debug')

    """
    log_level(message=message, level=logging.DEBUG, width=width, wrap=wrap, logger=logger, quiet=quiet)


def log_verbose(message: str,
                width: Optional[int] = None,
                wrap: Optional[bool] = None,
                logger: Optional[logging.Logger] = None,
                quiet: Optional[bool] = None,
                ) -> None:
    """
    logs VERBOSE

    >>> log_verbose('verbose')

    """
    log_level(message=message, level=log_levels.VERBOSE, width=width, wrap=wrap, logger=logger, quiet=quiet)


def log_info(message: str,
             width: Optional[int] = None,
             wrap: Optional[bool] = None,
             logger: Optional[logging.Logger] = None,
             quiet: Optional[bool] = None,
             ) -> None:
    """
    logs INFO

    >>> log_info('info')

    """
    log_level(message=message, level=logging.INFO, width=width, wrap=wrap, logger=logger, quiet=quiet)


def log_notice(message: str,
               width: Optional[int] = None,
               wrap: Optional[bool] = None,
               logger: Optional[logging.Logger] = None,
               quiet: Optional[bool] = None,
               ) -> None:
    """
    logs NOTICE

    >>> log_notice('notice')

    """
    log_level(message=message, level=log_levels.NOTICE, width=width, wrap=wrap, logger=logger, quiet=quiet)


def log_success(message: str,
                width: Optional[int] = None,
                wrap: Optional[bool] = None,
                logger: Optional[logging.Logger] = None,
                quiet: Optional[bool] = None,
                ) -> None:
    """
    logs SUCCESS

    >>> log_success('success')

    """
    log_level(message=message, level=log_levels.SUCCESS, width=width, wrap=wrap, logger=logger, quiet=quiet)


def log_warning(message: str,
                width: Optional[int] = None,
                wrap: Optional[bool] = None,
                logger: Optional[logging.Logger] = None,
                quiet: Optional[bool] = None,
                ) -> None:
    """
    logs WARNING

    >>> log_warning('warning')

    """
    log_level(message=message, level=logging.WARNING, width=width, wrap=wrap, logger=logger, quiet=quiet)


def log_error(message: str,
              width: Optional[int] = None,
              wrap: Optional[bool] = None,
              logger: Optional[logging.Logger] = None,
              quiet: Optional[bool] = None,
              ) -> None:
    """
    logs ERROR

    >>> log_error('error')

    """
    log_level(message=message, level=logging.ERROR, width=width, wrap=wrap, logger=logger, quiet=quiet)


def log_critical(message: str,
                 width: Optional[int] = None,
                 wrap: Optional[bool] = None,
                 logger: Optional[logging.Logger] = None,
                 quiet: Optional[bool] = None,
                 ) -> None:
    """
    logs CRITICAL

    >>> log_critical('critical')

    """

    log_level(message=message, level=logging.CRITICAL, width=width, wrap=wrap, logger=logger, quiet=quiet)


def log_level(message: str,
              level: Optional[int] = None,
              width: Optional[int] = None,
              wrap: Optional[bool] = None,
              logger: Optional[logging.Logger] = None,
              quiet: Optional[bool] = None,
              banner: bool = False
              ) -> None:
    """
    logs a message

    if there is no logger passed, the root logger will be used.


    >>> log_level('test')
    >>> log_level('test', quiet=True)
    >>> log_level('test', logging.SUCCESS, wrap=True)  # noqa
    >>> log_level('test', logging.ERROR, wrap=True)
    >>> log_level('test', logging.ERROR, wrap=False)
    >>> log_level('test', logging.ERROR, wrap=True, banner = True)
    >>> log_level('test', logging.ERROR, wrap=False, banner = True)
    >>> log_level('this is\\none nice piece of ham\\none nice piece of spam\\none more piece of wonderful spam', \
                   logging.ERROR, width=10, wrap=True)
    >>> log_level('this is\\none nice piece of ham\\none nice piece of spam\\none more piece of wonderful spam', \
                   logging.ERROR, width=10, wrap=False)
    >>> log_level('this is\\none nice piece of ham\\none nice piece of spam\\none more piece of wonderful spam', \
                   logging.ERROR, width=10, wrap=True, banner = True)
    >>> log_level('this is\\none nice piece of ham\\none nice piece of spam\\none more piece of wonderful spam', \
                   logging.ERROR, width=10, wrap=False, banner = True)
    """

    quiet = bool(lib_parameter.get_default_if_none(quiet, default=LogSettings.quiet))

    if quiet:
        return

    message = str(message)

    level = int(lib_parameter.get_default_if_none(level, default=LogSettings.new_logger_level))
    width = int(lib_parameter.get_default_if_none(width, default=LogSettings.width))
    wrap = bool(lib_parameter.get_default_if_none(wrap, default=LogSettings.wrap))

    if logger is None:
        logger = logging.getLogger()

    l_message = message.split('\n')

    if banner:
        sep_line = '*' * width
        logger.log(level=level, msg=sep_line)  # 140 characters is about the width in travis log screen
        for line in l_message:
            if wrap:
                l_wrapped_lines = textwrap.wrap(line, width=width - 2, tabsize=4, replace_whitespace=False, initial_indent='* ', subsequent_indent='* ')
                for wrapped_line in l_wrapped_lines:
                    msg_line = wrapped_line + (width - len(wrapped_line) - 1) * ' ' + '*'
                    logger.log(level=level, msg=msg_line)
            else:
                line = "* " + line.rstrip()
                if len(line) < width - 1:
                    line = line + (width - len(line) - 1) * ' ' + '*'
                logger.log(level=level, msg=line)
        logger.log(level=level, msg=sep_line)
        log_handlers.logger_flush_all_handlers(logger)
    else:
        for line in l_message:
            if wrap:
                l_wrapped_lines = textwrap.wrap(line, width=width, tabsize=4, replace_whitespace=False)
                for msg_line in l_wrapped_lines:
                    logger.log(level=level, msg=msg_line)
            else:
                msg_line = line.rstrip()
                logger.log(level=level, msg=msg_line)
                log_handlers.logger_flush_all_handlers(logger)


def colortest(quiet: bool = False) -> None:
    """ test banner colors

    >>> # Setup
    >>> LogSettings.use_colored_stream_handler=True
    >>> LogSettings.new_logger_level = 0
    >>> LogSettings.stream_handler_log_level = 0
    >>> LogSettings.stream = sys.stdout
    >>> setup_handler()
    >>> colortest()
    test ...
    >>> colortest(quiet=True)
    >>> # TearDown
    >>> LogSettings.stream = sys.stderr
    >>> setup_handler(remove_existing_stream_handlers=True)

    """
    if not quiet:
        log_spam('test level spam')
        log_debug('test level debug')
        log_verbose('test level verbose')
        log_info('test level info')
        log_notice('test level notice')
        log_success('test level success')
        log_warning('test level warning')
        log_error('test level error')
        log_critical('test level critical')
        humanfriendly.cli.demonstrate_ansi_formatting()


def setup_handler(logger: logging.Logger = logging.getLogger(), remove_existing_stream_handlers: bool = False) -> None:
    if LogSettings.use_colored_stream_handler:
        log_handlers.set_stream_handler_color(logger=logger,
                                              level=LogSettings.stream_handler_log_level,
                                              fmt=LogSettings.fmt,
                                              datefmt=LogSettings.datefmt,
                                              field_styles=LogSettings.field_styles,
                                              level_styles=LogSettings.level_styles,
                                              stream=LogSettings.stream,
                                              remove_existing_stream_handlers=remove_existing_stream_handlers)
    else:
        log_handlers.set_stream_handler(logger=logger,
                                        level=LogSettings.stream_handler_log_level,
                                        fmt=LogSettings.fmt,
                                        datefmt=LogSettings.datefmt,
                                        stream=LogSettings.stream,
                                        remove_existing_stream_handlers=remove_existing_stream_handlers)
