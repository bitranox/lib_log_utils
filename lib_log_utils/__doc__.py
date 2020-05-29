# PROJ
try:
    from . import __init__conf__
except ImportError:                 # pragma: no cover
    # imports for doctest
    import __init__conf__           # type: ignore  # pragma: no cover

__doc__ = """

Usage:
    {shell_command} (-h | -v | -i)
    {shell_command} spam            <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
    {shell_command} debug           <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
    {shell_command} verbose         <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
    {shell_command} info            <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
    {shell_command} notice          <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
    {shell_command} success         <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
    {shell_command} warning         <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
    {shell_command} error           <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
    {shell_command} critical        <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
    {shell_command} banner_spam     <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
    {shell_command} banner_debug    <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
    {shell_command} banner_verbose  <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
    {shell_command} banner_info     <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
    {shell_command} banner_notice   <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
    {shell_command} banner_success  <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
    {shell_command} banner_warning  <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
    {shell_command} banner_error    <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
    {shell_command} banner_critical <message> [ --banner_width=<bw>, (--wrap | --nowrap), --log_console=(True|False) ]
    {shell_command} color_test      [ --quiet=(True|False) ]

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
    {shell_command} debug "some debug message ${IFS}and here the second line" --log_console=${debug_messages}
    {shell_command} info "some info message" --log_console=${info_messages}
    ...


this module exposes no other useful functions to the commandline

""".format(shell_command=__init__conf__.shell_command, debug_messages='{debug_messages}', info_messages='{info_messages}', IFS='{IFS}')

# docopt syntax see : http://docopt.org/
