# STDLIB
import logging
import pathlib
import subprocess
import sys

logger = logging.getLogger()
package_dir = "lib_log_utils"
cli_filename = "lib_log_utils_cli.py"

path_cli_command = pathlib.Path(__file__).resolve().parent.parent / package_dir / cli_filename


def call_cli_command(commandline_args: str = "") -> bool:
    command = " ".join([sys.executable, str(path_cli_command), commandline_args])
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        return False
    return True


def test_cli_commands() -> None:
    # due to a bug in python 3.8.1 with setup.py test on travis we need to cancel the click tests there !
    if sys.version_info < (3, 8, 1) or sys.version_info >= (3, 8, 2):
        assert not call_cli_command("--unknown_option")
        assert call_cli_command("")
        assert call_cli_command("--version")
        assert call_cli_command("-h")
        assert call_cli_command("--program_info")
        assert call_cli_command("-c")
        assert call_cli_command("--colortest")
        assert not call_cli_command("unquoted string")
        assert not call_cli_command("--traceback unquoted string")
        assert call_cli_command('"log default level"')
        assert call_cli_command('-l error "log default level"')
        assert call_cli_command('"log default level" -l error')
