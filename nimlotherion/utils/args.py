

__all__ = ['cli_args']


import argparse
import json

from typing import Any


def _convert_json_like_string_to_dict(
        params: Any) -> dict[str, str | int | float | list | dict]:
    return json.loads(params)


def _convert_str_to_int_or_float(
        params: list[str]) -> list[str | int | float]:
    l: list = []
    for e in params:
        if e.isdigit():
            l.append(int(e))
        elif (e.replace('.', '').isdigit()
              | e.replace(',', '').isdigit()):
            e = e.replace(',', '.')
            l.append(float(e))
        else:
            l.append(e)
    return l


def _parse() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '-u', '--user',
        type=str,
        help='Username')
    parser.add_argument(
        '-g', '--user_group',
        type=str,
        help='User-group')
    parser.add_argument(
        '-j', '--j_param',
        help='Parameters in JSON-like string format. Convert to dict.',
        default={})
    parser.add_argument(
        '-l', '--l_param',
        help='Listed string parameters. Recognize: str, int, float. '
             'Convert to list.',
        action='append',
        default=[])
    parser.add_argument(
        '-v', '--verbosity',
        action='store_true',
        help='Enable additional information')
    p = parser.parse_args()
    if p.j_param:
        p.j_param = _convert_json_like_string_to_dict(p.j_param)
    if p.l_param:
        p.l_param = _convert_str_to_int_or_float(p.l_param)
    return p


def cli_args() -> argparse.Namespace:
    """Read and store client arguments.

        Command-line Args:
            -u, --user (str): Username.
            -g, --user_group (str): User-group.
            -j, --j_param (Dict[str, str | int | float | list | dict]):
                                        Parameters in JSON-like string format.
                                        Convert to dict.
            -l, --l_param (list[str, int, float], optional): Listed string
                                        parameters. Recognize from command
                                        line: str, int, float. Convert to list.
            -v, --verbosity (bool): Enable additional information.

            -h, --help: show help message.
    """
    return _parse()
