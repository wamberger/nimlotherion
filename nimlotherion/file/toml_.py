

__all__ = ['FileTOML']


import toml

from typing import Any
from typing import override

from nimlotherion.file.base import Base


class FileTOML(Base):
    """Class for working with `.toml` file."""

    @override
    def read(self, mode: str = 'r') -> dict[str, Any]:
        with open(self.file, mode=mode) as f:
            file = toml.load(f)
        return file

    @override
    def write(self, file: str = None) -> None:
        if file is None:
            file = self.file
        with open(file, 'w') as f:
            toml.dump(self.data, f)
