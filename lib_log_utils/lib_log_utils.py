# STDLIB

# noinspection PyUnresolvedReferences
import getpass
# noinspection PyUnresolvedReferences
import logging

# EXT
import fire

# PROJ
# imports for local pytest
try:
    from .log_banner import *       # type: ignore # pragma: no cover
    from .log_handlers import *     # type: ignore # pragma: no cover
    from .log_levels import *       # type: ignore # pragma: no cover

# imports for doctest
except ImportError:                 # type: ignore # pragma: no cover
    from log_banner import *        # type: ignore # pragma: no cover
    from log_handlers import *      # type: ignore # pragma: no cover
    from log_levels import *        # type: ignore # pragma: no cover


def main():
    BannerSettings.called_via_commandline = True
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
