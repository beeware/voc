package org.python.exceptions;

@org.python.Class(
    __doc__ = "Common base class for all exceptions"
)
public class BaseException extends java.lang.RuntimeException implements org.python.Object {

    public BaseException() {
        super();
        // System.out.println("EX: " + this);
    }

    public BaseException(String msg) {
        super(msg);
        // System.out.println("EX: " + this);
    }

    public BaseException(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args[0].toString());
    }

    public java.lang.Object toJava() {
        return this;
    }

    public java.lang.Object toObject() {
        return this;
    }

    public org.python.Object byValue() {
        return this;
    }

    public java.lang.String typeName() {
        return org.Python.typeName(this.getClass());
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
    @org.python.Method(
        __doc__ = "Create and return a new object.  See help(type) for accurate signature."
    )
    public org.python.Object __new__(org.python.Object cls) {
        return (org.python.types.Type) cls;
    }

    // @org.python.Method(
    //     __doc__ = "Initialize self.  See help(type(self)) for accurate signature."
    // )
    // public void __init__() {
    //     throw new org.python.exceptions.AttributeError(this, "__init__");
    // }


    @org.python.Method(
        __doc__ = "Return del(self)."
    )
    public void __del__() {
        throw new org.python.exceptions.AttributeError(this, "__del__");
    }

    @org.python.Method(
        __doc__ = "Return repr(self)."
    )
    public org.python.Object __repr__() {
        return new org.python.types.Str(this.getClass().getSimpleName() + "(\"" + this.getMessage() + "\",)");
    }

    @org.python.Method(
        __doc__ = "Return str(self)."
    )
    public org.python.Object __str__() {
        return new org.python.types.Str(this.getMessage());
    }

    @org.python.Method(
        __doc__ = "Return self<value."
    )
    public org.python.types.Bytes __bytes__() {
        throw new org.python.exceptions.AttributeError(this, "__bytes__");
    }

    @org.python.Method(
        __doc__ = "Return self<value."
    )
    public org.python.types.Str __format__(org.python.Object format_spec) {
        throw new org.python.exceptions.NotImplementedError("'" + this.typeName() + ".__format__' has not been implemented");
    }

    @org.python.Method(
        __doc__ = "Return self<value."
    )
    public org.python.Object __lt__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("'" + this.typeName() + ".__lt__' has not been implemented");
    }

    @org.python.Method(
        __doc__ = "Return self<=value."
    )
    public org.python.Object __le__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("'" + this.typeName() + ".__le__' has not been implemented");
    }

    @org.python.Method(
        __doc__ = "Return self==value."
    )
    public org.python.Object __eq__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("'" + this.typeName() + ".__eq__' has not been implemented");
    }

    @org.python.Method(
        __doc__ = "Return self!=value."
    )
    public org.python.Object __ne__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("'" + this.typeName() + ".__ne__' has not been implemented");
    }

    @org.python.Method(
        __doc__ = "Return self>value."
    )
    public org.python.Object __gt__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("'" + this.typeName() + ".__gt__' has not been implemented");
    }

    @org.python.Method(
        __doc__ = "Return self>=value."
    )
    public org.python.Object __ge__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("'" + this.typeName() + ".__ge__' has not been implemented");
    }

    @org.python.Method(
        __doc__ = "Return hash(self)."
    )
    public org.python.types.Int __hash__() {
        return new org.python.types.Int(this.hashCode());
    }

    @org.python.Method(
        __doc__ = "Return bool(self)."
    )
    public org.python.types.Bool __bool__() {
        throw new org.python.exceptions.AttributeError(this, "__bool__");
    }

    /**
     * Section 3.3.2 - Emulating container types
     */
    @org.python.Method(
        __doc__ = "Return getattr(self, name)."
    )
    public org.python.Object __getattr__(org.python.Object name) {
        try {
            return this.__getattr__(((org.python.types.Str) name).value);
        } catch (java.lang.ClassCastException e) {
            throw new org.python.exceptions.TypeError("__getattr__(): attribute name must be string");
        }
    }

    public org.python.Object __getattr__(java.lang.String name) {
        org.python.Object value = this.__getattr_null(name);
        if (value == null) {
            throw new org.python.exceptions.AttributeError(this, name);
        }
        return value;
    }

    public org.python.Object __getattr_null(java.lang.String name) {
        throw new org.python.exceptions.NotImplementedError("'" + this.typeName() + ".__getattribute__' has not been implemented");
    }

    @org.python.Method(
        __doc__ = "Return getattribute(self, name)."
    )
    public org.python.Object __getattribute__(org.python.Object name) {
        try {
            return this.__getattribute__(((org.python.types.Str) name).value);
        } catch (java.lang.ClassCastException e) {
            throw new org.python.exceptions.TypeError("__getattribute__(): attribute name must be string");
        }
    }

    public org.python.Object __getattribute__(java.lang.String name) {
        org.python.Object value = this.__getattribute_null(name);
        if (value == null) {
            throw new org.python.exceptions.AttributeError(this, name);
        }
        return value;
    }

    public org.python.Object __getattribute_null(java.lang.String name) {
        throw new org.python.exceptions.NotImplementedError("'" + this.typeName() + ".__getattribute__' has not been implemented");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __get__(org.python.Object instance, org.python.Object klass) {
        return this;
    }

    @org.python.Method(
        __doc__ = "Implement setattr(self, name, value)."
    )
    public void __setattr__(org.python.Object name, org.python.Object value) {
        try {
            this.__setattr__(((org.python.types.Str) name).value, value);
        } catch (java.lang.ClassCastException e) {
            throw new org.python.exceptions.TypeError("__setattr__(): attribute name must be string");
        }
    }

    public void __setattr__(java.lang.String name, org.python.Object value) {
        if (!this.__setattr_null(name, value)) {
            throw new org.python.exceptions.AttributeError(this, name);
        };
    }

    public boolean __setattr_null(java.lang.String name, org.python.Object value) {
        throw new org.python.exceptions.NotImplementedError("'" + this.typeName() + ".__setattr__' has not been implemented");
    }

    public void __set__(org.python.Object instance, org.python.Object value) {}

    @org.python.Method(
        __doc__ = "Implement delattr(self, name)."
    )
    public void __delattr__(org.python.Object name) {
        try {
            this.__delattr__(((org.python.types.Str) name).value);
        } catch (java.lang.ClassCastException e) {
            throw new org.python.exceptions.TypeError("__delattr__(): attribute name must be string");
        }
    }

    public void __delattr__(java.lang.String name) {
        if (!this.__delattr_null(name)) {
            throw new org.python.exceptions.AttributeError(this, name);
        };
    }

    public boolean __delattr_null(java.lang.String name) {
        throw new org.python.exceptions.NotImplementedError("'" + this.typeName() + ".__delattr__' has not been implemented");
    }

    @org.python.Method(
        __doc__ = "Implement dir(self, name)."
    )
    public org.python.Object __dir__() {
        throw new org.python.exceptions.NotImplementedError("'" + this.typeName() + ".__dir__' has not been implemented");
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

    public org.python.Object __contains__(org.python.Object item) {
        throw new org.python.exceptions.AttributeError(this, "__contains__");
    }

    public org.python.Object __not_contains__(org.python.Object item) {
        throw new org.python.exceptions.AttributeError(this, "__not_contains__");
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
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for ** or pow(): '" + this.typeName() + "', '" + other.typeName() + "', '" + modulus.typeName() + "'");
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


    public org.python.Object __iadd__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__iadd__");
    }

    public org.python.Object __isub__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__isub__");
    }

    public org.python.Object __imul__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__imul__");
    }

    public org.python.Object __itruediv__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__itruediv__");
    }

    public org.python.Object __ifloordiv__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__ifloordiv__");
    }

    public org.python.Object __imod__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__imod__");
    }

    public org.python.Object __idivmod__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__idivmod__");
    }

    public org.python.Object __ipow__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__ipow__");
    }

    public org.python.Object __ilshift__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__ilshift__");
    }

    public org.python.Object __irshift__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__irshift__");
    }

    public org.python.Object __iand__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__iand__");
    }

    public org.python.Object __ixor__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__ixor__");
    }

    public org.python.Object __ior__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__ior__");
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

    public org.python.Object __index__() {
        throw new org.python.exceptions.AttributeError(this, "__index__");
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
