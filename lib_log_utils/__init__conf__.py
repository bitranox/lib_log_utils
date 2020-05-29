name = 'lib_log_utils'
title = 'this library makes it easy to log colored messages and banners from python and from the commandline. text wrapping is supported.'
version = '0.1.0'
url = 'https://github.com/bitranox/lib_log_utils'
author = 'Robert Nowotny'
author_email = 'rnowotny1966@gmail.com'
shell_command = 'log_util'


def print_version() -> None:
    print('version: 0.1.0')


def print_info() -> None:
    print("""information for "lib_log_utils":

          this library makes it easy to log colored messages and banners from python and from the commandline. text wrapping is supported.

          Version      : 0.1.0
          url          : https://github.com/bitranox/lib_log_utils
          author       : Robert Nowotny
          author_email : rnowotny1966@gmail.com""")
