# single point for all configuration of the project

# stdlib
from setuptools import find_packages  # type: ignore
from typing import List, Dict

package_name = 'lib_log_utils'  # type: str
version = '0.1.0'
# codeclimate_link_hash - get it under https://codeclimate.com/github/<user>/<project>/badges
codeclimate_link_hash = 'fa8ed1c6aec724d3b4f7'  # for lib_log_utils

# cc_test_reporter_id - get it under https://codeclimate.com/github/<user>/<project> and press "test coverage"
cc_test_reporter_id = 'cc62399f4be04b06102d2abf0d9093568122ae927cccd884c5cdc9b2e856c85f'    # for lib_log_utils

# pypi_password
# to create the secret :
# cd /<repository>
# travis encrypt -r bitranox/lib_parameter pypi_password=*****
# copy and paste the encrypted password here
# replace with:
# travis_pypi_secure_code = '<code>'     # pypi secure password, without '"'
travis_pypi_secure_code = 'b/MeY1E7Ps+8bWyaUlMSXEcHpL16Q0sv16kRQ7W841GbBYruDq5YNt/u193gk67kHNPbkuVeKrtnpw8jfgT1ykiVI08vfqJKqGUBokhyFg0Tg0AwOgE49QQm'\
                          '6zFpZQ92QoFnEN2HDMgMts//XvF/fu6Phz6xTr4/rtyiLHXkVQ1UcAk+dmo9VG2AnCuPnDYr34gujJPj2N+3TAXZgbT+1IS9+yIIXelUphSMj4A1JuQlro7K'\
                          'AQuV2IuIaL88iiv8dsqJFcumQcBfYCSqZYhd8vRoRe3Io2G/q3nlrZp51Kr85eOfPHQI7QhPAiAweGRCZ31bc4rbZIj+orbcNncFB8kXThNzFq4v0/zaRkSI'\
                          'lnmwqkA4EU7mhm0z0m3FdAJ3hpi5Vcxpbj6juf5zzk6RZubmT6wdiW9F7vU9DT/j3cCk/C0vKw5bPt4uBikqYkwW1RKxZjUBPNJCfIwwuEuZciOS65lT2E9I'\
                          '8qxLUTWJAssNEjhnfHTkyXdiliQdFebRoyZrRG6YzrtWLTL+h5XNF6Vt8O9vCoOZPGPmYhz5EndjpEekN13tYxrrw0uLotxxdrDUfnc4GH0UwKMWVzjZBOf+'\
                          '4dm/+MoByOgmEwKR5MDnGrdkApj1CGM6LnCYiq1ad1m3Aa+AsqT914RFk1505v5WM+jgbl3KfmZYkGB2TB8='

# include package data files
# package_data = {package_name: ['some_file_to_include.txt']}
package_data = dict()       # type: Dict[str, List[str]]

author = 'Robert Nowotny'
author_email = 'rnowotny1966@gmail.com'
github_account = 'bitranox'

linux_tests = True
osx_tests = True
pypy_tests = True
windows_tests = True
wine_tests = False
badges_with_jupiter = False

# a short description of the Package - especially if You deploy on PyPi !
description = 'this library makes it easy to log colored messages and banners from python and from the commandline. text wrapping is supported.'

# #############################################################################################################################################################
# DEFAULT SETTINGS - no need to change usually, but can be adopted
# #############################################################################################################################################################

shell_command = 'log_util'
src_dir = package_name
module_name = package_name
init_config_title = description
init_config_name = package_name

# we ned to have a function main_commandline in module module_name - see examples
entry_points = {'console_scripts': ['{shell_command} = {src_dir}.{module_name}:main_commandline'
                .format(shell_command=shell_command, src_dir=src_dir, module_name=module_name)]}  # type: Dict[str, List[str]]

long_description = package_name  # will be overwritten with the content of README.rst if exists

packages = [package_name]

url = 'https://github.com/{github_account}/{package_name}'.format(github_account=github_account, package_name=package_name)
github_master = 'git+https://github.com/{github_account}/{package_name}.git'.format(github_account=github_account, package_name=package_name)
travis_repo_slug = github_account + '/' + package_name

CLASSIFIERS = ['Development Status :: 5 - Production/Stable',
               'Intended Audience :: Developers',
               'License :: OSI Approved :: MIT License',
               'Natural Language :: English',
               'Operating System :: OS Independent',
               'Programming Language :: Python',
               'Topic :: Software Development :: Libraries :: Python Modules']
