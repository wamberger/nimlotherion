

__all__ = ['Log']


import logging

from concurrent_log_handler import ConcurrentRotatingFileHandler


class Log:
    """It set up the log configurations and initiate the attributes."""

    __slots__ = ('info', 'warning', 'error', 'critical')

    def __init__(self, logs: dict[str, str], verbosity: bool = False) -> None:
        """
        Args:
            logs (Dict[str, str]):
                - Keys: 'level', 'info', 'warning', 'error' and 'critical'.
                - Values:
                    - Key level has str 'info', 'warning', 'error'
                        or 'critical'.
                    - Keys info | warning | error | critical:
                        Path with the log name including suffix where the
                        file will be stored.
                        Example: ../path/to/info.log
        """

        self._setup_logging(logs, verbosity)

        self.info: logging.Logger = logging.getLogger('info')
        self.warning: logging.Logger = logging.getLogger('warning')
        self.error: logging.Logger = logging.getLogger('error')
        self.critical: logging.Logger = logging.getLogger('critical')

    @staticmethod
    def _setup_logging(logs: dict[str, str], verbosity: bool = False) -> None:

        try:
            log_format = '[%(process)d] %(asctime)s [%(levelname)s] ' \
                         '[%(filename)s] %(funcName)s ' \
                         '(%(lineno)d): %(message)s'
            formatter = logging.Formatter(log_format)

            log_levels = ['info', 'warning', 'error', 'critical']
            if verbosity or logs['level'] == 'info':
                pass
            else:
                if logs['level'] == 'warning':
                    log_levels.remove('info')
                elif logs['level'] == 'error':
                    log_levels.remove('info')
                    log_levels.remove('warning')
                elif logs['level'] == 'critical':
                    log_levels.remove('info')
                    log_levels.remove('warning')
                    log_levels.remove('error')

            for level in log_levels:
                logger = logging.getLogger(level)
                log_filename = logs[level]
                log_handler = ConcurrentRotatingFileHandler(
                    log_filename,
                    maxBytes=1024 * 1024,
                    backupCount=3
                )
                log_handler.setLevel(getattr(logging, level.upper()))
                log_handler.setFormatter(formatter)
                logger.addHandler(log_handler)

            root_logger = logging.getLogger()
            root_logger.setLevel(logging.INFO)  # Set the root logger level to the lowest level you want to capture
        except Exception as e:
            raise Exception(f'Cannot configurate the log: {e}')
