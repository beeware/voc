Setting up your development environment
=======================================

The process of setting up a development environment is very similar to
the :doc:`/background/install` process. The biggest difference is that
instead of using the official BeeWare repository, you'll be using your own
Github fork.

As with the getting started guide, these instructions will assume that you
have Python 3.4+, a Java >=7 JDK, and Apache ANT installed.

**Note:** If you are on Linux, you will need to install an extra package to be able to run the test suite.
 * **Ubuntu** 12.04 and 14.04: ``libpython3.4-testsuite`` This can be done by running ``apt-get install libpython3.4-testsuite``.
 * **Ubuntu** 16.04 and 16.10: ``libpython3.5-testsuite`` This can be done by running ``apt-get install libpython3.5-testsuite``.
 * **Ubuntu** 18.04: ``libpython3.6-testsuite`` This can be done by running ``apt-get install libpython3.6-testsuite``.

Start by forking VOC into your own Github repository; then
check out your fork to your own computer into a development directory:

.. code-block:: bash

    $ mkdir voc-dev
    $ cd voc-dev
    $ git clone git@github.com:<your github username>/voc.git

Then create a virtual environment and install VOC into it:

.. code-block:: bash

    $ python3 -m venv env
    $ . env/bin/activate
    $ cd voc
    $ pip install -e .

For Windows the use of cmd under Administrator permission is suggested instead of PowerShell.

.. code-block:: batch

    > py -3 -m venv env
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

Running the full test suite will take quite a while - it takes 40 minutes on
the CI server. You can speed this up by running the tests in parallel via
pytest:

.. code-block:: bash

    $ pip install -r requirements/tests.txt
    $ py.test -n auto

You can specify the number of cores to utilize, or use ``auto`` as shown above
to use all available cores.

If you just want to run a single test, or a single group of tests, you can
provide command-line arguments.

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

Or you can use Cricket, a GUI tool for running test suites. To start cricket in the background:

.. code-block:: bash

    $ pip install -r requirements/tests.txt
    $ cricket-unittest &

This should open a GUI window that lists all the tests. From there you can "Run
all" or select specific tests and "Run selected."

Running the code style checks
-----------------------------

Before sending your pull request for review, you may want to run the style
checks locally.

These checks also run automatically in Travis, but you will avoid unnecessary
waiting time if you do this beforehand and fix your code to follow the style
rules.

In order to do that, first you need to install flake8::

    pip install flake8

Then, whenever you want to run the checks, run the following command inside the
project's directory::

    flake8 && ant checkstyle
