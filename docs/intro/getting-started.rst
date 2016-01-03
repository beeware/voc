Getting Started
===============

In this guide we will walk you through setting up your VOC environment for 
development and testing. We will assume that you have a working JDK and
Apache ANT installation and use virtualenv. 

Git a copy of pybee/voc
-----------------------
The first step is to fork voc by going to https://github.com/pybee/voc and 
pressing the fork button at the top. 

You are now ready to clone voc by typing in 

.. code-block:: bash

    git clone https://github.com/YOUR_ACCOUNT/voc.git

Setup VOC
---------
At this point you are ready to setup your isolated voc environment. To do this
you will need to do the following from the root voc directory

.. code-block:: bash

    $ virutalenv -p $(which python3) voc
    $ . voc/bin/activate
    $ pip install -e .


Building The Support Jar File
-----------------------------
The last thing we need to do is build the python support file. This can be done
by typing in the following from the VOC root directory

.. code-block:: bash
    
    $ ant java 
    
This should create a dist/python-java.jar file. This will be used when 
executing the java class that gets compilied. 


Next Steps
----------
At this point you are ready to begin your development. A good next step would 
be to read the `tutorials-0 <https://github.com/pybee/voc/blob/master/docs/tutorials/tutorial-0.rst>`_. 
