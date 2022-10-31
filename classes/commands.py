from dataclasses import dataclass
from typing import Union

import marshmallow_dataclass
from marshmallow import ValidationError

from constants import COMMANDS


@dataclass
class Commands:
    file_name: str
    cmd1: str
    value1: Union[str, int]
    cmd2: str
    value2: Union[str, int]

    def __post_init__(self):
        """Validate fields and concatenate commands name with '_'"""
        if self.cmd1 not in COMMANDS:
            raise ValidationError(f'Command passed as cmd1 ({self.cmd1}) is not a valid command. '
                                  f'Only {", ".join(COMMANDS)} allowed')
        if self.cmd2 not in COMMANDS:
            raise ValidationError(f'Command passed as cmd2 ({self.cmd2}) is not a valid command. '
                                  f'Only {", ".join(COMMANDS)} allowed')

        self.cmd1 = self.cmd1 + '_'
        self.cmd2 = self.cmd2 + '_'


CommandsSchema = marshmallow_dataclass.class_schema(Commands)

