

import os
from alchemyrohan.assemble import assemble_models


########################
# Adapt the code below #
########################

project_name = 'models'

table_names = [
    'users'
    ]

#db_creds = f"oracle+cx_oracle://bde:sisbde@tasmania:1521/entw"
db_creds = f"sqlite:///C:/Users/awa/work_desk/projects/siswork/tests/test_conn/test_sqlite.db"

########################
# Adapt the code above #
########################

dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(dir, os.pardir))

# You may need to adapt this code if you changed directory names or other paths
abs_path_to_models = os.path.join(parent_dir, project_name)
py_path_to_model = 'tests.test_conn.models'


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

