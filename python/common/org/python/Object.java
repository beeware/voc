package org.python;


public interface Object {
    /**
     * Extract a Java object that is the underlying representation
     * of this object (e.g., the java.util.Map behind a Python dict())
     */
    public java.lang.Object toJava();

    /**
     * Return the Python type name for this object.
     */
    public java.lang.String typeName();

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
    public org.python.Object __getattr__(java.lang.String name);
    public org.python.Object __getattribute__(java.lang.String name);
    public void __set__(org.python.Object instance, org.python.Object value);
    public void __setattr__(java.lang.String name, org.python.Object value);
    public void __delattr__(java.lang.String name);

    // Lastly, these methods are the public inteface to attribute
    // manipulation. This means they take Python objects as attributes,
    // and raise exceptions on failure.
    public org.python.Object __get__(org.python.Object instance, org.python.Object klass);
    public org.python.Object __getattr__(org.python.Object name);
    public org.python.Object __getattribute__(org.python.Object name);
    public void __setattr__(org.python.Object name, org.python.Object value);
    public void __delattr__(org.python.Object name);

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
    // public org.python.Object __call__(
    // );

    /**
     * Section 3.3.6 - Emulating container types
     */

    public org.python.Object __len__();
    public org.python.Object __getitem__(org.python.Object item);
    public void __setitem__(org.python.Object item, org.python.Object value);
    public void __delitem__(org.python.Object item);
    public org.python.Iterable __iter__();
    public org.python.Iterable __reversed__();
    public org.python.Object __contains__(org.python.Object item);

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

    public void __iadd__(org.python.Object other);
    public void __isub__(org.python.Object other);
    public void __imul__(org.python.Object other);
    public void __itruediv__(org.python.Object other);
    public void __ifloordiv__(org.python.Object other);
    public void __imod__(org.python.Object other);

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

    // /**
    //  * Section 3.3.8 - With statement context
    //  */
    // public org.python.Object __enter__();
    // public org.python.Object __exit__(org.python.Object exc_type, org.python.Object exc_value, org.python.Object traceback);
}