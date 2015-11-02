package org.python.exceptions;

@org.python.Class(
    __doc__ = "Common base class for all exceptions"
)
public class BaseException extends java.lang.RuntimeException implements org.python.Object {

    public BaseException() {
        super();
    }

    public BaseException(String msg) {
        super(msg);
    }

    /**
     * Proxy Java object methods onto their Python counterparts.
     */

    // @SuppressWarnings("unchecked")
    public boolean equals(java.lang.Object other) {
        try {
            return ((org.python.types.Bool) __eq__((org.python.types.Object) other)).value;
        } catch (ClassCastException e) {
            throw new org.python.exceptions.RuntimeError("Can't compare a Python object with non-Python object.");
        }
    }

    public int compareTo(java.lang.Object other) {
        try {
            if (((org.python.types.Bool) this.__lt__((org.python.types.Object) other)).value) {
                return -1;
            }
            else if (((org.python.types.Bool) this.__gt__((org.python.types.Object) other)).value) {
                return 1;
            }
            return 0;
        } catch (ClassCastException e) {
            throw new org.python.exceptions.RuntimeError("Can't compare a Python object with non-Python object.");
        }
    }

    public String toString() {
        return (String) __str__().value;
    }

    // protected void finalize() throws Throwable {
    //     try {
    //         // this.__del__();
    //     }
    //     finally {
    //         super.finalize();
    //     }
    // }

    /**
     * Python interface compatibility
     * Section 3.3.1 - Basic customization
     */
    // @org.python.Method(
    //     __doc__ = "Create and return a new object.  See help(type) for accurate signature."
    // )
    // public void __new__() {
    //     throw new org.python.exceptions.AttributeError(this, "__new__");
    // }
    public org.python.types.Type __new__(org.python.types.Type cls) {
        return cls;
    }

    // @org.python.Method(
    //     __doc__ = "Initialize self.  See help(type(self)) for accurate signature."
    // )
    // public void __init__() {
    //     throw new org.python.exceptions.AttributeError(this, "__init__");
    // }

    // public void __del__() {
    //     throw new org.python.exceptions.AttributeError(this, "__del__");
    // }

    @org.python.Method(
        __doc__ = "Return repr(self)."
    )
    public org.python.Object __repr__(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __repr__ doesn't take keyword arguments");
        }
        if (args.length == 0) {
            return this.__repr__();
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 0 arguments, got " + args.length);
        }
    }

    public org.python.types.Str __repr__() {
        return new org.python.types.Str(super.toString());
    }

    @org.python.Method(
        __doc__ = "Return str(self)."
    )
    public org.python.Object __str__(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __str__ doesn't take keyword arguments");
        }
        if (args.length == 0) {
            return this.__str__();
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 0 arguments, got " + args.length);
        }
    }

    public org.python.types.Str __str__() {
        return this.__repr__();
    }

    public org.python.types.Bytes __bytes__() {
        throw new org.python.exceptions.AttributeError(this, "__bytes__");
    }

    public org.python.types.Str __format__(org.python.Object value) {
        throw new org.python.exceptions.NotImplementedError("'" + org.Python.pythonTypeName(this) + ".__format__' has not been implemented");
    }

    public org.python.types.Str __format__(org.python.Object value, org.python.Object format_spec) {
        throw new org.python.exceptions.NotImplementedError("'" + org.Python.pythonTypeName(this) + ".__format__' has not been implemented");
    }

    @org.python.Method(
        __doc__ = "Return self<value."
    )
    public org.python.Object __lt__(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __lt__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__lt__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __lt__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("'" + org.Python.pythonTypeName(this) + ".__lt__' has not been implemented");
    }


    @org.python.Method(
        __doc__ = "Return self<=value."
    )
    public org.python.Object __le__(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __le__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__le__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __le__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("'" + org.Python.pythonTypeName(this) + ".__le__' has not been implemented");
    }

    @org.python.Method(
        __doc__ = "Return self==value."
    )
    public org.python.Object __eq__(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __eq__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__eq__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __eq__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("'" + org.Python.pythonTypeName(this) + ".__eq__' has not been implemented");
    }

    @org.python.Method(
        __doc__ = "Return self!=value."
    )
    public org.python.Object __ne__(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __ne__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__ne__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __ne__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("'" + org.Python.pythonTypeName(this) + ".__ne__' has not been implemented");
    }

    @org.python.Method(
        __doc__ = "Return self>value."
    )
    public org.python.Object __gt__(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __gt__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__gt__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __gt__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("'" + org.Python.pythonTypeName(this) + ".__gt__' has not been implemented");
    }

    @org.python.Method(
        __doc__ = "Return self>=value."
    )
    public org.python.Object __ge__(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __ge__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            return this.__ge__(args[0]);
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public org.python.Object __ge__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("'" + org.Python.pythonTypeName(this) + ".__ge__' has not been implemented");
    }

    @org.python.Method(
        __doc__ = "Return hash(self)."
    )
    public org.python.types.Int __hash__(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __hash__ doesn't take keyword arguments");
        }
        if (args.length == 0) {
            return this.__hash__();
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 0 arguments, got " + args.length);
        }
    }

    public org.python.types.Int __hash__() {
        return new org.python.types.Int(this.hashCode());
    }

    public org.python.types.Bool __bool__() {
        throw new org.python.exceptions.AttributeError(this, "__bool__");
    }


    /**
     * Section 3.3.2 - Emulating container types
     */

    @org.python.Method(
        __doc__ = "Return getattr(self, name)."
    )
    public org.python.Object __getattribute__(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __getattribute__ doesn't take keyword arguments");
        }
        org.python.Object value;
        if (args.length == 1) {
            if (args[0] instanceof org.python.types.Str) {
                value = this.__getattribute__(((org.python.types.Str) args[0]).value);
            } else {
                throw new org.python.exceptions.TypeError("__getattribute__(): attribute name must be string");
            }
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }

        return this.__get__(value, org.python.types.Type.pythonType(this.getClass()));
    }

    public org.python.Object __getattribute__(java.lang.String name) {
        throw new org.python.exceptions.NotImplementedError("'" + org.Python.pythonTypeName(this) + ".__getattribute__' has not been implemented");
    }

    public org.python.Object __get__(org.python.Object instance, org.python.types.Type klass) {
        return this;
    }

    @org.python.Method(
        __doc__ = "Implement setattr(self, name, value)."
    )
    public void __setattr__(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __setattr__ doesn't take keyword arguments");
        }
        if (args.length == 2) {
            if (args[0] instanceof org.python.types.Str) {
                this.__setattr__(((org.python.types.Str) args[0]).value, args[1]);
            } else {
                throw new org.python.exceptions.TypeError("delattr(): attribute name must be string");
            }
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 2 arguments, got " + args.length);
        }
    }

    public void __setattr__(java.lang.String name, org.python.Object value) {
        throw new org.python.exceptions.NotImplementedError("'" + org.Python.pythonTypeName(this) + ".__setattr__' has not been implemented");
    }

    @org.python.Method(
        __doc__ = "Implement delattr(self, name)."
    )
    public void __delattr__(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __delattr__ doesn't take keyword arguments");
        }
        if (args.length == 1) {
            if (args[0] instanceof org.python.types.Str) {
                this.__delattr__(((org.python.types.Str) args[0]).value);
            } else {
                throw new org.python.exceptions.TypeError("delattr(): attribute name must be string");
            }
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.length);
        }
    }

    public void __delattr__(java.lang.String name) {
        throw new org.python.exceptions.NotImplementedError("'" + org.Python.pythonTypeName(this) + ".__delattr__' has not been implemented");
    }

    public org.python.types.List __dir__() {
        throw new org.python.exceptions.NotImplementedError("'" + org.Python.pythonTypeName(this) + ".__dir__' has not been implemented");
    }

    /**
     * Section 3.3.4 - Customizing instance and subclass checks
     */
    // public org.python.Object __instancecheck__(org.python.Object instance) {
    //     throw new org.python.exceptions.AttributeError(this, "__instancecheck__");
    // }

    // public org.python.Object __subclasscheck__(org.python.Object subclass) {
    //     throw new org.python.exceptions.AttributeError(this, "__subclasscheck__");
    // }

    /**
     * Section 3.3.5 - Emulating callable objects
     */
    // public org.python.Object __call__(org.python.Object... args) {
    //     throw new org.python.exceptions.AttributeError(this, "__call__");
    // }

    /**
     * Section 3.3.6 - Emulating container types
     */

    public org.python.types.Int __len__() {
        throw new org.python.exceptions.AttributeError(this, "__len__");
    }

    public org.python.Object __getitem__(org.python.Object index) {
        throw new org.python.exceptions.AttributeError(this, "__getitem__");
    }

    public void __setitem__(org.python.Object index, org.python.Object value) {
        throw new org.python.exceptions.AttributeError(this, "__setitem__");
    }

    public void __delitem__(org.python.Object index) {
        throw new org.python.exceptions.AttributeError(this, "__delitem__");
    }


    public org.python.Iterable __iter__() {
        throw new org.python.exceptions.AttributeError(this, "__iter__");
    }

    public org.python.Iterable __reversed__() {
        throw new org.python.exceptions.AttributeError(this, "__reversed__");
    }


    /**
     * Section 3.3.7 - Emulating numeric types
     */

    public org.python.Object __add__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__add__");
    }

    public org.python.Object __sub__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__sub__");
    }

    public org.python.Object __mul__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__mul__");
    }

    public org.python.Object __truediv__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__truediv__");
    }

    public org.python.Object __floordiv__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__floordiv__");
    }

    public org.python.Object __mod__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__mod__");
    }

    public org.python.Object __divmod__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__divmod__");
    }

    public org.python.Object __pow__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__pow__");
    }

    public org.python.Object __pow__(org.python.Object other, org.python.Object modulus) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for ** or pow(): '" + org.Python.pythonTypeName(this) + "', '" + org.Python.pythonTypeName(other) + "', '" + org.Python.pythonTypeName(modulus) + "'");
    }

    public org.python.Object __lshift__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__lshift__");
    }

    public org.python.Object __rshift__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__rshift__");
    }

    public org.python.Object __and__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__and__");
    }

    public org.python.Object __xor__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__xor__");
    }

    public org.python.Object __or__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__or__");
    }


    public void __iadd__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__iadd__");
    }

    public void __isub__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__isub__");
    }

    public void __imul__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__imul__");
    }

    public void __itruediv__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__itruediv__");
    }

    public void __ifloordiv__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__ifloordiv__");
    }

    public void __imod__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__im__");
    }


    public org.python.Object __neg__() {
        throw new org.python.exceptions.AttributeError(this, "__neg__");
    }

    public org.python.Object __pos__() {
        throw new org.python.exceptions.AttributeError(this, "__pos__");
    }

    public org.python.Object __abs__() {
        throw new org.python.exceptions.AttributeError(this, "__abs__");
    }

    public org.python.Object __invert__() {
        throw new org.python.exceptions.AttributeError(this, "__invert__");
    }

    public org.python.Object __not__() {
        throw new org.python.exceptions.AttributeError(this, "__not__");
    }

    public org.python.Object __complex__(org.python.Object real, org.python.Object imag) {
        throw new org.python.exceptions.AttributeError(this, "__complex__");
    }

    public org.python.types.Int __int__() {
        throw new org.python.exceptions.AttributeError(this, "__int__");
    }

    public org.python.types.Float __float__() {
        throw new org.python.exceptions.AttributeError(this, "__float__");
    }

    public org.python.Object __round__() {
        throw new org.python.exceptions.AttributeError(this, "__round__");
    }

    public org.python.Object __round__(org.python.Object ndigits) {
        throw new org.python.exceptions.AttributeError(this, "__round__");
    }


    /**
     * Section 3.3.8 - With statement context
     */
    // public org.python.Object __enter__() {
    //     throw new org.python.exceptions.AttributeError(this, "__enter__");
    // }

    // public org.python.Object __exit__(org.python.Object exc_type, org.python.Object exc_value, org.python.Object traceback) {
    //     throw new org.python.exceptions.AttributeError(this, "__exit__");
    // }
}
