

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
from tests.test_conn.models.Users import Users
from tests.test_conn.models.Email import Email



class TestDatabaseInsert(unittest.TestCase):
        
    def test_insert_okay(self):

        #test_conn = DatabaseManager(test_db_creds['my_sqlite'])
        test_db = DatabaseManager(test_db_creds['my_oracle'])


        test_db.setup_db()
        #Base.metadata.create_all(test_conn.engine)

        user1 = Users(
            name='alice', 
            email='alice@email.com',
            age=23,
            heigh=170.3,
            data=b'\x01'
            )
        
        user1 = Users(
            name='alice', 
            email='alice@email.com',
            age=23,
            heigh=170.3,
            data=b'\x01'
            )

        user2 = Users(name='joe', email='alice@email.com')

        email = Email(email='awa@email.com', text='test awa', persnr=9000)

        email1 = Email(email='awa@email.com111', text='test awa', persnr=9000)

        email1.text = 'adasdadadasda'

        #test_conn.insert_only(email1)

        is_insert = test_db.insert_with_chk(Email, email, email.email)

        #self.assertTrue(is_insert[0])

        email = Email(email='awa@test.com', text='test awa', persnr=9000)

        is_insert = test_db.insert_with_chk(Email, email, email.email)
        
        self.assertFalse(is_insert[0])


if __name__ == '__main__':
    unittest.main()