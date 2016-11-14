Getting Started
===============

In this guide we will walk you through setting up your VOC environment for
development and testing. We will assume that you have a working Python 3, JDK,
Apache ANT installation and use virtualenv.

The default version apt-get provides on Ubuntu 16.04 is 3.5+ but VOC won't build on Python3.5+. Hence, a separate 
Python 3.4+ installation would be required. 

Checking Dependencies
---------------------

To check if you have Python installed, run ``python --version`` at the command line

.. code-block:: bash

	$ python --version
	Python 3.4.4

To check if you have the JDK installed, run ``javac -version``

.. code-block:: bash

	$ javac -version
	javac 1.7.0_101

To check if Apache ANT is installed, run ``ant -version``

.. code-block:: bash

	$ ant -version
	Apache Ant(TM) version 1.9.7 compiled on April 24 2016


Get a copy of VOC
-----------------

The first step is to create a project directory, and clone VOC:

.. code-block:: bash

    $ mkdir tutorial
    $ cd tutorial
    $ git clone https://github.com/pybee/voc.git

Then create a virtual environment and install VOC into it:

.. code-block:: bash

    $ virtualenv -p $(which python3) env
    $ . env/bin/activate
    $ cd voc
    $ pip install -e .

For Windows the use of cmd under Administrator permission is suggested instead of PowerShell.

.. code-block:: bash

    > virtualenv -p "C:\Python35\python.exe" env
    > env\Scripts\activate.bat
    > cd voc
    > pip install -e .



Building the support JAR file
-----------------------------

Next, you need to build the Python support file:

.. code-block:: bash

    $ ant java

This should create a ``dist/python-java-support.jar`` file. This JAR
file is a support library that implements Python-like behavior and
provides the Python standard library for the Java environment. This
JAR file must be included on the classpath for any VOC-generated
project.

Next Steps
----------

You now have a working VOC environment, so you can :doc:`start the first
tutorial </tutorials/tutorial-0>`.
