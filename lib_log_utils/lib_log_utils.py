# STDLIB
import errno
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
try:
    from .log_banner import *       # type: ignore # pragma: no cover
except (ImportError, ModuleNotFoundError):
    from log_banner import *        # type: ignore # pragma: no cover


def main() -> None:
    try:
        BannerSettings.called_via_commandline = True
        # we must not call fire if the program is called via pytest
        print(sys.argv)
        is_called_via_pytest = [(sys_arg != '') for sys_arg in sys.argv if 'pytest' in sys_arg]
        if not is_called_via_pytest:
            fire.Fire({'banner_color_test': banner_color_test,
                       'banner_spam': banner_spam,
                       'banner_debug': banner_debug,
                       'banner_verbose': banner_verbose,
                       'banner_info': banner_info,
                       'banner_notice': banner_notice,
                       'banner_success': banner_success,
                       'banner_warning': banner_warning,
                       'banner_error': banner_error,
                       'banner_critical': banner_critical})

    except FileNotFoundError:
        # see https://www.thegeekstuff.com/2010/10/linux-error-codes for error codes
        # No such file or directory
        sys.exit(errno.ENOENT)      # pragma: no cover
    except FileExistsError:
        # File exists
        sys.exit(errno.EEXIST)      # pragma: no cover
    except TypeError:
        # Invalid Argument
        sys.exit(errno.EINVAL)      # pragma: no cover
        # Invalid Argument
    except ValueError:
        sys.exit(errno.EINVAL)      # pragma: no cover


if __name__ == '__main__':
    main()
