

import os
import sys
import unittest
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))

from unittest.mock import patch
from nimlotherion.utils.args import CliArgs
from nimlotherion.utils.config import CliConfig

from tests._test_utility_files.test_expections import test_expected_config_dict


class TestCli(unittest.TestCase):

    def test_args_user(self):
        # Simulate command-line arguments
        args = ['args.py', '-u', 'Admin']

        with patch('sys.argv', args):

            cli_args = CliArgs()
            read_args = cli_args.args

            result = repr(read_args)  # Use repr() to get a string representation without extra formatting

        print(result)

    def test_args_user_group(self):
        args = ['args.py', '-g', 'test_group']

        with patch('sys.argv', args):
            cli_args = CliArgs()
            read_args = cli_args.args

            result = repr(read_args)

        print(result)

    def test_args_list_params(self):
        args = ['args.py', '-l', 'Alice', '2', 'Joe', '1.2']

        with patch('sys.argv', args):
            cli_args = CliArgs()
            read_args = cli_args.args

            result = repr(read_args)

        print(result)

    def test_args_json_params(self):
        args = [
            'args.py', '-j',
            '{'
            '"test": "a", '
            '"marco": 334, '
            '"bool": "True", '
            '"float": 2.3, '
            '"list": [], '
            '"dict": {}'
            '}'
        ]

        with patch('sys.argv', args):
            cli_args = CliArgs()
            read_args = cli_args.args

            result = repr(read_args)

        print(result)

    def test_args_all(self):
        args = [
            'args.py',
            '-u', 'test_user',
            '-g', 'test_group',
            '-l', 'Alice', '2', 'Joe', '1.2',
            '-j', '{"test": "a", "marco": 334}'
        ]

        expected_result = "Namespace(user='test_user', " \
                          "user_group='test_group', " \
                          "j_param={'test': 'a', 'marco': 334}, " \
                          "l_param=['Alice', 2, 'Joe', 1.2], verbosity=False)"

        with patch('sys.argv', args):
            cli_args = CliArgs()
            read_args = cli_args.args

            result = repr(read_args)

        print(result)
        self.assertEqual(result, expected_result)

    def test_config_file(self):

            path = 'C:\\Users\\awa\\work_desk\\projects\\nimlotherion\\tests\\_test_utility_files\\test_config.yaml'
            result = CliConfig('yaml', path)

            a = result['db']
            result.setup_locale()
            asda = f"{a}"

            self.assertEqual(result.config, test_expected_config_dict)


if __name__ == '__main__':
    unittest.main()
