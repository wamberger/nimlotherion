
import os
import sys
import unittest
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))


from nimlotherion.utils.audit import DatabaseAudit


class TestDatabaseAudit(unittest.TestCase):

    def test_audit_insert(self):

        audit = DatabaseAudit('Tester', 'Admin')

        audit.append_insert('test insert1')
        audit.append_insert('test insert2')
        audit.append_insert('test insert3')
        audit.append_insert('test insert4')

        audit.write_inserts('audit.txt')

    def test_audit_update(self):

        audit = DatabaseAudit('Tester', 'Admin')

        audit.append_update('test update1')
        audit.append_update('test update2')
        audit.append_update('test update3')
        audit.append_update('test update4')

        audit.write_updates('audit.txt')

    def test_audit_delete(self):

        audit = DatabaseAudit('Tester', 'Admin')

        audit.append_deletion('test deletion1')
        audit.append_deletion('test deletion2')
        audit.append_deletion('test deletion3')
        audit.append_deletion('test deletion4')

        audit.write_deletions('audit.txt')


if __name__ == '__main__':
    unittest.main()
