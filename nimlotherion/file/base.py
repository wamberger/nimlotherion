

__all__ = ['Base']


from typing import Any
from typing import Iterator


class Base:
    def __init__(self, file: str) -> None:
        self.file: str = file
        self.data: dict[str, Any] = self.read()

    def __contains__(self, item: str) -> bool:
        return item in self.data

    def __getitem__(self, key: str) -> dict[str, Any]:
        return self.data[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.data[key] = value

    def __delitem__(self, key: str) -> None:
        del self.data[key]

    def __iter__(self) -> Iterator[tuple[str, Any]]:
        return iter(self.data.items())

    def __len__(self) -> int:
        return len(self.data)

    def keys(self):
        return self.data.keys()

    def values(self) -> Any:
        return self.data.values()

    def items(self):
        return self.data.items()

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)

    def read(self, mode: str = 'r') -> dict[str, Any]:
        ...

    def write(self, file: str = None) -> None:
        ...
