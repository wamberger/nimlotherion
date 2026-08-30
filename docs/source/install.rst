
.. raw:: html

   <br />

Installation
############

.. raw:: html

   <br />

Python Version
==============

We recommend using the latest version of `Python`_.
The software supports Python 3.10 and newer.

.. _Python: https://www.python.org/

You will also need the `pip`_ package manager. 
If you don't have it installed, install the latest version.

.. _pip: https://pypi.org/project/pip/


.. raw:: html

   <br />


Dependencies
============

These distributions will be installed automatically when installing nimlotherion:

* `chardet`_ is character encoding auto-detection in Python.
* `PyYaml`_ is a *.yaml* parser and emitter for Python.
* `python-dateutil`_ module provides powerful extensions to the standard datetime module, available in Python.
* `SQLAlchemy`_ is the Python SQL toolkit and Object Relational Mapper

.. _chardet: https://chardet.readthedocs.io/en/latest/index.html
.. _PyYaml: https://pyyaml.org/
.. _python-dateutil: https://dateutil.readthedocs.io/en/stable/index.html
.. _SQLAlchemy: https://www.sqlalchemy.org/

Optional distributions if *create_models.py* will be used:

* `alchemyrohan`_ is an extension package for SqlAlchemy which automatically creates the database models according to the database schema.

More about it in :ref:`nimlotherion-Build-Label`.

.. _alchemyrohan: https://github.com/wamberger/alchemyrohan

.. raw:: html

   <br />

.. _Virtual-Environments-Label:

Virtual Environments
====================

We recommend using virtual environment in development and in production 
to manage the dependencies for your project.

.. code-block:: bash
    :caption: Unix
    
    mkdir myproject
    cd myproject
    python3 -m venv venv

.. code-block:: bash
    :caption: Windows
    
    mkdir myproject
    cd myproject
    python -m venv venv

To activate use the following command:

.. code-block:: bash
    :caption: Unix
    
    . venv/bin/activate

.. code-block:: bash
    :caption: Windows
    
    venv\Scripts\activate

In order to leave the environment you enter in command like *deactivate*.

.. raw:: html

   <br />


Install nimlotherion
===============
 
Thus you need to download the `nimlotherion`_ file and you enter this command in terminal:

.. _nimlotherion: http://evo-git/py/nimlotherion/blob/master/dist/

.. code-block:: bash

    pip install ./nimlotherion-0.x.x.tar.gz


To install nimlotherion within the activated (:ref:`Virtual-Environments-label`) or
in gobal environment you need to give following command:

.. code-block:: bash
    :caption: Unix/Windows
    
    pip install nimlotherion

.. raw:: html

   <br />
