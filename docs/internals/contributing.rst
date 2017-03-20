Contributing to VOC
=======================


If you experience problems with VOC, `log them on GitHub`_.

If you want to contribute code, please `fork the code`_ and `submit a pull request`_.

If you're a newcomer to the project looking for how to start contributing,
you may find useful the `First Timers Guide`_.

.. _log them on Github: https://github.com/pybee/voc/issues
.. _fork the code: https://github.com/pybee/voc
.. _submit a pull request: https://github.com/pybee/voc/pulls
.. _First Timers Guide: http://pybee.org/contributing/how/first-time/what/voc/

Setting up your development environment
---------------------------------------

The process of setting up a development environment is very similar to
the :doc:`/intro/getting-started` process. The biggest difference is that
instead of using the official PyBee repository, you'll be using your own
Github fork.

As with the getting started guide, these instructions will assume that you
have Python 3.4+, a Java 7 or Java 8 JDK, and Apache ANT installed, and have virtualenv available for use.

**Note:** If you are on Linux, you will need to install an extra package to be able to run the test suite. 
* **Ubuntu** 12.04 and 14.04: ``libpython3.4-testsuite`` This can be done by running ``apt-get install libpython3.4-testsuite``.
* **Ubuntu** 16.04 and 16.10: ``libpython3.5-testsuite`` This can be done by running ``apt-get install libpython3.5-testsuite``.

Start by forking VOC into your own Github repository; then
check out your fork to your own computer into a development directory:

.. code-block:: bash

    $ mkdir voc-dev
    $ cd voc-dev
    $ git clone git@github.com:<your github username>/voc.git

Then create a virtual environment and install VOC into it:

.. code-block:: bash

    $ virtualenv -p $(which python3) env
    $ . env/bin/activate
    $ cd voc
    $ pip install -e .

For Windows the use of cmd under Administrator permission is suggested instead of PowerShell.

.. code-block:: batch

    > virtualenv -p "C:\Python34\python.exe" env
    > env\Scripts\activate.bat
    > cd voc
    > pip install -e .

You're now ready to run the test suite!

Running the test suite
----------------------

To run the entire test suite, type:

.. code-block:: bash

    $ python setup.py test

To capture unexpected successes and new failures in test:

.. code-block:: bash

    $ python setup.py test 2>&1 | grep -E 'success|FAIL'

Running the full test suite will take quite a while - it takes 40 minutes on the CI server. You can speed this up by running the tests in parallel via pytest:

.. code-block:: bash

    $ pip install -r requirements/tests.txt
    $ py.test -n auto

You can specify the number of cores to utilize, or use ``auto`` as shown above to use all available cores.

If you just want to run a single test, or a single group of tests, you can provide command-line arguments.

To run a single test, provide the full dotted-path to the test:

.. code-block:: bash

    $ python setup.py test -s tests.datatypes.test_str.BinaryStrOperationTests.test_add_bool

To run a full test case, do the same, but stop at the test case name:

.. code-block:: bash

    $ python setup.py test -s tests.datatypes.test_str.BinaryStrOperationTests

Or, to run all the Str datatype tests:

.. code-block:: bash

    $ python setup.py test -s tests.datatypes.test_str

Or, to run all the datatypes tests:

.. code-block:: bash

    $ python setup.py test -s tests.datatypes


Running the code style checks
-----------------------------

Before sending your pull request for review, you may want to run the style checks locally.

These checks also run automatically in Travis, but you will avoid unnecessary
waiting time if you do this beforehand and fix your code to follow the style
rules.

In order to do that, first you need to install flake8::

    pip install flake8

Then, whenever you want to run the checks, run the following command inside the
project's directory::

    flake8 && ant checkstyle


Working with code for Java bytecode
-----------------------------------

If you find yourself needing to work with the parts of VOC that generates Java bytecode,
you might find helpful these pointers:

* `A Python interpreter written in Python`_ will get you started on how stack based
  machines work. While the examples aren't for the JVM, the workings of the machines
  are similar enough to help you get used to the thinking.

* The `Java bytecode instructions` are represented by classes in :py:mod:`voc.java.opcodes`
  that inherit from :py:class:`voc.java.opcodes.Opcode`.
  Most of the code to generate bytecode is in the :py:mod:`voc.python.ast` module, and
  the bytecode generating code is often a sequence of instances of these
  opcode classes calling the method :py:meth:`~voc.python.blocks.Accumulator.add_opcodes`
  for the current context.

* The :py:meth:`~voc.python.blocks.Accumulator.add_opcodes` method also support helpers that work
  as pseudo-instructions, which allow to generate more complex sequences of instructions,
  like the ``IF()``, ``TRY()``, ``CATCH()`` from the :py:mod:`voc.voc.python.structures` module.
  It's easier to understand how these work finding an example of usage in VOC itself.
  Ask in Gitter, if you need help with it.

Troubleshooting generated bytecode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Troubleshooting issues in the generated bytecode can be a bit hard.

There are some tools that can help you to see what's going on.
You can use a tool available in the `ASM`_ project to check the bytecode for problems.

Download the ASM binary distribution from the `ASM`_ project, extract the file in
some directory and create a script like this::

    ASM_VERSION=5.2
    ASM_HOME=/path/to/asm-${ASM_VERSION}/lib

    [ -n "$2" ] || { echo "Usage: $(basename $0) CLASSPATH CLASS_TO_ANALYSE"; exit 1; }

    asm_file="$ASM_HOME/asm-${ASM_VERSION}.jar"
    [ -f "$asm_file" ] ||  { echo "Couldn't find file $asm_file"; exit 1; }

    classpath=$1
    class_to_analyse=$2

    java -cp "$ASM_HOME/asm-${ASM_VERSION}.jar:$ASM_HOME/asm-tree-${ASM_VERSION}.jar:$ASM_HOME/asm-analysis-${ASM_VERSION}.jar:$ASM_HOME/asm-util-${ASM_VERSION}.jar:$classpath" org.objectweb.asm.util.CheckClassAdapter $class_to_analyse

Then you can call it like::

    asm.sh /PATH/TO/voc/dist/python-java-support.jar:. path.to.JavaClass

This will give you a brief diagnosis of problems found in the bytecode for the given
Java class, and if possible will print a friendlier version of the bytecode.

If you just want to see a human friendly version of the Java bytecode
to double check the generated code, you can also try the command::

    javap -c path.to.JavaClass

.. _A Python interpreter written in Python: http://www.aosabook.org/en/500L/a-python-interpreter-written-in-python.html
.. _Java bytecode instructions: https://en.wikipedia.org/wiki/Java_bytecode_instruction_listings
.. _ASM: http://asm.ow2.org/download/index.html
