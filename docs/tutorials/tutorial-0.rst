Tutorial 0 - Hello, world!
==========================

In this tutorial, you'll take a really simple "Hello, world!" program written in
Python, convert it into a classfile, and run it on the Java Virtual Machine.

Setup
-----

This tutorial assumes you've read and followed the instructions in
:doc:`/intro/getting-started`. If you've done this, you should have:

* Java 7 installed and available on your path,
* A ``tutorial`` directory with a VOC checkout,
* A activated Python 3.4 virtual environment,
* VOC installed in that virtual environment,
* A compiled VOC support library.

Start a new project
-------------------

Lets start by creating a ``tutorial0`` directory:

.. code-block:: python

    $ mkdir tutorial0
    $ cd tutorial0

Then create a file called ``example.py`` in this directory.
Add the following Python code to ``example.py``:

.. code-block:: python

    print("Hello World!")

Save the file. Run VOC over this file, compiling the Python code into a Java
class file:

.. code-block:: bash

    $ python -m voc example.py

You will see output like the following:

.. code-block:: bash

    Creating class 'example'...
    Writing example/__init__.class...
    Done.

This will produce an ``__init__.class`` in the ``python/example`` namespace.
This classfile can run on any Java 1.7+ VM. To run the project, type:

.. code-block:: bash

    $ java -XX:-UseSplitVerifier -classpath ../voc/dist/python-java.jar:. python.example.__init__
    Hello, World

.. note:: Java 8

   If you are using Java 8, substitute ``-noverify`` in place of ``-XX:-UseSplitVerifier``.

Congratulations! You've just run your first Python program under Java using
VOC! Now you're ready to get a little more adventurous.
