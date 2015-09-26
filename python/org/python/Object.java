package org.python;

public interface Object {

    /**
     * Return the python name for this class.
     */
    public java.lang.String getPythonName();

    /**
     * Python interface compatibility
     * Section 3.3.1 - Basic customization
     */

    // public void __new__(); {
    // }

    // public void __init__(); {
    // }

    public void __del__();

    public org.python.types.Str __repr__();

    public org.python.types.Str __str__();

    public org.python.types.Bytes __bytes__();

    public org.python.types.Str __format__();

    public org.python.Object __lt__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __lt__(org.python.Object other);

    public org.python.Object __le__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __le__(org.python.Object other);

    public org.python.Object __eq__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __eq__(org.python.Object other);

    public org.python.Object __ne__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __ne__(org.python.Object other);

    public org.python.Object __gt__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __gt__(org.python.Object other);

    public org.python.Object __ge__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __ge__(org.python.Object other);

    public org.python.types.Int __hash__();

    public org.python.types.Bool __bool__();

    /**
     * Section 3.3.2 - Emulating container types
     */
    // The cast back from java Object to Hashtable is, strictly speaking,
    // unchecked, but given we know it's an Object, we know value is a Map.
    public org.python.Object __getattr__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __getattr__(org.python.Object name);
    public org.python.Object __getattr__(java.lang.String name);

    public org.python.Object __getattribute__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __getattribute__(org.python.Object name);
    public org.python.Object __getattribute__(java.lang.String name);

    public void __setattr__(org.python.Object [] args, java.util.Hashtable kwargs);
    public void __setattr__(org.python.Object name, org.python.Object value);
    public void __setattr__(java.lang.String name, org.python.Object value);

    public void __delattr__(org.python.Object [] args, java.util.Hashtable kwargs);
    public void __delattr__(org.python.Object name);
    public void __delattr__(java.lang.String name);

    public org.python.types.List __dir__();

    /**
     * Section 3.3.4 - Customizing instance and subclass checks
     */
    public org.python.Object __instancecheck__(org.python.Object instance);

    public org.python.Object __subclasscheck__(org.python.Object subclass);

    /**
     * Section 3.3.5 - Emulating callable objects
     */
    public org.python.Object __call__(org.python.Object... args);

    /**
     * Section 3.3.6 - Emulating container types
     */

    public org.python.types.Int __len__();

    public org.python.types.Int __length_hint__();

    public org.python.Object __getitem__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __getitem__(org.python.Object index);
    public org.python.Object __getitem__(int index);

    public org.python.Object __missing__(org.python.Object key);

    public void __setitem__(org.python.Object [] args, java.util.Hashtable kwargs);
    public void __setitem__(org.python.Object index, org.python.Object value);
    public void __setitem__(int index, org.python.Object value);

    public org.python.Iterable __iter__();

    public org.python.Iterable __reversed__();

    public org.python.types.Bool __contains__(org.python.Object item);

    /**
     * Section 3.3.7 - Emulating numeric types
     */

    public org.python.Object __add__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __add__(org.python.Object other);

    public org.python.Object __sub__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __sub__(org.python.Object other);

    public org.python.Object __mul__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __mul__(org.python.Object other);

    public org.python.Object __truediv__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __truediv__(org.python.Object other);

    public org.python.Object __floordiv__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __floordiv__(org.python.Object other);

    public org.python.Object __mod__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __mod__(org.python.Object other);

    public org.python.Object __divmod__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __divmod__(org.python.Object other);

    public org.python.Object __pow__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __pow__(org.python.Object other);

    public org.python.Object __lshift__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __lshift__(org.python.Object other);

    public org.python.Object __rshift__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __rshift__(org.python.Object other);

    public org.python.Object __and__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __and__(org.python.Object other);

    public org.python.Object __xor__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __xor__(org.python.Object other);

    public org.python.Object __or__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __or__(org.python.Object other);

    public org.python.Object __radd__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __radd__(org.python.Object other);

    public org.python.Object __rsub__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __rsub__(org.python.Object other);

    public org.python.Object __rmul__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __rmul__(org.python.Object other);

    public org.python.Object __rtruediv__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __rtruediv__(org.python.Object other);

    public org.python.Object __rfloordiv__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __rfloordiv__(org.python.Object other);

    public org.python.Object __rmod__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __rmod__(org.python.Object other);

    public org.python.Object __rdivmod__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __rdivmod__(org.python.Object other);

    public org.python.Object __rpow__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __rpow__(org.python.Object other);

    public org.python.Object __rlshift__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __rlshift__(org.python.Object other);

    public org.python.Object __rrshift__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __rrshift__(org.python.Object other);

    public org.python.Object __rand__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __rand__(org.python.Object other);

    public org.python.Object __rxor__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __rxor__(org.python.Object other);

    public org.python.Object __ror__(org.python.Object [] args, java.util.Hashtable kwargs);
    public org.python.Object __ror__(org.python.Object other);

    public void __iadd__(org.python.Object [] args, java.util.Hashtable kwargs);
    public void __iadd__(org.python.Object other);

    public void __isub__(org.python.Object [] args, java.util.Hashtable kwargs);
    public void __isub__(org.python.Object other);

    public void __imul__(org.python.Object [] args, java.util.Hashtable kwargs);
    public void __imul__(org.python.Object other);

    public void __itruediv__(org.python.Object [] args, java.util.Hashtable kwargs);
    public void __itruediv__(org.python.Object other);

    public void __ifloordiv__(org.python.Object [] args, java.util.Hashtable kwargs);
    public void __ifloordiv__(org.python.Object other);

    public void __imod__(org.python.Object [] args, java.util.Hashtable kwargs);
    public void __imod__(org.python.Object other);

    public void __ipow__(org.python.Object [] args, java.util.Hashtable kwargs);
    public void __ipow__(org.python.Object other);

    public void __ilshift__(org.python.Object [] args, java.util.Hashtable kwargs);
    public void __ilshift__(org.python.Object other);

    public void __irshift__(org.python.Object [] args, java.util.Hashtable kwargs);
    public void __irshift__(org.python.Object other);

    public void __iand__(org.python.Object [] args, java.util.Hashtable kwargs);
    public void __iand__(org.python.Object other);

    public void __ixor__(org.python.Object [] args, java.util.Hashtable kwargs);
    public void __ixor__(org.python.Object other);

    public void __ior__(org.python.Object [] args, java.util.Hashtable kwargs);
    public void __ior__(org.python.Object other);

    public org.python.Object __neg__();
    public org.python.Object __pos__();
    public org.python.Object __abs__();
    public org.python.Object __invert__();

    public org.python.Object __not__();
    public org.python.Object __complex__(org.python.Object [] args, java.util.Hashtable kwargs);

    public org.python.types.Int __int__();
    public org.python.types.Float __float__();
    public org.python.Object __round__();

    /**
     * Section 3.3.8 - With statement context
     */
    public org.python.Object __enter__();
    public org.python.Object __exit__(org.python.Object exc_type, org.python.Object exc_value, org.python.Object traceback);

}