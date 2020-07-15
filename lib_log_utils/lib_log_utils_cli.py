# STDLIB
import os
import sys
from typing import Optional

# EXT
import click

# CONSTANTS
CLICK_CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

# PROJ
try:
    from . import __init__conf__
    from . import lib_log_utils
    from . import log_levels
except (ImportError, ModuleNotFoundError):  # pragma: no cover
    # imports for doctest
    import __init__conf__                   # type: ignore  # pragma: no cover
    import lib_log_utils                    # type: ignore  # pragma: no cover
    import log_levels                       # type: ignore  # pragma: no cover

import logging


def info() -> None:
    """
    >>> info()
    Info for ...

    """
    __init__conf__.print_info()


def do_log(message: str, level: Optional[int] = None, banner_width: Optional[int] = None, wrap_text: Optional[bool] = None,
           log_console: Optional[str] = None, banner: bool = False, force: bool = False) -> None:
    """
    >>> do_log('test', banner=False)
    >>> do_log('test', banner=True)

    """
    set_log_level()
    set_banner_width(banner_width, force)
    set_wrap_text(wrap_text, force)
    set_quiet(log_console, force)

    if banner:
        lib_log_utils.banner_level(message=message, level=level)
    else:
        lib_log_utils.log_level(message=message, level=level)


def set_log_level() -> None:
    """
    >>> # Setup
    >>> log_level_default = lib_log_utils.LogSettings.new_logger_level

    >>> # no env Set
    >>> set_log_level()
    >>> assert lib_log_utils.LogSettings.new_logger_level == log_level_default

    >>> # env Set spam
    >>> os.environ['log_utils_log_level']='spam'
    >>> set_log_level()
    >>> assert lib_log_utils.LogSettings.new_logger_level == 5

    >>> # env Set 42
    >>> os.environ['log_utils_log_level']='42'
    >>> set_log_level()
    >>> assert lib_log_utils.LogSettings.new_logger_level == 42

    >>> # env Set unknown
    >>> os.environ['log_utils_log_level']='unknown'
    >>> set_log_level()
    Traceback (most recent call last):
        ...
    ValueError: the environment setting "log_utils_log_level" has to be from ...

    >>> # Teardown
    >>> del os.environ['log_utils_log_level']
    >>> lib_log_utils.LogSettings.new_logger_level = log_level_default

    """
    if 'log_utils_log_level' in os.environ:
        valid_str_values = ['SPAM', 'DEBUG', 'VERBOSE', 'INFO', 'NOTICE', 'SUCCESS', 'WARNING', 'ERROR', 'CRITICAL']
        try:
            log_level = int(os.environ['log_utils_log_level'])
            lib_log_utils.LogSettings.new_logger_level = log_level
            return
        except ValueError:
            pass

        log_level_name = os.environ['log_utils_log_level'].upper()
        if log_level_name not in valid_str_values:
            raise ValueError('the environment setting "log_utils_log_level" has to be from 0-50 or one of the predefined logging levels : {}'.format(
                ', '.join(valid_str_values)))

        lib_log_utils.LogSettings.new_logger_level = logging._nameToLevel[log_level_name]


def set_banner_width(banner_width: Optional[int] = None, force: bool = False) -> None:
    # env settings have precedence, unless force=True - if nothing is passed, the default value will be used
    """
    >>> # Setup
    >>> default_banner_width = lib_log_utils.LogSettings.banner_width

    >>> # No env Setting, banner_width=None
    >>> set_banner_width()
    >>> assert lib_log_utils.LogSettings.banner_width == default_banner_width

    >>> # No env Setting, banner_width = default + 1
    >>> set_banner_width(default_banner_width + 1)
    >>> assert lib_log_utils.LogSettings.banner_width == default_banner_width + 1

    >>> # Env Setting = default + 2, banner_width=None
    >>> os.environ['log_utils_banner_width'] = str(default_banner_width + 2)
    >>> set_banner_width()
    >>> assert lib_log_utils.LogSettings.banner_width == default_banner_width + 2

    >>> # Env Setting = default + 3, banner_width=default (env has precedence)
    >>> os.environ['log_utils_banner_width'] = str(default_banner_width + 3)
    >>> set_banner_width(default_banner_width)
    >>> assert lib_log_utils.LogSettings.banner_width == default_banner_width + 3

    >>> # Env Setting = default + 3, banner_width=default + 4, force = True (parameter has precedence)
    >>> set_banner_width(default_banner_width + 4, True)
    >>> assert lib_log_utils.LogSettings.banner_width == default_banner_width + 4

    >>> # provoke Error wrong type
    >>> os.environ['log_utils_banner_width'] = 'abc'
    >>> set_banner_width()
    Traceback (most recent call last):
        ...
    ValueError: invalid environment setting for "log_utils_banner_width", must be numerical and >= 10

    >>> # provoke Error too small
    >>> os.environ['log_utils_banner_width'] = '9'
    >>> set_banner_width()
    Traceback (most recent call last):
        ...
    ValueError: invalid environment setting for "log_utils_banner_width", must be numerical and >= 10

    >>> # Teardown
    >>> lib_log_utils.LogSettings.banner_width = default_banner_width
    >>> del os.environ['log_utils_banner_width']

    """

    if 'log_utils_banner_width' in os.environ:
        if banner_width is not None and force:
            lib_log_utils.LogSettings.banner_width = banner_width
        else:
            s_error = 'invalid environment setting for "log_utils_banner_width", must be numerical and >= 10'
            try:
                banner_width = int(os.environ['log_utils_banner_width'])
            except ValueError:
                raise ValueError(s_error)
            if banner_width < 10:
                raise ValueError(s_error)
            lib_log_utils.LogSettings.banner_width = banner_width
    else:
        if banner_width is not None:
            lib_log_utils.LogSettings.banner_width = banner_width


def set_wrap_text(wrap_text: Optional[bool] = None, force: bool = False) -> None:
    # env settings have precedence, unless force=True - if nothing is passed, the default value will be used
    """
    >>> # Setup
    >>> default_wrap_text = lib_log_utils.LogSettings.wrap_text

    >>> # No env Setting, wrap_text=None
    >>> set_wrap_text()
    >>> assert lib_log_utils.LogSettings.wrap_text == default_wrap_text

    >>> # No env Setting, wrap_text = not default_wrap_text
    >>> set_wrap_text(not default_wrap_text)
    >>> assert lib_log_utils.LogSettings.wrap_text != default_wrap_text

    >>> # Env Setting = not default_wrap_text, wrap_text=None
    >>> os.environ['log_utils_wrap_text'] = str(not default_wrap_text)
    >>> set_wrap_text()
    >>> assert lib_log_utils.LogSettings.wrap_text != default_wrap_text

    >>> # Env Setting = not default_wrap_text, wrap_text=default_wrap_text (env has precedence)
    >>> os.environ['log_utils_wrap_text'] = str(not default_wrap_text)
    >>> set_wrap_text(default_wrap_text)
    >>> assert lib_log_utils.LogSettings.wrap_text != default_wrap_text

    >>> # Env Setting = not default_wrap_text, wrap_text=default_wrap_text (parameter has precedence)
    >>> set_wrap_text(default_wrap_text, True)
    >>> assert lib_log_utils.LogSettings.wrap_text == default_wrap_text

    >>> # provoke Error
    >>> os.environ['log_utils_wrap_text'] = 'something'
    >>> set_wrap_text()
    Traceback (most recent call last):
        ...
    ValueError: invalid environment setting for "log_utils_wrap_text", must be "True" or "False"

    >>> # Teardown
    >>> lib_log_utils.LogSettings.wrap_text = default_wrap_text
    >>> del os.environ['log_utils_wrap_text']

    """
    if 'log_utils_wrap_text' in os.environ:
        if wrap_text is not None and force:
            lib_log_utils.LogSettings.wrap_text = wrap_text
        else:
            if os.environ['log_utils_wrap_text'].lower().startswith('false'):
                lib_log_utils.LogSettings.wrap_text = False
            elif os.environ['log_utils_wrap_text'].lower().startswith('true'):
                lib_log_utils.LogSettings.wrap_text = True
            else:
                raise ValueError('invalid environment setting for "log_utils_wrap_text", must be "True" or "False"')
    else:
        if wrap_text is not None:
            lib_log_utils.LogSettings.wrap_text = wrap_text


def set_quiet(log_console: Optional[str] = None, force: bool = False) -> None:
    # env settings have precedence, unless force=True - if nothing is passed, the default value will be used
    """
    >>> # Setup
    >>> default_quiet = lib_log_utils.LogSettings.quiet

    >>> # No env Setting, log_console=None
    >>> set_quiet()
    >>> assert lib_log_utils.LogSettings.quiet == default_quiet

    >>> # No env Setting, log_console = default_quiet
    >>> set_quiet(str(default_quiet))
    >>> assert lib_log_utils.LogSettings.quiet != default_quiet

    >>> # Env Setting = not default_quiet, log_console=None
    >>> os.environ['log_utils_quiet'] = str(not default_quiet)
    >>> set_quiet()
    >>> assert lib_log_utils.LogSettings.quiet != default_quiet

    >>> # Env Setting = not default_quiet, log_console=not default_quiet (env has precedence)
    >>> os.environ['log_utils_quiet'] = str(not default_quiet)
    >>> set_quiet(str(not default_quiet))
    >>> assert lib_log_utils.LogSettings.quiet != default_quiet

    >>> # Env Setting = not default_quiet, log_console=default_quiet (parameter has precedence)
    >>> set_quiet(str(not default_quiet), True)
    >>> assert lib_log_utils.LogSettings.quiet == default_quiet

    >>> # provoke Error
    >>> os.environ['log_utils_quiet'] = 'something'
    >>> set_quiet()
    Traceback (most recent call last):
        ...
    ValueError: invalid environment setting for "log_utils_quiet", must be "True" or "False"

    >>> # Teardown
    >>> lib_log_utils.LogSettings.quiet = default_quiet
    >>> del os.environ['log_utils_quiet']

    """
    quiet = False

    if log_console is not None:
        # this is intentionally, we accept every value, only "false" is handled !
        if log_console.lower().startswith('false'):
            quiet = True
        else:
            quiet = False

    if 'log_utils_quiet' in os.environ:
        if log_console is not None and force:
            lib_log_utils.LogSettings.quiet = quiet
        else:
            if os.environ['log_utils_quiet'].lower().startswith('false'):
                lib_log_utils.LogSettings.quiet = False
            elif os.environ['log_utils_quiet'].lower().startswith('true'):
                lib_log_utils.LogSettings.quiet = True
            else:
                raise ValueError('invalid environment setting for "log_utils_quiet", must be "True" or "False"')
    else:
        if log_console is not None:
            lib_log_utils.LogSettings.quiet = quiet


@click.group(help=__init__conf__.title, context_settings=CLICK_CONTEXT_SETTINGS)
@click.version_option(version=__init__conf__.version,
                      prog_name=__init__conf__.shell_command,
                      message='{} version %(version)s'.format(__init__conf__.shell_command))
def cli_main() -> None:                     # pragma: no cover
    pass


@cli_main.command('program_info', context_settings=CLICK_CONTEXT_SETTINGS)
def cli_program_info() -> None:
    """ get program informations """
    info()


@cli_main.command('spam', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default=None, help='disable console logging if "False"')
@click.option('--force', type=bool, default=False, help='take precedence over environment settings')
def cli_spam(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: Optional[str], force: bool) -> None:
    """ logs a spam message """
    level = log_levels.SPAM
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, force=force)


@cli_main.command('debug', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default=None, help='disable console logging if "False"')
@click.option('--force', type=bool, default=False, help='take precedence over environment settings')
def cli_debug(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: Optional[str], force: bool) -> None:
    """ logs a debug message """
    level = logging.DEBUG
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, force=force)


@cli_main.command('verbose', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default=None, help='disable console logging if "False"')
@click.option('--force', type=bool, default=False, help='take precedence over environment settings')
def cli_verbose(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: Optional[str], force: bool) -> None:
    """ logs a verbose message """
    level = log_levels.VERBOSE
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, force=force)


@cli_main.command('info', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default=None, help='disable console logging if "False"')
@click.option('--force', type=bool, default=False, help='take precedence over environment settings')
def cli_info(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: Optional[str], force: bool) -> None:
    """ logs a info message """
    level = logging.INFO
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, force=force)


@cli_main.command('notice', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default=None, help='disable console logging if "False"')
@click.option('--force', type=bool, default=False, help='take precedence over environment settings')
def cli_notice(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: Optional[str], force: bool) -> None:
    """ logs a notice message """
    level = log_levels.NOTICE
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, force=force)


@cli_main.command('success', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default=None, help='disable console logging if "False"')
@click.option('--force', type=bool, default=False, help='take precedence over environment settings')
def cli_success(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: Optional[str], force: bool) -> None:
    """ logs a success message """
    level = log_levels.SUCCESS
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, force=force)


@cli_main.command('warning', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default=None, help='disable console logging if "False"')
@click.option('--force', type=bool, default=False, help='take precedence over environment settings')
def cli_warning(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: Optional[str], force: bool) -> None:
    """ logs a warning message """
    level = logging.WARNING
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, force=force)


@cli_main.command('error', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default=None, help='disable console logging if "False"')
@click.option('--force', type=bool, default=False, help='take precedence over environment settings')
def cli_error(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: Optional[str], force: bool) -> None:
    """ logs a error message """
    level = logging.ERROR
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, force=force)


@cli_main.command('critical', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default=None, help='disable console logging if "False"')
@click.option('--force', type=bool, default=False, help='take precedence over environment settings')
def cli_critical(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: Optional[str], force: bool) -> None:
    """ logs a critical message """
    level = logging.CRITICAL
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, force=force)


@cli_main.command('banner_spam', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default=None, help='disable console logging if "False"')
@click.option('--force', type=bool, default=False, help='take precedence over environment settings')
def cli_banner_spam(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: Optional[str], force: bool) -> None:
    """ logs a spam message banner """
    level = log_levels.SPAM
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, banner=True, force=force)


@cli_main.command('banner_debug', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default=None, help='disable console logging if "False"')
@click.option('--force', type=bool, default=False, help='take precedence over environment settings')
def cli_banner_debug(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: Optional[str], force: bool) -> None:
    """ logs a debug message banner """
    level = logging.DEBUG
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, banner=True, force=force)


@cli_main.command('banner_verbose', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default=None, help='disable console logging if "False"')
@click.option('--force', type=bool, default=False, help='take precedence over environment settings')
def cli_banner_verbose(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: Optional[str], force: bool) -> None:
    """ logs a verbose message banner"""
    level = log_levels.VERBOSE
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, banner=True, force=force)


@cli_main.command('banner_info', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default=None, help='disable console logging if "False"')
@click.option('--force', type=bool, default=False, help='take precedence over environment settings')
def cli_banner_info(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: Optional[str], force: bool) -> None:
    """ logs a info message banner """
    level = logging.INFO
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, banner=True, force=force)


@cli_main.command('banner_notice', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default=None, help='disable console logging if "False"')
@click.option('--force', type=bool, default=False, help='take precedence over environment settings')
def cli_banner_notice(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: Optional[str], force: bool) -> None:
    """ logs a notice message banner """
    level = log_levels.NOTICE
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, banner=True, force=force)


@cli_main.command('banner_success', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default=None, help='disable console logging if "False"')
@click.option('--force', type=bool, default=False, help='take precedence over environment settings')
def cli_banner_success(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: Optional[str], force: bool) -> None:
    """ logs a success message banner """
    level = log_levels.SUCCESS
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, banner=True, force=force)


@cli_main.command('banner_warning', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default=None, help='disable console logging if "False"')
@click.option('--force', type=bool, default=False, help='take precedence over environment settings')
def cli_banner_warning(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: Optional[str], force: bool) -> None:
    """ logs a warning message banner """
    level = logging.WARNING
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, banner=True, force=force)


@cli_main.command('banner_error', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default=None, help='disable console logging if "False"')
@click.option('--force', type=bool, default=False, help='take precedence over environment settings')
def cli_banner_error(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: Optional[str], force: bool) -> None:
    """ logs a error message banner """
    level = logging.ERROR
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, banner=True, force=force)


@cli_main.command('banner_critical', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default=None, help='disable console logging if "False"')
@click.option('--force', type=bool, default=False, help='take precedence over environment settings')
def cli_banner_critical(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: Optional[str], force: bool) -> None:
    """ logs a critical message banner"""
    level = logging.CRITICAL
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, banner=True, force=force)


@cli_main.command('colortest', context_settings=CLICK_CONTEXT_SETTINGS)
def cli_colortest() -> None:
    """ prints a color test """
    lib_log_utils.colortest()


# entry point if main
if __name__ == '__main__':
    try:
        lib_log_utils.LogSettings.use_colored_stream_handler = True
        cli_main()
    except Exception as e:
        print(e, file=sys.stderr)
        # TODO EXIT CODE, FULL TRACE (?) option --traceback (?)
