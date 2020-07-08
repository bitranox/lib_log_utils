# STDLIB
from typing import Optional, Union

import logging
import logging.handlers
import platform
import subprocess
import textwrap
from typing import Any, Dict

# OWN
import lib_parameter

# PROJ
# imports for local pytest
try:
    from . import log_handlers
    from . import log_levels
except ImportError:                 # pragma: no cover
    import log_handlers             # type: ignore # pragma: no cover
    import log_levels               # type: ignore # pragma: no cover


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


class BannerSettings(object):
    called_via_commandline = False
    # fmt = '[{username}@%(hostname)s][%(asctime)s][%(levelname)-8s]: %(message)s'.format(username=getpass.getuser())
    fmt = '%(message)s'
    datefmt = '%Y-%m-%d %H:%M:%S'
    banner_width = 140
    wrap_text = True
    quiet = False

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
    banner_level(message=message, level=log_levels.SPAM, banner_width=banner_width, wrap_text=wrap_text, logger=logger, quiet=quiet)


def banner_debug(message: str,
                 banner_width: Optional[int] = None,
                 wrap_text: Optional[bool] = None,
                 logger: Optional[logging.Logger] = None,
                 quiet: Optional[bool] = None,
                 ) -> None:
    banner_level(message=message, level=logging.DEBUG, banner_width=banner_width, wrap_text=wrap_text, logger=logger, quiet=quiet)


def banner_verbose(message: str,
                   banner_width: Optional[int] = None,
                   wrap_text: Optional[bool] = None,
                   logger: Optional[logging.Logger] = None,
                   quiet: Optional[bool] = None,
                   ) -> None:
    banner_level(message=message, level=log_levels.VERBOSE, banner_width=banner_width, wrap_text=wrap_text, logger=logger, quiet=quiet)


def banner_info(message: str,
                banner_width: Optional[int] = None,
                wrap_text: Optional[bool] = None,
                logger: Optional[logging.Logger] = None,
                quiet: Optional[bool] = None,
                ) -> None:
    banner_level(message=message, level=logging.INFO, banner_width=banner_width, wrap_text=wrap_text, logger=logger, quiet=quiet)


def banner_notice(message: str,
                  banner_width: Optional[int] = None,
                  wrap_text: Optional[bool] = None,
                  logger: Optional[logging.Logger] = None,
                  quiet: Optional[bool] = None,
                  ) -> None:
    banner_level(message=message, level=log_levels.NOTICE, banner_width=banner_width, wrap_text=wrap_text, logger=logger, quiet=quiet)


def banner_success(message: str,
                   banner_width: Optional[int] = None,
                   wrap_text: Optional[bool] = None,
                   logger: Optional[logging.Logger] = None,
                   quiet: Optional[bool] = None,
                   ) -> None:
    banner_level(message=message, level=log_levels.SUCCESS, banner_width=banner_width, wrap_text=wrap_text, logger=logger, quiet=quiet)


def banner_warning(message: str,
                   banner_width: Optional[int] = None,
                   wrap_text: Optional[bool] = None,
                   logger: Optional[logging.Logger] = None,
                   quiet: Optional[bool] = None,
                   ) -> None:
    banner_level(message=message, level=logging.WARNING, banner_width=banner_width, wrap_text=wrap_text, logger=logger, quiet=quiet)


def banner_error(message: str,
                 banner_width: Optional[int] = None,
                 wrap_text: Optional[bool] = None,
                 logger: Optional[logging.Logger] = None,
                 quiet: Optional[bool] = None,
                 ) -> None:
    banner_level(message=message, level=logging.ERROR, banner_width=banner_width, wrap_text=wrap_text, logger=logger, quiet=quiet)


def banner_critical(message: str,
                    banner_width: Optional[int] = None,
                    wrap_text: Optional[bool] = None,
                    logger: Optional[logging.Logger] = None,
                    quiet: Optional[bool] = None,
                    ) -> None:
    banner_level(message=message, level=logging.CRITICAL, banner_width=banner_width, wrap_text=wrap_text, logger=logger, quiet=quiet)


def banner_level(message: str,
                 level: Optional[int] = None,
                 banner_width: Optional[int] = None,
                 wrap_text: Optional[bool] = None,
                 logger: Optional[logging.Logger] = None,
                 quiet: Optional[bool] = None,
                 ) -> None:
    """
    >>> BannerSettings.called_via_commandline = True
    >>> # noinspection PyUnresolvedReferences
    >>> banner_level('test')
    >>> banner_level('test', logging.SUCCESS, wrap_text=True)
    >>> banner_level('test', logging.ERROR, wrap_text=True)
    >>> banner_level('test', logging.ERROR, wrap_text=False)
    >>> banner_level('das is\\ndas ist\\ndas ist   ein   test\\ndas ist   ein   weiterer test', logging.ERROR, banner_width=10, wrap_text=True)
    >>> banner_level('das is\\ndas ist\\ndas ist   ein   test\\ndas ist   ein   weiterer test', logging.ERROR, banner_width=10, wrap_text=False)
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

    level = lib_parameter.get_default_if_none(level, default=logging.INFO)
    banner_width = lib_parameter.get_default_if_none(banner_width, default=BannerSettings.banner_width)
    wrap_text = lib_parameter.get_default_if_none(wrap_text, default=BannerSettings.wrap_text)
    quiet = lib_parameter.get_default_if_none(quiet, default=BannerSettings.quiet)

    if logger is None:
        logger = logging.getLogger()

    if not quiet:
        message = str(message)
        if BannerSettings.called_via_commandline:
            log_handlers.add_stream_handler_color(level=level, fmt=BannerSettings.fmt, datefmt=BannerSettings.datefmt,
                                                  field_styles=BannerSettings.field_styles, level_styles=BannerSettings.level_styles)
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
    >>> log_level('test', logging.SUCCESS, wrap_text=True)
    >>> log_level('test', logging.ERROR, wrap_text=True)
    >>> log_level('test', logging.ERROR, wrap_text=False)
    >>> log_level('das is\\ndas ist\\ndas ist   ein   test\\ndas ist   ein   weiterer test', logging.ERROR, banner_width=10, wrap_text=True)
    >>> log_level('das is\\ndas ist\\ndas ist   ein   test\\ndas ist   ein   weiterer test', logging.ERROR, banner_width=10, wrap_text=False)
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

    level = int(lib_parameter.get_default_if_none(level, default=logging.INFO))
    banner_width = int(lib_parameter.get_default_if_none(banner_width, default=BannerSettings.banner_width))
    wrap_text = bool(lib_parameter.get_default_if_none(wrap_text, default=BannerSettings.wrap_text))
    quiet = bool(lib_parameter.get_default_if_none(quiet, default=BannerSettings.quiet))

    if logger is None:
        logger = logging.getLogger()

    if not quiet:
        message = str(message)

        if BannerSettings.called_via_commandline:
            log_handlers.add_stream_handler_color(level=level, fmt=BannerSettings.fmt, datefmt=BannerSettings.datefmt,
                                                  field_styles=BannerSettings.field_styles, level_styles=BannerSettings.level_styles)

        l_message = message.split('\n')
        for line in l_message:
            if wrap_text:
                l_wrapped_lines = textwrap.wrap(line, width=banner_width, tabsize=4, replace_whitespace=False)
                for msg_line in l_wrapped_lines:
                    logger.log(level=level, msg=msg_line)
            else:
                msg_line = line.rstrip()
                logger.log(level=level, msg=msg_line)


def banner_color_test(quiet: bool = False) -> None:
    """ test banner colors

    >>> banner_color_test()
    >>> banner_color_test(quiet=True)

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
