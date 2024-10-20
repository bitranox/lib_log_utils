lib_log_utils
=============


Version v1.4.15 as of 2024-10-20 see `Changelog`_

|build_badge| |codeql| |license| |jupyter| |pypi|
|pypi-downloads| |black| |codecov| |cc_maintain| |cc_issues| |cc_coverage| |snyk|



.. |build_badge| image:: https://github.com/bitranox/lib_log_utils/actions/workflows/python-package.yml/badge.svg
   :target: https://github.com/bitranox/lib_log_utils/actions/workflows/python-package.yml


.. |codeql| image:: https://github.com/bitranox/lib_log_utils/actions/workflows/codeql-analysis.yml/badge.svg?event=push
   :target: https://github.com//bitranox/lib_log_utils/actions/workflows/codeql-analysis.yml

.. |license| image:: https://img.shields.io/github/license/webcomics/pywine.svg
   :target: http://en.wikipedia.org/wiki/MIT_License

.. |jupyter| image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/bitranox/lib_log_utils/master?filepath=lib_log_utils.ipynb

.. for the pypi status link note the dashes, not the underscore !
.. |pypi| image:: https://img.shields.io/pypi/status/lib-log-utils?label=PyPI%20Package
   :target: https://badge.fury.io/py/lib_log_utils

.. badge until 2023-10-08:
.. https://img.shields.io/codecov/c/github/bitranox/lib_log_utils
.. badge from 2023-10-08:
.. |codecov| image:: https://codecov.io/gh/bitranox/lib_log_utils/graph/badge.svg
   :target: https://codecov.io/gh/bitranox/lib_log_utils

.. |cc_maintain| image:: https://img.shields.io/codeclimate/maintainability-percentage/bitranox/lib_log_utils?label=CC%20maintainability
   :target: https://codeclimate.com/github/bitranox/lib_log_utils/maintainability
   :alt: Maintainability

.. |cc_issues| image:: https://img.shields.io/codeclimate/issues/bitranox/lib_log_utils?label=CC%20issues
   :target: https://codeclimate.com/github/bitranox/lib_log_utils/maintainability
   :alt: Maintainability

.. |cc_coverage| image:: https://img.shields.io/codeclimate/coverage/bitranox/lib_log_utils?label=CC%20coverage
   :target: https://codeclimate.com/github/bitranox/lib_log_utils/test_coverage
   :alt: Code Coverage

.. |snyk| image:: https://snyk.io/test/github/bitranox/lib_log_utils/badge.svg
   :target: https://snyk.io/test/github/bitranox/lib_log_utils

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/lib-log-utils
   :target: https://pypi.org/project/lib-log-utils/
   :alt: PyPI - Downloads

this library makes it easy to log colored messages from python and from the commandline. Text Wrapping is supported.

whenever possible, it tries to autodetect the correct settings for colored output.

currently the settings for TRAVIS and BINDER/Jupyter are detected automatically

----

automated tests, Github Actions, Documentation, Badges, etc. are managed with `PizzaCutter <https://github
.com/bitranox/PizzaCutter>`_ (cookiecutter on steroids)

Python version required: 3.8.0 or newer

tested on recent linux with python 3.8, 3.9, 3.10, 3.11, 3.12, pypy-3.9, pypy-3.10, graalpy-24.1 - architectures: amd64

`good code coverage <https://codeclimate.com/github/bitranox/lib_log_utils/test_coverage>`_, flake8 style checking ,mypy static type checking ,tested under `Linux, macOS, Windows <https://github.com/bitranox/lib_log_utils/actions/workflows/python-package.yml>`_, automatic daily builds and monitoring

----

- `Try it Online`_
- `Usage`_
- `Usage from Commandline`_
- `Installation and Upgrade`_
- `Requirements`_
- `Acknowledgements`_
- `Contribute`_
- `Report Issues <https://github.com/bitranox/lib_log_utils/blob/master/ISSUE_TEMPLATE.md>`_
- `Pull Request <https://github.com/bitranox/lib_log_utils/blob/master/PULL_REQUEST_TEMPLATE.md>`_
- `Code of Conduct <https://github.com/bitranox/lib_log_utils/blob/master/CODE_OF_CONDUCT.md>`_
- `License`_
- `Changelog`_

----

Try it Online
-------------

You might try it right away in Jupyter Notebook by using the "launch binder" badge,
or click `here <https://mybinder.org/v2/gh/bitranox/lib_log_utils/master?filepath=lib_log_utils.ipynb>`_

Usage
-----------

Python
-----------


import the module and check the code - it is very easy and documented there

as soon as I have some time, this will be completed (help welcome)


Commandline
-----------

.. code-block:: bash

   Usage:

        log_util (-h | --version | --program_info)
        log_util [Options] "<message>"
        log_util "<message>" [Options]

   Options:
        -h, --help          show help
        --version           show version
        --program_info      show Program Info


Arguments
---------

message
    the message to log



Options
-------

===========================  ====================================================================================
option                       description
===========================  ====================================================================================
-l --level <level>           the log level as number or predefined value, default = INFO
-b --banner                  log as banner
-w --width <width>           the width of the message or the banner, if text wrap is used, default = 140
-s --silent <True|False> **  disables the output if set to "True" (not case sensitive)**, default = False
-q --quiet                   disables the output (as flag), default = False
-f --force                   take precedence over environment settings, default = False
--wrap --nowrap              use text wrap (this is the default value), default = True
--traceback --no-traceback   show traceback on commandline error, default = False
-e --extended                extended log format, default = plain
-p --plain                   plain log format, default = plain
-c --colortest               color test
===========================  ====================================================================================


\**This makes it possible to silence messages elegantly in a shellscript:

.. code-block:: bash

        #!/bin/bash

        # disable deprecation messages
        DEP_MSG_OFF="True"

       ...
       ...
       log_util -l warning "some deprecation message" --silent=${DEP_MSG_OFF}
       log_util -l info "another deprecation message" --silent=${DEP_MSG_OFF}
       ...


log levels
--------------------

=========   ===========
Text        Integer
=========   ===========
NOTSET      0
SPAM        5
DEBUG       10
VERBOSE     15
INFO        20
NOTICE      25
WARNING     30
SUCCESS     35
ERROR       40
CRITICAL    50
=========   ===========


Environment Settings
--------------------

========================  =======================================================================================
environment variable      function
========================  =======================================================================================
LOG_UTIL_FMT              the log format - either "plain", "extended" or a custom formatting string, default = plain
LOG_UTIL_LEVEL            the level of the logger, one of the predefined log levels, or "0" - "50", default = 0
LOG_UTIL_WIDTH            the banner width if text wrap is used, must be >="10", default = 140
LOG_UTIL_WRAP             if text wrap should be used, must be True or False (not case sensitive), default = True
LOG_UTIL_QUIET            if the logger is used at all - must be True or False (not case sensitive), default = False
COLOREDLOGS_LOG_FORMAT    `as described in coloredlogs <https://coloredlogs.readthedocs.io/en/latest/api.html#environment-variables>`_
COLOREDLOGS_DATE_FORMAT   `as described in coloredlogs <https://coloredlogs.readthedocs.io/en/latest/api.html#environment-variables>`_
COLOREDLOGS_FIELD_STYLES  `as described in coloredlogs <https://coloredlogs.readthedocs.io/en/latest/api.html#environment-variables>`_
COLOREDLOGS_LEVEL_STYLES  `as described in coloredlogs <https://coloredlogs.readthedocs.io/en/latest/api.html#environment-variables>`_
========================  =======================================================================================

environment settings take precedence over commandline arguments, unless --force is passed to the commandline


EXAMPLES
--------


.. code-block:: bash

    # multi-line banner
    log_util -l warning "Line1${IFS}Line2${IFS}Line3"

    # only show log messages from level WARNING upwards
    export LOG_UTIL_LEVEL=WARNING

    log_util -l info   "spam"   # this is not shown
    log_util -l error  "ham"    # this is shown

    # reset the log_level to 0 (the default value)
    unset LOG_UTIL_LEVEL

Usage from Commandline
------------------------

.. code-block::

   Usage: log_util [OPTIONS] [MESSAGE]

     colored log messages and banners from commandline and python

   Options:
     --version                     Show the version and exit.
     -e, --extended                extended log format
     -p, --plain                   plain log format
     -b, --banner                  log as banner
     -w, --width INTEGER           wrap width, default=140
     --wrap / --nowrap             wrap text
     -s, --silent TEXT             disable logging if "True"
     -q, --quiet                   disable logging as flag
     -f, --force                   take precedence over environment settings
     -l, --level TEXT              log level as number or predefined Level
     --program_info                get program info
     -c, --colortest               color test
     --traceback / --no-traceback  return traceback information on cli
     -h, --help                    Show this message and exit.

Installation and Upgrade
------------------------

- Before You start, its highly recommended to update pip:


.. code-block::

    python -m pip --upgrade pip

- to install the latest release from PyPi via pip (recommended):

.. code-block::

    python -m pip install --upgrade lib_log_utils


- to install the latest release from PyPi via pip, including test dependencies:

.. code-block::

    python -m pip install --upgrade lib_log_utils[test]

- to install the latest version from github via pip:


.. code-block::

    python -m pip install --upgrade git+https://github.com/bitranox/lib_log_utils.git


- include it into Your requirements.txt:

.. code-block::

    # Insert following line in Your requirements.txt:
    # for the latest Release on pypi:
    lib_log_utils

    # for the latest development version :
    lib_log_utils @ git+https://github.com/bitranox/lib_log_utils.git

    # to install and upgrade all modules mentioned in requirements.txt:
    python -m pip install --upgrade -r /<path>/requirements.txt


- to install the latest development version, including test dependencies from source code:

.. code-block::

    # cd ~
    $ git clone https://github.com/bitranox/lib_log_utils.git
    $ cd lib_log_utils
    python -m pip install -e .[test]

- via makefile:
  makefiles are a very convenient way to install. Here we can do much more,
  like installing virtual environments, clean caches and so on.

.. code-block:: shell

    # from Your shell's homedirectory:
    $ git clone https://github.com/bitranox/lib_log_utils.git
    $ cd lib_log_utils

    # to run the tests:
    $ make test

    # to install the package
    $ make install

    # to clean the package
    $ make clean

    # uninstall the package
    $ make uninstall

Requirements
------------
following modules will be automatically installed :

.. code-block:: bash

    ## Project Requirements
    click
    coloredlogs
    cli_exit_tools
    lib_parameter
    lib_platform
    lib_programname

Acknowledgements
----------------

- special thanks to "uncle bob" Robert C. Martin, especially for his books on "clean code" and "clean architecture"

Contribute
----------

I would love for you to fork and send me pull request for this project.
- `please Contribute <https://github.com/bitranox/lib_log_utils/blob/master/CONTRIBUTING.md>`_

License
-------

This software is licensed under the `MIT license <http://en.wikipedia.org/wiki/MIT_License>`_

---

Changelog
=========

- new MAJOR version for incompatible API changes,
- new MINOR version for added functionality in a backwards compatible manner
- new PATCH version for backwards compatible bug fixes

v1.4.15
--------
2023-07-21:
    - require minimum python 3.8
    - remove python 3.7 tests
    - introduce PEP517 packaging standard
    - introduce pyproject.toml build-system
    - remove mypy.ini
    - remove pytest.ini
    - remove setup.cfg
    - remove setup.py
    - remove .bettercodehub.yml
    - remove .travis.yml
    - update black config
    - clean ./tests/test_cli.py
    - add codeql badge
    - move 3rd_party_stubs outside the src directory to ``./.3rd_party_stubs``
    - add pypy 3.10 tests
    - add python 3.12-dev tests


v1.4.14.2
---------
2022-06-02: update to github actions checkout@v3 and setup-python@v3

v1.4.14
--------
2022-03-29: remedy mypy type error in lob_log_utils_cli

v1.4.13
---------
2022-03-25:
 - fix ValueError: underlying buffer has been detached on github Actions Windows
 - implement github actions
 - update documentation and tests
 - list ./dist dir if existing
 - fix requirements.txt

v1.4.10
---------
2020-10-09: service release
    - update travis build matrix for linux 3.9-dev
    - update travis build matrix (paths) for windows 3.9 / 3.10

v1.4.9
--------
2020-08-08: service release
    - fix documentation
    - fix travis
    - deprecate pycodestyle
    - implement flake8

v1.4.8
---------
2020-08-01: fix doctests in windows

v1.4.7
---------
2020-08-01: fix pypi deploy

v1.4.6
---------
2020-07-31: fix travis build

v0.4.5
---------
2020-07-29: fix environ.pop issue in doctest


v0.4.4
---------
2020-07-29: feature release
    - use the new pizzacutter template

v0.4.3
---------
2020-07-27: feature release
    - use cli_exit_tools
    - add banner parameter, to temporary disable/enable banner

v0.4.2
---------
2020-07-23: separate travis profile

v0.4.1
---------
2020-07-23: change color profiles

v0.4.0
---------
2020-07-23: feature release
    - correct print_exception_traceback is stdout, stderr = None
    - added formatting parameter, custom log formatter

v0.3.0
---------
2020-07-22: feature release
    - autodetect travis settings
    - autodetect binder/jupyter settings

v0.2.0
---------
2020-07-22: feature release
    - log_exception_traceback and print_exception_traceback will also report stdout, stderr if present


v0.1.4
---------
2020-07-17: feature release
    - bump coverage

v0.1.3
---------
2020-07-17: feature release
    - comprehensive *--colortest*
    - automatically select 8 colors profile for travis

v0.1.2
---------
2020-07-16: feature release
    - store settings in environment for commandline use
    - cleanup
    - release on pypi
    - fix cli test
    - enable traceback option on cli errors
    - jupyter notebook

v0.1.1
---------
2020-07-06: patch release
    - new click cli
    - use PizzaCutter Template

v0.0.2
---------
development

v0.0.1
---------
2019-09-03: Initial public release

