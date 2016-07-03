Tutorial 0 - Hello, world!
==========================

In this tutorial, you'll take a really simple "Hello, world!" program written in
Python, convert it into a classfile, and run it on the Java Virtual Machine.

Setup
-----

This tutorial assumes you've read and followed the instructions in
:doc:`/intro/getting-started`. If you've done this, you should have:

* Java 6 (or higher) installed and available on your path,
* A ``tutorial`` directory with a VOC checkout,
* A activated Python 3.4 virtual environment,
* VOC installed in that virtual environment,
* A compiled VOC support library.

Start a new project
-------------------

Let's start by creating a ``tutorial0`` directory in the tutorial directory alongside the ``voc`` directory you just cloned into:

.. code-block:: bash

    $ mkdir tutorial0
    $ cd tutorial0

So that your directory structure looks like::

    tutorial
    ├── tutorial0
    └── voc

Then create a file called ``example.py`` in this ``tutorial0`` directory.
Add the following Python code to ``example.py``:

.. code-block:: python

    print("Hello World!")

Save the file. Run VOC over this file, compiling the Python code into a Java
class file:

.. code-block:: bash

    $ voc -v example.py

This runs the VOC compiler over the ``example.py`` source file. The ``-v`` flag
asks VOC to use verbose output so you can see what is going on.
You will see output like the following:

.. code-block:: bash

    Compiling example.py ...
    Adding default main method...
    Writing python/example/__init__.class ...

This will produce an ``__init__.class`` in the ``python/example`` namespace.
This classfile can run on any Java 6 (or higher) VM. To run the project, type:

* On Linux / OS X

.. code-block:: bash

    $ java -classpath ../voc/dist/python-java.jar:. python.example.__init__
    Hello World!

* On Windows

.. code-block:: bash

    > java -classpath ../voc/dist/python-java.jar;. python.example.__init__
    Hello World!


Congratulations! You've just run your first Python program under Java using
VOC! Now you're ready to get a little more adventurous.
