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

Please remember to replace ``/path/to/voc`` with the actual path to your VOC 
repository (e.g. ``/home/myusername/src/voc-dev/voc``). In case you don't really want 
to do that for some reason, you'll need to
remember to replace ``$VOC_DIR`` with the full VOC directory any time it
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
Ensure you're inside of the correct directory, and make sure to include the correct path to the ``python-java-support.jar`` file and the current directory in the classpath, separated by ``:``.


Extending a Java class
----------------------

For extending a Java class, you will need to use some special syntax.
Here is an example code which creates three Java threads, by
extending the ``java.lang.Thread``::

    from java.lang import Math


    class MyThread(extends=java.lang.Thread):
        def __init__(self, id):
            self.id = id
            self.counter = 0

        def run(self) -> void:
            print('Starting thread %d' % self.id)
            for i in range(10):
                self.sleep(Math.random() * 1000)
                self.counter += 1
                print('Thread %d executed %d times' % (self.id, self.counter))


    MyThread(1).start()
    MyThread(2).start()
    MyThread(3).start()

There are two important syntax features to notice here:

1) Extending a Java class: ``MyThread(extends=java.lang.Thread)``

.. note:: Notice how we provide the full absolute path to the Java class being extended.
    This is required even if you import the class, because of a limitation of the current
    way the transpilation is implemented.

2) Annotating return type for the run() method: ``-> void``. This is needed in order
for the method to be executable from the Java side. In practice, VOC generates two
methods like these: one to be callable from Python code, and the other with the
Java types got from the annotations.

Compiling and running this will give you an output like::

    Starting thread 1
    Starting thread 2
    Starting thread 3
    Thread 3 executed 1 times
    Thread 3 executed 2 times
    Thread 1 executed 1 times
    Thread 3 executed 3 times
    Thread 2 executed 1 times
    Thread 1 executed 2 times
    Thread 3 executed 4 times
    Thread 2 executed 2 times
    Thread 3 executed 5 times
    ...


Example: extending HashMap
~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is another example, showing how to extend a Java class with slightly more
involved type annotations, and calling the parent class method::

    class SpyingHashMap(extends=java.util.HashMap):
        def __init__(self):
            self.counter = 0

        def put(self, key: java.lang.Object, value: java.lang.Object) -> java.lang.Object:
            print('Putting %s in key %s' % (value, key))
            return super().put(key, value)


    m = SpyingHashMap()
    m.put("hello", "it's me")
    m.put("from where?", "the other side")
    print('map entries are:', m.entrySet())

Here again it's important to notice how the type annotations need the full
absolute path for the types.

Compiling and running the above code will give you::

    Putting it's me in key hello
    Putting the other side in key from where?
    map entries are: [hello=it's me, from where?=the other side]


.. TODO:: add an example with custom constructor

Common problems
~~~~~~~~~~~~~~~

1) Forgetting to declare ``self`` as argument for the run method, will give you an error like this::

    Exception in thread "main" java.lang.ClassFormatError:
        Arguments can't fit into locals in class file python/extend_thread/MyThread

If you get the above error, double check that you're declaring the ``self`` as first argument in all methods of the Python classes.


2) Trying to extend a Java interface instead of implementing it, will give you this error::

    Exception in thread "main" java.lang.IncompatibleClassChangeError:
        class python.error_extends.MyThread has interface java.lang.Runnable as super class

If you get the above error, make sure the thing you're trying to extend is a class and not an interface. Look below to see how to implement a Java interface.


Implementing a Java interface
-----------------------------

Implementing a Java interface is similar to extending a Java class: much like in Java,
you simply use ``implements`` instead of ``extends``.

Here is the threads example from earlier, re-written to use a Python class
implementing the Java interface ``java.lang.Runnable``::


    from java.lang import Math, Thread


    class MyThread(implements=java.lang.Runnable):
        def __init__(self, id):
            self.id = id
            self.counter = 0

        def run(self) -> void:
            print('Starting thread %d' % self.id)
            for i in range(10):
                Thread.sleep(Math.random() * 1000)
                self.counter += 1
                print('Thread %d executed %d times' % (self.id, self.counter))


    Thread(MyThread(1)).start()
    Thread(MyThread(2)).start()
    Thread(MyThread(3)).start()



.. _classpath: https://en.wikipedia.org/wiki/Classpath_(Java)
