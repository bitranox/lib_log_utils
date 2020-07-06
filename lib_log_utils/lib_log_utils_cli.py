# STDLIB
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


@click.group(help=__init__conf__.title, context_settings=CLICK_CONTEXT_SETTINGS)
@click.version_option(version=__init__conf__.version,
                      prog_name=__init__conf__.shell_command,
                      message='{} version %(version)s'.format(__init__conf__.shell_command))
def cli_main() -> None:                     # pragma: no cover
    pass                                    # pragma: no cover


@cli_main.command('program_info', context_settings=CLICK_CONTEXT_SETTINGS)
def cli_program_info() -> None:             # pragma: no cover
    """ get program informations """
    info()                                  # pragma: no cover


@cli_main.command('spam', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_spam(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:                         # pragma: no cover
    """ logs a spam message """
    level = log_levels.SPAM                                                                                                      # pragma: no cover
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console)                     # pragma: no cover


@cli_main.command('debug', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_debug(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:                        # pragma: no cover
    """ logs a debug message """
    level = logging.DEBUG                                                                                                        # pragma: no cover
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console)                     # pragma: no cover


@cli_main.command('verbose', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_verbose(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:                      # pragma: no cover
    """ logs a verbose message """
    level = log_levels.VERBOSE                                                                                                   # pragma: no cover
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console)                     # pragma: no cover


@cli_main.command('info', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_info(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:                         # pragma: no cover
    """ logs a info message """
    level = logging.INFO                                                                                                         # pragma: no cover
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console)                     # pragma: no cover


@cli_main.command('notice', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_notice(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:                       # pragma: no cover
    """ logs a notice message """
    level = log_levels.NOTICE                                                                                                    # pragma: no cover
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console)                     # pragma: no cover


@cli_main.command('success', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_success(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:                      # pragma: no cover
    """ logs a success message """
    level = log_levels.SUCCESS                                                                                                   # pragma: no cover
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console)                     # pragma: no cover


@cli_main.command('warning', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_warning(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:                      # pragma: no cover
    """ logs a warning message """
    level = logging.WARNING                                                                                                      # pragma: no cover
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console)                     # pragma: no cover


@cli_main.command('error', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_error(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:                        # pragma: no cover
    """ logs a error message """
    level = logging.ERROR                                                                                                        # pragma: no cover
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console)                     # pragma: no cover


@cli_main.command('critical', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_critical(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:                     # pragma: no cover
    """ logs a critical message """
    level = logging.CRITICAL                                                                                                     # pragma: no cover
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console)                     # pragma: no cover


@cli_main.command('banner_spam', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_banner_spam(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:                  # pragma: no cover
    """ logs a spam message banner """
    level = log_levels.SPAM                                                                                                      # pragma: no cover
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, banner=True)        # pragma: no cover


@cli_main.command('banner_debug', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_banner_debug(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:                 # pragma: no cover
    """ logs a debug message banner """
    level = logging.DEBUG                                                                                                        # pragma: no cover
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, banner=True)        # pragma: no cover


@cli_main.command('banner_verbose', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_banner_verbose(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:               # pragma: no cover
    """ logs a verbose message banner"""
    level = log_levels.VERBOSE                                                                                                   # pragma: no cover
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, banner=True)        # pragma: no cover


@cli_main.command('banner_info', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_banner_info(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:                  # pragma: no cover
    """ logs a info message banner """
    level = logging.INFO                                                                                                         # pragma: no cover
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, banner=True)        # pragma: no cover


@cli_main.command('banner_notice', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_banner_notice(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:                # pragma: no cover
    """ logs a notice message banner """
    level = log_levels.NOTICE                                                                                                    # pragma: no cover
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, banner=True)        # pragma: no cover


@cli_main.command('banner_success', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_banner_success(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:               # pragma: no cover
    """ logs a success message banner """
    level = log_levels.SUCCESS                                                                                                   # pragma: no cover
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, banner=True)        # pragma: no cover


@cli_main.command('banner_warning', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_banner_warning(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:               # pragma: no cover
    """ logs a warning message banner """
    level = logging.WARNING                                                                                                      # pragma: no cover
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, banner=True)        # pragma: no cover


@cli_main.command('banner_error', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_banner_error(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:                 # pragma: no cover
    """ logs a error message banner """
    level = logging.ERROR                                                                                                        # pragma: no cover
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, banner=True)        # pragma: no cover


@cli_main.command('banner_critical', context_settings=CLICK_CONTEXT_SETTINGS)
@click.argument('message')
@click.option('--banner_width', type=int, default=None, help='banner width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='if to wrap text in banners')
# if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
# if parameter --log_console is not present, it is also considered as True
# This makes it possible to silence messages elegantly in a shellscript
@click.option('--log_console', type=str, default='True', help='disable console logging if "False"')
def cli_banner_critical(message: str, banner_width: Optional[int], wrap: Optional[bool], log_console: str) -> None:              # pragma: no cover
    """ logs a critical message banner"""
    level = logging.CRITICAL                                                                                                     # pragma: no cover
    do_log(message=message, level=level, banner_width=banner_width, wrap_text=wrap, log_console=log_console, banner=True)        # pragma: no cover


@cli_main.command('color_test', context_settings=CLICK_CONTEXT_SETTINGS)
def cli_color_test() -> None:                                                                                                    # pragma: no cover
    """ prints a color test """
    lib_log_utils.banner_color_test()


# entry point if main
if __name__ == '__main__':
    lib_log_utils.BannerSettings.called_via_commandline = True
    cli_main()
