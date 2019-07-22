"""Setuptools entry point."""
import codecs
import os
import subprocess
import sys


def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", "--upgrade", package])


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules'
]

description = 'Log Utils'

dirname = os.path.dirname(__file__)
readme_filename = os.path.join(dirname, 'README.rst')

long_description = description
if os.path.exists(readme_filename):
    try:
        readme_content = codecs.open(readme_filename, encoding='utf-8').read()
        long_description = readme_content
    except Exception:
        pass

install('https://github.com/bitranox/lib_cast/archive/master.zip')
install('https://github.com/bitranox/lib_parameter/archive/master.zip')
install('https://github.com/bitranox/lib_doctest_pycharm/archive/master.zip')


setup(
    name='lib_log_utils',
    version='0.0.1',
    description=description,
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author='Robert Nowotny',
    author_email='rnowotny1966@gmail.com',
    url='https://github.com/bitranox/lib_log_utils',
    packages=['lib_log_utils'],
    install_requires=['pytest', 'typing'],
    classifiers=CLASSIFIERS,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'])