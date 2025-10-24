import os
from datetime import datetime
from pathlib import Path

from domain.ports.backuper import Backuper


class Windows11Backuper(Backuper):
    def __init__(
        self,
        directory: Path,
        command_template: str = 'xcopy "{}" "{}" /s /e /i /y /q',
        new_dir_name_template: str = "{}_backup_{}",
        datetime_format="%Y-%m-%dT%H-%M-%S",
    ) -> None:
        self.directory = directory
        self.command_template = command_template
        self.new_dir_name_template = new_dir_name_template
        self.datetime_format = datetime_format

    def run(self) -> None:
        now = datetime.now()
        new_dir_name = self.new_dir_name_template.format(
            self.directory.name, now.strftime(self.datetime_format)
        )
        command = self.command_template.format(
            self.directory, self.directory.parent / new_dir_name
        )
        os.system(command)
