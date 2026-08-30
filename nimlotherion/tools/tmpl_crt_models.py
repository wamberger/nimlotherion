

def tmp_create_models_py() -> str:
    return """

import os
from alchemyrohan.assemble import assemble_models


########################
# Adapt the code below #
########################

project_name = 'test_project'

table_names = [
    'table_name1', 
    'table_name2'
    ]

db_creds = f"oracle+oracledb://db_user:db_password@db_host:db_port/db_sid"
db_creds = f"sqlite:///{dir}{os.sep}test_sqlite{os.sep}test.db"

########################
# Adapt the code above #
########################

dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(dir, os.pardir))

# You may need to adapt this code if you changed directory names or other paths
abs_path_to_models = os.path.join(parent_dir, project_name, 'models')
py_path_to_model = 'need_to_replace_code'

try:
    assemble_models(
        db_creds, 
        table_names, 
        abs_path_to_models,
        py_path_to_model
        )
    exit(0)
except Exception as e:
    print(e)
    exit(1)

"""