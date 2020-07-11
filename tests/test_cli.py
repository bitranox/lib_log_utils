# EXT
from click.testing import CliRunner

# OWN
import lib_log_utils.lib_log_utils_cli as lib_log_utils_cli

runner = CliRunner()
runner.invoke(lib_log_utils_cli.cli_main, ['--version'])
runner.invoke(lib_log_utils_cli.cli_main, ['-h'])
runner.invoke(lib_log_utils_cli.cli_main, ['program_info'])

runner.invoke(lib_log_utils_cli.cli_main, ['spam', 'test spam'])
runner.invoke(lib_log_utils_cli.cli_main, ['debug', 'test debug'])
runner.invoke(lib_log_utils_cli.cli_main, ['verbose', 'test verbose'])
runner.invoke(lib_log_utils_cli.cli_main, ['info', 'test info'])
runner.invoke(lib_log_utils_cli.cli_main, ['notice', 'test notice'])
runner.invoke(lib_log_utils_cli.cli_main, ['success', 'test success'])
runner.invoke(lib_log_utils_cli.cli_main, ['warning', 'test warning'])
runner.invoke(lib_log_utils_cli.cli_main, ['error', 'test error'])
runner.invoke(lib_log_utils_cli.cli_main, ['critical', 'test critical'])

runner.invoke(lib_log_utils_cli.cli_main, ['banner_spam', 'test banner_spam'])
runner.invoke(lib_log_utils_cli.cli_main, ['banner_debug', 'test banner_debug'])
runner.invoke(lib_log_utils_cli.cli_main, ['banner_verbose', 'test banner_verbose'])
runner.invoke(lib_log_utils_cli.cli_main, ['banner_info', 'test banner_info'])
runner.invoke(lib_log_utils_cli.cli_main, ['banner_notice', 'test banner_notice'])
runner.invoke(lib_log_utils_cli.cli_main, ['banner_success', 'test banner_success'])
runner.invoke(lib_log_utils_cli.cli_main, ['banner_warning', 'test banner_warning'])
runner.invoke(lib_log_utils_cli.cli_main, ['banner_error', 'test banner_error'])
runner.invoke(lib_log_utils_cli.cli_main, ['banner_critical', 'test banner_critical'])

runner.invoke(lib_log_utils_cli.cli_main, ['color_test'])
