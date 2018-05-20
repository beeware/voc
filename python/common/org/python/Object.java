package org.python;

public interface Object extends Comparable {
    /**
     * Return a Java object that is the underlying data representation
     * of this object (e.g., the java.util.Map behind a Python dict()).
     * If the object is a pure Python object, calling this on an instance
     * returns itself.
     */
    public java.lang.Object toJava();

    /**
     * Return a Java object that is the best representation of the
     * object being manipulated. This is used as the target for function
     * invocation. Python-side objects will return themselves; Wrapped
     * Java objects will return the wrapped object.
     */
    public java.lang.Object toObject();

    /**
     * Return the Python boolean interpretation of the object. This is
     * used when the object is the subject of a logical comparison.
     */
    public boolean toBoolean();

    /**
     * Return the Python type for this object.
     */
    public org.python.types.Type type();

    /**
     * Return the Python type name for this object.
     */
    public java.lang.String typeName();

    /**
     * Return a version of the object that can be used when returning by
     * value. For most objects, this will be itself; but primitive types
     * need to return a copy of themselves to ensure that they aren't
     * modified.
     */
    public org.python.Object byValue();

    /**
     * Python interface compatibility
     * Section 3.3.1 - Basic customization
     */

    public org.python.Object __new__(org.python.Object cls);

    // public void __init__();

    public void __del__();

    public org.python.Object __repr__();
    public org.python.Object __str__();

    public org.python.Object __bytes__();
    public org.python.Object __format__(org.python.Object format);

    public org.python.Object __lt__(org.python.Object other);
    public org.python.Object __le__(org.python.Object other);
    public org.python.Object __eq__(org.python.Object other);
    public org.python.Object __ne__(org.python.Object other);
    public org.python.Object __gt__(org.python.Object other);
    public org.python.Object __ge__(org.python.Object other);

    public org.python.Object __hash__();

    public org.python.Object __bool__();

    /**
     * Section 3.3.2 - Emulating container types
     */

    // These four methods are the internal implementations of
    // attribute manipulation. They return null/false in case of
    // failure; that failure is then interpreted by the public
    // interface method.
    public org.python.Object __getattr_null(java.lang.String name);
    public org.python.Object __getattribute_null(java.lang.String name);
    public boolean __setattr_null(java.lang.String name, org.python.Object value);
    public boolean __delattr_null(java.lang.String name);

    // These four methods implement the internal interface to
    // attribute manipulation. This means they accept raw Java strings
    // as attribute names, and they raise exceptions on failure.
    // These are the methods that are invoked by VOC-generated code.
    public org.python.Object __getattr__(java.lang.String name);
    public org.python.Object __getattribute__(java.lang.String name);
    public void __setattr__(java.lang.String name, org.python.Object value);
    public void __delattr__(java.lang.String name);

    // Lastly, these methods are the public inteface to attribute
    // manipulation. This means they take Python objects as attributes,
    // and raise exceptions on failure.
    public org.python.Object __getattr__(org.python.Object name);
    public org.python.Object __getattribute__(org.python.Object name);
    public void __setattr__(org.python.Object name, org.python.Object value);
    public void __delattr__(org.python.Object name);

    // These are the prototypes for the descriptor protocol.
    public org.python.Object __get__(org.python.Object instance, org.python.Object klass);
    public void __set__(org.python.Object instance, org.python.Object value);
    public void __delete__(org.python.Object instance);

    // Attribute name retrieval.
    public org.python.Object __dir__();

    /**
     * Section 3.3.4 - Customizing instance and subclass checks
     */
    // public org.python.Object __instancecheck__();
    // public org.python.Object __subclasscheck__();

    /**
     * Section 3.3.5 - Emulating callable objects
     */
    // public org.python.Object __call__();

    /**
     * Section 3.3.6 - Emulating container types
     */

    public org.python.Object __len__();
    public org.python.Object __getitem__(org.python.Object item);
    public void __setitem__(org.python.Object item, org.python.Object value);
    public void __delitem__(org.python.Object item);
    public org.python.Object __iter__();
    public org.python.Object __reversed__();
    public org.python.Object __contains__(org.python.Object item);

    public org.python.Object __next__();

    /**
     * Section 3.3.7 - Emulating numeric types
     */

    public org.python.Object __add__(org.python.Object other);
    public org.python.Object __sub__(org.python.Object other);
    public org.python.Object __mul__(org.python.Object other);
    public org.python.Object __truediv__(org.python.Object other);
    public org.python.Object __floordiv__(org.python.Object other);
    public org.python.Object __mod__(org.python.Object other);
    public org.python.Object __divmod__(org.python.Object other);
    public org.python.Object __pow__(org.python.Object other, org.python.Object modulus);
    public org.python.Object __lshift__(org.python.Object other);
    public org.python.Object __rshift__(org.python.Object other);
    public org.python.Object __and__(org.python.Object other);
    public org.python.Object __xor__(org.python.Object other);
    public org.python.Object __or__(org.python.Object other);

    public org.python.Object __iadd__(org.python.Object other);
    public org.python.Object __isub__(org.python.Object other);
    public org.python.Object __imul__(org.python.Object other);
    public org.python.Object __itruediv__(org.python.Object other);
    public org.python.Object __ifloordiv__(org.python.Object other);
    public org.python.Object __imod__(org.python.Object other);
    public org.python.Object __idivmod__(org.python.Object other);
    public org.python.Object __ipow__(org.python.Object other);
    public org.python.Object __ilshift__(org.python.Object other);
    public org.python.Object __irshift__(org.python.Object other);
    public org.python.Object __iand__(org.python.Object other);
    public org.python.Object __ixor__(org.python.Object other);
    public org.python.Object __ior__(org.python.Object other);

    public org.python.Object __neg__();
    public org.python.Object __pos__();
    public org.python.Object __abs__();
    public org.python.Object __invert__();

    public org.python.Object __not__();
    public org.python.Object __not_contains__(org.python.Object item);

    public org.python.Object __complex__(org.python.Object real, org.python.Object imag);
    public org.python.Object __int__();
    public org.python.Object __float__();
    public org.python.Object __round__(org.python.Object ndigits);

    public org.python.Object __index__();

    // /**
    //  * Section 3.3.8 - With statement context
    //  */
    // public org.python.Object __enter__();
    // public org.python.Object __exit__(org.python.Object exc_type, org.python.Object exc_value, org.python.Object traceback);
}
