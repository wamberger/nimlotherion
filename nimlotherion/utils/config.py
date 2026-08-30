

__all__ = ['config']


import locale

from typing import Any

from nimlotherion.file import read_file
from nimlotherion.file.yaml_ import FileYAML
from nimlotherion.file.toml_ import FileTOML
from nimlotherion.file.json_ import FileJSON
from nimlotherion.file.csv_ import FileCSV


type DataObject = FileCSV | FileYAML | FileTOML | FileJSON


def setup_locale(local: dict) -> None:
    try:
        if not local or not isinstance(local, dict):
            locale.setlocale(locale.LC_ALL, '')
        else:
            lc_all = local.get('lc_all')
            lc_time = local.get('lc_time')
            lc_numeric = local.get('lc_numeric')

            if lc_all:
                locale.setlocale(locale.LC_ALL, lc_all)
            if lc_time:
                locale.setlocale(locale.LC_TIME, lc_time)
            if lc_numeric:
                locale.setlocale(locale.LC_NUMERIC, lc_numeric)
    except Exception as e:
        raise Exception(f"Error with 'locale': {e}") from e


def config(file_format: str, file: str) -> DataObject:
    cfg = read_file(file_format, file)
    setup_locale(cfg.get('locale'))
    return cfg
