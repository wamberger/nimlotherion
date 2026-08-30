
import os
import sys
import unittest
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))


class TestFileModule(unittest.TestCase):

    def test_rewrite_keep_last_lines(self):

        rewrite_keep_last_lines('audit.txt', -5)

        a = 1

if __name__ == '__main__':
    unittest.main()
