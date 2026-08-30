

__all__ = ['FileYAML']


import yaml

from typing import Any
from typing import override

from nimlotherion.file.base import Base


class FileYAML(Base):
    """Class for working with `.yaml` file."""

    @override
    def read(self, mode: str = 'r') -> dict[str, Any]:
        with open(self.file, mode) as f:
            file = yaml.full_load(f)
        return file

    @override
    def write(self, file: str = None) -> None:
        if file is None:
            file = self.file
        with open(file, 'w') as f:
            yaml.dump(self.data, f)
