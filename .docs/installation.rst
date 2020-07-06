- Before You start, its highly recommended to update pip and setup tools:


.. code-block:: bash

    python -m pip --upgrade pip
    python -m pip --upgrade setuptools
    python -m pip --upgrade wheel

.. include:: ./installation_via_pypi.rst

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


.. include:: ./installation_via_makefile.rst
