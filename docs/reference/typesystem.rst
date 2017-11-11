The VOC type system
===================

VOC works by operating on a layer of "Python-like" objects. A Python-like
object is any object that implements the ``org.python.Object`` interface. This
interface consists of all the "dunder" methods, like ``__getattr__``,
``__setattr__``, ``__init__``, ``__repr__`` and ``__str__``, that the Python
interpreter might use on a Python object.

The default implementation of ``org.python.Object`` is
``org.python.types.Object``. This is the VOC representation of the base Object
class. As any Python object can be thrown as an exception,
``org.python.types.Object`` extends ``java.lang.RuntimeException``.

The Python ``dict`` builtin type is implemented in the class
``org.python.types.Dict``. This class is a subclass of
``org.python.types.Object``. All methods and attributes of a Python ``dict``
are implemented as instance methods and attributes of this class.

The Python builtin type ``type`` is implemented as ``org.python.types.Type``,
which is *also* a subclass of ``org.python.types.Object``. Instances of
``org.python.types.Type`` contain a reference to the Java class that instances
of that Python type will be constructed from. As a result, instances of
``org.python.types.Type`` can be invoked as a function to create instances of
the class wrapped by the type. All instances of Python-like objects can be
interrogated for their type.  There will only be one instance of
``org.python.types.Type`` for any given Python-like object.

So - there is an instance of ``org.python.types.Type`` that refers to
``org.python.types.Dict``; and all instances of ``org.python.types.Dict``
contain a reference of that ``org.python.types.Type`` instance. The
``org.python.types.Type`` instance referring to ``org.python.types.Dict``
(which will be indexed as ``"dict"``) can be invoked to create new
``org.python.types.Dict`` instances.

Type origins
------------

VOC Types are classified according to their origin. There are four possible
origins for a type:

* Builtin types
* Python types
* Java types
* Extension types

Builtin Types
~~~~~~~~~~~~~

These are data types built into the VOC support library. All the basic Python
types like ``dict`` and ``list`` are Builtin types. The standard Python
exceptions are also builtin types.

Python instance attributes are stored on the Java instance. When storing
instance attributes, VOC will look for a Field on the Java class that
matches the name of the Python attribute; if one exists, and it has been
annotated in the Java source with a ``@org.python.Attribute`` annotation,
that field will be used for storage. Otherwise, the value will be placed in
the `__dict__` for the instance.

Python instance methods are instance methods on the Java class, with
prototypes that match Python name-for-name, excluding the ``self`` argument,
which will be implicitly added. ``*args`` is mapped to ``org.python.Object []
args``, and ``**kwargs`` to ``java.util.Map<java.lang.String,
org.python.Object> kwargs``. Arguments with default values should be passed in
as ``null`` (a Java ``null``, not a Python ``None``); the method
implementation is then responsible for substituting an appropriate Python
value if a null was provided in the argument list.

* Each Object class has a static `__class__` attribute, which is an instance
* of ``org.python.types.Type()``, constructed wrapping the Java class
* implementing instances of the Python instances of that type. This type can
* be retrieved by calling the `type()` method on the Java instance (which is
* part of the ``org.python.Object`` interface)


Python Types
~~~~~~~~~~~~

Python types are types that are declared in Python, extending the base Python
``object`` (either explicitly, implicitly, or as a subclass of a class that is
itself an explicit or implicit subclass of ``object``).

* All Python instance attributes are stored as values in __dict__.

* Python instance methods are rolled out as a pair of methods on the Java class:

  * a static method that takes an extra `self` argument

  * an instance method


Java Types
~~~~~~~~~~

Any object that exists in the Java namespace can be proxied into the Python
environment as a Java Type.

The Java object instance is wrapped in an implementation of
`org.python.java.Object`, which acts as a proxy tying python `__getattr__` and
`__setattr__` to the equivalent reflection methods in Java.


Extension Types
~~~~~~~~~~~~~~~

Extension types are types that have been declared in Python, but extend a Java
type.

Implementation details
----------------------

There are quirks to some of the implemenations of some Python types.

Modules
~~~~~~~

* Implemented in a ``__init__.class`` file, regardless of whether one is
  actually used in the Python source.

* Instance of a class, extending org.python.types.Module

* Registered as sys.modules[modulename]

Class
~~~~~

* Implemented in a <classname>.class file
