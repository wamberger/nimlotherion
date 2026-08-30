

def tmpl_pyproject_toml(
        auth: str, auth_email: str, project: str, desc: str) -> str:

    return f'''

[build-system]
requires = ["pdm-backend"]
build-backend = "pdm.backend"


[project]
name = "{project}"
version = "0.0.1"
dependencies = []
requires-python = ">=3.12"
authors = [
  {{ name = "{auth}", email = "{auth_email}" }},
]
maintainers = [
  {{name = "{auth}", email = "{auth_email}"}}
]
description = "{desc}"
readme = "README.md"
license = {{file = "LICENSE"}}
keywords = []
classifiers = [
    "Development Status :: 2 - Pre-Alpha",
    "Intended Audience :: Developers",
    "Topic :: Microframework :: Build Tools",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.12",
    "Operating System :: OS Independent"
]


[project.urls]
Homepage = ""
Documentation = ""
Repository = ".git"
Issues = ""
Changelog = "../CHANGELOG.md"

'''
