Tutorial 1 - Interoperating with Java
=====================================

In this tutorial you'll learn how to use VOC to write Python code
interoperating with Java, namely, how to write Python code that calls Java and
how to make your code callable by Java.


Setup
-----

This tutorial assumes you've read and followed the instructions in
:doc:`/background/install` and that you've successfully followed
:doc:`tutorial-0` -- if you haven't done that yet, please do it before this.

Once you've followed that, it will be helpful if you set an environment variable
``VOC_DIR`` to your local VOC repository. If you're using Linux or Mac, you can do
that by writing in your current terminal::

    VOC_DIR=/path/to/voc

In case you don't really want to do that for some reason, you'll need to
remember to replace ``$VOC_DIR`` by the full VOC directory any time it
appears in the commands below.


Calling a Java method
---------------------

Many Java APIs can be called by simply using the imports and calling
with the equivalent Python types. Here is a simple example that calls
the ``System.getProperty()`` Java method to show some information about
your Java runtime environment::


    from java.lang import System

    print("Your JRE version is", System.getProperty('java.version'))
    print("You're using Java from vendor", System.getProperty('java.vendor'))
    print("The current class path is", System.getProperty('java.class.path'))

Try putting the above into a file named ``javainfo.py``, and compile it with
``voc -v javainfo.py``.

Then, run it with ``java -cp $VOC_DIR/dist/python-java-support.jar:. python.javainfo``.
You will see something like this ::

    Your JRE version is 1.8.0_151
    You're using Java from vendor Oracle Corporation
    The current class path is /home/elias/src/voc-dev/voc/dist/python-java-support.jar:.

The actual text will vary according to your installed version of Java JDK.

The argument ``-cp`` is the so-called Java `classpath`_, and is used by the JVM to locate packages and classes needed by a program.


How does it work?
~~~~~~~~~~~~~~~~~

Behind the scenes, VOC is generating code that uses proxy objects to access
Java code, converts Python types like strings into Java strings before calling
methods like Java's ``System.getProperty()``.

To know more about how this work, see the section about :doc:`../reference/typesystem`.

Common problems
~~~~~~~~~~~~~~~

If you see an error message like::

    Error: Could not find or load main class python.javainfo

This usually happens because the classpath is incorrect, causing the JVM to fail to find the class or something that was imported in a class.
Make sure to include the correct path to the ``python-java-support.jar`` file and the current directory in the classpath, separated by ``:``.


Extending a Java class
----------------------

TODO: example extending a java class.


Implementing a Java interface
-----------------------------

TODO: example implementing a Java interface, which can be called by Java code.

.. _classpath: https://en.wikipedia.org/wiki/Classpath_(Java)
