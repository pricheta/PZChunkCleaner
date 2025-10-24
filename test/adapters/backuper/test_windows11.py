from pathlib import Path
from unittest.mock import Mock

from adapters.backuper.windows11 import Windows11Backuper


def test_run_success(mocker):
    directory = Path('C:/Users')

    os = mocker.patch(
        'adapters.backuper.windows11.os',
        Mock(),
    )

    backuper = Windows11Backuper(directory=directory)
    backuper.run()

    ran_command = os.system.call_args_list[0].args[0]

    assert 'xcopy "C:\\Users" "C:\\Users_backup_' in ran_command
    assert '/s /e /i /y /q' in ran_command
