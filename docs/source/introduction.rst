
.. raw:: html

   <br />

Introduction
############

Overview
========

The **nimlotherion** is python library for reading or working with the data
saved in different file formats.

creating software which transfers data
from one source to another where ETL (Extract, transform, load), synchronization, 
replication or migration process is used. Therefore is the software suitable for
small or big backgroud processes or tasks and needs to be, 
but not necessarily, integrated into another GUI software.

The library has an option to extract data using web-API, database or flat file
like *.csv*. The loading can be done using any database, usually 
operational database, or a web-API. The transformation process like 
formatting, mapping, cleaning, joining or aggregating of data are the 
core functions of the library.

One of the main advantages of the library is that there are many functions
available where the date and time is calculating.

.. raw:: html

   <br />

Purpose
=======

The library is meant to be used by developers to help them build
various lightweight software applications in the field of transferring 
data from one *point* to another — independent of the source — 
and whose data may also need to be transformed.

We recommend the library for small background software applications that
perform various transfer tasks and are executed either through another 
background program or by end-users via a GUI.

.. raw:: html

   <br />

Philosophy
==========

On the one hand, there are often programs that share similar code, meaning, 
and even tasks. On the other hand, they still perform distinct tasks, 
and often, with additional code and task extensions, it leads to *spaghetti* code, 
which is difficult to maintain. This is where the issue arises, 
necessitating the need for separate code. Thus, project emerged from the idea 
of creating a library for small, similar, and flexible, yet
independent programs that run in the background

The separation is necessary not only for better maintenance and monitoring 
but also for ease of replacement, if needed. As modules can be 
replaced or modified without infecting other parts of the code, so can 
also small programs be either corrected, extended, refactored, or entirely 
replaced with new code without affecting any other background program or 
his behaviour which lies in the same environment.

.. raw:: html

   <br />
