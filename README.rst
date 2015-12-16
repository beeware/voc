.. image:: http://pybee.org/voc/static/images/voc-72.png
    :target: https://pybee.org/voc

VOC
===

.. image:: https://travis-ci.org/pybee/voc.svg?branch=master
    :target: https://travis-ci.org/pybee/voc

A transpiler that converts Python bytecode into Java bytecode.

This is experimental code. If it breaks, you get to keep all the shiny pieces.

What it does:

* Provides an API to let you programmatically create Java class files.

* Compiles a Python 3.4 source file into a Java class file in a nominated
  package. Supports the conversion of:

  * Class definition and construction

  * Class instantiation

  * Method definition and invocation

  * Some mathematical operations

  * Some operations and methods on primitive types

  * Exception handling

  * for/while/if constructs

  * Identification of mainline entry points

  * Static initialization of modules.

  * List comprehensions

  * Keyword arguments

  * `import`, `from X import Y` and `from X import *` statements for Python code

  * Importing and using native Java APIs

  * Implementing Java interfaces.

  * Extending Java classes.

It *doesn't* currently support (this list is incomplete):

* Subclassing Python classes

* Generators

* with statements

* ``exec()``/``eval()``

These things are all *possible* - it's just a matter of time
and development effort. The order listed here is a rough indicator of
development priorities.

Quickstart
----------

Using Python 3.4, install ``voc``, then run it over your python script::

    $ pip install voc
    $ python -m voc path/to/your/example.py
    Creating class 'example'...
    Writing example.class...
    Done.

This will produce an ``example.class``, in the ``python`` namespace, that you can
run on any Java 1.7+ VM. To run the classfile, you'll need the Python support
libraries. These will eventually be available as a download; for now, you'll
need to compile them. See below for compilation instructions.

Once you've got the support Jarfile, you can run the example.class ensuring that
the support jarfile is in your classpath. For example, using the Oracle Java VM,
you would run::

    $ java -XX:-UseSplitVerifier -classpath dist/python-java.jar:. python.example
    Hello, World

The ``-CC:-UseSplitVerifier`` argument is necessary to turn off stack map
verification in Java 7. This could be addressed by computing stack maps
for generated code.

Compiling the support library
-----------------------------

Oracle Java
~~~~~~~~~~~

To compile the Python support libraries for Java (the Oracle JVM)::

    $ ant java

This will create a ``dist`` directory that contains ``python-java.jar``.

Android
~~~~~~~

To compile for Android, you'll need to `download the Android SDK`_. You only
need the standalone SDK (see "Other install options") - you don't have to
download the fully Android Studio if you don't want to.

Once you've downloaded and installed the SDK, create a ``local.properties``
in the top level ``voc`` project directory, containing a single line::

    sdk.dir=<path to SDK>/sdk

You can then run ``ant`` to compile ``dist/python-android.jar``::

    $ ant android

You can then add ``dist/python-android.jar`` to your Android project.

.. _download the Android SDK: https://developer.android.com/sdk/index.html

Documentation
-------------

Documentation for VOC can be found on `Read The Docs`_.

Why "VOC"?
----------

The `Vereenigde Oostindische Compagnie (VOC)`_, or Dutch East India Company,
is often considered the be the world's first multinational corporation. It was
also the first company to issue shares, and facilitate the trading of those
shares. It was granted a 21 year monopoly to carry out trade activities in
Asia, primarily the Spice Islands - the Dutch East Indies. They established a
major trading port at Batavia - now Jakarta, on the island of Java (now part
of Indonesia). As a result of their monopoly, the VOC became an incredibly
valuable company, issuing an 18% annual dividend for almost 200 years.

VOC was... the world's first Enterprise using Java. (rimshot!)

VOC is also a backronym for "Vestigial Output Compiler". Or "Vexing Obtuse
Compiler". Or "Valuable Obscure Compiler". Or "Varigated Ocelot Calibrator".
It's your choice.

.. _Vereenigde Oostindische Compagnie (VOC): https://en.wikipedia.org/wiki/Dutch_East_India_Company

Community
---------

VOC is part of the `BeeWare suite`_. You can talk to the community through:

* `@pybeeware on Twitter`_

* The `BeeWare Users Mailing list`_, for questions about how to use the BeeWare suite.

* The `BeeWare Developers Mailing list`_, for discussing the development of new features in the BeeWare suite, and ideas for new tools for the suite.

Contributing
------------

If you experience problems with VOC, `log them on GitHub`_. If you
want to contribute code, please `fork the code`_ and `submit a pull request`_.

.. _BeeWare suite: http://pybee.org
.. _Read The Docs: http://voc.readthedocs.org
.. _@pybeeware on Twitter: https://twitter.com/pybeeware
.. _BeeWare Users Mailing list: https://groups.google.com/forum/#!forum/beeware-users
.. _BeeWare Developers Mailing list: https://groups.google.com/forum/#!forum/beeware-developers
.. _log them on Github: https://github.com/pybee/voc/issues
.. _fork the code: https://github.com/pybee/voc
.. _submit a pull request: https://github.com/pybee/voc/pulls

