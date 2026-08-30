

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

from nimlotherion.conn.db import Database
from tests._test_utility_files.test_args import test_db_creds

# test models
from tests.test_conn.models.Email import Email


class TestDatabase(unittest.TestCase):

    def test_all_options(self):

        db = Database(test_db_creds['my_oracle'])
        db.ping_db()

        e = ['awa@emaildsa', 'awa@sdasda', 'awa@email.at', 'awa@bisoss',
             'awa@emailaadsa', 'awa@sdasdaaaa', 'awa@email.ataa', 'awa@bisosasas',
             'awa@emaila22adsa', 'awa@sdasd11aaaa', 'awa@email.atawa', 'awa@bisosaass']

        for _ in e:
            email = Email(email=_, persnr=9000)
            try:
                db.insert(email)
            except Exception as e:
                print(e)

        emails = db.get_by_custom_query(model=Email, equal={'persnr': 9000})

        db.update(emails, {'text': 'awa update test'})

        emails1 = db.get_by_custom_query(model=Email, equal={'persnr': 9000})

        for e in emails1:
            try:
                db.delete(e)
            except Exception as e:
                print(e)

        end = 1


if __name__ == '__main__':
    unittest.main()
