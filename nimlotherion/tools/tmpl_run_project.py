

def tmpl_run_project() -> str:

    return """

import os
import sys
import asyncio

sys.path.append(os.path.dirname(os.getcwd()))

import logging
from datetime import datetime, time


def log_task_scheduler(msg):

    logging.basicConfig(
        filename='task_scheduler.log', 
        level=logging.INFO, 
        format='%(asctime)s[%(levelname)s] %(message)s'
        )

    logging.info(msg)


def run_one_instance():
    current_time = datetime.now().time()
    target_time = time(13, 2)

    arguments_list = [
        ("arg1_value1", 
         "arg2_value1", 
         "arg3_value1", 
         "arg4_value1", 
         "arg5_value1", 
         "arg6_value1", 
         "arg7_value1", 
         "arg8_value1", 
         "arg9_value1", 
         "arg10_value1"
         ),
        ("arg1_value2", 
         "arg2_value2", 
         "arg3_value2", 
         "arg4_value2", 
        ),
        # Add more argument sets as needed
    ]

    from test_file import test_func

    if current_time >= target_time:
        log_task_scheduler('Start module 1')
        for args in arguments_list:
            test_func(args)
        log_task_scheduler('End module 1')


async def run_multiple_instances():

    import test_project.tasks.test_file as tf

    arguments_list = [
        ("arg1_value1", 
         "arg2_value1", 
         "arg3_value1", 
         "arg4_value1", 
         "arg5_value1", 
         "arg6_value1", 
         "arg7_value1", 
         "arg8_value1", 
         "arg9_value1", 
         "arg10_value1"
         ),
        ("arg1_value2", 
         "arg2_value2", 
         "arg3_value2", 
         "arg4_value2", 
        ),
        # Add more argument sets as needed
    ]
    
    for args in arguments_list:
        process = await asyncio.create_subprocess_exec(
            sys.executable, tf.__file__, *args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        stdout, stderr = await process.communicate()
        log_task_scheduler(f"Subprocess output: {stdout.decode().strip()}")
        log_task_scheduler(f"Subprocess error: {stderr.decode().strip()}")


if __name__ == "__main__":
    
    run_one_instance()

    asyncio.run(run_multiple_instances())


"""