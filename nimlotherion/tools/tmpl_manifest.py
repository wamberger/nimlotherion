

def tmpl_manifest_in(project_name: str) -> str:

    return f'''

recursive-include {project_name} *

global-exclude */__pycache__/*

'''
