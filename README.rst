lib_log_utils
=============

|travis_build| |license| |jupyter| |pypi|

|codecov| |better_code| |cc_maintain| |cc_issues| |cc_coverage| |snyk|


.. |travis_build| image:: https://img.shields.io/travis/bitranox/lib_log_utils/master.svg
   :target: https://travis-ci.org/bitranox/lib_log_utils

.. |license| image:: https://img.shields.io/github/license/webcomics/pywine.svg
   :target: http://en.wikipedia.org/wiki/MIT_License

.. |jupyter| image:: https://mybinder.org/badge_logo.svg
 :target: https://mybinder.org/v2/gh/bitranox/lib_log_utils/master?filepath=lib_log_utils.ipynb

.. for the pypi status link note the dashes, not the underscore !
.. |pypi| image:: https://img.shields.io/pypi/status/lib-log-utils?label=PyPI%20Package
   :target: https://badge.fury.io/py/lib_log_utils

.. |codecov| image:: https://img.shields.io/codecov/c/github/bitranox/lib_log_utils
   :target: https://codecov.io/gh/bitranox/lib_log_utils

.. |better_code| image:: https://bettercodehub.com/edge/badge/bitranox/lib_log_utils?branch=master
   :target: https://bettercodehub.com/results/bitranox/lib_log_utils

.. |cc_maintain| image:: https://img.shields.io/codeclimate/maintainability-percentage/bitranox/lib_log_utils?label=CC%20maintainability
   :target: https://codeclimate.com/github/bitranox/lib_log_utils/maintainability
   :alt: Maintainability

.. |cc_issues| image:: https://img.shields.io/codeclimate/issues/bitranox/lib_log_utils?label=CC%20issues
   :target: https://codeclimate.com/github/bitranox/lib_log_utils/maintainability
   :alt: Maintainability

.. |cc_coverage| image:: https://img.shields.io/codeclimate/coverage/bitranox/lib_log_utils?label=CC%20coverage
   :target: https://codeclimate.com/github/bitranox/lib_log_utils/test_coverage
   :alt: Code Coverage

.. |snyk| image:: https://img.shields.io/snyk/vulnerabilities/github/bitranox/lib_log_utils
   :target: https://snyk.io/test/github/bitranox/lib_log_utils

this library makes it easy to log colored messages from python and from the commandline. Text Wrapping is supported.

----

automated tests, Travis Matrix, Documentation, Badges, etc. are managed with `PizzaCutter <https://github
.com/bitranox/PizzaCutter>`_ (cookiecutter on steroids)

Python version required: 3.6.0 or newer

tested on linux "bionic" with python 3.6, 3.7, 3.8, 3.8-dev, pypy3

`good code coverage <https://codecov.io/gh/bitranox/lib_log_utils>`_, codestyle checking ,mypy static type checking ,tested under `Linux, macOS, Windows <https://travis-ci.org/bitranox/lib_log_utils>`_, automatic daily builds and monitoring

----

- `Try it Online`_
- `Installation and Upgrade`_
- `Usage`_
- `Usage from Commandline`_
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

You might try it right away in Jupyter Notebook by using the "launch binder" badge, or click `here <https://mybinder.org/v2/gh/{{rst_include.
repository_slug}}/master?filepath=lib_log_utils.ipynb>`_

Installation and Upgrade
------------------------

- Before You start, its highly recommended to update pip and setup tools:


.. code-block:: bash

    python -m pip --upgrade pip
    python -m pip --upgrade setuptools
    python -m pip --upgrade wheel

- to install the latest release from PyPi via pip (recommended):

.. code-block:: bash

    # install latest release from PyPi
    python -m pip install --upgrade lib_log_utils

    # test latest release from PyPi without installing (can be skipped)
    python -m pip install lib_log_utils --install-option test

- to install the latest development version from github via pip:


.. code-block:: bash

    # normal install
    python -m pip install --upgrade git+https://github.com/bitranox/lib_log_utils.git

    # to test without installing (can be skipped)
    python -m pip install git+https://github.com/bitranox/lib_log_utils.git --install-option test

    # to install and upgrade all dependencies regardless of version number
    python -m pip install --upgrade git+https://github.com/bitranox/lib_log_utils.git --upgrade-strategy eager


- include it into Your requirements.txt:

.. code-block:: bash

    # Insert following line in Your requirements.txt:
    # for the latest Release on pypi:
    lib_log_utils

    # for the latest development version :
    lib_log_utils @ git+https://github.com/bitranox/lib_log_utils.git

    # to install and upgrade all modules mentioned in requirements.txt:
    python -m pip install --upgrade -r /<path>/requirements.txt



- to install the latest development version from source code:

.. code-block:: bash

    # cd ~
    $ git clone https://github.com/bitranox/lib_log_utils.git
    $ cd lib_log_utils

    # to test without installing (can be skipped)
    python setup.py test

    # normal install
    python setup.py install

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

Usage
-----------

.. code-block::

    import the module and check the code - its easy and documented there, including doctest examples.
    in case of any questions the usage section might be expanded at a later time


Commandline
-----------

.. code-block:: bash

   Usage:
       log_util (-h | -v | -i)
       log_util spam            <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
       log_util debug           <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
       log_util verbose         <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
       log_util info            <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
       log_util notice          <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
       log_util success         <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
       log_util warning         <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
       log_util error           <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
       log_util critical        <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
       log_util banner_spam     <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
       log_util banner_debug    <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
       log_util banner_verbose  <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
       log_util banner_info     <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
       log_util banner_notice   <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
       log_util banner_success  <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
       log_util banner_warning  <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
       log_util banner_error    <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
       log_util banner_critical <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
       log_util color_test      [ --quiet=(True|False) ]

   Options:
       -h, --help          show help
       -v, --version       show version
       -i, --info          show Info


if parameter *--log_console* is anything else then *False* (not case sensitive), then it is considered as True.

if parameter *--log_console* is not present, it is also considered as True

This makes it possible to silence messages elegantly in a shellscript:

.. code-block:: bash

       #!/bin/bash
       debug_messages="False"
       info_messages="True"
       ...
       ...
       log_util debug "some debug message ${IFS}and here the second line" --log_console=${debug_messages}
       log_util info "some info message" --log_console=${info_messages}
       ...

Usage from Commandline
------------------------

.. code-block:: bash

   Usage: log_util [OPTIONS] COMMAND [ARGS]...

     colored log messages and banners from commandline and python

   Options:
     --version   Show the version and exit.
     -h, --help  Show this message and exit.

   Commands:
     banner_critical  logs a critical message banner
     banner_debug     logs a debug message banner
     banner_error     logs a error message banner
     banner_info      logs a info message banner
     banner_notice    logs a notice message banner
     banner_spam      logs a spam message banner
     banner_success   logs a success message banner
     banner_verbose   logs a verbose message banner
     banner_warning   logs a warning message banner
     color_test       prints a color test
     critical         logs a critical message
     debug            logs a debug message
     error            logs a error message
     info             logs a info message
     notice           logs a notice message
     program_info     get program informations
     spam             logs a spam message
     success          logs a success message
     verbose          logs a verbose message
     warning          logs a warning message

Requirements
------------
following modules will be automatically installed :

.. code-block:: bash

    ## Project Requirements
    click
    coloredlogs
    lib_parameter @ git+https://github.com/bitranox/lib_parameter.git
    lib_platform @ git+https://github.com/bitranox/lib_platform.git
    lib_programname @ git+https://github.com/bitranox/lib_programname.git

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


0.1.2
-----
2020-07-14: feature release
    - store settings in environment for commandline use
    - default log level for commandline ?
    - default width 115 chars (get terminal width otherwise?) in jupyter ?
    - colored output in jupyter should work !

    - cleanup
    - release on pypi


0.1.1
-----
2020-07-06: patch release
    - new click cli
    - use PizzaCutter Template

0.0.2
-----
development

0.0.1
-----
2019-09-03: Initial public release

