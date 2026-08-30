

__all__ = ['FileJSON']


import json

from typing import Any
from typing import override

from nimlotherion.file.base import Base


class FileJSON(Base):
    """Class for working with `.json` file."""

    @override
    def read(self, mode: str = 'r') -> dict[str, Any]:
        with open(self.file, mode=mode) as f:
            file = json.load(f)
        return file

    @override
    def write(self, file: str = None) -> None:
        if file is None:
            file = self.file
        with open(file, 'w') as f:
            json.dump(self.data, f)
