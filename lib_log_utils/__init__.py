import pathlib
from .lib_log_utils import *
# noinspection PyUnresolvedReferences
from .log_banner import *
# noinspection PyUnresolvedReferences
from .log_handlers import *
# noinspection PyUnresolvedReferences
from .log_levels import *
# noinspection PyUnresolvedReferences
from .log_traceback import *


def get_version() -> str:
    with open(str(pathlib.Path(__file__).parent / 'version.txt'), mode='r') as version_file:
        version = version_file.readline()
    return version


__title__ = 'lib_log_utils'
__version__ = get_version()
__name__ = 'lib_log_utils'
