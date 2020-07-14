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
           log_console: str = 'True', banner: bool = False) -> None:
    """
    >>> do_log('test', log_console='True', banner=False)
    >>> do_log('test', log_console='False', banner=True)

    """

    if log_console.lower() == 'false':
        quiet = True
    else:
        quiet = False

    if banner:
        lib_log_utils.banner_level(message=message, level=level, banner_width=banner_width, wrap_text=wrap_text, logger=None, quiet=quiet)
    else:
        lib_log_utils.log_level(message=message, level=level, banner_width=banner_width, wrap_text=wrap_text, logger=None, quiet=quiet)


def get_env_settings() -> None:
    if 'log_utils_level' in os.environ:
        lib_log_utils.LogSettings.new_logger_level = int(os.environ['log_utils_level'])

    if 'log_utils_fmt' in os.environ:
        lib_log_utils.LogSettings.fmt = os.environ['log_utils_fmt']

    if 'log_utils_banner_width' in os.environ:
        lib_log_utils.LogSettings.banner_width = int(os.environ['log_utils_banner_width'])

    if 'log_utils_wrap_text' in os.environ:
        if os.environ['log_utils_wrap_text'].lower() == 'true':
            lib_log_utils.LogSettings.wrap_text = True
        else:
            lib_log_utils.LogSettings.wrap_text = False

    if 'log_utils_quiet' in os.environ:
        if os.environ['log_utils_quiet'].lower() == 'true':
            lib_log_utils.LogSettings.quiet = True
        else:
            lib_log_utils.LogSettings.quiet = False

    if 'log_utils_stream' in os.environ:
        if os.environ['log_utils_stream'].lower().startswith('stdout'):
            lib_log_utils.LogSettings.stream = sys.stdout
        elif os.environ['log_utils_stream'].lower().startswith('stderr'):
            lib_log_utils.LogSettings.stream = sys.stderr
        else:
            raise ValueError('invalid setting for stream')


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
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_spam(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:
    """ logs a spam message """
    level = log_levels.SPAM
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console)


@cli_main.command('debug', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_debug(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:
    """ logs a debug message """
    level = logging.DEBUG
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console)


@cli_main.command('verbose', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_verbose(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:
    """ logs a verbose message """
    level = log_levels.VERBOSE
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console)


@cli_main.command('info', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_info(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:
    """ logs a info message """
    level = logging.INFO
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console)


@cli_main.command('notice', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_notice(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:
    """ logs a notice message """
    level = log_levels.NOTICE
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console)


@cli_main.command('success', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_success(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:
    """ logs a success message """
    level = log_levels.SUCCESS
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console)


@cli_main.command('warning', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_warning(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:
    """ logs a warning message """
    level = logging.WARNING
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console)


@cli_main.command('error', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_error(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:
    """ logs a error message """
    level = logging.ERROR
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console)


@cli_main.command('critical', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_critical(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:
    """ logs a critical message """
    level = logging.CRITICAL
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console)


@cli_main.command('banner_spam', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_banner_spam(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:
    """ logs a spam message banner """
    level = log_levels.SPAM
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, banner=True)


@cli_main.command('banner_debug', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_banner_debug(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:
    """ logs a debug message banner """
    level = logging.DEBUG
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, banner=True)


@cli_main.command('banner_verbose', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_banner_verbose(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:
    """ logs a verbose message banner"""
    level = log_levels.VERBOSE
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, banner=True)


@cli_main.command('banner_info', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_banner_info(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:
    """ logs a info message banner """
    level = logging.INFO
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, banner=True)


@cli_main.command('banner_notice', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_banner_notice(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:
    """ logs a notice message banner """
    level = log_levels.NOTICE
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, banner=True)


@cli_main.command('banner_success', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_banner_success(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:
    """ logs a success message banner """
    level = log_levels.SUCCESS
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, banner=True)


@cli_main.command('banner_warning', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_banner_warning(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:
    """ logs a warning message banner """
    level = logging.WARNING
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, banner=True)


@cli_main.command('banner_error', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_banner_error(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:
    """ logs a error message banner """
    level = logging.ERROR
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, banner=True)


@cli_main.command('banner_critical', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_banner_critical(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:
    """ logs a critical message banner"""
    level = logging.CRITICAL
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, banner=True)


@cli_main.command('color_test', context_settings=CLICK_CONTEXT_SETTINGS)
def cli_color_test() -> None:
    """ prints a color test """
    lib_log_utils.banner_color_test()


# entry point if main
if __name__ == '__main__':
    lib_log_utils.LogSettings.add_streamhandler_color = True
    cli_main()
