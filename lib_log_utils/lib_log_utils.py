# STDLIB

# noinspection PyUnresolvedReferences
import getpass
# noinspection PyUnresolvedReferences
import logging
import logging.handlers
import textwrap
from typing import Dict

# EXT
import fire

# PROJ
# imports for local pytest
try:
    from .log_handlers import *     # type: ignore # pragma: no cover
# imports for doctest
except ImportError:                 # type: ignore # pragma: no cover
    from log_handlers import *      # type: ignore # pragma: no cover


logging.SPAM = 5
logging.VERBOSE = 15
logging.NOTICE = 25
logging.SUCCESS = 35


class BannerSettings(object):
    called_via_commandline = False
    fmt = '[{username}@%(hostname)s][%(asctime)s][%(levelname)-8s]: %(message)s'.format(username=getpass.getuser())
    datefmt = '%Y-%m-%d %H:%M:%S'

    field_styles = {
                        'asctime': {'color': 'green'},
                        'hostname': {'color': 'green'},                         # 'hostname': {'color': 'magenta'},
                        'levelname': {'color': 'green'},                        # 'levelname': {'color': 'black', 'bold': True},
                        'name': {'color': 'blue'},
                        'programname': {'color': 'cyan'}
                   }                                                            # type: Dict[str, Dict[str, Any]]

    level_styles = {
                        'level 5': {'color': 'green', 'faint': True},           # level 5   - SPAM
                        'debug': {'color': 'blue', 'bright': True},             # level 10  - DEBUG     # 'debug': {'color': 'green'},
                        'level 15': {'color': 'blue'},                          # level 15  - VERBOSE
                        'info': {},                                             # level 20  - INFO
                        'level 25': {'color': 'magenta'},                       # level 25  - NOTICE
                        'warning': {'color': 'yellow'},                         # level 30  - WARNING
                        'level 35': {'color': 'green', 'bold': True},           # level 35  - SUCCESS
                        'error': {'color': 'red', 'bright': True},              # level 40  - ERROR
                        'critical': {'background': 'red', 'bright': True},      # level 50  - CRITICAL
                    }                                                           # type: Dict[str, Dict[str, Any]]


def banner_spam(message: str, banner_width: int = 140, wrap_text: bool = True, logger: logging.Logger = logging.getLogger()) -> None:
    banner_level(message=message, level=logging.SPAM, banner_width=banner_width, wrap_text=wrap_text, logger=logger)


def banner_debug(message: str, banner_width: int = 140, wrap_text: bool = True, logger: logging.Logger = logging.getLogger()) -> None:
    banner_level(message=message, level=logging.DEBUG, banner_width=banner_width, wrap_text=wrap_text, logger=logger)


def banner_verbose(message: str, banner_width: int = 140, wrap_text: bool = True, logger: logging.Logger = logging.getLogger()) -> None:
    banner_level(message=message, level=logging.VERBOSE, banner_width=banner_width, wrap_text=wrap_text, logger=logger)


def banner_info(message: str, banner_width: int = 140, wrap_text: bool = True, logger: logging.Logger = logging.getLogger()) -> None:
    banner_level(message=message, level=logging.INFO, banner_width=banner_width, wrap_text=wrap_text, logger=logger)


def banner_notice(message: str, banner_width: int = 140, wrap_text: bool = True, logger: logging.Logger = logging.getLogger()) -> None:
    banner_level(message=message, level=logging.NOTICE, banner_width=banner_width, wrap_text=wrap_text, logger=logger)


def banner_success(message: str, banner_width: int = 140, wrap_text: bool = True, logger: logging.Logger = logging.getLogger()) -> None:
    banner_level(message=message, level=35, banner_width=banner_width, wrap_text=wrap_text, logger=logger)


def banner_warning(message: str, banner_width: int = 140, wrap_text: bool = True, logger: logging.Logger = logging.getLogger()) -> None:
    banner_level(message=message, level=logging.WARNING, banner_width=banner_width, wrap_text=wrap_text, logger=logger)


def banner_error(message: str, banner_width: int = 140, wrap_text: bool = True, logger: logging.Logger = logging.getLogger()) -> None:
    banner_level(message=message, level=logging.ERROR, banner_width=banner_width, wrap_text=wrap_text, logger=logger)


def banner_critical(message: str, banner_width: int = 140, wrap_text: bool = True, logger: logging.Logger = logging.getLogger()) -> None:
    banner_level(message=message, level=logging.CRITICAL, banner_width=banner_width, wrap_text=wrap_text, logger=logger)


def banner_level(message: str, level: int = logging.INFO, banner_width: int = 140, wrap_text: bool = True, logger: logging.Logger = logging.getLogger()) -> None:
    """
    >>> BannerSettings.called_via_commandline = True
    >>> banner_level('test', logging.SUCCESS, wrap_text=True)
    >>> banner_level('test', logging.ERROR, wrap_text=True)
    >>> banner_level('test', logging.ERROR, wrap_text=False)
    >>> banner_level('das is\\ndas ist\\ndas ist   ein   test\\ndas ist   ein   weiterer test', logging.ERROR, banner_width=10, wrap_text=True)
    >>> banner_level('das is\\ndas ist\\ndas ist   ein   test\\ndas ist   ein   weiterer test', logging.ERROR, banner_width=10, wrap_text=False)

    """
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


def main():
    BannerSettings.called_via_commandline = True
    fire.Fire({
        'banner_spam': banner_spam,
        'banner_debug': banner_debug,
        'banner_verbose': banner_verbose,
        'banner_info': banner_info,
        'banner_notice': banner_notice,
        'banner_success': banner_success,
        'banner_warning': banner_warning,
        'banner_error': banner_error,
        'banner_critical': banner_critical,
    })


if __name__ == '__main__':
    main()
