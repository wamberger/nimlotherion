

import os
import sys
import unittest
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))

from nimlotherion.email.smtp import SmtpHolder


from tests._test_utility_files.test_expections import test_smtp_creds


class TestEmail(unittest.TestCase):

    def test_smtp(self):

        smtp_holder = SmtpHolder(test_smtp_creds)

        #print(smtp_holder.example_name.__dict__)
        self.assertEqual(
            smtp_holder.example_name.__dict__, 
            test_smtp_creds['example_name']
            )


if __name__ == '__main__':
    unittest.main()