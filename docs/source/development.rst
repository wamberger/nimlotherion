.. raw:: html

   <br />

.. _development_label:

Development
###########

This chapter is only for developers.

If you haven't already installed project localy, 
please go to :ref:`installation_label` section.

.. raw:: html

   <br />

Architecture Overview
*********************

The software uses *EvoApp* as GUI for the configuration and 
execution. In the *EvoApp* the :ref:`tables_label` are available and 
can be customized.
In the :ref:`tables_label` is defined what module/task will be executed 
and with what properties. Because in the :ref:`tables_label` you specify 
from where the source data will come and where, how and what will be saved.

In the source code, the whole process is outlined in the execution module.



Copilot
In the realm of software programming, software architecture description encompasses a set of practices for expressing, communicating, and analyzing software architectures. It serves as a blueprint for a system, providing an abstraction to manage complexity and establish communication and coordination mechanisms among its components12.

Here are some key aspects of software architecture description:

Structure and Elements:
The software architecture describes the structure or structures of the system. It includes software elements, their externally visible properties, and the relationships among them2.
These elements can be modules, components, services, or other building blocks that make up the software system.
Modeling and Representation:
Architecture descriptions are largely a modeling activity. Architects use various forms of representation, such as text, informal drawings, diagrams, or other formalisms (modeling languages), to capture the architecture1.
Multiple views of the architecture address specific concerns of different stakeholders. Each view has a viewpoint documenting its purpose, audience, and modeling conventions1.
Beyond Technical Issues:
Contrary to a common misconception, architecture descriptions don’t solely focus on technical issues. They also address concerns relevant to various stakeholders, including cost, schedule, and process management1.
Stakeholder concerns extend beyond structural aspects to include behavioral, aesthetic, and other extra-functional aspects of the system1.
In summary, software architecture description provides a structured solution, guiding the development process while optimizing quality attributes like performance and security3. It’s a crucial foundation for building robust and effective software systems.

In case of data transforming the framework can do the following tasks:
Cleaning: Fixing inconsistencies, removing duplicates, handling missing values.
Formatting: Converting data types (e.g., string to date), standardizing units of measurement.
Mapping: Matching source fields to target schema, resolving naming differences.
Aggregating: Summarizing data (e.g., calculating monthly sales averages).
Joining: Combining data from multiple sources based on common fields.


.. raw:: html

   <br />

Code Structure and Guidelines
*****************************

Style
=====

We use PEP8 style guide for naming conventions of code files, 
classes, functions, and variables. If you are not familar with it, 
read `here <https://peps.python.org/pep-0008/>`_ about it.

The names of functions, files, classes or varibles should be short 
description about their value or meaning.

.. raw:: html

   <br />

.. _directories_label:

Directories
===========

The software has some own and standard folders. The latter came with framework **siswork**.

*log/*
------

Is standard folder where framework by default saves log files.

*models/*
---------

Is standard folder where framework by default saves SqlAlchemy models when created.

In some cases you will need manually to make changes in the code of models.

*modules/*
----------

In this directory goes every executable *program* from *main.py* and stand-alone modules.

*utils/*
--------

Is individual folder and here goes reusable or other undefined code - functions, classes, etc.

Here is also code for modifications and other similar tasks.


.. raw:: html

   <br />

Main Files and Entry Points
===========================

With framework come some main files. 

*main.py*
---------

This is the entry point of all modules.

.. code-block:: python
    
    if __name__ == '__main__':
        importlib.import_module('modules.' + SETTINGS.args.module)

The above code from *main.py* is telling us that all programs will be 
executed depending on the *module* argument.

*settings.py*
-------------

This is default file from framework. It will be as first called in *main.py* 
and initiate all the user-preferences which will be later used.

.. code-block:: python

    __all__ = [
    'SETTINGS',
    'DB_SESSION',
    'LOG'
    ]


    import os
    import siswork


    try:

        SETTINGS = siswork.config.SettingsHolder(
            os.path.dirname(__file__)
            )

    except Exception as e:
        print("Cannot proceed futher."\
            " Framework's init folders or data is changed.")
        print(e)
        exit(-1)

    # local database by default
    DB_SESSION = SETTINGS.db_engine.primary_db.engine

    LOG = SETTINGS.log

This code never change. But you may add some global variables.

The *SETTINGS* variable is an object who contains all the user-preferences 
and configurations.


*config.yaml*
-------------

The current configuration file. More about, look at :ref:`configuration_label`.

Folder *modules/*
-----------------

In this directory are among others, the executable modules. 
More about, look at :ref:`modules_label`.

.. raw:: html

   <br />


Arguments
=========

.. code-block:: python
    :caption: Default arguments

    -u, --user          Username
    -g, --user_group    Usergroup
    -m, --module        module to execute
    -bl, --b_logic      business_logic
    -o, --prompts       Optional arguments

    -h, --help          show help message
    -v, --verbosity     Additional info -> for debugging

The program is using framework's default arguments. 
However, ignoring the current or adding additional arguments is possible.

.. raw:: html

   <br />

Dependencies
============

Currently the program is using the following dependencies:

* `PyYaml`_ - for reading *YAML* file
* `oracledb`_ - for connecting to oracle database
* `python-dateutil`_ - for converting *string numbers* into datatime object

.. _PyYaml: https://pyyaml.org/
.. _oracledb: https://oracle.github.io/python-oracledb/
.. _python-dateutil: https://github.com/dateutil/dateutil

.. raw:: html

   <br />

Documentation Within Code
=========================

Within the source files, the code does not necessarily 
need to be commented if the naming convention and code 
structure are readable. However, annotations are obligatory.

.. raw:: html

   <br />

Separation of Concerns
======================

As described in :ref:`directories_label` the code should be separated 
in own folders and named according to its purpose.

.. raw:: html

   <br />

Building
********

In the utter part of the project's directory is a *setup.py* file. 
This file is called to create the new distribution files.

.. code-block:: bash

    python3 setup.py sdist


The command above creates tar.gz file in *dist/* folder.

.. code-block:: bash

    python3 setup.py bdist_wheel


The command creates *.whl* file in *dist/* folder.

The **MANIFEST.in** file describes which not *standard* folders or files 
will be includen in distribution file.

.. raw:: html

   <br />


    Development:
        Code structure.
        Building and compilation.
        Code guidelines.
        API reference.
        Frameworks and libraries.

    Testing and Debugging:
        Testing guidelines.
        Debugging tips and techniques.


