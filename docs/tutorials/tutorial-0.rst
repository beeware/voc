Tutorial 0 - Hello, world!
==========================

In this tutorial, you'll take a really simple "Hello, world!" program written in
Python, convert it into a classfile, and run it on the Java Virtual Machine.

Setup
-----

This tutorial assumes you've read and followed the instructions in
:doc:`/intro/getting-started`. If you've done this, you should have:

* Java 7 installed and available on your path
* A activated Python 3.4 virtual environment
* `voc` installed in that virtual environment

Start a new project
-------------------

TODO - write an actual tutorial :-)


then run it over your python script::
    $ pip install voc
    $ python -m voc path/to/your/example.py
    Creating class 'example'...
    Writing example/__init__.class...
    Done.

This will produce an ``__init__.class``, in the ``python/example`` namespace,
that you can run on any Java 1.7+ VM. To run the classfile, you'll need the
Python support libraries. These will eventually be available as a download;
for now, you'll need to compile them. See below for compilation instructions.

Once you've got the support Jarfile, you can run the example.class ensuring that
the support jarfile is in your classpath. For example, using the Oracle Java VM,
you would run::

    $ java -XX:-UseSplitVerifier -classpath dist/python-java.jar:. python.example.__init__
    Hello, World

.. note: Java 8

   If you are using Java 8, substitute ``-noverify`` in place of ``-XX:-UseSplitVerifier``.
