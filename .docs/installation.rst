- Before You start, its highly recommended to update pip:


.. code-block::

    python -m pip --upgrade pip


.. include:: ./installation_via_pypi.rst

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


.. include:: ./installation_via_makefile.rst
