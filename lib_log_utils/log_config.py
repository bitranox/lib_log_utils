# stdlib
import getpass
import logging
import os
import platform
import subprocess
import sys
from typing import Dict, Union

# OWN
import lib_platform
import lib_programname

# Custom Types
FieldAndLevelStyles = Dict[str, Dict[str, Union[str, bool]]]


class LogSettings(object):
    """ this holds all the Logger Settings - You can overwrite that values as needed from Your module """

    use_colored_stream_handler = True

    fmt_extended = '[{username}@{hostname}][{programname}@%(process)d][%(asctime)s][%(levelname)-8s]: %(message)s' \
        .format(username=getpass.getuser(),
                hostname=lib_platform.hostname_short,
                programname=lib_programname.get_path_executed_script().stem,
                )

    # todo: we might can get the ppid program name for cli
    fmt_extended_cli = '[{username}@{hostname}][%(asctime)s][%(levelname)-8s]: %(message)s' \
        .format(username=getpass.getuser(),
                hostname=lib_platform.hostname_short,
                )

    fmt_plain = '%(message)s'

    fmt = fmt_plain

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

    field_styles: FieldAndLevelStyles = \
        {
            'asctime': {'color': 'green'},
            'hostname': {'color': 'green'},                                   # 'hostname': {'color': 'magenta'},
            'levelname': {'color': 'yellow'},                                 # 'levelname': {'color': 'black', 'bold': True},
            'name': {'color': 'blue'},
            'programname': {'color': 'cyan'}
            }

    level_styles_256: FieldAndLevelStyles = \
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

    level_styles_8: FieldAndLevelStyles = \
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

    level_styles = level_styles_256


log_settings = LogSettings()


def autodetect_settings() -> int:
    """
    tries to detect and set the number of colors automatically
    - selects 8 colors for travis automatically
    - selects stream sys.stdout for jupyter binder automatically

    >>> # test Windows / Linux
    >>> if platform.system().lower() == 'windows':
    ...     assert autodetect_settings() > 0
    ... else:
    ...     assert autodetect_settings() > 0

    >>> # Test Travis
    >>> if 'TRAVIS' in os.environ:
    ...    assert autodetect_settings() > 0
    ...    save_travis_env = os.environ['TRAVIS']
    ...    discard = os.environ.pop('TRAVIS', None)
    ...    assert autodetect_settings() > 0
    ...    os.environ['TRAVIS'] = save_travis_env
    ... else:
    ...    os.environ['TRAVIS'] = 'true'
    ...    assert autodetect_settings() == 8
    ...    discard = os.environ.pop('TRAVIS', None)

    >>> # Test Binder Jupyter
    >>> os.environ['JUPYTERHUB_BASE_URL'] = '/binder/jupyter/'
    >>> assert autodetect_settings() > 0
    >>> if not 'TRAVIS' in os.environ:
    ...     assert log_settings.stream == sys.stdout
    >>> log_settings.stream = sys.stderr
    >>> os.environ['JUPYTERHUB_BASE_URL'] = '/something/else/'
    >>> assert autodetect_settings() > 0
    >>> if not 'TRAVIS' in os.environ:
    ...     assert log_settings.stream == sys.stderr
    >>> discard = os.environ.pop('JUPYTERHUB_BASE_URL', None)

    """
    if 'TRAVIS' in os.environ:
        # note that there will be no colored output on travis, as soon as
        # a secret is in travis.yaml, since then the output is filtered.
        # see also : https://travis-ci.community/t/ansi-colors-in-console-does-not-work-anymore/6608
        log_settings.level_styles = log_settings.level_styles_8
        colors = 8
        return colors

    if 'JUPYTERHUB_BASE_URL' in os.environ:
        # for binder we need stdout as stream
        if os.environ['JUPYTERHUB_BASE_URL'].lower() == '/binder/jupyter/':
            log_settings.level_styles = log_settings.level_styles_256
            log_settings.stream = sys.stdout
            colors = 256
            return colors

    if platform.system().lower() != 'windows':
        try:
            # capture_output not available under python 3.6 !
            # my_process = subprocess.run(['tput', 'colors'], check=True, capture_output=True)
            # colors = int(my_process.stdout)
            output = subprocess.check_output(['tput', 'colors'], stderr=subprocess.PIPE)
            colors = int(output)
        except subprocess.CalledProcessError:       # pragma: no cover
            colors = 256                            # pragma: no cover
    else:
        colors = 256
    return colors


autodetect_settings()
