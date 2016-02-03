Contributing to VOC
=======================


If you experience problems with VOC, `log them on GitHub`_. If you want to contribute code, please `fork the code`_ and `submit a pull request`_.

.. _log them on Github: https://github.com/pybee/voc/issues
.. _fork the code: https://github.com/pybee/voc
.. _submit a pull request: https://github.com/pybee/voc/pulls


Setting up your development environment
---------------------------------------

The process of setting up a development environment is very similar to
the :doc:`/intro/getting-started` process. The biggest difference is that
instead of using the official PyBee repository, you'll be using your own
Github fork .

As with the getting started guide, these instructions will assume that you
have Python3, a Java 7 or Java 8 JDK, and Apache ANT installed, and have virtualenv available for use.

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
    $ pip install -e .

You're now ready to run the test suite!

Running the test suite
----------------------

To run the entire test suite, type:

.. code-block:: bash

    $ cd voc
    $ python setup.py test

This will take quite a while - it takes 40 minutes on the CI server. If you just want to run a single test, or a single group of tests, you can provide command-line arguments.

To run a single test, provide the full dotted-path to the test:

.. code-block:: bash

    $ python setup.py test -s tests.datatypes.test_str.BinaryStrOperationTests.test_add_bool

To run a full test case, do the same, but stop at the test case name:

.. code-block:: bash

    $ python setup.py test -s tests.datatypes.test_str.BinaryStrOperationTests

Or, to run all the Str datatype tests:

    $ python setup.py test -s tests.datatypes.test_str

Or, to run all the datatypes tests:

    $ python setup.py test -s tests.datatypes

