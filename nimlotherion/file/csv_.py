

__all__ = ['FileCSV']


import csv
import chardet

from typing import Any
from typing import Iterator


class FileCSV:
    def __init__(
            self,
            file: str,
            header: bool = False,
            delimiter: str = None,
            encoding: str = None,
            mode: str = None) -> None:

        self.file: str = file
        if encoding is not None:
            self.encoding: str = encoding
        else:
            self._set_encoding()
        if delimiter is not None:
            self.delimiter: str = delimiter
        else:
            self._set_delimiter()
        if header is not None:
            self.header: bool = header
        else:
            self._set_header()
        self.data: list[dict[str, Any]] = self.read(mode)

    def __getitem__(self, index: int) -> dict[str, Any]:
        return self.data[index]

    def __contains__(self, item: str) -> bool:
        return item in self.data

    def __setitem__(self, index: int, value: Any) -> None:
        self.data[index] = value

    def __delitem__(self, index: int) -> None:
        del self.data[index]

    def __iter__(self) -> Iterator[dict[str, Any]]:
        return iter(self.data)

    def __len__(self) -> int:
        return len(self.data)

    def _set_encoding(self, num_lines: int = 20) -> None:
        with open(self.file, 'rb') as f:
            raw_data = b''.join([f.readline() for _ in range(num_lines)])
        self.encoding = chardet.detect(raw_data)['encoding']

    def _set_delimiter(self) -> None:
        with open(self.file, encoding=self.encoding) as f:
            self.delimiter = csv.Sniffer().sniff(f.read(4096)).delimiter

    def _set_header(self) -> None:
        with open(self.file, encoding=self.encoding) as f:
            self.header = csv.Sniffer().has_header(f.read(4096))

        with open(self.file, encoding=self.encoding, newline='') as f:
            csv_reader = csv.reader(f)
            if len(list(csv_reader)) == 1:
                self.header = False

    def append(self, item: dict[str, Any]) -> None:
        self.data.append(item)

    def extend(self, items: list[dict[str, Any]]) -> None:
        self.data.extend(items)

    def insert(self, index: int, item: dict[str, Any]) -> None:
        self.data.insert(index, item)

    def remove(self, item: dict[str, Any]) -> None:
        self.data.remove(item)

    def pop(self, index: int = None) -> dict[str, Any]:
        return self.data.pop(index)

    def clear(self) -> None:
        self.data.clear()

    def index(self, item: dict[str, Any]) -> int:
        return self.data.index(item)

    def count(self, item: dict[str, Any]) -> int:
        return self.data.count(item)

    def reverse(self) -> None:
        self.data.reverse()

    def sort(self, key: str = None, reverse: bool = False) -> None:
        self.data.sort(key=key, reverse=reverse)

    def read(self, mode: str = 'r') -> list[dict[str, Any]]:
        with open(self.file, mode=mode, encoding=self.encoding) as f:
            if self.header:
                data = [row for row in csv.DictReader(
                    f, delimiter=self.delimiter)]
                self.convert_to_numeric()
                return data
            else:
                data = [self.crt_excel_header(row) for row in csv.reader(
                    f, delimiter=self.delimiter)]
                self.convert_to_numeric()
                return data

    def write(self, file: str = None) -> None:
        if file is None:
            file = self.file
        with open(file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(self.get_header())
            for row in self.extract_values():
                writer.writerows(row)

    def convert_to_numeric(self) -> None:
        for e in self.data:
            for k, v in e.items():
                if v.isdigit():
                    e.update({k: int(v)})
                elif (v.replace('.', '').isdigit()
                      | v.replace(',', '').isdigit()):
                    v = v.replace(',', '.')
                    e.update({k: float(v)})

    def get_header(self) -> list[str]:
        header: list = []
        for elem in self.data:
            for k, v in elem.items():
                header.append(k)
            break
        return header

    def extract_values(self) -> list[list]:
        rows: list = []
        for elem in self.data:
            row: list = []
            for k, v in elem.items():
                row.append(v)
            rows.append(row)
        return rows

    @staticmethod
    def crt_excel_header(row: list) -> dict:
        def excel_ori_header() -> str:
            for i in range(0, 26):
                yield chr(i + 65)

            for j in range(0, 26):
                for i in range(0, 26):
                    yield f'{chr(j + 65)}{chr(i + 65)}'

        d: dict = {}
        for elem, let in zip(row, excel_ori_header()):
            d[let] = elem
        return d
