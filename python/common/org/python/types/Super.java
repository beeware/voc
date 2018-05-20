package org.python.types;

public class Super implements org.python.Object {
    public org.python.types.Type klass;
    public org.python.Object instance;

    /**
     * A utility method to update the internal value of this object.
     *
     * Used by __i*__ operations to do an in-place operation.
     * On a base object, it will always fail. Subclasses should override
     * to provide the relevant assignment info.
     */
    void setValue(org.python.Object obj) {
        throw new org.python.exceptions.RuntimeError("super object cannot be updated.");
    }

    public java.lang.Object toJava() {
        return this;
    }

    public java.lang.Object toObject() {
        return this.instance;
    }

    public boolean toBoolean() {
        return true;
    }

    public org.python.Object byValue() {
        return this;
    }

    public org.python.types.Type type() {
        return null;
    }

    public java.lang.String typeName() {
        return "super";
    }

    /**
     * Construct a new object instance.
     */
    public Super(org.python.Object klass) {
        this(klass, org.python.types.NoneType.NONE);
    }

    public Super(org.python.Object klass, org.python.Object instance) {
        try {
            this.klass = (org.python.types.Type) klass;
        } catch (java.lang.ClassCastException e) {
            throw new org.python.exceptions.TypeError(java.lang.String.format("must be type, not %s", klass.typeName()));
        }
        this.instance = instance;
    }

    /**
     * Proxy Java object methods onto their Python counterparts.
     */
    public boolean equals(java.lang.Object other) {
        if (other instanceof org.python.Object) {
            org.python.Object result = org.python.types.Object.__cmp_bool__(this, (org.python.Object) other, org.python.types.Object.CMP_OP.EQ);
            return ((org.python.types.Bool) result).value;
        } else {
            throw new org.python.exceptions.RuntimeError("Can't compare a Python object with non-Python object.");
        }
    }

    public int compareTo(java.lang.Object other) {
        try {
            if (((org.python.types.Bool) this.__lt__((org.python.Object) other)).value) {
                return -1;
            } else if (((org.python.types.Bool) this.__gt__((org.python.Object) other)).value) {
                return 1;
            }
            return 0;
        } catch (java.lang.ClassCastException e) {
            throw new org.python.exceptions.RuntimeError("Can't compare a Python object with non-Python object.");
        }
    }

    public java.lang.String toString() {
        return ((org.python.types.Str) this.__str__()).value;
    }

    protected void finalize() throws Throwable {
        try {
            this.__del__();
        } finally {
            super.finalize();
        }
    }

    /**
     * Python interface compatibility
     * Section 3.3.1 - Basic customization
     */
    @org.python.Method(
            __doc__ = "Create and return a new object.  See help(type) for accurate signature."
    )
    public org.python.Object __new__(org.python.Object klass) {
        org.python.types.Type cls = (org.python.types.Type) klass;
        return cls;
    }

    // public void __init__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
    //     throw new org.python.exceptions.AttributeError(this, "__init__");
    // }

    @org.python.Method(
            __doc__ = "Destroy an existing object. See help(type) for accurate signature."
    )
    public void __del__() {
    }

    @org.python.Method(
            __doc__ = "Return repr(self)."
    )
    public org.python.Object __repr__() {
        return new org.python.types.Str(String.format("<super %s, %s>", this.klass, this.instance));
    }

    @org.python.Method(
            __doc__ = "Return str(self)."
    )
    public org.python.Object __str__() {
        return this.__repr__();
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __bytes__() {
        throw new org.python.exceptions.AttributeError(this, "__bytes__");
    }

    @org.python.Method(
            __doc__ = "default object formatter",
            args = {"format_string"}
    )
    public org.python.Object __format__(org.python.Object format_string) {
        throw new org.python.exceptions.NotImplementedError("'super().__format__' has not been implemented");
    }

    @org.python.Method(
            __doc__ = "Return self<value.",
            args = {"other"}
    )
    public org.python.Object __lt__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("'super().__lt__' has not been implemented");
    }

    @org.python.Method(
            __doc__ = "Return self<=value.",
            args = {"other"}
    )
    public org.python.Object __le__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("'super().__le__' has not been implemented");
    }

    @org.python.Method(
            __doc__ = "Return self==value.",
            args = {"other"}
    )
    public org.python.Object __eq__(org.python.Object other) {
        return new org.python.types.Bool(System.identityHashCode(this) == System.identityHashCode(other));
    }

    @org.python.Method(
            __doc__ = "Return self!=value.",
            args = {"other"}
    )
    public org.python.Object __ne__(org.python.Object other) {
        // By default, __ne__() delegates to __eq__() and inverts the result unless it is NotImplemented.
        // see: http://bugs.python.org/issue4395
        org.python.Object result = this.__eq__(other);
        if (result instanceof org.python.types.NotImplementedType) {
            return result;
        }
        return new org.python.types.Bool(!((org.python.types.Bool) result).value);
    }

    @org.python.Method(
            __doc__ = "Return self>value.",
            args = {"other"}
    )
    public org.python.Object __gt__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("'super().__gt__' has not been implemented");
    }

    @org.python.Method(
            __doc__ = "Return self>=value.",
            args = {"other"}
    )
    public org.python.Object __ge__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("'super().__ge__' has not been implemented");
    }

    @org.python.Method(
            __doc__ = "Return hash(self)."
    )
    public org.python.Object __hash__() {
        return new org.python.types.Int(this.hashCode());
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __bool__() {
        throw new org.python.exceptions.AttributeError(this, "__bool__");
    }

    /**
     * Section 3.3.2 - Emulating container types
     */
    @org.python.Method(
            __doc__ = "",
            args = {"attr"}
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
        return null;
    }

    @org.python.Method(
            __doc__ = "Return getattr(self, name).",
            args = {"name"}
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
        // Look for local instance attributes first
        // org.Python.debug("SUPER " + this.klass + " GETATTRIBUTE ", name);
        org.python.Object value = null;
        java.util.List<org.python.Object> bases = ((org.python.types.Tuple) this.klass.__dict__.get("__bases__")).value;

        value = this.klass.__getattribute_null(name + "$super");

        if (value == null) {
            // org.Python.debug("    look to bases of ", this.klass);
            // org.Python.debug("            which are ", bases);

            for (org.python.Object base : bases) {
                // org.Python.debug("            check ", base);
                value = base.__getattribute_null(name);
                if (value != null) {
                    break;
                }
            }
        }

        if (value == null) {
            throw new org.python.exceptions.NotImplementedError("Can't get attributes on super() (yet!)");
        }

        // org.Python.debug("VALUE: SUPER GETATTRIBUTE " + name, value);
        // Post-process the value retrieved, using the binding fr
        return value.__get__(this.instance, this.klass);
    }

    @org.python.Method(
            __doc__ = "Return an attribute of instance, which is of type owner.",
            args = {"instance", "klass"}
    )
    public org.python.Object __get__(org.python.Object instance, org.python.Object klass) {
        // System.out.println("__GET__ on " + this + " " + this.getClass());
        return this;
    }

    @org.python.Method(
            __doc__ = "Implement setattr(self, name, value).",
            args = {"name", "value"}
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
        }
    }

    public boolean __setattr_null(java.lang.String name, org.python.Object value) {
        // org.Python.debug("SUPER SETATTR %s" % name, value);
        // If the attribute already exists, then it's OK to set it.
        org.python.Object attr = this.klass.__getattribute_null(name);

        // if (attr == null) {
        //     this.__dict__.put(name, value);
        // } else {
        //     attr.__set__(this, value);
        // }
        return true;
    }

    public void __set__(org.python.Object instance, org.python.Object value) {
    }

    @org.python.Method(
            __doc__ = "Implement delattr(self, name).",
            args = {"attr"}
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
        }
    }

    public boolean __delattr_null(java.lang.String name) {
        // org.python.Object result = __dict__.remove(name);
        // return (result != null);
        return false;
    }

    public void __delete__(org.python.Object instance) {
    }

    @org.python.Method(
            __doc__ = "__dir__() -> list\ndefault dir() implementation"
    )
    public org.python.Object __dir__() {
        org.python.types.List names = new org.python.types.List(new java.util.ArrayList());

        // names.extend(this.__class__.__dir__());
        // names.sort();

        return names;
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
    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __len__() {
        throw new org.python.exceptions.AttributeError(this, "__len__");
    }

    // public org.python.Object __length_hint__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
    //     throw new org.python.exceptions.AttributeError(this, "__length_hint__");
    // }

    @org.python.Method(
            __doc__ = "",
            args = {"index"}
    )
    public org.python.Object __getitem__(org.python.Object index) {
        throw new org.python.exceptions.AttributeError(this, "__getitem__");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"key"}
    )
    public org.python.Object __missing__(org.python.Object key) {
        throw new org.python.exceptions.AttributeError(this, "__missing__");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"index", "value"}
    )
    public void __setitem__(org.python.Object index, org.python.Object value) {
        throw new org.python.exceptions.AttributeError(this, "__setitem__");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"index"}
    )
    public void __delitem__(org.python.Object index) {
        throw new org.python.exceptions.AttributeError(this, "__delitem__");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __iter__() {
        throw new org.python.exceptions.AttributeError(this, "__iter__");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __reversed__() {
        throw new org.python.exceptions.AttributeError(this, "__reversed__");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __next__() {
        throw new org.python.exceptions.AttributeError(this, "__next__");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"item"}
    )
    public org.python.Object __contains__(org.python.Object item) {
        throw new org.python.exceptions.AttributeError(this, "__contains__");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"item"}
    )
    public org.python.Object __not_contains__(org.python.Object item) {
        throw new org.python.exceptions.AttributeError(this, "__not_contains__");
    }

    /**
     * Section 3.3.7 - Emulating numeric types
     */
    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __add__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for +: 'super()' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __sub__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for -: 'super()' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __mul__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for *: 'super()' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __truediv__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for /: 'super()' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __floordiv__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for //: 'super()' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __mod__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for %: 'super()' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __divmod__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for divmod(): 'super()' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other", "modulus"}
    )
    public org.python.Object __pow__(org.python.Object other, org.python.Object modulus) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for ** or pow(): 'super()' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __lshift__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for <<: 'super()' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __rshift__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for >>: 'super()' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __and__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for &: 'super()' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __xor__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for ^: 'super()' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __or__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for |: 'super()' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __radd__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__radd__");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __rsub__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__rsub__");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __rmul__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__rmul__");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __rtruediv__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__rtruediv__");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __rfloordiv__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__rfloordiv__");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __rmod__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__rmod__");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __rdivmod__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__rdivmod__");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __rpow__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__rpow__");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __rlshift__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__rlshift__");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __rrshift__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__rrshift__");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __rand__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__rand__");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __rxor__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__rxor__");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __ror__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__ror__");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __iadd__(org.python.Object other) {
        try {
            this.setValue(this.__add__(other));
            return this;
        } catch (org.python.exceptions.TypeError e) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for +=: 'super()' and '" + other.typeName() + "'");
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __isub__(org.python.Object other) {
        try {
            return this.__sub__(other);
        } catch (org.python.exceptions.TypeError e) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for -=: 'super()' and '" + other.typeName() + "'");
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __imul__(org.python.Object other) {
        try {
            this.setValue(this.__mul__(other));
            return this;
        } catch (org.python.exceptions.TypeError e) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for *=: 'super()' and '" + other.typeName() + "'");
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __itruediv__(org.python.Object other) {
        try {
            this.setValue(this.__truediv__(other));
            return this;
        } catch (org.python.exceptions.TypeError e) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for /=: 'super()' and '" + other.typeName() + "'");
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __ifloordiv__(org.python.Object other) {
        try {
            this.setValue(this.__floordiv__(other));
            return this;
        } catch (org.python.exceptions.TypeError e) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for //=: 'super()' and '" + other.typeName() + "'");
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __imod__(org.python.Object other) {
        try {
            this.setValue(this.__mod__(other));
            return this;
        } catch (org.python.exceptions.TypeError e) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for %=: 'super()' and '" + other.typeName() + "'");
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __idivmod__(org.python.Object other) {
        try {
            this.setValue(this.__pow__(other, null));
            return this;
        } catch (org.python.exceptions.TypeError e) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for //=: '" + this.typeName() + "' and '" + other.typeName() + "'");
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __ipow__(org.python.Object other) {
        try {
            this.setValue(this.__pow__(other, null));
            return this;
        } catch (org.python.exceptions.TypeError e) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for **=: 'super()' and '" + other.typeName() + "'");
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __ilshift__(org.python.Object other) {
        try {
            this.setValue(this.__lshift__(other));
            return this;
        } catch (org.python.exceptions.TypeError e) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for <<=: 'super()' and '" + other.typeName() + "'");
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __irshift__(org.python.Object other) {
        try {
            this.setValue(this.__rshift__(other));
            return this;
        } catch (org.python.exceptions.TypeError e) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for >>=: 'super()' and '" + other.typeName() + "'");
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __iand__(org.python.Object other) {
        try {
            return this.__and__(other);
        } catch (org.python.exceptions.TypeError e) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for &=: 'super()' and '" + other.typeName() + "'");
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __ixor__(org.python.Object other) {
        try {
            this.setValue(this.__xor__(other));
            return this;
        } catch (org.python.exceptions.TypeError e) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for ^=: 'super()' and '" + other.typeName() + "'");
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __ior__(org.python.Object other) {
        try {
            return this.__or__(other);
        } catch (org.python.exceptions.TypeError e) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for |=: 'super()' and '" + other.typeName() + "'");
        }
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __neg__() {
        throw new org.python.exceptions.AttributeError(this, "__neg__");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __pos__() {
        throw new org.python.exceptions.AttributeError(this, "__pos__");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __abs__() {
        throw new org.python.exceptions.AttributeError(this, "__abs__");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __invert__() {
        throw new org.python.exceptions.AttributeError(this, "__invert__");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __not__() {
        return new org.python.types.Bool(!((org.python.types.Bool) this.__bool__()).value);
    }

    @org.python.Method(
            __doc__ = "",
            args = {"real", "imag"}
    )
    public org.python.Object __complex__(org.python.Object real, org.python.Object imag) {
        throw new org.python.exceptions.AttributeError(this, "__complex__");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __int__() {
        throw new org.python.exceptions.AttributeError(this, "__int__");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __float__() {
        throw new org.python.exceptions.AttributeError(this, "__float__");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"ndigits"}
    )
    public org.python.Object __round__(org.python.Object ndigits) {
        throw new org.python.exceptions.AttributeError(this, "__round__");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __index__() {
        throw new org.python.exceptions.AttributeError(this, "__index__");
    }

    /**
     * Section 3.3.8 - With statement context
     */
    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __enter__() {
        throw new org.python.exceptions.AttributeError(this, "__enter__");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __exit__(org.python.Object exc_type, org.python.Object exc_value, org.python.Object traceback) {
        throw new org.python.exceptions.AttributeError(this, "__exit__");
    }
}
