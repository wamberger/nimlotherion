

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


class TestDatabaseUpdate(unittest.TestCase):
        
    def test_update(self):

        test_db = DatabaseManager(test_db_creds['my_oracle'])
        test_db.setup_db()

        email = {
            'email': 'adsadasda@email.com',
            'text': 'updated',
            'persnr': 9000
        }

        is_update = test_db.update_using_p_key(Email, 'adsadasda@email.com', email)

        print(is_update[1])
        self.assertFalse(is_update[0])

        email = {
            'email': 'awa@email.com',
            'text': 'updated new',
            'persnr': 9000
        }

        is_update = test_db.update_using_p_key(Email, 'awa@email.com', email)

        print(is_update[1])
        self.assertTrue(is_update[0])
    

if __name__ == '__main__':
    unittest.main()