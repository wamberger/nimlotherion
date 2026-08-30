

def tmpl_main_py(auth: str, project: str) -> str:
    
    return f'''

"""
Template for the default entry point of task modules.

You can edit the code or remove the file - it is not bound on framework.
"""

__title__ = '{project}'

__author__ = '{auth}'

__version__ = '0.1.0'
__status__ = 'Alpha'


import os
import importlib
import {project}.cli as cli

from {project}.loggers.log import LogManager


##########################################
# Adapt, change or delete the code below #
##########################################

path = os.path.join(os.path.join(os.getcwd(), os.pardir), os.pardir, 'config_{project}.yaml')
cli_config = cli.CliConfig('yaml', path)

cli_args = cli.CliArgs()

log = LogManager(cli_config.config['log'], cli_args.args.verbosity)

##########################################
# Adapt, change or delete the code above #
##########################################


if __name__ == '__main__':

    if cli_args.args.verbosity:
        log.info.info(
            f'Start the program with the module: {{cli_args.args.module}}')

    importlib.import_module('tasks.' + cli_args.args.module)
    exit(0)

'''
