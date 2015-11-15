Contributing to VOC
=======================


If you experience problems with VOC, `log them on GitHub`_. If you want to contribute code, please `fork the code`_ and `submit a pull request`_.

.. _log them on Github: https://github.com/pybee/voc/issues
.. _fork the code: https://github.com/pybee/voc
.. _submit a pull request: https://github.com/pybee/voc/pulls


Setting up your development environment
---------------------------------------

The recommended way of setting up your development envrionment for VOC
is to install a virtual environment, install the required dependencies and
start coding. Assuming that you are using ``virtualenvwrapper``, you only have
to run::

    $ git clone git@github.com:pybee/voc.git
    $ cd voc
    $ mkvirtualenv voc
    # or if you use python2 by default
    # mkvirtualenv -p /usr/bin/python3 voc

VOC uses ``unittest`` for its own test
suite as well as additional helper modules for testing. To install all the
requirements for VOC, you have to run the following commands within your
virutal envrionment::

    $ pip install -e .

Now you are ready to start hacking! Have fun!
