package org.python.types;


public class Object implements org.python.Object {
    public java.util.Map<java.lang.String, org.python.Object> attrs;

    /**
     * A utility method to update the internal value of this object.
     *
     * Used by __i*__ operations to do an in-place operation.
     * On a base object, it will always fail. Subclasses should override
     * to provide the relevant assignment info.
     */
    void setValue(org.python.Object obj) {
        throw new org.python.exceptions.RuntimeError("'" + org.Python.typeName(this) + "' object cannot be updated.");
    }

    public java.lang.Object toValue() {
        return this;
    }

    /**
     * Construct a new object instance.
     *
     * The argument `empty` is used to flag placeholder objects. These are
     * transient objects that exist during instantiation of other objects;
     * as a result, they don't have attributes or any of the other usual
     * infrastructure of a Python object.
     */
    protected Object(boolean empty) {
        if (!empty) {
            this.attrs = new java.util.HashMap<java.lang.String, org.python.Object>();
            org.python.types.Type cls = org.python.types.Type.pythonType(this.getClass());
            this.__new__(cls);
        }
    }

    public Object() {
        this(false);
    }

    /**
     * Proxy Java object methods onto their Python counterparts.
     */
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
            else if (((org.python.types.Bool) this.__lt__((org.python.types.Object) other)).value) {
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

    protected void finalize() throws Throwable {
        try {
            this.__del__();
        }
        finally {
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
    public org.python.types.Type __new__(org.python.types.Type cls) {
        this.attrs.put("__class__", cls);
        if (cls.is_placeholder()) {
            cls.add_reference(this);
        }
        return cls;
    }


    // public void __init__() {
    //     throw new org.python.exceptions.AttributeError(this, "__init__");
    // }

    public void __del__() {
        throw new org.python.exceptions.AttributeError(this, "__del__");
    }

    @org.python.Method(
        __doc__ = "Return repr(self)."
    )
    public org.python.Object __repr__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __lt__ doesn't take keyword arguments");
        }
        if (args.size() != 0) {
            throw new org.python.exceptions.TypeError("Expected 0 arguments, got " + args.size());
        }
        return this.__repr__();
    }

    public org.python.types.Str __repr__() {
        return new org.python.types.Str(String.format("<%s object at 0x%x>", org.Python.typeName(this), this.hashCode()));
    }

    @org.python.Method(
        __doc__ = "Return str(self)."
    )
    public org.python.Object __str__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __lt__ doesn't take keyword arguments");
        }
        if (args.size() != 0) {
            throw new org.python.exceptions.TypeError("Expected 0 arguments, got " + args.size());
        }
        return this.__str__();
    }

    public org.python.types.Str __str__() {
        return this.__repr__();
    }

    public org.python.types.Bytes __bytes__() {
        throw new org.python.exceptions.AttributeError(this, "__bytes__");
    }

    public org.python.types.Str __format__(org.python.Object format_spec) {
        throw new org.python.exceptions.NotImplementedError("'" + org.Python.typeName(this) + ".__format__' has not been implemented");
    }

    public org.python.Object __lt__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __lt__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            return this.__lt__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __lt__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("'" + org.Python.typeName(this) + ".__lt__' has not been implemented");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __le__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __le__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            return this.__le__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __le__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("'" + org.Python.typeName(this) + ".__le__' has not been implemented");
    }


    public org.python.Object __eq__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __eq__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            return this.__eq__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __eq__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("'" + org.Python.typeName(this) + ".__eq__' has not been implemented");
    }


    public org.python.Object __ne__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __ne__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            return this.__ne__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __ne__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("'" + org.Python.typeName(this) + ".__ne__' has not been implemented");
    }

    public org.python.Object __gt__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __gt__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            return this.__gt__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __gt__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("'" + org.Python.typeName(this) + ".__gt__' has not been implemented");
    }

    public org.python.Object __ge__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __ge__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            return this.__ge__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __ge__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("'" + org.Python.typeName(this) + ".__ge__' has not been implemented");
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

    public org.python.Object __getattr__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __getattr__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            if (args.get(0) instanceof org.python.types.Str) {
                return this.__getattr__(((org.python.types.Str) args.get(0)).value);
            } else {
                throw new org.python.exceptions.TypeError("getattr(): attribute name must be string");
            }
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __getattr__(org.python.Object name) {
        if (name instanceof org.python.types.Str) {
            return this.__getattr__(((org.python.types.Str) name).value);
        } else {
            throw new org.python.exceptions.TypeError("getattr(): attribute name must be string");
        }
    }

    public org.python.Object __getattr__(java.lang.String name) {
        throw new org.python.exceptions.AttributeError(this, "__getattr__");
    }

    public org.python.Object __getattribute__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __getattribute__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            if (args.get(0) instanceof org.python.types.Str) {
                return this.__getattribute__(((org.python.types.Str) args.get(0)).value);
            } else {
                throw new org.python.exceptions.TypeError("__getattribute__(): attribute name must be string");
            }
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __getattribute__(org.python.Object name) {
        if (name instanceof org.python.types.Str) {
            return this.__getattribute__(((org.python.types.Str) name).value);
        } else {
            throw new org.python.exceptions.TypeError("__getattribute__: attribute name must be string");
        }
    }

    @SuppressWarnings("unchecked")
    public org.python.Object __getattribute__(java.lang.String name) {
        // Look for local instance attributes first
        // System.out.println("ATTRS " + this.attrs);
        org.python.Object value = this.attrs.get(name);
        if (value == null) {
            try {
                // No instance attribute; look for a class attribute.
                org.python.types.Type klass = (org.python.types.Type) this.attrs.get("__class__");
                // System.out.println("CLASS ATTRS " + klass.attrs);
                value = klass.attrs.get(name);

                if (value == null) {
                    // No class attribute; Try the __getattr__ helper.
                    value = this.__getattr__(name);
                }
            } catch (org.python.exceptions.AttributeError e) {
                throw new org.python.exceptions.AttributeError(this, name);
            }
        }

        return value.__get__(this, org.python.types.Type.pythonType(this.getClass()));
    }

    public org.python.Object __get__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.RuntimeError("Descriptor method __get__ does not accept keyword arguments.");
        }
        if (args.size() == 2) {
            return this.__get__(args.get(0), (org.python.types.Type) args.get(1));
        } else {
            throw new org.python.exceptions.RuntimeError("Descriptor method __get__ takes exactly 2 arguments (" + args.size() + " given).");
        }
    }

    public org.python.Object __get__(org.python.Object instance, org.python.types.Type klass) {
        return this;
    }

    public void __setattr__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __setattr__ doesn't take keyword arguments");
        }
        if (args.size() == 2) {
            if (args.get(0) instanceof org.python.types.Str) {
                this.__setattr__(((org.python.types.Str) args.get(0)).value, args.get(1));
            } else {
                throw new org.python.exceptions.TypeError("setattr(): attribute name must be string");
            }
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 2 arguments, got " + args.size());
        }
    }

    public void __setattr__(org.python.Object name, org.python.Object value) {
        if (name instanceof org.python.types.Str) {
            this.__setattr__(((org.python.types.Str) name).value, value);
        } else {
            throw new org.python.exceptions.TypeError("setattr(): attribute name must be string");
        }
    }

    public void __setattr__(java.lang.String name, org.python.Object value) {
        // The base object can't have attribute set on it unless the attribute already exists.
        if (this.getClass() == org.python.types.Object.class) {
            if (this.attrs.get(name) == null) {
                throw new org.python.exceptions.AttributeError(this, name);
            }
        }
        attrs.put(name, value);

        // If there is a native field of the same name, set it.
        try {
            java.lang.reflect.Field field = this.getClass().getField(name);
            field.set(this, value);
        } catch (NoSuchFieldException e) {
            // System.out.println("Not a native field");
        } catch (IllegalAccessException e) {
            throw new org.python.exceptions.RuntimeError("Illegal access to native field " + name);
        }
    }

    public void __delattr__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __delattr__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            if (args.get(0) instanceof org.python.types.Str) {
                this.__delattr__(((org.python.types.Str) args.get(0)).value);
            } else {
                throw new org.python.exceptions.TypeError("delattr(): attribute name must be string");
            }
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public void __delattr__(org.python.Object name) {
        if (name instanceof org.python.types.Str) {
            this.__delattr__(((org.python.types.Str) name).value);
        } else {
            throw new org.python.exceptions.TypeError("deltattr(): attribute name must be string");
        }
    }

    public void __delattr__(java.lang.String name) {
        org.python.Object result = attrs.remove(name);
        if (result == null) {
            throw new org.python.exceptions.AttributeError(this, name);
        }
    }

    public org.python.types.List __dir__() {
        throw new org.python.exceptions.NotImplementedError("'" + org.Python.typeName(this) + ".__dir__' has not been implemented");
    }


    /**
     * Section 3.3.4 - Customizing instance and subclass checks
     */
    public org.python.Object __instancecheck__(org.python.Object instance) {
        throw new org.python.exceptions.AttributeError(this, "__instancecheck__");
    }

    public org.python.Object __subclasscheck__(org.python.Object subclass) {
        throw new org.python.exceptions.AttributeError(this, "__subclasscheck__");
    }


    /**
     * Section 3.3.5 - Emulating callable objects
     */
    public org.python.Object __call__(org.python.Object... args) {
        throw new org.python.exceptions.AttributeError(this, "__call__");
    }


    /**
     * Section 3.3.6 - Emulating container types
     */

    public org.python.types.Int __len__() {
        throw new org.python.exceptions.AttributeError(this, "__len__");
    }

    public org.python.types.Int __length_hint__() {
        throw new org.python.exceptions.AttributeError(this, "__length_hint__");
    }


    public org.python.Object __getitem__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __getitem__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            return this.__getitem__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __getitem__(org.python.Object index) {
        System.out.println("GETITEM " + this);
        throw new org.python.exceptions.AttributeError(this, "__getitem__");
    }

    public org.python.Object __missing__(org.python.Object key) {
        throw new org.python.exceptions.AttributeError(this, "__missing__");
    }


    public void __setitem__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __setitem__ doesn't take keyword arguments");
        }
        if (args.size() == 2) {
            this.__setitem__(args.get(0), args.get(1));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 2 arguments, got " + args.size());
        }
    }

    public void __setitem__(org.python.Object index, org.python.Object value) {
        throw new org.python.exceptions.AttributeError(this, "__setitem__");
    }

    public void __setitem__(int index, org.python.Object value) {
        this.__setitem__(new org.python.types.Int(index), value);
    }


    public void __delitem__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __delitem__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            this.__delitem__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public void __delitem__(org.python.Object index) {
        throw new org.python.exceptions.AttributeError(this, "__delitem__");
    }

    public void __delitem__(int index) {
        this.__delitem__(new org.python.types.Int(index));
    }


    public org.python.Iterable __iter__() {
        throw new org.python.exceptions.AttributeError(this, "__iter__");
    }

    public org.python.Iterable __reversed__() {
        throw new org.python.exceptions.AttributeError(this, "__reversed__");
    }

    public org.python.types.Bool __contains__(org.python.Object item) {
        throw new org.python.exceptions.AttributeError(this, "__contains__");
    }


    /**
     * Section 3.3.7 - Emulating numeric types
     */

    public org.python.Object __add__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __add__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            return this.__add__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __add__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for +: '" + org.Python.typeName(this) + "' and '" + org.Python.typeName(other) + "'");
    }


    public org.python.Object __sub__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __sub__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            return this.__sub__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __sub__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for -: '" + org.Python.typeName(this) + "' and '" + org.Python.typeName(other) + "'");
    }


    public org.python.Object __mul__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __mul__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            return this.__mul__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __mul__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for *: '" + org.Python.typeName(this) + "' and '" + org.Python.typeName(other) + "'");
    }


    public org.python.Object __truediv__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __truediv__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            return this.__truediv__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __truediv__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for /: '" + org.Python.typeName(this) + "' and '" + org.Python.typeName(other) + "'");
    }


    public org.python.Object __floordiv__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __floordiv__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            return this.__floordiv__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __floordiv__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for //: '" + org.Python.typeName(this) + "' and '" + org.Python.typeName(other) + "'");
    }


    public org.python.Object __mod__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __mod__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            return this.__mod__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __mod__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for %: '" + org.Python.typeName(this) + "' and '" + org.Python.typeName(other) + "'");
    }


    public org.python.Object __divmod__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __divmod__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            return this.__divmod__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __divmod__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__divmod__");
    }


    public org.python.Object __pow__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __pow__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            return this.__pow__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __pow__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for ** or pow(): '" + org.Python.typeName(this) + "' and '" + org.Python.typeName(other) + "'");
    }

    public org.python.Object __pow__(org.python.Object other, org.python.Object modulus) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for ** or pow(): '" + org.Python.typeName(this) + "', '" + org.Python.typeName(other) + "', '" + org.Python.typeName(modulus) + "'");
    }


    public org.python.Object __lshift__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __lshift__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            return this.__lshift__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __lshift__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for <<: '" + org.Python.typeName(this) + "' and '" + org.Python.typeName(other) + "'");
    }


    public org.python.Object __rshift__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rshift__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            return this.__rshift__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __rshift__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for >>: '" + org.Python.typeName(this) + "' and '" + org.Python.typeName(other) + "'");
    }


    public org.python.Object __and__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __and__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            return this.__and__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __and__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for &: '" + org.Python.typeName(this) + "' and '" + org.Python.typeName(other) + "'");
    }


    public org.python.Object __xor__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __xor__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            return this.__xor__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __xor__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for ^: '" + org.Python.typeName(this) + "' and '" + org.Python.typeName(other) + "'");
    }


    public org.python.Object __or__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __or__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            return this.__or__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __or__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for |: '" + org.Python.typeName(this) + "' and '" + org.Python.typeName(other) + "'");
    }


    public org.python.Object __radd__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __radd__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            return this.__radd__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __radd__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for + (reversed): '" + org.Python.typeName(other) + "' and '" + org.Python.typeName(this) + "'");
    }


    public org.python.Object __rsub__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rsub__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            return this.__rsub__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __rsub__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for - (reversed): '" + org.Python.typeName(other) + "' and '" + org.Python.typeName(this) + "'");
    }


    public org.python.Object __rmul__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rmul__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            return this.__rmul__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __rmul__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for * (reversed): '" + org.Python.typeName(other) + "' and '" + org.Python.typeName(this) + "'");
    }


    public org.python.Object __rtruediv__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rtruediv__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            return this.__rtruediv__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __rtruediv__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for / (reversed): '" + org.Python.typeName(other) + "' and '" + org.Python.typeName(this) + "'");
    }


    public org.python.Object __rfloordiv__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rfloordiv__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            return this.__rfloordiv__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __rfloordiv__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for // (reversed): '" + org.Python.typeName(other) + "' and '" + org.Python.typeName(this) + "'");
    }


    public org.python.Object __rmod__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rmod__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            return this.__rmod__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __rmod__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for % (reversed): '" + org.Python.typeName(other) + "' and '" + org.Python.typeName(this) + "'");
    }


    public org.python.Object __rdivmod__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rdivmod__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            return this.__rdivmod__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __rdivmod__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for divmod (reversed): '" + org.Python.typeName(other) + "' and '" + org.Python.typeName(this) + "'");
    }


    public org.python.Object __rpow__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rpow__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            return this.__rpow__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __rpow__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for ^ or pow() (reversed): '" + org.Python.typeName(other) + "' and '" + org.Python.typeName(this) + "'");
    }


    public org.python.Object __rlshift__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rlshift__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            return this.__rlshift__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __rlshift__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for << (reversed): '" + org.Python.typeName(other) + "' and '" + org.Python.typeName(this) + "'");
    }


    public org.python.Object __rrshift__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rrshift__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            return this.__rrshift__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __rrshift__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for >> (reversed): '" + org.Python.typeName(other) + "' and '" + org.Python.typeName(this) + "'");
    }


    public org.python.Object __rand__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rand__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            return this.__rand__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __rand__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for & (reversed): '" + org.Python.typeName(other) + "' and '" + org.Python.typeName(this) + "'");
    }


    public org.python.Object __rxor__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rxor__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            return this.__rxor__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __rxor__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for ^ (reversed): '" + org.Python.typeName(other) + "' and '" + org.Python.typeName(this) + "'");
    }


    public org.python.Object __ror__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __ror__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            return this.__ror__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __ror__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for | (reversed): '" + org.Python.typeName(other) + "' and '" + org.Python.typeName(this) + "'");
    }


    public void __iadd__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __iadd__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            this.__iadd__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public void __iadd__(org.python.Object other) {
        try {
            this.setValue(this.__add__(other));
        } catch (org.python.exceptions.TypeError e) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for +=: '" + org.Python.typeName(this) + "' and '" + org.Python.typeName(other) + "'");
        }
    }


    public void __isub__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __isub__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            this.__isub__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public void __isub__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__isub__");
    }


    public void __imul__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __imul__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            this.__imul__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public void __imul__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__imul__");
    }


    public void __itruediv__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __itruediv__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            this.__itruediv__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public void __itruediv__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__itruediv__");
    }


    public void __ifloordiv__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __ifloordiv__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            this.__ifloordiv__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public void __ifloordiv__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__ifloordiv__");
    }


    public void __imod__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __imod__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            this.__imod__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public void __imod__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__imod__");
    }


    public void __ipow__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __ipow__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            this.__ipow__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public void __ipow__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__ipow__");
    }


    public void __ilshift__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __ilshift__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            this.__ilshift__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public void __ilshift__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__ilshift__");
    }


    public void __irshift__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __irshift__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            this.__irshift__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public void __irshift__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__irshift__");
    }


    public void __iand__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __iand__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            this.__iand__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public void __iand__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__iand__");
    }


    public void __ixor__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __ixor__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            this.__ixor__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public void __ixor__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__ixor__");
    }


    @org.python.Method(
        __doc__ = ""
    )
    public void __ior__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __ior__ doesn't take keyword arguments");
        }
        if (args.size() == 1) {
            this.__ior__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public void __ior__(org.python.Object other) {
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
        return new org.python.types.Bool(!this.__bool__().value);
    }

    public org.python.Object __complex__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.AttributeError(this, "__complex__");
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
    public org.python.Object __enter__() {
        throw new org.python.exceptions.AttributeError(this, "__enter__");
    }

    public org.python.Object __exit__(org.python.Object exc_type, org.python.Object exc_value, org.python.Object traceback) {
        throw new org.python.exceptions.AttributeError(this, "__exit__");
    }

}
