Contributing to VOC's code
==========================

In the following instructions, we're going to assume you’re familiar with
Github and making pull requests. We're also going to assume some entry level
Python and Java; if anything we describe here doesn’t make sense, don’t
worry - we're more than happy to fill in the gaps. At this point, we don’t know
what you don’t know!

This tutorial is also going to focus on code contributions. If your interests
and skills are in documentation, :doc:`we have a separate contributors guide
<contribute-docs>` just for you.

Do the tutorial first!
----------------------

Before you make your first contribution, take VOC for a spin. The
instructions in the :doc:`getting started guide </tutorial/tutorial-0>` *should*
be enough to get going. If you get stuck, that points to your first
contribution - work out what instructions would have made you *not* get stuck,
and contribute an update to the README.

Set up your development environment
-----------------------------------

Having run the tutorial, you need to :doc:`set up your environment for VOC
development <development-env>`. The VOC development environment is very
similar to the tutorial environment, but you'll be using your own fork of
VOC's source code, rather than the official repository.

Your first contribution
------------------------

In order to make Java bytecode behave like Python, VOC needs to implement all
the eccentricities of Python behavior. For example, Python allows you to
multiply a string by an integer, resulting in a duplicated string (e.g., ``
“foo” * 3`` => ``“foofoofoo”``). This *isn’t* legal Java, however; Javas
behavior can be quite different to Python, depending on circumstances - so we
need to provide a library that reproduces the desired Python behavior in
Java.

This includes:

 * all the basic operators for Python datatypes (e.g., add, multiply, etc)

 * all the basic methods that can be invoked on Python datatypes (e.g.,
   ``list.sort()``

 * all the pieces of the Python standard library that are written in C

As you might imagine, this means there's lots of work to be done! If you're
looking for something to implement for your first contribution, here's a
few places to look:

 * Compare the list of methods implemented in Javas with the list
   of methods that are available at the Python prompt. If there's a method
   missing, try adding that method.

 * Look through the Java source code looking for ``NotImplementedError``.
   Any method with an existing prototype where the Javas implementation
   raises ``NotImplementedError`` indicates the method is either partially or
   completely unimplemented. Try to fill in the gap!

 * Try writing some Python code and running it in Batavia. If the code doesn't
   run as you'd expect, work out why, and submit a pull request!


Contributing tests for checking Standard Library Modules
--------------------------------------------------------

-  The purpose of the Standard Library tests are to ensure that the packages from the
   Python standard library are working within voc.
-  You can check out the status of tests, such as if they exist and if
   they are passing, with the following commands from within the voc
   directory:
-  ``python tools/compile_stdlib.py java --collect-status && python tools/build_stdlib_report.py --html``
-  Check out the resultant ``voc/report.html`` file.

How to create a new test
~~~~~~~~~~~~~~~~~~~~~~~~

-  Create a new python file in the voc/stdlib_tests directory with the name
   ``test_LibraryName``. This test name must match the name of
   the python standard library module you are testing.
-  Import the module that needs testing into the test_LibraryName.py file.
-  Try to instantiate the module as an object and call multiple methods for it.
-  Make sure you have followed the guide at :doc:`/background/install`
-  Compile the test ``voc test_YourTestName``
-  Run the code with
   ``java -cp /YourPath/voc/dist/python-java-support.jar:/YourPath/ python.test_YourTestName``

Test Guidelines
~~~~~~~~~~~~~~~

-  Try to avoid using other libraries.
-  If using other libraries, be careful as they may not be implemented
   yet and this will cause further yak shaving.
-  If the feature is not yet implemented, the tests will fail, but we
   will have some tests for when the feature is implemented and the
   report will be updated. Thanks for contributing!

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
