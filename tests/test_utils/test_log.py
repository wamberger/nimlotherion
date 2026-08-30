

import os
import sys
import unittest
import logging
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))

from unittest.mock import patch 
from unittest.mock import MagicMock

from tests._test_utility_files.test_args import test_log_cfg

from nimlotherion.utils.log import LogManager


class TestLogging(unittest.TestCase):

    def setUp(self):
        self.logger_patch = patch('logging.getLogger')
        self.mock_logger = self.logger_patch.start()

    def tearDown(self):
        self.logger_patch.stop()

    def test_logging_behavior(self):

        logger_instance = self.mock_logger.return_value
        logger_instance.info = MagicMock()

        log = LogManager(test_log_cfg)

        log.info.info('test info')
        log.warning.warning('test warning')
        log.error.error('test error')
        log.critical.critical('test critical')

        #logging.getLogger('info').info('Test info')
        #logger_instance.info.assert_called_once_with('Test info')

        info = logging.getLogger('info')
        info.info("test info var")
        logger_instance.info.assert_called_once_with('test info var')

        #logging.getLogger('warning').warning('Test warning')
        #logger_instance.warning.assert_called_once_with('Test warning')
        warning = logging.getLogger('warning')
        warning.warning("test warning var")
        logger_instance.warning.assert_called_once_with('test warning var')

        logging.getLogger('error').error('Test error')
        logger_instance.error.assert_called_once_with('Test error')
        
        critical = logging.getLogger('critical')
        critical.critical("test critical var")
        logger_instance.critical.assert_called_once_with('test critical var')


if __name__ == '__main__':
    unittest.main()
