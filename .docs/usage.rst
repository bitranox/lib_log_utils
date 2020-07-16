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

======================  =======================================================================================
environment variable    function
======================  =======================================================================================
LOG_UTIL_LEVEL          the level of the logger, one of the predefined log levels, or "0" - "50", default = 0
LOG_UTIL_WIDTH          the banner width if text wrap is used, must be >="10", default = 140
LOG_UTIL_WRAP           if text wrap should be used, must be True or False (not case sensitive), default = True
LOG_UTIL_QUIET          if the logger is used at all - must be True or False (not case sensitive), default = False
======================  =======================================================================================

environment settings take precedence over commandline arguments, unless --force is passed to the commandline


EXAMPLES
--------


.. code-block:: bash

    # multi-line banner
    log_util -l warning "Line1${IFS}Line2${IFS}Line3"

    # use log_level
    export log_utils_log_level=WARNING

    log_util -l info   "spam"   # this is not shown
    log_util -l error  "ham"    # this is shown

    # disable log_level
    unset log_utils_log_level
