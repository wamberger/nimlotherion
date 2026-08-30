
.. raw:: html

   <br />

Getting Started
###############

Build App
=========

To start

.. code-block:: bash

    pip install ./nimlotherion-0.x.x.tar.gz


.. raw:: html

   <br />

Distribution
============

For bringing software to client's server, you need to Download this `file`_, 
otherwise ignore this section and go to :ref:`Get-the-Source-Code-label`.

As first you need to be sure that all the needed software is installed on the client's server. 
if not, go again through the previous two sections.

When you have brought your *data_importer.0.x.x.tar.gz* file to the client's SFA folder enter the next command:

.. code-block:: bash

    nimlotherion-ext-tar ./data_importer-0.x.x.tar.gz


.. _file: http://evo-git/py/data_importer/blob/master/dist/


If you only need to bring the current version to the client's server 
then you can ignore the :ref:`Get-the-Source-Code-label` section and go to :ref:`Dependencies_label`.


.. raw:: html

   <br />

.. _Get-the-Source-Code-label:

Get the Source Code
===================

If your device has not already installed `Git`_, then you need to `install`_ it.

After the Git is available on your devide, you can go to data_importer's repository and `download`_ it or you can clone it via git:

.. _download: http://evo-git/py/data_importer

.. code-block:: bash

   git clone --recursive http://evo-git/py/data_importer.git


.. _Git: https://git-scm.com/
.. _install: https://git-scm.com/downloads


.. raw:: html

   <br />

.. _Dependencies_label:

Dependencies
============

Install the following packages/libraries

* `PyYaml`_
* `oracledb`_
* `python-dateutil`_

.. _PyYaml: https://pyyaml.org/
.. _oracledb: https://oracle.github.io/python-oracledb/
.. _python-dateutil: https://github.com/dateutil/dateutil

with the following command when you navigate to the *data_importer* folder:

.. code-block:: bash
    
   pip -r requirements.txt


.. raw:: html

   <br />


Integrating with EvoApp
=======================

In the directory **requirements/** are installers for creating and integrating tables into the EvoApp.

On Windows OS double click:: 
    
   win_install_req.bat

On Unix-Like OS execute in terminal::
    
   unix_install_req

.. raw:: html

   <br />


.. _configuration_label:

Configuration
*************

The **data_importer** has one *built-in* configuration file *config.yaml*.

.. raw:: html

   <br />

Locale
======

This part in configuration file should be leaved as it is. Only if you know why you want to change it.

.. raw:: html

   <br />

Log
===

There are four log levels:

- DEBUG
- INFO
- WARN
- ERROR/FATAL

which you can define in config.yaml file:

.. code-block:: yaml
   :caption: Example with INFO

      log_global_level: INFO


In */log* directory are four different log files, each one for one log level. This files will be made there by default with *siswork* framework.
But you can change the names and location of files in config.yaml file.

.. code-block:: yaml
   :caption: Example of *WARN*

      log_warn:
         log_filename: log_warn.log
         log_abspath:

In example above and by default the file name of *WARN* is *log_warn.log* and
by default is *log_abspath* empty and will be saved in */log* folder.

There is one more log file - exception

.. code-block:: yaml

   log_exc:
      log_filename: log_exc.log
      log_abspath:

This log will be only used when the program ends unexpected.

.. raw:: html

   <br />

Database
========

In config.yaml file you will see:: 
   
   primary_db:

As primary database we mean the database which is used by your program. 
This is also the database where the default tables needs to be installed.

All futher databases can be named individual and added in *config.yaml* file::
   
   example_name:

can be::

   my_data_base:


Furthermore you need to give also database credentials:

.. code-block:: yaml

   dialect: 
   sql_driver:
   user: 
   password:
   host:
   port:
   service:

.. raw:: html

   <br />

API
===

The same as with database, you can add and name your APIs with individual naming and type its credentials

.. code-block:: yaml

   example_name:
      url:
      header:
      key:
      token:
      user:
      password:


.. raw:: html

   <br />


SMTP
====

Also with E-Mail settings you have the same rules as with API and Database configuration.

You can add multiple SMTP and individual name

.. code-block:: yaml

   example_name:
      smtp_host:
      smtp_port:
      smtp_user:
      smtp_password:
      smtp_start_TLS:


.. raw:: html

   <br />

Individual Configuration
========================

By default the *siswork* framework only needs the configuration mention above. 
But if you need to add new configurations for your program in config.yaml, 
then those will be available in the code under *config* object.

.. raw:: html

   <br />

User Guide
**********

We recommend that the program should be used only by administrators 
if there is a  work with the sensitive data.


.. raw:: html

   <br />

Settings Tables
===============

There are seven standard settings/database tables for user to customize the preferences of the program.

+---------------+------------------------------------------------+
|     Table     |                    Purpose                     |
+===============+================================================+
|   task_pref   | User-settings for task/modules                 |
+---------------+------------------------------------------------+
|   col_pref    | User-settings for single columns               |
+---------------+------------------------------------------------+
| subtask_pref  | User-settings for additional task/module       |
+---------------+------------------------------------------------+
|  modify_pref  | User-settings for manipulation of data         |
+---------------+------------------------------------------------+
|   file_pref   | The location of the file with import data      |
+---------------+------------------------------------------------+
|    db_pref    | Settings to connect and read external Database |
+---------------+------------------------------------------------+
| truncate_data | backup of truncate data                        |
+---------------+------------------------------------------------+

For more information and how to setup, look to :ref:`tables_label`


.. raw:: html

   <br />

With EvoApp
===========

Currently is the software integrated into EvoApp application via *report* module 
and the **data_importer** directory must be at the same level as it is of **Pyre**.
Because the *Pyre* is configurated that it calls *data_importer* from the same level directory.

The tables to set preferences are visible in the EvoApp *maintance*. 
In most cases you will need to set *task_pref*, *col_pref* and *file_pref* or *db_pref*.

After you customize the preferences, you need to navigate to the main menu of EvoApp 
where is an icon with the name *data_importer*. There you choose the *task*/*business_logic* and *module*.

The task/business_logic is user's individual naming. For :ref:`modules_label` look the chapter.

If you run the program with *start* and you tick off the *pdf_report* in *task_pref*. 
Then you will receive an *.pdf* file. Otherwise the program will run only in background and nothing will appear in application.


.. raw:: html

   <br />

Other GUI
=========

At the moment there is no other App or GUI for this program available.

Look :ref:`development_label`.

.. raw:: html

   <br />

Use cases and scenarios
=======================

Before using it, be sure that you are familiar with :ref:`tables_label`.

Import from *.csv* file
-----------------------

1. Customize *task_pref*
2. Customize *file_pref*
3. Customize *col_pref*
4. Start the program in EvoApp menu or run it in background

Import from *.csv* file with editing
------------------------------------

1. Customize *task_pref*
2. Customize *file_pref*
3. Customize *modify_pref*
4. Customize *col_pref*
5. Start the program in EvoApp menu or run it in background

Import from *.csv* file with subtask
------------------------------------

1. Customize *task_pref*
2. Customize *subtask_pref*
3. Customize *file_pref*
4. Customize *col_pref*
5. Start the program in EvoApp menu or run it in background

Import from *.csv* file with subtask and editing
------------------------------------------------

1. Customize *task_pref*
2. Customize *subtask_pref*
3. Customize *file_pref*
4. Customize *modify_pref*
5. Customize *col_pref*
6. Start the program in EvoApp menu or run it in background

Import from external database
-----------------------------

Be sure that you configurated the *config.yaml* properly.

1. Customize *task_pref*
2. Customize *db_pref*
3. Customize *col_pref*
4. Start the program in EvoApp menu or run it in background


Import from external database with editing
------------------------------------------

1. Customize *task_pref*
2. Customize *db_pref*
3. Customize *modify_pref*
4. Customize *col_pref*
5. Start the program in EvoApp menu or run it in background

Import from external database with subtask
------------------------------------------

1. Customize *task_pref*
2. Customize *subtask_pref*
3. Customize *db_pref*
4. Customize *col_pref*
5. Start the program in EvoApp menu or run it in background

Import from external database with subtask and editing
------------------------------------------------------

1. Customize *task_pref*
2. Customize *subtask_pref*
3. Customize *db_pref*
4. Customize *modify_pref*
5. Customize *col_pref*
6. Start the program in EvoApp menu or run it in background

.. raw:: html

   <br />
