

__all__ = ['build_template']


import os
import sys

from typing import Dict


def _read_args() -> Dict[str, str]:
    """
    Returns:
        Dict[str, str]:
            - project_name: name of the project.
            - project_path: where the project's directory
                            will be created.
    """

    user_args = {}
    try:
        user_args['project_name'] = sys.argv[1].lower()
    except Exception as e:
        raise MissingReqArgument(
            f'{e} - name of project is missing as argument')

    if len(sys.argv) == 3:
        user_args['project_path'] = sys.argv[2]
    else:
        user_args['project_path'] = os.getcwd()

    return user_args


def build_template() -> None:
    """Create a new project with file and directories.

    Prompts:
        1 - project_name: the name of the project.
        2 - project_path: Path to the directory where the
            project's folder will be created.

    Returns:
        None
    """

    user_args = _read_args()

    auth: str = input("Please enter the name of the author: ")
    auth_email: str = input('Please enter your E-Mail: ')
    desc: str = input('Please give a short description of your project: ')

    print('Build start!')
    
    print(f"Path to the project: {user_args['project_path']}")

    proj_path = os.path.join(
      user_args['project_path'], 
      user_args['project_name']
      )

    os.mkdir(proj_path)
    print("Project's directory created")

    fi.write_empty_file(os.path.join(proj_path, 'README.md'))
    print('File created: README.md')

    fi.write_empty_file(os.path.join(proj_path, 'CHANGELOG.md'))
    print('File created: CHANGELOG.md')

    fi.write_empty_file(os.path.join(proj_path, 'LICENSE'))
    print('File created: LICENSE')

    fi.write_empty_file(os.path.join(proj_path, 'requirements.txt'))
    print('File created: requirements.txt')

    fi.write_file(
        os.path.join(proj_path, 'MANIFEST.in'),
        t.tmpl_manifest_in(user_args['project_name']))
    print('File created: MANIFEST.in')
    
    fi.write_file(
        os.path.join(proj_path, 'pyproject.toml'),
        t.tmpl_pyproject_toml(auth, auth_email, user_args['project_name'], desc))
    print('File created: pyproject.toml')

    os.mkdir(os.path.join(proj_path, 'tests'))
    print('Directory created: tests/')

    help_files = os.path.join(proj_path, 'help_files')

    os.mkdir(help_files)
    print('Directory created: help_files/')

    fi.write_file(
        os.path.join(help_files, f"run_{user_args['project_name']}.py"),
        t.tmpl_run_project())
    print(f"File created: run_{user_args['project_name']}.py")

    fi.write_file(
        os.path.join(help_files, f'create_models.py'),
        t.tmp_create_models_py())
    print('File created: create_models.py')

    fi.write_file(
        os.path.join(help_files, f"config_{user_args['project_name']}.yaml"),
        t.tmpl_config_yaml())
    print(f"File created: config_{user_args['project_name']}.yaml")

    source_code = os.path.join(proj_path, user_args['project_name'])

    os.mkdir(source_code)
    print(f"Directory created: {user_args['project_name']}/")

    os.makedirs(os.path.join(source_code, 'tasks'))
    print(f"Directory created: tasks/")

    os.makedirs(os.path.join(source_code, 'models'))
    print(f"Directory created: models/")

    os.makedirs(os.path.join(source_code, 'utils'))
    print(f"Directory created: utils/")

    fi.write_file(
        os.path.join(source_code, 'main.py'),
        t.tmpl_main_py(auth, user_args['project_name']))
    print('File created: main.py')

    print('Build done!')


if __name__ == '__main__':
    build_template()
