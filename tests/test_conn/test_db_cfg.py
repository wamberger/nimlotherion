

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



from sqlalchemy.exc import SQLAlchemyError

from nimlotherion.conn.db import DatabaseManager
from nimlotherion.conn.db import DatabaseManagerHolder

from tests._test_utility_files.test_args import test_db_creds


class TestDatabaseCfg(unittest.TestCase):

    def test_db_manager_holder(self):
        
        # test 1
        db_mgr_hldr = DatabaseManagerHolder()

        db_mgr_hldr.load_databases(test_db_creds)

        self.assertIsInstance(db_mgr_hldr.databases, dict)

        self.assertEqual(
            len(db_mgr_hldr.databases), 5) 
        
        self.assertNotEqual(
            len(db_mgr_hldr.databases), 6)

        test_db = db_mgr_hldr.databases.get('my_sqlite')

        self.assertIsInstance(test_db, DatabaseManager)

        # test 2
        db_mgr_hldr_1 = DatabaseManagerHolder(test_db_creds)

        test_db_1 = db_mgr_hldr_1.get_database('my_sqlite')

        self.assertIsInstance(test_db_1, DatabaseManager)

        test_db_2 = db_mgr_hldr_1.get_database('not_exist')

        self.assertIsNone(test_db_2)

        # test 3
        db_mgr_hldr_1 = DatabaseManagerHolder()

        test_db_3 = db_mgr_hldr_1.get_database('not_exist')

        self.assertIsNone(test_db_3)


    def test_db_manager(self):
        
        #test 1
        test_db_1 = DatabaseManager(test_db_creds['my_sqlite'])

        test_db_1.setup_db()

        test_db_1.ping_db()

        #test 2
        db_mgr_hldr = DatabaseManagerHolder(test_db_creds)

        test_db_2 = db_mgr_hldr.get_database('my_oracle')

        test_db_2.setup_db()

        test_db_2.ping_db()

        #test 3
        test_db_3 = db_mgr_hldr.databases.get('example_name1')

        with self.assertRaises(ConnectionError) as context:
            test_db_3.setup_db()
            
        err_msg_1 = 'Cannot create engine or connect to '\
            'the database: Not specified. Error: '\
            "Can't load plugin: sqlalchemy.dialects:oracle.ddd"
        
        self.assertIn(err_msg_1, str(context.exception))

        # test 4
        test_db_4 = db_mgr_hldr.databases.get('example_name2')
        
        test_db_4.setup_db()

        with self.assertRaises(SQLAlchemyError) as context:
            test_db_4.ping_db()

        err_msg_2 = '(cx_Oracle.DatabaseError) ORA-01017: '\
            'Benutzername/Kennwort ungültig; Anmeldung '\
            'abgelehnt\n(Background on this error '\
            'at: https://sqlalche.me/e/20/4xp6)'
        
        self.assertIn(err_msg_2, str(context.exception))

        #test 5
        test_db_5 = db_mgr_hldr.databases.get('example_name4')
        
        test_db_5.setup_db()

        with self.assertRaises(SQLAlchemyError) as context:
            test_db_5.ping_db()

        err_msg_3 = '(cx_Oracle.DatabaseError) ORA-12505: TNS: '\
            'Listener kann in Connect-Deskriptor angegebene SID '\
            'aktuell nicht auflösen\n(Background on this error '\
            'at: https://sqlalche.me/e/20/4xp6)'
        
        self.assertIn(err_msg_3, str(context.exception))


if __name__ == '__main__':
    unittest.main()