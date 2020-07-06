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
