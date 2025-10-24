import os
from datetime import datetime
from pathlib import Path

from domain.ports.backuper import Backuper


class Windows11Backuper(Backuper):
    def __init__(
        self,
        command_template:str = 'xcopy "{}" "{}" /s /e /i /y /q',
        new_dir_name_template: str = '{}_backup_{}',
    ) -> None:
        self.command_template = command_template
        self.new_dir_name_template = new_dir_name_template

    def run(self, directory: Path) -> None:
        now = datetime.now()
        parent = directory.parent
        new_dir_name = self.new_dir_name_template.format(directory.name, now.strftime("%Y-%m-%dT%H-%M-%S"))
        command = self.command_template.format(directory, parent / new_dir_name)
        os.system(command)
