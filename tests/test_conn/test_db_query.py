

import os
import sys
import unittest
sys.path.append(os.path.abspath(
    os.path.join(
        os.path.join(os.getcwd(), os.pardir), 
        os.pardir)
        ))


import oracledb
oracledb.init_oracle_client(lib_dir=rf"C:\oracle\product\instantclient_19_20")

from sqlalchemy.orm.query import Query
from nimlotherion.conn.db import DatabaseManager
from tests._test_utility_files.test_args import test_db_creds

# test models
from tests.test_conn.models.Pers import Pers


class TestDatabaseQuery(unittest.TestCase):

    def test_get_all(self):

        test_db = DatabaseManager(test_db_creds['my_oracle'])

        test = test_db.get_all(Pers)
        
        self.assertIsNotNone(test)

        self.assertIsInstance(test, list)

    def test_get_by_p_key(self):

        test_db = DatabaseManager(test_db_creds['my_oracle'])

        test_db.setup_db()

        test = test_db.get_by_p_key(Pers, 9000)

        self.assertIsNotNone(test)

        self.assertIsInstance(test, Pers)

    def test_get_custom_equal(self):

        test_db = DatabaseManager(test_db_creds['my_oracle'])

        test_db.setup_db()

        test = test_db.get_custom_equal(
            Pers,
            {'produktiv': 'J'}
            )

        self.assertIsNotNone(test)

        self.assertIsInstance(test, Query)
        
        with self.assertRaises(AttributeError) as context:
            test_order_by = test_db.get_custom_equal(
                Pers,
                {'produktiv': 'J'},
                'ccccc'
            )
        
        # looping the string as 'p' as first char
        self.assertIn("type object 'Pers' has no attribute 'c'", str(context.exception))
        
        test_order_by = test_db.get_custom_equal(
                Pers,
                {'produktiv': 'J'},
                ['persnr']
                )

        with self.assertRaises(SyntaxError) as context:
            test_order_by = test_db.get_custom_equal(
                Pers,
                {'produktiv': 'J'},
                [None]
            )
        
        self.assertIn("invalid syntax", str(context.exception))


    def test_get_custom_equal_and_greater_than(self):

        test_db = DatabaseManager(test_db_creds['my_oracle'])

        test_db.setup_db()

        test = test_db.get_custom_equal_and_greater_than(
            Pers,
            {'zuname': 'awa_test', 'persnr': 1000},
            {'angbis': 20240101}
            )

        self.assertIsNotNone(test)

        self.assertIsInstance(test, Query)

    def test_get_custom_equal_and_less_than(self):

        test_db = DatabaseManager(test_db_creds['my_oracle'])

        test_db.setup_db()

        test = test_db.get_custom_equal_and_less_than(
            Pers,
            {'produktiv': 'N'},
            {'angbis': 20240101}
            )

        self.assertIsNotNone(test)

        self.assertIsInstance(test, Query)


if __name__ == '__main__':
    unittest.main()