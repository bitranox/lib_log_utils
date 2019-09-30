# STDLIB
# noinspection PyUnresolvedReferences
import getpass
# noinspection PyUnresolvedReferences
import logging
import sys

# EXT
# noinspection PyBroadException
try:
    import fire                             # type: ignore
except Exception:
    # maybe we dont need fire if not called via commandline, so accept if it is not there
    pass

# PROJ
# imports for local pytest
try:
    from .log_banner import *       # type: ignore # pragma: no cover

# imports for doctest
except ImportError:                 # type: ignore # pragma: no cover
    from log_banner import *        # type: ignore # pragma: no cover


def main() -> None:
    BannerSettings.called_via_commandline = True
    # we must not call fire if the program is called via pytest
    is_called_via_pytest = [(sys_arg != '') for sys_arg in sys.argv if 'pytest' in sys_arg]
    if not is_called_via_pytest:
        fire.Fire({
            'banner_color_test': banner_color_test,
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
