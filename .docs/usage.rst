.. code-block::

    import the module and check the code - its easy and documented there, including doctest examples.
    in case of any questions the usage section might be expanded at a later time


Commandline
-----------

.. code-block:: bash

   Usage:
       log_util (-h | -v | -i)
       log_util spam            <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False), --force ]
       log_util debug           <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False), --force ]
       log_util verbose         <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False), --force ]
       log_util info            <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False), --force ]
       log_util notice          <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False), --force ]
       log_util success         <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False), --force ]
       log_util warning         <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False), --force ]
       log_util error           <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False), --force ]
       log_util critical        <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False), --force ]
       log_util banner_spam     <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False), --force ]
       log_util banner_debug    <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False), --force ]
       log_util banner_verbose  <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False), --force ]
       log_util banner_info     <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False), --force ]
       log_util banner_notice   <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False), --force ]
       log_util banner_success  <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False), --force ]
       log_util banner_warning  <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False), --force ]
       log_util banner_error    <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False), --force ]
       log_util banner_critical <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False), --force ]
       log_util colortest      [ --quiet=(True|False) ]

   Options:
       -h, --help          show help
       -v, --version       show version
       -i, --info          show Info


Arguments
---------

message
    the message to log

colortest
    print a test colored message



Parameter
---------

--banner_width  the width of the message or the banner, if text wrap is used, default = 140

--wrap          use text wrap (this is the default value), default = True

--nowrap        do not use text wrap

--force         take precedence over environment settings


--log_console   if True, we log to the console, if False, we skip the output

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


Environment Settings
--------------------

======================  =======================================================================================
environment variable    function
======================  =======================================================================================
log_utils_log_level     the level of the logger, one of the predefined Log_levels, or "0" - "50", default = 0
log_utils_banner_width  the banner width if text wrap is used, must be >="10", default = 140
log_utils_wrap_text     if text wrap should be used, must be True or False (not case sensitive), default = True
log_utils_quiet         if the logger is used at all - must be True or False (not case sensitive), default = False
======================  =======================================================================================

environment settings take precedence over commandline arguments, unless --force is passed to the commandline
