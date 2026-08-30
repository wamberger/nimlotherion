

.. raw:: html

   <br />


Security Considerations
#######################

Authentication and Authorization
********************************

The *data_importer* use framework for any connections or logins. 
The credentials are saved in the *config.yaml* file.

How framework works, read the documentation about **nimlotherion**.

.. raw:: html

   <br />

Data Protection
***************

You should always allow only authorizated personal to customize 
user-settings and to have knowledge about the schema of the used databases.

For the encryption and other security issues you should use the framework.

.. raw:: html

   <br />

Using *eval* Options in Settings
********************************

The Python *eval* function is called when you set in the 
:ref:`modify_pref_label` a code which should be executed.

The functions which calls `*eval* <https://docs.python.org/3/library/functions.html#eval>` 
should always be called in such way that it cannot execute 
a malicious code. It should always check the string or 
it should be called with other code structure together.


.. raw:: html

   <br />

Logging and Auditing
********************

All the sensitive data should **ONLY** be printed in log files, such like:

* database's table schemas
* passwords
* source code
* errors
* warnings
* debugging messages

.. raw:: html

   <br />


Vulnerability Management
************************

Explain how the development team monitors 
and addresses security vulnerabilities, 
including the process for applying patches and updates.

Dependency Management:

Highlight the importance of keeping third-party 
libraries and dependencies up to date to avoid 
vulnerabilities introduced by outdated components.


.. raw:: html

   <br />

