# STDLIB
import os
import sys
from typing import List, Optional

# EXT
import click    # noqa

# CONSTANTS
CLICK_CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

# PROJ
try:
    from . import __init__conf__
    from . import cli_exit_tools
    from . import lib_log_utils
    from . import log_levels
except (ImportError, ModuleNotFoundError):  # pragma: no cover
    # imports for doctest
    import __init__conf__                   # type: ignore  # pragma: no cover
    import cli_exit_tools                   # type: ignore  # pragma: no cover
    import lib_log_utils                    # type: ignore  # pragma: no cover
    import log_levels                       # type: ignore  # pragma: no cover


def cli_info() -> None:
    """
    >>> cli_info()
    Info for ...

    """
    __init__conf__.print_info()


def do_log(message: str, level_str: str = 'info', banner: bool = False, width: Optional[int] = None,
           wrap: Optional[bool] = None, silent: Optional[str] = None, quiet: Optional[bool] = None, force: bool = False) -> None:

    """
    >>> do_log('test', banner=False)
    >>> do_log('test', banner=True)

    """
    if silent is not None:
        # this is intentionally, we accept every value, only "true" is handled !
        if silent.lower().startswith('true'):
            quiet = True
        else:
            quiet = False

    level = log_levels.get_log_level_from_str(level_str)
    set_logger_level_from_env()
    set_width_from_env(width, force)
    set_wrap_from_env(wrap, force)
    set_quiet_from_env(quiet, force)
    lib_log_utils.log_level(message=message, level=level, banner=banner)


def set_logger_level_from_env() -> None:
    """
    >>> # Setup
    >>> log_level_default = lib_log_utils.LogSettings.new_logger_level

    >>> # no env Set
    >>> set_logger_level_from_env()
    >>> assert lib_log_utils.LogSettings.new_logger_level == log_level_default

    >>> # env Set spam
    >>> os.environ['log_utils_log_level']='spam'
    >>> set_logger_level_from_env()
    >>> assert lib_log_utils.LogSettings.new_logger_level == 5

    >>> # env Set unknown
    >>> os.environ['log_utils_log_level']='unknown'
    >>> set_logger_level_from_env()
    Traceback (most recent call last):
        ...
    ValueError: the environment setting "log_utils_log_level" has to be from ...

    >>> # Teardown
    >>> del os.environ['log_utils_log_level']
    >>> lib_log_utils.LogSettings.new_logger_level = log_level_default

    """

    if 'log_utils_log_level' in os.environ:
        try:
            lib_log_utils.LogSettings.new_logger_level = log_levels.get_log_level_from_str(os.environ['log_utils_log_level'])
        except ValueError:
            raise ValueError('the environment setting "log_utils_log_level" has to be from 0-50 or one of the predefined logging levels')


def set_width_from_env(width: Optional[int] = None, force: bool = False) -> None:
    # env settings have precedence, unless force=True - if nothing is passed, the default value will be used
    """
    >>> # Setup
    >>> default_banner_width = lib_log_utils.LogSettings.width

    >>> # No env Setting, width=None
    >>> set_width_from_env()
    >>> assert lib_log_utils.LogSettings.width == default_banner_width

    >>> # No env Setting, width = default + 1
    >>> set_width_from_env(default_banner_width + 1)
    >>> assert lib_log_utils.LogSettings.width == default_banner_width + 1

    >>> # Env Setting = default + 2, width=None
    >>> os.environ['log_utils_width'] = str(default_banner_width + 2)
    >>> set_width_from_env()
    >>> assert lib_log_utils.LogSettings.width == default_banner_width + 2

    >>> # Env Setting = default + 3, width=default (env has precedence)
    >>> os.environ['log_utils_width'] = str(default_banner_width + 3)
    >>> set_width_from_env(default_banner_width)
    >>> assert lib_log_utils.LogSettings.width == default_banner_width + 3

    >>> # Env Setting = default + 3, width=default + 4, force = True (parameter has precedence)
    >>> set_width_from_env(default_banner_width + 4, True)
    >>> assert lib_log_utils.LogSettings.width == default_banner_width + 4

    >>> # provoke Error wrong type
    >>> os.environ['log_utils_width'] = 'abc'
    >>> set_width_from_env()
    Traceback (most recent call last):
        ...
    ValueError: invalid environment setting for "log_utils_width", must be numerical and >= 10

    >>> # provoke Error too small
    >>> os.environ['log_utils_width'] = '9'
    >>> set_width_from_env()
    Traceback (most recent call last):
        ...
    ValueError: invalid environment setting for "log_utils_width", must be numerical and >= 10

    >>> # Teardown
    >>> lib_log_utils.LogSettings.width = default_banner_width
    >>> del os.environ['log_utils_width']

    """

    if 'log_utils_width' in os.environ:
        if width is not None and force:
            lib_log_utils.LogSettings.width = width
        else:
            s_error = 'invalid environment setting for "log_utils_width", must be numerical and >= 10'
            try:
                width = int(os.environ['log_utils_width'])
            except ValueError:
                raise ValueError(s_error)
            if width < 10:
                raise ValueError(s_error)
            lib_log_utils.LogSettings.width = width
    else:
        if width is not None:
            lib_log_utils.LogSettings.width = width


def set_wrap_from_env(wrap_text: Optional[bool] = None, force: bool = False) -> None:
    # env settings have precedence, unless force=True - if nothing is passed, the default value will be used
    """
    >>> # Setup
    >>> default_wrap_text = lib_log_utils.LogSettings.wrap_text

    >>> # No env Setting, wrap_text=None
    >>> set_wrap_from_env()
    >>> assert lib_log_utils.LogSettings.wrap_text == default_wrap_text

    >>> # No env Setting, wrap_text = not default_wrap_text
    >>> set_wrap_from_env(not default_wrap_text)
    >>> assert lib_log_utils.LogSettings.wrap_text != default_wrap_text

    >>> # Env Setting = not default_wrap_text, wrap_text=None
    >>> os.environ['log_utils_wrap_text'] = str(not default_wrap_text)
    >>> set_wrap_from_env()
    >>> assert lib_log_utils.LogSettings.wrap_text != default_wrap_text

    >>> # Env Setting = not default_wrap_text, wrap_text=default_wrap_text (env has precedence)
    >>> os.environ['log_utils_wrap_text'] = str(not default_wrap_text)
    >>> set_wrap_from_env(default_wrap_text)
    >>> assert lib_log_utils.LogSettings.wrap_text != default_wrap_text

    >>> # Env Setting = not default_wrap_text, wrap_text=default_wrap_text (parameter has precedence)
    >>> set_wrap_from_env(default_wrap_text, True)
    >>> assert lib_log_utils.LogSettings.wrap_text == default_wrap_text

    >>> # provoke Error
    >>> os.environ['log_utils_wrap_text'] = 'something'
    >>> set_wrap_from_env()
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


def set_quiet_from_env(quiet: Optional[bool] = None, force: bool = False) -> None:
    # env settings have precedence, unless force=True - if nothing is passed, the default value will be used
    # parameter -q is anything else then "True" (not case sensitive), or not set, it is considered as False.
    """
    >>> # Setup
    >>> default_quiet = lib_log_utils.LogSettings.quiet

    >>> # No env Setting, log_console=None
    >>> set_quiet_from_env()
    >>> assert lib_log_utils.LogSettings.quiet == default_quiet

    >>> # No env Setting, log_console = default_quiet
    >>> set_quiet_from_env(not default_quiet)
    >>> assert lib_log_utils.LogSettings.quiet != default_quiet

    >>> # Env Setting = not default_quiet, log_console=None
    >>> os.environ['log_utils_quiet'] = str(not default_quiet)
    >>> set_quiet_from_env()
    >>> assert lib_log_utils.LogSettings.quiet != default_quiet

    >>> # Env Setting = not default_quiet, log_console=not default_quiet (env has precedence)
    >>> os.environ['log_utils_quiet'] = str(not default_quiet)
    >>> set_quiet_from_env(default_quiet)
    >>> assert lib_log_utils.LogSettings.quiet != default_quiet

    >>> # Env Setting = not default_quiet, log_console=default_quiet (parameter has precedence)
    >>> set_quiet_from_env(default_quiet, True)
    >>> assert lib_log_utils.LogSettings.quiet == default_quiet

    >>> # provoke Error
    >>> os.environ['log_utils_quiet'] = 'something'
    >>> set_quiet_from_env()
    Traceback (most recent call last):
        ...
    ValueError: invalid environment setting for "log_utils_quiet", must be "True" or "False"

    >>> # Teardown
    >>> lib_log_utils.LogSettings.quiet = default_quiet
    >>> del os.environ['log_utils_quiet']

    """

    if 'log_utils_quiet' in os.environ:
        if quiet is not None and force:
            lib_log_utils.LogSettings.quiet = quiet
        else:
            if os.environ['log_utils_quiet'].lower().startswith('false'):
                lib_log_utils.LogSettings.quiet = False
            elif os.environ['log_utils_quiet'].lower().startswith('true'):
                lib_log_utils.LogSettings.quiet = True
            else:
                raise ValueError('invalid environment setting for "log_utils_quiet", must be "True" or "False"')
    else:
        if quiet is not None:
            lib_log_utils.LogSettings.quiet = quiet


@click.command(help=__init__conf__.title, context_settings=CLICK_CONTEXT_SETTINGS)
@click.version_option(version=__init__conf__.version,
                      prog_name=__init__conf__.shell_command,
                      message='{} version %(version)s'.format(__init__conf__.shell_command))
@click.option('-b', '--banner', is_flag=True, type=bool, default=False, help='log as banner')
@click.option('-w', '--width', type=int, default=None, help='wrap width, default=140')
@click.option('--wrap/--nowrap', type=bool, default=None, help='wrap text')
# if parameter -q is anything else then "True" (not case sensitive), or not set, it is considered as False.
# This makes it possible to silence messages elegantly in a shellscript
@click.option('-s', '--silent', type=str, default=None, help='disable logging if "True"')
@click.option('-q', '--quiet', is_flag=True, type=bool, default=None, help='disable logging as flag')
@click.option('-f', '--force', is_flag=True, type=bool, default=False, help='take precedence over environment settings')
@click.option('-l', '--level', type=str, default="info", help='log level as number or predefined Level')
@click.option('--program_info', is_flag=True, type=bool, default=False, help='get program info')
@click.option('-c', '--colortest', is_flag=True, type=bool, default=False, help='color test')
@click.option('--traceback/--no-traceback', is_flag=True, type=bool, default=None, help='return traceback information on cli')
@click.argument('message', required=False, default='')
def cli_main(message: str, level: str, banner: bool, width: Optional[int], wrap: Optional[bool],
             silent: Optional[str], quiet: Optional[bool], force: bool, program_info: bool, colortest: bool, traceback: Optional[bool] = None) -> None:
    """ log a message """
    if traceback is not None:
        cli_exit_tools.config.traceback = traceback
    if program_info:
        cli_info()
    elif colortest:
        lib_log_utils.colortest()
    else:
        do_log(message=message, level_str=level, banner=banner, width=width, wrap=wrap, silent=silent, quiet=quiet, force=force)


# entry point if main
if __name__ == '__main__':
    try:
        cli_main()
    except Exception as exc:
        cli_exit_tools.print_exception_message()
        sys.exit(cli_exit_tools.get_system_exit_code(exc))
