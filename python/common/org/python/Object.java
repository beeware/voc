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


    public org.python.Object __new__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __new__(org.python.types.Type cls);

    // public void __init__();
    //     java.util.List<org.python.Object> args,
    //     java.util.Map<java.lang.String, org.python.Object> kwargs,
    //     java.util.List<org.python.Object> default_args,
    //     java.util.Map<java.lang.String, org.python.Object> default_kwargs
    // );


    public void __del__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public void __del__();


    public org.python.Object __repr__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __repr__();


    public org.python.Object __str__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __str__();


    public org.python.Object __bytes__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __bytes__();


    public org.python.Object __format__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __format__(org.python.Object format);


    public org.python.Object __lt__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __lt__(org.python.Object other);


    public org.python.Object __le__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __le__(org.python.Object other);


    public org.python.Object __eq__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __eq__(org.python.Object other);


    public org.python.Object __ne__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __ne__(org.python.Object other);


    public org.python.Object __gt__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __gt__(org.python.Object other);


    public org.python.Object __ge__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __ge__(org.python.Object other);


    public org.python.Object __hash__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __hash__();


    public org.python.Object __bool__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __bool__();

    /**
     * Section 3.3.2 - Emulating container types
     */

    public org.python.Object __getattribute__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __getattribute__(java.lang.String name);


    public org.python.Object __get__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __get__(org.python.Object instance, org.python.types.Type klass);


    public void __setattr__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public void __setattr__(java.lang.String name, org.python.Object value);


    public void __delattr__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public void __delattr__(java.lang.String name);


    public org.python.Object __dir__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __dir__();

    /**
     * Section 3.3.4 - Customizing instance and subclass checks
     */
    // public org.python.Object __instancecheck__(
    //     java.util.List<org.python.Object> args,
    //     java.util.Map<java.lang.String, org.python.Object> kwargs,
    //     java.util.List<org.python.Object> default_args,
    //     java.util.Map<java.lang.String, org.python.Object> default_kwargs
    // );
    // public org.python.Object __subclasscheck__(
    //     java.util.List<org.python.Object> args,
    //     java.util.Map<java.lang.String, org.python.Object> kwargs,
    //     java.util.List<org.python.Object> default_args,
    //     java.util.Map<java.lang.String, org.python.Object> default_kwargs
    // );

    /**
     * Section 3.3.5 - Emulating callable objects
     */
    // public org.python.Object __call__(
    //     java.util.List<org.python.Object> args,
    //     java.util.Map<java.lang.String, org.python.Object> kwargs,
    //     java.util.List<org.python.Object> default_args,
    //     java.util.Map<java.lang.String, org.python.Object> default_kwargs
    // );

    /**
     * Section 3.3.6 - Emulating container types
     */


    public org.python.Object __len__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __len__();


    public org.python.Object __getitem__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __getitem__(org.python.Object item);

    public void __setitem__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public void __setitem__(org.python.Object item, org.python.Object value);

    public void __delitem__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public void __delitem__(org.python.Object item);


    public org.python.Iterable __iter__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Iterable __iter__();


    public org.python.Iterable __reversed__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Iterable __reversed__();


    public org.python.Object __contains__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __contains__(org.python.Object item);

    /**
     * Section 3.3.7 - Emulating numeric types
     */


    public org.python.Object __add__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __add__(org.python.Object other);

    public org.python.Object __sub__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __sub__(org.python.Object other);

    public org.python.Object __mul__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __mul__(org.python.Object other);

    public org.python.Object __truediv__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __truediv__(org.python.Object other);

    public org.python.Object __floordiv__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __floordiv__(org.python.Object other);

    public org.python.Object __mod__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __mod__(org.python.Object other);

    public org.python.Object __divmod__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __divmod__(org.python.Object other);

    public org.python.Object __pow__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __pow__(org.python.Object other, org.python.Object modulus);
    public org.python.Object __pow__(org.python.Object other);

    public org.python.Object __lshift__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __lshift__(org.python.Object other);

    public org.python.Object __rshift__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __rshift__(org.python.Object other);

    public org.python.Object __and__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __and__(org.python.Object other);

    public org.python.Object __xor__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __xor__(org.python.Object other);

    public org.python.Object __or__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __or__(org.python.Object other);


    public void __iadd__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public void __iadd__(org.python.Object other);

    public void __isub__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public void __isub__(org.python.Object other);

    public void __imul__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public void __imul__(org.python.Object other);

    public void __itruediv__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public void __itruediv__(org.python.Object other);

    public void __ifloordiv__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public void __ifloordiv__(org.python.Object other);

    public void __imod__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public void __imod__(org.python.Object other);


    public org.python.Object __neg__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __neg__();

    public org.python.Object __pos__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __pos__();

    public org.python.Object __abs__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __abs__();

    public org.python.Object __invert__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __invert__();


    public org.python.Object __not__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __not__();

    public org.python.Object __not_contains__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __not_contains__(org.python.Object item);


    public org.python.Object __complex__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __complex__(org.python.Object real, org.python.Object imag);

    public org.python.Object __int__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __int__();

    public org.python.Object __float__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __float__();

    public org.python.Object __round__(
        java.util.List<org.python.Object> args,
        java.util.Map<java.lang.String, org.python.Object> kwargs,
        java.util.List<org.python.Object> default_args,
        java.util.Map<java.lang.String, org.python.Object> default_kwargs
    );
    public org.python.Object __round__(org.python.Object ndigits);
    public org.python.Object __round__();

    // /**
    //  * Section 3.3.8 - With statement context
    //  */
    // public org.python.Object __enter__(
    //     java.util.List<org.python.Object> args,
    //     java.util.Map<java.lang.String, org.python.Object> kwargs,
    //     java.util.List<org.python.Object> default_args,
    //     java.util.Map<java.lang.String, org.python.Object> default_kwargs
    // );
    // public org.python.Object __exit__(org.python.Object exc_type, org.python.Object exc_value, org.python.Object traceback);

}