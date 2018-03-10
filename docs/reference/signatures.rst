Python signatures for Java-defined methods
==========================================

In essence, a method is not much different from a Java method. One defines a
method as follows. Here is a simple example of a 1-argument function.

.. code-block:: java

    @org.python.Method(
        __doc__ = "foobar(fizz) -> buzz" +
            "\n" +
            "Return the foobarified version of fizz.\n",
        args = {"fizz"}
    )
    public function org.python.Object foobar(org.python.Object fizz) {
        return buzz;
    }

The ``org.python.Method`` creates an annotation on the method. Allowable values
are

**name**
    The name of the method. If not specifies, uses reflection to get the name.
**__doc__**
    The documentation string of the method.
**args**
    An array of argument names.
**varargs**
    The name of the argument that should get all other values.
**default_args**
    An array of argument names that get "default" values.  The handling of the
    default values should be done by checking the argument null`
**kwonlyargs**
    An array of arguments that may only be supplied as a
    keyword argument.
**kwargs**
    A name of the argument that recieves the keyword arguments.

Examples
--------

Because examples speak clearer than a thousand words.

A function with no arguments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is a sample of a function always returning the same value. Since it has
no arguments, there is no need to supply any of the named

.. code-block:: python

    def constant_4():
        """Return 4, always and ever."""
        return 4

.. code-block:: java

    @org.python.Method(
        __doc__ = "Return 4, always and ever."
    )
    public org.python.Object constant_4() {
        return org.python.types.Int(4);
    }


A function with two arguments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Another simple function is that of adding two given numbers.

.. code-block:: python

    def add(num1, num2):
        """Add two numbers."""
        return num1 + num2

.. code-block:: java

    @org.python.Method(
        __doc__ = "Add two numbers.",
        args = {"num1", "num2"}
    )
    public org.python.Object add(org.python.Object num1, org.python.Object num2) {
        // Left as exercise for the reader.
    }


A function with a default argument
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Similarly, we might want to make the second argument optional, allowing you
to either add ``1`` to the number, or the supplied argument.

.. code-block:: python

    def inc(num, delta=1):
        """Increment a number."""
        return num + delta

.. code-block:: java

    @org.python.Method(
        __doc__ = "Add two numbers.",
        args = {"num"},
        default_args = {"delta"}
    )
    public org.python.Object inc(org.python.Object num, org.python.Object delta) {
        if (delta == null) {
            delta = new org.python.types.Int(1);
        }
        // Left as exercise for the reader.
    }


A function with variable arguments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Of course, sometimes you don't want to specify a specific number of arguments,
but accept as many as you can get. For instance, the ``min`` function.

.. code-block:: python

    def min(first, *others):
        """Get the minimum of the supplied arguments."""
        val = first
        for other in others:
            if other < val:
                val = other
        return val

.. code-block:: java

    @org.python.Method(
        __doc__ = "Get the minimum of the supplied arguments.""",
        args = {"first"},
        varargs = "others"
    )
    public org.python.Object min(org.python.Object first, org.python.types.Tuple others) {
        org.python.Object val = first;
        for (org.python.Object other: others) {
            if (other.__lt__(val)) {
                val = other;
            }
        }
        return val;
    }

A function accepting keyword arguments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    def loop_kwargs(**kwargs):
        """Loop over the kwargs to this function."""
        for k in kwargs:
          pass

.. code-block:: java

    @org.python.Method(
        __doc__ = "Loop over the kwargs to this function.",
        args = {},
        kwargs = "kwargs"
    )
    public org.python.Object loop_kwargs(org.python.types.Dict kwargs) {
        Map<org.python.Object, org.python.Object> kwargValues = kwargs.value;
        for (org.python.Object key : kwargValues.keySet()) {
          // The keys will always be python Str objects
          org.python.types.Str keyStr = (org.python.types.Str) key;
        }
        return org.python.types.NoneType.NONE;
    }
