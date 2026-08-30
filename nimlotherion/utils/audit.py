

__all__ = ['Audit']


import os

from datetime import datetime
from typing import Iterable

from nimlotherion.utils.crypto import CryptoSafe


class Audit:

    def __init__(
            self,
            user: str,
            user_group: str,
            file: str,
            intro_text: str = None,
            lines_to_keep: int = -100000) -> None:

        self.user: str = user
        self.user_group: str = user_group
        self.file: str = file
        self.intro_text: str = intro_text
        self.lines_to_keep: int = lines_to_keep
        self.data: list[CryptoSafe] = []

    def __bool__(self):
        return True if self.data else False

    def _set_info_txt(self) -> str:
        now = datetime.now().strftime('%c')
        pid = os.getpid()
        return f'{pid}[{now}] User:[{self.user} ({self.user_group})] '

    @staticmethod
    def decode(data: Iterable[CryptoSafe]) -> list[str]:
        d: list = []
        for e in data:
            d.append(e.decrypt().decode('utf-8'))
        return d

    def append(self, data: str) -> None:
        token = CryptoSafe(
            bytes(
                f"{self._set_info_txt()}"
                f"{f"{self.intro_text} " if self.intro_text else ""}"
                f"{data}",
                'utf-8'))
        self.data.append(token)

    def write(self) -> None:
        """ file must be .txt """
        with open(self.file, 'a') as f:
            data = self.decode(self.data)
            for row in data:
                f.write(row + '\n')

        self.rewrite_keep_last_lines()

    def rewrite_keep_last_lines(self) -> None:
        """Rewrite the file and keep the last lines.

        Args:
            file (str): absolute path to the filename.
            lines_to_keep (int, optional): it must be negative number.
                                           Default is 100.000 lines.
        """

        with open(self.file, 'r') as f:
            lines = f.readlines()

        new_lines = lines[self.lines_to_keep:]  # keep the last lines

        with open(self.file, 'w') as f:
            f.writelines(new_lines)
