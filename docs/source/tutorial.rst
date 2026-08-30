
.. raw:: html

   <br />

Tutorials
#########

This tutorial will demonstrate how to use the framework using the 
standard approach. However, you can also use it by simply 
importing the modules.

.. raw:: html

   <br />

.. _Tutorial-1-Basic-Label:

Tutorial 1: Basic
*****************

.. _Siswork-Build-Label:

Siswork-Build
=============

To create a new project with standard directories and files, 
you need to enter the following code into the command line:

.. code-block:: bash
    :caption: Unix

    siswork-build <project_name>


After a few prompts, it will create a directory with the *project_name* 
and a structure similar to that of a standard Python package.

.. code-block:: bash

   project_name/
   ├── setup.py
   ├── requirements.txt
   ├── MANIFEST.in
   ├── README.md
   ├── CHANGELOG.md
   ├── tests/
   ├── help_files/
   │     ├── run_project_name.py
   │     ├── create_models.py
   │     └── config_project_name.yaml
   └── project_name/
         ├── main.py
         ├── settings.py
         ├── models/
         ├── tasks/
         └── utils/
   

The *setup.py* is used to create the distribution 
that is employed in production. More about it in :ref:`Distribution-Label`.

The *requirements.txt* file contains dependencies that the project 
needs to function properly and in the *MANIFEST.in* file, you can add 
additional directories or files that you want to include in 
your distribution. By default, it includes the *requirements.txt* 
file and the content of the *project_name* and *help_files* directories.
Keep in mind that the code in *project_name* is for production.

In your *README.md* file, you describe your project's overview, 
purpose, functions, tests,...and tutorial. If your project's 
description is very long, you should consider creating separate, 
organized documentation. *CHANGELOG.md* is for a record of all 
notable changes made to the project over the time.

The files and subfolders in the *help_files/*, *tests/* and *project_name/* 
directories are described here :ref:`Tutorial-1-Basic-Label`.
It should be noted that the source code is, and should be, 
only in the *project_name* directory.

After creating your project's directory using :ref:`Siswork-Build-Label`, 
you can also create your project's own environment 
(:ref:`Virtual-Environments-Label`). However, I will not 
be using our own environment in this tutorial.

.. raw:: html

   <br />

Source Code
===========

As first we need to focus on the source code folder:

.. code-block:: bash

   project_name/
         ├── main.py
         ├── settings.py
         ├── apis/
         ├── models/
         ├── tasks/
         └── utils/


*main.py*
---------

This is by default entry point for all *tasks*. However, 
you may change the code or remove the file.





As first we need to create new module, so we
to navigate into *modules/* directory. Here you create a new module/script - 
Let we call it *example.py*.

.. raw:: html

   <br />


.. _Distribution-Label:

Distribution
------------

The a *setup.py* file is called to create the new distribution files.

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
