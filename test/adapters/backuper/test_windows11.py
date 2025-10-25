from datetime import datetime
from unittest.mock import patch

import pytest

from adapters.backuper.windows11 import Windows11Backuper


NOW = datetime.now()


@pytest.fixture
def tmp_dir(tmp_path):
    src_dir = tmp_path / "data"
    src_dir.mkdir()
    return src_dir


@patch("os.system")
@patch("adapters.backuper.windows11.datetime")
def test_run_creates_correct_backup_command(mock_datetime, mock_os_system, tmp_dir):

    mock_datetime.now.return_value = NOW

    backuper = Windows11Backuper(directory=tmp_dir)

    backuper.run()

    expected_new_dir_name = f"data_backup_{NOW.strftime(backuper.datetime_format)}"
    expected_command = backuper.command_template.format(tmp_dir, tmp_dir.parent / expected_new_dir_name)

    mock_os_system.assert_called_once_with(expected_command)


@patch("os.system")
@patch("adapters.backuper.windows11.datetime")
def test_run_uses_custom_templates(mock_datetime, mock_os_system, tmp_dir):
    mock_datetime.now.return_value = NOW

    backuper = Windows11Backuper(
        directory=tmp_dir,
        command_template='echo COPY "{}" "{}"',
        new_dir_name_template="{}_ARCHIVE_{}",
        datetime_format="%Y%m%d-%H%M",
    )

    backuper.run()

    expected_new_dir_name = f"data_ARCHIVE_{NOW.strftime(backuper.datetime_format)}"
    expected_command = f'echo COPY "{tmp_dir}" "{tmp_dir.parent / expected_new_dir_name}"'

    mock_os_system.assert_called_once_with(expected_command)
