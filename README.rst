lib_log_utils
=============

|Pypi Status| |license| |maintenance|

|Build Status| |Codecov Status| |Better Code| |code climate| |code climate coverage| |snyk security|

.. |license| image:: https://img.shields.io/github/license/webcomics/pywine.svg
   :target: http://en.wikipedia.org/wiki/MIT_License
.. |maintenance| image:: https://img.shields.io/maintenance/yes/2021.svg
.. |Build Status| image:: https://travis-ci.org/bitranox/lib_log_utils.svg?branch=master
   :target: https://travis-ci.org/bitranox/lib_log_utils
.. for the pypi status link note the dashes, not the underscore !
.. |Pypi Status| image:: https://badge.fury.io/py/lib-log-utils.svg
   :target: https://badge.fury.io/py/lib_log_utils
.. |Codecov Status| image:: https://codecov.io/gh/bitranox/lib_log_utils/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/bitranox/lib_log_utils
.. |Better Code| image:: https://bettercodehub.com/edge/badge/bitranox/lib_log_utils?branch=master
   :target: https://bettercodehub.com/results/bitranox/lib_log_utils
.. |snyk security| image:: https://snyk.io/test/github/bitranox/lib_log_utils/badge.svg
   :target: https://snyk.io/test/github/bitranox/lib_log_utils
.. |code climate| image:: https://api.codeclimate.com/v1/badges/fa8ed1c6aec724d3b4f7/maintainability
   :target: https://codeclimate.com/github/bitranox/lib_log_utils/maintainability
   :alt: Maintainability
.. |code climate coverage| image:: https://api.codeclimate.com/v1/badges/fa8ed1c6aec724d3b4f7/test_coverage
   :target: https://codeclimate.com/github/bitranox/lib_log_utils/test_coverage
   :alt: Code Coverage

this library makes it easy to log colored messages from python and from the commandline. Text Wrapping is supported.

automated tests, Travis Matrix, Documentation, Badges for this Project are managed with `lib_travis_template <https://github
.com/bitranox/lib_travis_template>`_ - check it out

supports python 3.6-3.8, pypy3 and possibly other dialects.

`100% code coverage <https://codecov.io/gh/bitranox/lib_log_utils>`_, mypy static type checking, tested under `Linux, macOS, Windows and Wine <https://travis-ci
.org/bitranox/lib_log_utils>`_, automatic daily builds  and monitoring

----

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

Installation and Upgrade
------------------------

Before You start, its highly recommended to update pip and setup tools:


.. code-block:: bash

    python3 -m pip --upgrade pip
    python3 -m pip --upgrade setuptools
    python3 -m pip --upgrade wheel


install latest version with pip (recommended):

.. code-block:: bash

    # upgrade all dependencies regardless of version number (PREFERRED)
    python3 -m pip install --upgrade git+https://github.com/bitranox/lib_log_utils.git --upgrade-strategy eager

    # test without installing (can be skipped)
    python3 -m pip install git+https://github.com/bitranox/lib_log_utils.git --install-option test

    # normal install
    python3 -m pip install --upgrade git+https://github.com/bitranox/lib_log_utils.git


install latest pypi Release (if there is any):

.. code-block:: bash

    # latest Release from pypi
    python3 -m pip install --upgrade lib_log_utils

    # test without installing (can be skipped)
    python3 -m pip install lib_log_utils --install-option test

    # normal install
    python3 -m pip install --upgrade lib_log_utils



include it into Your requirements.txt:

.. code-block:: bash

    # Insert following line in Your requirements.txt:
    # for the latest Release on pypi (if any):
    lib_log_utils
    # for the latest Development Version :
    lib_log_utils @ git+https://github.com/bitranox/lib_log_utils.git

    # to install and upgrade all modules mentioned in requirements.txt:
    python3 -m pip install --upgrade -r /<path>/requirements.txt


Install from source code:

.. code-block:: bash

    # cd ~
    $ git clone https://github.com/bitranox/lib_log_utils.git
    $ cd lib_log_utils

    # test without installing (can be skipped)
    python3 setup.py test

    # normal install
    python3 setup.py install


via makefile:

if You are on linux, makefiles are a very convenient way to install. Here we can do much more, like installing virtual environment, clean caches and so on.
This is still in development and not recommended / working at the moment:

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

Usage from Commandline
------------------------

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

   if parameter --log_console is anything else then "False" (not case sensitive), then it is considered as True.
   if parameter --log_console is not present, it is also considered as True
   This makes it possible to silence messages elegantly in a shellscript:

       #!/bin/bash
       debug_messages="False"
       info_messages="True"
       ...
       ...
       log_util debug "some debug message ${IFS}and here the second line" --log_console=${debug_messages}
       log_util info "some info message" --log_console=${info_messages}
       ...


   this module exposes no other useful functions to the commandline

Requirements
------------
following modules will be automatically installed :

.. code-block:: bash

    ## Project Requirements
    coloredlogs
    docopt
    lib_doctest_pycharm @ git+https://github.com/bitranox/lib_doctest_pycharm.git
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

0.0.2
-----
development

0.0.1
-----
2019-09-03: Initial public release

