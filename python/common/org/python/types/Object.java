package org.python.types;

public class Object extends java.lang.RuntimeException implements org.python.Object {
    public java.util.Map<java.lang.String, org.python.Object> __dict__;
    public org.python.types.Type __class__;
    public org.python.types.Type.Origin origin;

    /**
     * A utility method to update the internal value of this object.
     *
     * Used by __i*__ operations to do an in-place operation.
     * On a base object, it will always fail. Subclasses should override
     * to provide the relevant assignment info.
     */
    void setValue(org.python.Object obj) {
        throw new org.python.exceptions.RuntimeError("'" + this.typeName() + "' object cannot be updated.");
    }

    public java.lang.Object toJava() {
        return this;
    }

    public java.lang.Object toObject() {
        return this;
    }

    public boolean toBoolean() {
        try {
            return ((org.python.types.Bool) this.__bool__()).value;
        } catch (org.python.exceptions.AttributeError ae) {
            try {
                return ((org.python.types.Int) this.__len__()).value != 0;
            } catch (org.python.exceptions.AttributeError ae2) {
                return true;
            }
        }
    }

    public org.python.Object byValue() {
        return this;
    }

    /**
     * Return the Python type for this object.
     */
    public org.python.types.Type type() {
        return this.__class__;
    }

    public java.lang.String typeName() {
        return org.Python.typeName(this.getClass());
    }

    /**
     * Construct a new object instance.
     *
     * The argument `origin` is used to describe where the object is defined -
     * Python or Java. It can also be "PLACEHOLDER" - these are transient objects
     * that exist during instantiation of other objects. As a result, they don't
     * have attributes or any of the other usual infrastructure of a Python object.
     *
     * klass is the underlying java class being represented by this object.
     * In the case of a Python object, the klass is the Java manifestation of
     * the object; when wrapping Java objects, the native class of the object
     * is used.
     */
    protected Object(org.python.types.Type.Origin origin, java.lang.Class klass, java.lang.String msg) {
        super(msg);
        this.origin = origin;
        this.__dict__ = new java.util.HashMap<java.lang.String, org.python.Object>();
        if (origin != org.python.types.Type.Origin.PLACEHOLDER) {
            if (klass == null) {
                klass = this.getClass();
            }
            this.__new__(org.python.types.Type.pythonType(klass));
        }
    }

    protected Object(org.python.types.Type.Origin origin, java.lang.Class klass) {
        this(origin, klass, "");
    }

    public Object() {
        this(org.python.types.Type.Origin.PYTHON, null);
    }

    public Object(java.lang.String msg) {
        this(org.python.types.Type.Origin.PYTHON, null, msg);
    }

    @org.python.Method(
            __doc__ = "The most base type"
    )
    public Object(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        this(org.python.types.Type.Origin.PYTHON, null);
        if (args != null && args.length > 0) {
            throw new org.python.exceptions.TypeError("object() takes no parameters");
        } else if (kwargs != null && kwargs.size() > 0) {
            throw new org.python.exceptions.TypeError("object() takes no parameters");
        }
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
        } catch (ClassCastException e) {
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
        this.__class__ = (org.python.types.Type) klass;
        if (this.__class__.origin == org.python.types.Type.Origin.PLACEHOLDER) {
            this.__class__.add_reference(this);
        }
        return this.__class__;
    }

    @org.python.Method(
            __doc__ = "Initialize self.  See help(type(self)) for accurate signature."
    )
    public void __init__() {
    }

    @org.python.Method(
            __doc__ = "Destroy an existing object. See help(type) for accurate signature."
    )
    public void __del__() {
    }

    @org.python.Method(
            __doc__ = "Return repr(self)."
    )
    public org.python.Object __repr__() {
        return new org.python.types.Str(String.format("<%s object at 0x%x>", this.typeName(), this.hashCode()));
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
        throw new org.python.exceptions.NotImplementedError("'" + this.typeName() + ".__format__' has not been implemented");
    }

    @org.python.Method(
            __doc__ = "Return self<value.",
            args = {"other"}
    )
    public org.python.Object __lt__(org.python.Object other) {
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "Return self<=value.",
            args = {"other"}
    )
    public org.python.Object __le__(org.python.Object other) {
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "Return self==value.",
            args = {"other"}
    )
    public org.python.Object __eq__(org.python.Object other) {
        if (this == other) {
            return new org.python.types.Bool(true);
        } else {
            return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
        }
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
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "Return self>=value.",
            args = {"other"}
    )
    public org.python.Object __ge__(org.python.Object other) {
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
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
        // org.Python.debug("GETATTRIBUTE ", name);
        // org.Python.debug("SELF ", this.__repr__());
        // org.Python.debug("ATTRS ", this.__dict__);

        org.python.Object value = this.__dict__.get(name);

        if (value == null) {
            // Look to the class for an attribute
            // org.Python.debug("no instance attribute");
            value = this.__class__.__getattribute_null(name);
            if (value == null) {
                // org.Python.debug("no class attribute");
                // Use the descriptor protocol
                value = this.__getattr_null(name);
                if (value == null) {
                    // org.Python.debug("no descriptor protocol");
                    // Still nothing - give up, and return a value
                    // that can be interpreted as an exception.
                    return null;
                }
            }
        }
        // org.Python.debug(String.format("GETATTRIBUTE %s = ", name), value);
        // Post-process the value retrieved.

        return value.__get__(this, this.__class__);
    }

    @org.python.Method(
            __doc__ = "",
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
        // org.Python.debug(String.format("SETATTR %s", name), value);
        // org.Python.debug("SELF ", this.__repr__());
        // org.Python.debug("ATTRS ", this.__dict__);

        // If the attribute already exists, then it's OK to set it.
        org.python.Object attr = this.__class__.__getattribute_null(name);
        // org.Python.debug("ATTR ", attr);

        // The base object can't have attribute set on it unless the attribute already exists.
        if (this.getClass() == org.python.types.Object.class) {
            if (attr == null) {
                return false;
            }
        }

        if (attr == null) {
            this.__dict__.put(name, value);
        } else {
            // if attribute is not a descriptor add it to local instance
            if (!(attr instanceof org.python.types.Property)) {
                this.__dict__.put(name, value);
            }
            attr.__set__(this, value);
        }

        return true;
    }

    @org.python.Method(
            __doc__ = "",
            args = {"instance", "value"}
    )
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
            throw new org.python.exceptions.TypeError("attribute name must be string, not '" + name.typeName() + "'");
        }
    }

    public void __delattr__(java.lang.String name) {
        if (!this.__delattr_null(name)) {
            throw new org.python.exceptions.AttributeError(this, name);
        }
    }

    public boolean __delattr_null(java.lang.String name) {
        // org.Python.debug(String.format("DELATTR %s", name));
        // org.Python.debug("SELF ", this.__repr__());
        // org.Python.debug("ATTRS ", this.__dict__);

        // If the attribute already exists, then it's OK to set it.
        org.python.Object attr = this.__class__.__getattribute_null(name);

        if (attr == null) {
            org.python.Object result = this.__dict__.remove(name);
            return result != null && !(result instanceof org.python.exceptions.AttributeError);
        } else {
            attr.__delete__(this);
            return true;
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"instance", "value"}
    )
    public void __delete__(org.python.Object instance) {
    }

    @org.python.Method(
            __doc__ = "__dir__() -> list\ndefault dir() implementation"
    )
    public org.python.Object __dir__() {
        org.python.types.List names = new org.python.types.List(new java.util.ArrayList(this.__dict__.keySet()));

        names.extend(this.__dict__.get("__class__").__dir__());
        names.sort(null, null);

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
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for +: '" + this.typeName() + "' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __sub__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for -: '" + this.typeName() + "' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __mul__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for *: '" + this.typeName() + "' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __truediv__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for /: '" + this.typeName() + "' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __floordiv__(org.python.Object other) {
        if (other instanceof org.python.types.Complex) {
            throw new org.python.exceptions.TypeError("can't take floor of complex number.");
        } else {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for //: '" + this.typeName() + "' and '" + other.typeName() + "'");
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __mod__(org.python.Object other) {
        if (other instanceof org.python.types.Complex) {
            throw new org.python.exceptions.TypeError("can't mod complex numbers.");
        } else {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for %: '" + this.typeName() + "' and '" + other.typeName() + "'");
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __divmod__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for divmod(): '" + this.typeName() + "' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other", "modulus"}
    )
    public org.python.Object __pow__(org.python.Object other, org.python.Object modulus) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for ** or pow(): '" + this.typeName() + "' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __lshift__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for <<: '" + this.typeName() + "' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __rshift__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for >>: '" + this.typeName() + "' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __and__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for &: '" + this.typeName() + "' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __xor__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for ^: '" + this.typeName() + "' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __or__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for |: '" + this.typeName() + "' and '" + other.typeName() + "'");
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
            return this.__add__(other);
        } catch (org.python.exceptions.TypeError ae) {
            if (ae.getMessage().startsWith("unsupported operand")) {
                throw new org.python.exceptions.TypeError("unsupported operand type(s) for +=: '" + this.typeName() + "' and '" + other.typeName() + "'");
            } else {
                throw ae;
            }
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
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for -=: '" + this.typeName() + "' and '" + other.typeName() + "'");
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __imul__(org.python.Object other) {
        try {
            return this.__mul__(other);
        } catch (org.python.exceptions.TypeError e) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for *=: '" + this.typeName() + "' and '" + other.typeName() + "'");
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __itruediv__(org.python.Object other) {
        try {
            return this.__truediv__(other);
        } catch (org.python.exceptions.TypeError e) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for /=: '" + this.typeName() + "' and '" + other.typeName() + "'");
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __ifloordiv__(org.python.Object other) {
        try {
            return this.__floordiv__(other);
        } catch (org.python.exceptions.TypeError e) {
            if (other instanceof org.python.types.Complex) {
                throw new org.python.exceptions.TypeError("can't take floor of complex number.");
            } else {
                throw new org.python.exceptions.TypeError("unsupported operand type(s) for //=: '" + this.typeName() + "' and '" + other.typeName() + "'");
            }
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __imod__(org.python.Object other) {
        try {
            return this.__mod__(other);
        } catch (org.python.exceptions.TypeError e) {
            if (other instanceof org.python.types.Complex) {
                throw new org.python.exceptions.TypeError("can't mod complex numbers.");
            } else {
                throw new org.python.exceptions.TypeError("unsupported operand type(s) for %=: '" + this.typeName() + "' and '" + other.typeName() + "'");
            }
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __idivmod__(org.python.Object other) {
        try {
            this.setValue(this.__divmod__(other));
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
        return this.__pow__(other, null);
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
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for <<=: '" + this.typeName() + "' and '" + other.typeName() + "'");
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
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for >>=: '" + this.typeName() + "' and '" + other.typeName() + "'");
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
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for &=: '" + this.typeName() + "' and '" + other.typeName() + "'");
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __ixor__(org.python.Object other) {
        try {
            return this.__xor__(other);
        } catch (org.python.exceptions.TypeError e) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for ^=: '" + this.typeName() + "' and '" + other.typeName() + "'");
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
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for |=: '" + this.typeName() + "' and '" + other.typeName() + "'");
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
            __doc__ = ""
    )
    public org.python.Object __index__() {
        throw new org.python.exceptions.AttributeError(this, "__index__");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"ndigits"}
    )
    public org.python.Object __round__(org.python.Object ndigits) {
        throw new org.python.exceptions.AttributeError(this, "__round__");
    }

    // Need to implement Is __eq__ Is Not __ne__
    // In __contains__ (reversed operands) Not In __not_contains__ (reversed operands)
    //
    // for Is and Is Not, falls through to here only when either side is a constant in python
    // which ends up as org.python.types.[Int|Float|Complex], otherwise it's dealt with
    // by object reference comparison IF_ACMEQ. so we fall through to __eq__!
    public enum CMP_OP {
        GE(">=", "__ge__", "__le__"),
        GT(">", "__gt__", "__lt__"),
        EQ("==", "__eq__", "__eq__"),
        NE("!=", "__ne__", "__ne__"),
        LE("<=", "__le__", "__ge__"),
        LT("<", "__lt__", "__gt__");

        public final String oper;
        public final String operMethod;
        public final String reflOperMethod;
        CMP_OP(java.lang.String oper, java.lang.String operMethod, java.lang.String reflOperMethod) {
            this.oper = oper;
            this.operMethod = operMethod;
            this.reflOperMethod = reflOperMethod;
        }
    }

    /* This method is used from standard library datatypes, etc */
    public static org.python.Object __cmp__(org.python.Object v, org.python.Object w,
            org.python.types.Object.CMP_OP op) {
        return __cmp__(v, w, op.oper, op.operMethod, op.reflOperMethod);
    }

    /* This method is used from standard library container datatypes */
    public static org.python.Object __cmp_bool__(org.python.Object v, org.python.Object w,
            org.python.types.Object.CMP_OP op) {
        // identity implies equality
        if (v == w) {
            if (op == org.python.types.Object.CMP_OP.EQ) {
                return new org.python.types.Bool(true);
            } else if (op == org.python.types.Object.CMP_OP.NE) {
                return new org.python.types.Bool(false);
            }
        }
        org.python.Object result = __cmp__(v, w, op.oper, op.operMethod, op.reflOperMethod);
        if (result instanceof org.python.types.Bool) {
            return result;
        } else {
            return result.__bool__();
        }
    }

    /* This method is invoked from the AST for Compare nodes */
    public static org.python.Object __cmp__(org.python.Object v, org.python.Object w, java.lang.String oper,
            java.lang.String operMethod, java.lang.String reflOperMethod) {
        org.python.Object result = org.python.types.NotImplementedType.NOT_IMPLEMENTED;
        boolean reflectedChecked = v.type() != w.type()
                && ((org.python.types.Bool) org.Python.isinstance(w, v.type())).value;

        if (reflectedChecked) {
            result = invokeComparison(w, v, reflOperMethod);
            if (result != org.python.types.NotImplementedType.NOT_IMPLEMENTED) {
                return result;
            }
        }

        result = invokeComparison(v, w, operMethod);
        if (result != org.python.types.NotImplementedType.NOT_IMPLEMENTED) {
            return result;
        }

        if (!reflectedChecked) {
            result = invokeComparison(w, v, reflOperMethod);
            if (result != org.python.types.NotImplementedType.NOT_IMPLEMENTED) {
                return result;
            }
        }

        if (oper.equals("==")) {
            return new org.python.types.Bool(v == w);
        } else if (oper.equals("!=")) {
            return new org.python.types.Bool(v != w);
        }

        if (org.Python.VERSION < 0x03060000) {
            throw new org.python.exceptions.TypeError(String.format(
                "unorderable types: %s() %s %s()", v.typeName(), oper, w.typeName()));
        } else {
            throw new org.python.exceptions.TypeError(String.format(
                "'%s' not supported between instances of '%s' and '%s'", oper, v.typeName(), w.typeName()));
        }
    }

    private static org.python.Object invokeComparison(org.python.Object x, org.python.Object y, String methodName) {
        if (methodName == null) {
            return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
        }

        org.python.Object comparator = x.__getattribute_null(methodName);
        if (comparator == null || !(comparator instanceof org.python.types.Method)) {
            return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
        }

        org.python.Object[] args = new org.python.Object[1];
        args[0] = y;
        return (org.python.Object) ((org.python.types.Method) comparator).invoke(args, null);
    }
}
