import os
from datetime import datetime
from pathlib import Path

CD_COMMAND = 'cd %s'
MAKE_BACKUP_COMMAND = 'xcopy "{}" "{}" /s /e /i /y /q'

def run_command(command: str):
    os.system(command)


def make_directory_backup(directory: Path):
    parent = directory.parent

    now = datetime.now()

    new_dir_name = f'{directory.name}_backup_{now.strftime("%H-%M %d-%m-%Y")}'
    command = MAKE_BACKUP_COMMAND.format(directory, parent/new_dir_name)

    run_command(command)

    return parent/new_dir_name

