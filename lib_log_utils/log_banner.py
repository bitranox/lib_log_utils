# STDLIB

# noinspection PyUnresolvedReferences
import getpass
# noinspection PyUnresolvedReferences
import logging
import logging.handlers
import platform
import subprocess
import textwrap
from typing import Any, Dict

# PROJ
# imports for local pytest
try:
    from .log_handlers import *     # type: ignore # pragma: no cover
    from .log_levels import *     # type: ignore # pragma: no cover
# imports for doctest
except ImportError:                 # type: ignore # pragma: no cover
    from log_handlers import *      # type: ignore # pragma: no cover
    from log_levels import *     # type: ignore # pragma: no cover


class BannerSettings(object):
    called_via_commandline = False
    # fmt = '[{username}@%(hostname)s][%(asctime)s][%(levelname)-8s]: %(message)s'.format(username=getpass.getuser())
    fmt = '%(message)s'
    datefmt = '%Y-%m-%d %H:%M:%S'

    field_styles = {
        'asctime': {'color': 'green'},
        'hostname': {'color': 'green'},                         # 'hostname': {'color': 'magenta'},
        'levelname': {'color': 'yellow'},                       # 'levelname': {'color': 'black', 'bold': True},
        'name': {'color': 'blue'},
        'programname': {'color': 'cyan'}
    }                                                           # type: Dict[str, Dict[str, Any]]

    """
    level_styles = {
        'spam': {'color': 'magenta', 'bright': True},                       # level 5   - SPAM
        'debug': {'color': 'blue', 'bright': True},                         # level 10  - DEBUG
        'verbose': {'background': 'blue', 'bright': True},                  # level 15  - VERBOSE
        'info': {},                                                         # level 20  - INFO
        'notice': {'background': 'magenta', 'bright': True},                # level 25  - NOTICE
        'warning': {'color': 'red', 'bright': True},                        # level 30  - WARNING
        'success': {'color': 'green', 'bright': True},                      # level 35  - SUCCESS
        'error': {'background': 'red', 'bright': True},                     # level 40  - ERROR
        'critical': {'background': 'red'},                                  # level 50  - CRITICAL
    }                                                                       # type: Dict[str, Dict[str, Any]]

    """
    level_styles = {
        'spam': {'color': 95},                                              # level 5   - SPAM
        'debug': {'color': 94},                                             # level 10  - DEBUG
        'verbose': {'color': 44},                                           # level 15  - VERBOSE
        'info': {},                                                         # level 20  - INFO
        'notice': {'color': 45},                                            # level 25  - NOTICE
        'warning': {'color': 91},                                           # level 30  - WARNING
        'success': {'color': 92},                                           # level 35  - SUCCESS
        'error': {'color': 41},                                             # level 40  - ERROR
        'critical': {'color': 101},                                         # level 50  - CRITICAL
    }                                                                       # type: Dict[str, Dict[str, Any]]




def get_terminal_colors() -> int:
    """
    >>> if platform.system().lower() == 'windows':
    ...     assert get_terminal_colors() == 256
    ... else:
    ...    assert get_terminal_colors() == 8 or get_terminal_colors() == 256

    """
    if platform.system().lower() != 'windows':
        s_colors = subprocess.check_output(['tput', 'colors'])
        colors = int(s_colors)
    else:
        colors = 256
    return colors


def banner_spam(message: str, banner_width: int = 140, wrap_text: bool = True, logger: logging.Logger = logging.getLogger()) -> None:
    banner_level(message=message, level=logging.SPAM, banner_width=banner_width, wrap_text=wrap_text, logger=logger)        # type: ignore


def banner_debug(message: str, banner_width: int = 140, wrap_text: bool = True, logger: logging.Logger = logging.getLogger()) -> None:
    banner_level(message=message, level=logging.DEBUG, banner_width=banner_width, wrap_text=wrap_text, logger=logger)


def banner_verbose(message: str, banner_width: int = 140, wrap_text: bool = True, logger: logging.Logger = logging.getLogger()) -> None:
    banner_level(message=message, level=logging.VERBOSE, banner_width=banner_width, wrap_text=wrap_text, logger=logger)     # type: ignore


def banner_info(message: str, banner_width: int = 140, wrap_text: bool = True, logger: logging.Logger = logging.getLogger()) -> None:
    banner_level(message=message, level=logging.INFO, banner_width=banner_width, wrap_text=wrap_text, logger=logger)


def banner_notice(message: str, banner_width: int = 140, wrap_text: bool = True, logger: logging.Logger = logging.getLogger()) -> None:
    banner_level(message=message, level=logging.NOTICE, banner_width=banner_width, wrap_text=wrap_text, logger=logger)      # type: ignore


def banner_success(message: str, banner_width: int = 140, wrap_text: bool = True, logger: logging.Logger = logging.getLogger()) -> None:
    banner_level(message=message, level=logging.SUCCESS, banner_width=banner_width, wrap_text=wrap_text, logger=logger)     # type: ignore


def banner_warning(message: str, banner_width: int = 140, wrap_text: bool = True, logger: logging.Logger = logging.getLogger()) -> None:
    banner_level(message=message, level=logging.WARNING, banner_width=banner_width, wrap_text=wrap_text, logger=logger)


def banner_error(message: str, banner_width: int = 140, wrap_text: bool = True, logger: logging.Logger = logging.getLogger()) -> None:
    banner_level(message=message, level=logging.ERROR, banner_width=banner_width, wrap_text=wrap_text, logger=logger)


def banner_critical(message: str, banner_width: int = 140, wrap_text: bool = True, logger: logging.Logger = logging.getLogger()) -> None:
    banner_level(message=message, level=logging.CRITICAL, banner_width=banner_width, wrap_text=wrap_text, logger=logger)


def banner_level(message: str, level: int = logging.INFO, banner_width: int = 140, wrap_text: bool = True,
                 logger: logging.Logger = logging.getLogger()) -> None:
    """
    >>> BannerSettings.called_via_commandline = True
    >>> banner_level('test', logging.SUCCESS, wrap_text=True)
    >>> banner_level('test', logging.ERROR, wrap_text=True)
    >>> banner_level('test', logging.ERROR, wrap_text=False)
    >>> banner_level('das is\\ndas ist\\ndas ist   ein   test\\ndas ist   ein   weiterer test', logging.ERROR, banner_width=10, wrap_text=True)
    >>> banner_level('das is\\ndas ist\\ndas ist   ein   test\\ndas ist   ein   weiterer test', logging.ERROR, banner_width=10, wrap_text=False)

    """
    message = str(message)
    if BannerSettings.called_via_commandline:
        add_stream_handler_color(level=level, fmt=BannerSettings.fmt, datefmt=BannerSettings.datefmt, field_styles=BannerSettings.field_styles,
                                 level_styles=BannerSettings.level_styles)
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


def log_spam(message: str, banner_width: int = 140, wrap_text: bool = True, logger: logging.Logger = logging.getLogger()) -> None:
    log_level(message=message, level=logging.SPAM, banner_width=banner_width, wrap_text=wrap_text, logger=logger)       # type: ignore


def log_debug(message: str, banner_width: int = 140, wrap_text: bool = True, logger: logging.Logger = logging.getLogger()) -> None:
    log_level(message=message, level=logging.DEBUG, banner_width=banner_width, wrap_text=wrap_text, logger=logger)


def log_verbose(message: str, banner_width: int = 140, wrap_text: bool = True, logger: logging.Logger = logging.getLogger()) -> None:
    log_level(message=message, level=logging.VERBOSE, banner_width=banner_width, wrap_text=wrap_text, logger=logger)    # type: ignore


def log_info(message: str, banner_width: int = 140, wrap_text: bool = True, logger: logging.Logger = logging.getLogger()) -> None:
    log_level(message=message, level=logging.INFO, banner_width=banner_width, wrap_text=wrap_text, logger=logger)


def log_notice(message: str, banner_width: int = 140, wrap_text: bool = True, logger: logging.Logger = logging.getLogger()) -> None:
    log_level(message=message, level=logging.NOTICE, banner_width=banner_width, wrap_text=wrap_text, logger=logger)     # type: ignore


def log_success(message: str, banner_width: int = 140, wrap_text: bool = True, logger: logging.Logger = logging.getLogger()) -> None:
    log_level(message=message, level=logging.SUCCESS, banner_width=banner_width, wrap_text=wrap_text, logger=logger)    # type: ignore


def log_warning(message: str, banner_width: int = 140, wrap_text: bool = True, logger: logging.Logger = logging.getLogger()) -> None:
    log_level(message=message, level=logging.WARNING, banner_width=banner_width, wrap_text=wrap_text, logger=logger)


def log_error(message: str, banner_width: int = 140, wrap_text: bool = True, logger: logging.Logger = logging.getLogger()) -> None:
    log_level(message=message, level=logging.ERROR, banner_width=banner_width, wrap_text=wrap_text, logger=logger)


def log_critical(message: str, banner_width: int = 140, wrap_text: bool = True, logger: logging.Logger = logging.getLogger()) -> None:
    log_level(message=message, level=logging.CRITICAL, banner_width=banner_width, wrap_text=wrap_text, logger=logger)


def log_level(message: str, level: int = logging.INFO, banner_width: int = 140, wrap_text: bool = True,
              logger: logging.Logger = logging.getLogger()) -> None:

    message = str(message)

    if BannerSettings.called_via_commandline:
        add_stream_handler_color(level=level, fmt=BannerSettings.fmt, datefmt=BannerSettings.datefmt, field_styles=BannerSettings.field_styles,
                                 level_styles=BannerSettings.level_styles)

    l_message = message.split('\n')
    for line in l_message:
        if wrap_text:
            l_wrapped_lines = textwrap.wrap(line, width=banner_width, tabsize=4, replace_whitespace=False)
            for msg_line in l_wrapped_lines:
                logger.log(level=level, msg=msg_line)
        else:
            msg_line = line.rstrip()
            logger.log(level=level, msg=msg_line)


def banner_color_test() -> None:
    """ test banner colors

    >>> banner_color_test()

    """
    banner_spam('test level spam')
    banner_debug('test level debug')
    banner_verbose('test level verbose')
    banner_info('test level info')
    banner_notice('test level notice')
    banner_success('test level success')
    banner_warning('test level warning')
    banner_error('test level error')
    banner_critical('test level critical')
