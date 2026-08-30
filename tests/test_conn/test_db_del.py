

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

from nimlotherion.conn.db import DatabaseManager
from tests._test_utility_files.test_args import test_db_creds

# test models
from tests.test_conn.models.Email import Email


class TestDatabaseDelete(unittest.TestCase):

    def test_delete_using_primary_key(self):

        test_db = DatabaseManager(test_db_creds['my_oracle'])



        test = test_db.delete(
            Email,
            'awa@email.com111'
            )

        self.assertFalse(test[0])
        print(test)
        test = test_db.delete_using_p_key(
            Email,
            'awa@email.com'
            )
        print(test)
        self.assertTrue(test[0])


if __name__ == '__main__':
    unittest.main()
