

import os
import sys
import unittest
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))

from nimlotherion.file.csv_ import FileCSV


class TestFileCSV(unittest.TestCase):

    def test_create_file(self):

        path = os.path.join(os.path.join(os.getcwd(), os.pardir, '_test_utility_files'), 'test_csv_file1.csv')

        file = FileCSV(path)

        self.assertEqual(file.file, path)

    def test_header(self):

        path = os.path.join(
            os.path.join(os.getcwd(), os.pardir, '_test_utility_files'),
            'test_csv_file1.csv')
        file = FileCSV(path)
        self.assertFalse(file.header)

        path = os.path.join(
            os.path.join(os.getcwd(), os.pardir, '_test_utility_files'),
            'test_csv_file3.csv')
        file = FileCSV(path)
        self.assertTrue(file.header)

        path = os.path.join(
            os.path.join(os.getcwd(), os.pardir, '_test_utility_files'),
            'test_csv_file2.csv')
        file = FileCSV(path)
        self.assertFalse(file.header)

    def test_delimiter(self):

        path = os.path.join(
            os.path.join(os.getcwd(), os.pardir, '_test_utility_files'),
            'test_csv_file1.csv')
        file = FileCSV(path)
        self.assertEqual(file.delimiter, ';')

        path = os.path.join(
            os.path.join(os.getcwd(), os.pardir, '_test_utility_files'),
            'test_csv_file2.csv')
        file = FileCSV(path)
        self.assertEqual(file.delimiter, ':')

        path = os.path.join(
            os.path.join(os.getcwd(), os.pardir, '_test_utility_files'),
            'test_csv_file3.csv')
        file = FileCSV(path)
        self.assertEqual(file.delimiter, ',')

    def test_convert_numeric(self):

        path = os.path.join(
            os.path.join(os.getcwd(), os.pardir, '_test_utility_files'),
            'test_csv_file1.csv')
        file = FileCSV(path)
        file.read()
        file.convert_to_numeric()
        a = 1

    def test_read(self):

        path = os.path.join(
            os.path.join(os.getcwd(), os.pardir, '_test_utility_files'),
            'test_csv_file1.csv')
        file = FileCSV(path)
        file.read()
        self.assertTrue(file.data)
        self.assertIsInstance(file.data, list)

        path = os.path.join(
            os.path.join(os.getcwd(), os.pardir, '_test_utility_files'),
            'test_csv_file2.csv')
        file = FileCSV(path)
        file.read()
        self.assertTrue(file.data)
        self.assertIsInstance(file.data, list)

        path = os.path.join(
            os.path.join(os.getcwd(), os.pardir, '_test_utility_files'),
            'test_csv_file3.csv')
        file = FileCSV(path)
        file.read()
        self.assertTrue(file.data)
        self.assertIsInstance(file.data, list)


if __name__ == '__main__':
    unittest.main()
