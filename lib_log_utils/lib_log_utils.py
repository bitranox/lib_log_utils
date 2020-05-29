# STDLIB
from docopt import docopt                   # type: ignore
import errno
from typing import Dict, Union
# noinspection PyUnresolvedReferences
import getpass
# noinspection PyUnresolvedReferences
import logging
import sys

# PROJ
try:
    from .__doc__ import __doc__
    from . import __init__conf__
    from .log_banner import *       # type: ignore # pragma: no cover
except ImportError:
    # imports for doctest
    from __doc__ import __doc__     # type: ignore  # pragma: no cover
    import __init__conf__           # type: ignore  # pragma: no cover
    from log_banner import *        # type: ignore # pragma: no cover


def set_options(docopt_args: Dict[str, Union[bool, str]]) -> None:
    """
    >>> docopt_args = dict()
    >>> docopt_args['--banner_width']='10'
    >>> docopt_args['--wrap']=True
    >>> docopt_args['--nowrap']=False
    >>> docopt_args['--log_console']=False

    >>> set_options(docopt_args)
    >>> assert BannerSettings.banner_width == 10
    >>> assert not BannerSettings.quiet
    >>> assert BannerSettings.wrap_text
    >>> assert not BannerSettings.quiet

    >>> docopt_args['--wrap']=False
    >>> docopt_args['--nowrap']=True
    >>> docopt_args['--log_console']=True
    >>> set_options(docopt_args)
    >>> assert not BannerSettings.wrap_text
    >>> assert not BannerSettings.quiet

    >>> docopt_args['--log_console']='False'''
    >>> set_options(docopt_args)
    >>> assert BannerSettings.quiet

    >>> docopt_args['--banner_width']='not_int_convertible'
    >>> set_options(docopt_args)    # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
        ...
    ValueError: Parameter "--width" needs to be convertible to integer

    """

    if docopt_args['--banner_width']:
        try:
            banner_width = int(docopt_args['--banner_width'])
        except (ValueError, TypeError):
            error_msg = 'Parameter "--width" needs to be convertible to integer'
            log_critical(error_msg)
            raise ValueError(error_msg)
        BannerSettings.banner_width = banner_width

    if docopt_args['--wrap']:
        BannerSettings.wrap_text = True
    elif docopt_args['--nowrap']:
        BannerSettings.wrap_text = False

    if docopt_args['--log_console']:
        if str(docopt_args['--log_console']).lower() == 'false':
            BannerSettings.quiet = True


# we might import this module and call main from another program and pass docopt args manually
def main(docopt_args: Dict[str, Union[bool, str]]) -> None:
    """
    >>> docopt_args = dict()

    >>> docopt_args['<message>']='test'
    >>> docopt_args['--banner_width']=False
    >>> docopt_args['--wrap']=False
    >>> docopt_args['--nowrap']=False
    >>> docopt_args['--log_console']=False

    >>> docopt_args['spam']=False
    >>> docopt_args['debug']=False
    >>> docopt_args['verbose']=False
    >>> docopt_args['info']=False
    >>> docopt_args['notice']=False
    >>> docopt_args['success']=False
    >>> docopt_args['warning']=False
    >>> docopt_args['error']=False
    >>> docopt_args['critical']=False
    >>> docopt_args['banner_spam']=False
    >>> docopt_args['banner_debug']=False
    >>> docopt_args['banner_verbose']=False
    >>> docopt_args['banner_info']=False
    >>> docopt_args['banner_notice']=False
    >>> docopt_args['banner_success']=False
    >>> docopt_args['banner_warning']=False
    >>> docopt_args['banner_error']=False
    >>> docopt_args['banner_critical']=False
    >>> docopt_args['color_test']=False

    >>> docopt_args['--version'] = True
    >>> docopt_args['--info'] = False
    >>> main(docopt_args)   # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
    version: ...

    >>> docopt_args['--version'] = False
    >>> docopt_args['--info'] = True
    >>> main(docopt_args)   # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
    information for ...

    >>> docopt_args['--version'] = False
    >>> docopt_args['--info'] = False
    >>> main(docopt_args)

    >>> docopt_args['color_test']=True
    >>> main(docopt_args)

    >>> docopt_args['banner_critical']=True
    >>> docopt_args['<message>']='banner_critical'
    >>> main(docopt_args)

    >>> docopt_args['banner_error']=False
    >>> docopt_args['<message>']='banner_error'
    >>> main(docopt_args)

    >>> docopt_args['banner_warning']=False
    >>> docopt_args['<message>']='banner_warning'
    >>> main(docopt_args)

    >>> docopt_args['banner_success']=False
    >>> docopt_args['<message>']='banner_success'
    >>> main(docopt_args)

    >>> docopt_args['banner_notice']=False
    >>> docopt_args['<message>']='banner_notice'
    >>> main(docopt_args)

    >>> docopt_args['banner_info']=False
    >>> docopt_args['<message>']='banner_info'
    >>> main(docopt_args)

    >>> docopt_args['banner_verbose']=False
    >>> docopt_args['<message>']='banner_verbose'
    >>> main(docopt_args)

    >>> docopt_args['banner_debug']=False
    >>> docopt_args['<message>']='banner_debug'
    >>> main(docopt_args)

    >>> docopt_args['banner_spam']=False
    >>> docopt_args['<message>']='banner_spam'
    >>> main(docopt_args)

    >>> docopt_args['critical']=False
    >>> docopt_args['<message>']='critical'
    >>> main(docopt_args)

    >>> docopt_args['error']=False
    >>> docopt_args['<message>']='error'
    >>> main(docopt_args)

    >>> docopt_args['warning']=False
    >>> docopt_args['<message>']='warning'
    >>> main(docopt_args)

    >>> docopt_args['success']=False
    >>> docopt_args['<message>']='success'
    >>> main(docopt_args)

    >>> docopt_args['notice']=False
    >>> docopt_args['<message>']='notice'
    >>> main(docopt_args)

    >>> docopt_args['info']=False
    >>> docopt_args['<message>']='info'
    >>> main(docopt_args)

    >>> docopt_args['verbose']=False
    >>> docopt_args['<message>']='verbose'
    >>> main(docopt_args)

    >>> docopt_args['debug']=False
    >>> docopt_args['<message>']='debug'
    >>> main(docopt_args)

    >>> docopt_args['spam']=False
    >>> docopt_args['<message>']='spam'
    >>> main(docopt_args)


    """

    if docopt_args['--version']:
        __init__conf__.print_version()

    if docopt_args['--info']:
        __init__conf__.print_info()

    set_options(docopt_args)

    message = str(docopt_args['<message>'])

    if docopt_args['spam']:
        log_spam(message)
    elif docopt_args['debug']:
        log_debug(message)
    elif docopt_args['verbose']:
        log_verbose(message)
    elif docopt_args['info']:
        log_info(message)
    elif docopt_args['notice']:
        log_notice(message)
    elif docopt_args['success']:
        log_success(message)
    elif docopt_args['warning']:
        log_warning(message)
    elif docopt_args['error']:
        log_error(message)
    elif docopt_args['critical']:
        log_critical(message)

    elif docopt_args['banner_spam']:
        banner_spam(message)
    elif docopt_args['banner_debug']:
        banner_debug(message)
    elif docopt_args['banner_verbose']:
        banner_verbose(message)
    elif docopt_args['banner_info']:
        banner_info(message)
    elif docopt_args['banner_notice']:
        banner_notice(message)
    elif docopt_args['banner_success']:
        banner_success(message)
    elif docopt_args['banner_warning']:
        banner_warning(message)
    elif docopt_args['banner_error']:
        banner_error(message)
    elif docopt_args['banner_critical']:
        banner_critical(message)
    elif docopt_args['color_test']:
        banner_color_test()


# entry point via commandline
def main_commandline() -> None:
    """
    >>> main_commandline()  # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
        ...
    docopt.DocoptExit: ...

    """
    BannerSettings.called_via_commandline = True
    docopt_args = docopt(__doc__)
    main(docopt_args)               # pragma: no cover


# entry point if main
if __name__ == '__main__':
    try:
        main_commandline()
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
