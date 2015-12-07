package org.python.types;


public class Object implements org.python.Object {
    public java.util.Map<java.lang.String, org.python.Object> attrs;
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
     * the object; when wrapping Java objects, the native class of the object is used.
     */
    protected Object(org.python.types.Type.Origin origin, java.lang.Class klass) {
        if (origin != org.python.types.Type.Origin.PLACEHOLDER) {
            this.attrs = new java.util.HashMap<java.lang.String, org.python.Object>();
            if (klass == null) {
                klass = this.getClass();
            }
            this.__new__(org.python.types.Type.pythonType(klass));
        }
    }

    public Object() {
        this(org.python.types.Type.Origin.PYTHON, null);
    }

    /**
     * Proxy Java object methods onto their Python counterparts.
     */
    public boolean equals(java.lang.Object other) {
        try {
            java.util.List<org.python.Object> eq_args = new java.util.ArrayList<org.python.Object>(1);
            eq_args.add((org.python.types.Object) other);
            return ((org.python.types.Bool) __eq__(eq_args, null, null, null)).value;
        } catch (ClassCastException e) {
            throw new org.python.exceptions.RuntimeError("Can't compare a Python object with non-Python object.");
        }
    }

    public int compareTo(java.lang.Object other) {
        try {
            if (((org.python.types.Bool) this.__lt__((org.python.Object) other)).value) {
                return -1;
            }
            else if (((org.python.types.Bool) this.__gt__((org.python.Object) other)).value) {
                return 1;
            }
            return 0;
        } catch (ClassCastException e) {
            throw new org.python.exceptions.RuntimeError("Can't compare a Python object with non-Python object.");
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public java.lang.String toString() {
        return ((org.python.types.Str) this.__str__()).value;
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
    public org.python.Object __new__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __lt__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        org.python.types.Type cls = (org.python.types.Type) args.get(0);
        this.attrs.put("__class__", cls);
        if (cls.origin == org.python.types.Type.Origin.PLACEHOLDER) {
            cls.add_reference(this);
        }
        return cls;
    }

    public org.python.Object __new__(org.python.types.Type klass) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(klass);
        return this.__new__(args, null, null, null);
    }

    // public void __init__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
    //     throw new org.python.exceptions.AttributeError(this, "__init__");
    // }

    @org.python.Method(
        __doc__ = "Destroy an existing object. See help(type) for accurate signature."
    )
    public void __del__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.AttributeError(this, "__del__");
    }

    public void __del__() {
        this.__del__(null, null, null, null);
    }

    @org.python.Method(
        __doc__ = "Return repr(self)."
    )
    public org.python.Object __repr__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __repr__ doesn't take keyword arguments");
        } else if (args != null && args.size() != 0) {
            throw new org.python.exceptions.TypeError("Expected 0 arguments, got " + args.size());
        }

        return new org.python.types.Str(String.format("<%s object at 0x%x>", this.typeName(), this.hashCode()));
    }

    public org.python.Object __repr__() {
        return this.__repr__(null, null, null, null);
    }

    @org.python.Method(
        __doc__ = "Return str(self)."
    )
    public org.python.Object __str__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __str__ doesn't take keyword arguments");
        } else if (args != null && args.size() != 0) {
            throw new org.python.exceptions.TypeError("Expected 0 arguments, got " + args.size());
        }

        return this.__repr__(null, null, null, null);
    }

    public org.python.Object __str__() {
        return this.__str__(null, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __bytes__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.AttributeError(this, "__bytes__");
    }

    public org.python.Object __bytes__() {
        return this.__bytes__(null, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __format__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("'" + this.typeName() + ".__format__' has not been implemented");
    }

    public org.python.Object __format__(org.python.Object format) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add((org.python.types.Object) format);
        return this.__format__(args, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __lt__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __lt__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        throw new org.python.exceptions.NotImplementedError("'" + this.typeName() + ".__lt__' has not been implemented");
    }

    public org.python.Object __lt__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add((org.python.types.Object) other);
        return this.__lt__(args, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __le__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __le__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        throw new org.python.exceptions.NotImplementedError("'" + this.typeName() + ".__le__' has not been implemented");
    }

    public org.python.Object __le__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add((org.python.types.Object) other);
        return this.__le__(args, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __eq__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __eq__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        return new org.python.types.Bool(System.identityHashCode(this) == System.identityHashCode(args.get(0)));
    }

    public org.python.Object __eq__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add((org.python.types.Object) other);
        return this.__eq__(args, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __ne__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __ne__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        return new org.python.types.Bool(System.identityHashCode(this) != System.identityHashCode(args.get(0)));
    }

    public org.python.Object __ne__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add((org.python.types.Object) other);
        return this.__ne__(args, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __gt__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __gt__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        throw new org.python.exceptions.NotImplementedError("'" + this.typeName() + ".__gt__' has not been implemented");
    }

    public org.python.Object __gt__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add((org.python.types.Object) other);
        return this.__gt__(args, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __ge__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __ge__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        throw new org.python.exceptions.NotImplementedError("'" + this.typeName() + ".__ge__' has not been implemented");
    }

    public org.python.Object __ge__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add((org.python.types.Object) other);
        return this.__ge__(args, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __hash__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __hash__ doesn't take keyword arguments");
        } else if (args != null && args.size() != 0) {
            throw new org.python.exceptions.TypeError("Expected 0 arguments, got " + args.size());
        }

        return new org.python.types.Int(this.hashCode());
    }

    public org.python.Object __hash__() {
        return this.__hash__(null, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __bool__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.AttributeError(this, "__bool__");
    }

    public org.python.Object __bool__() {
        return this.__bool__(null, null, null, null);
    }

    /**
     * Section 3.3.2 - Emulating container types
     */

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __getattr__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __getattr__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        } else if (!(args.get(0) instanceof org.python.types.Str)) {
            throw new org.python.exceptions.TypeError("getattr(): attribute name must be string");
        }

        throw new org.python.exceptions.AttributeError(this, "__getattr__");
    }

    public org.python.Object __getattr__(java.lang.String name) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(new org.python.types.Str(name));
        return this.__getattr__(args, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __getattribute__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __getattribute__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        } else if (!(args.get(0) instanceof org.python.types.Str)) {
            throw new org.python.exceptions.TypeError("__getattribute__(): attribute name must be string");
        }

        java.lang.String name = ((org.python.types.Str) args.get(0)).value;

        // Look for local instance attributes first
        // System.out.println("ATTRS " + this.attrs);
        org.python.Object value = this.attrs.get(name);
        if (value == null) {
            try {
                // No instance attribute; look for a class attribute.
                try {

                    org.python.types.Type klass = (org.python.types.Type) this.attrs.get("__class__");
                    value = klass.__getattribute__(args, kwargs, default_args, default_kwargs);
                } catch (org.python.exceptions.AttributeError e) {
                    // No class attribute; Try the __getattr__ helper.
                    value = this.__getattr__(name);
                }
            } catch (org.python.exceptions.AttributeError e) {
                throw new org.python.exceptions.AttributeError(this, name);
            }
        }

        return value.__get__(this, org.python.types.Type.pythonType(this.getClass()));
    }

    public org.python.Object __getattribute__(java.lang.String name) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(new org.python.types.Str(name));
        return this.__getattribute__(args, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __get__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.RuntimeError("Descriptor method __get__ does not accept keyword arguments.");
        } else if (args == null || args.size() != 2) {
            throw new org.python.exceptions.RuntimeError("Descriptor method __get__ takes exactly 2 arguments (" + args.size() + " given).");
        }

        return this;
    }

    public org.python.Object __get__(org.python.Object instance, org.python.types.Type klass) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(2);
        args.add(instance);
        args.add(klass);
        return this.__get__(args, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public void __setattr__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __setattr__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 2) {
            throw new org.python.exceptions.TypeError("Expected 2 arguments, got " + args.size());
        } else if (!(args.get(0) instanceof org.python.types.Str)) {
            throw new org.python.exceptions.TypeError("setattr(): attribute name must be string");
        }

        java.lang.String name = ((org.python.types.Str) args.get(0)).value;
        org.python.Object value = args.get(1);

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

    public void __setattr__(java.lang.String name, org.python.Object value) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(2);
        args.add(new org.python.types.Str(name));
        args.add(value);
        this.__setattr__(args, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public void __delattr__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __delattr__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        } else if (!(args.get(0) instanceof org.python.types.Str)) {
            throw new org.python.exceptions.TypeError("delattr(): attribute name must be string");
        }

        java.lang.String name = ((org.python.types.Str) args.get(0)).value;
        org.python.Object result = attrs.remove(name);
        if (result == null) {
            throw new org.python.exceptions.AttributeError(this, name);
        }
    }

    public void __delattr__(java.lang.String name) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(new org.python.types.Str(name));
        this.__delattr__(args, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __dir__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __dir__ doesn't take keyword arguments");
        } else if (args != null && args.size() != 0) {
            throw new org.python.exceptions.TypeError("Expected 0 arguments, got " + args.size());
        }

        org.python.types.List names = new org.python.types.List(new java.util.ArrayList(this.attrs.keySet()));
        org.python.types.List cls_names = (org.python.types.List) this.attrs.get("__class__").__dir__(null, null, null, null);

        java.util.List<org.python.Object> extend_args = new java.util.ArrayList<org.python.Object>(1);
        extend_args.add(cls_names);

        names.extend(extend_args, null, null, null);
        names.sort(null, null, null, null);
        return names;
    }

    public org.python.Object __dir__() {
        return this.__dir__(null, null, null, null);
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

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __len__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.AttributeError(this, "__len__");
    }

    public org.python.Object __len__() {
        return this.__len__(null, null, null, null);
    }

    public org.python.Object __length_hint__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.AttributeError(this, "__length_hint__");
    }


    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __getitem__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __getitem__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            return this.__getitem__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public org.python.Object __getitem__(org.python.Object index) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(index);
        return this.__getitem__(args, null, null, null);
    }

    public org.python.Object __missing__(org.python.Object key) {
        throw new org.python.exceptions.AttributeError(this, "__missing__");
    }


    @org.python.Method(
        __doc__ = ""
    )
    public void __setitem__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __setitem__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 2) {
            throw new org.python.exceptions.TypeError("Expected 2 arguments, got " + args.size());
        }
        throw new org.python.exceptions.AttributeError(this, "__setitem__");
    }

    public void __setitem__(org.python.Object index, org.python.Object value) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(index);
        args.add(value);
        this.__setitem__(args, null, null, null);
    }

    public void __setitem__(int index, org.python.Object value) {
        this.__setitem__(new org.python.types.Int(index), value);
    }


    @org.python.Method(
        __doc__ = ""
    )
    public void __delitem__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __delitem__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            this.__delitem__(args.get(0));
        } else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public void __delitem__(org.python.Object index) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(index);
        this.__getitem__(args, null, null, null);
    }

    public void __delitem__(int index) {
        this.__delitem__(new org.python.types.Int(index));
    }


    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Iterable __iter__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.AttributeError(this, "__iter__");
    }

    public org.python.Iterable __iter__() {
        return this.__iter__(null, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Iterable __reversed__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.AttributeError(this, "__reversed__");
    }

    public org.python.Iterable __reversed__() {
        return this.__reversed__(null, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __contains__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __contains__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        throw new org.python.exceptions.AttributeError(this, "__contains__");
    }

    public org.python.Object __contains__(org.python.Object item) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(item);
        return this.__contains__(args, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __not_contains__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __not_contains__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        throw new org.python.exceptions.AttributeError(this, "__not_contains__");
    }

    public org.python.Object __not_contains__(org.python.Object item) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(item);
        return this.__not_contains__(args, null, null, null);
    }

    /**
     * Section 3.3.7 - Emulating numeric types
     */

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __add__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __add__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        org.python.Object other = args.get(0);
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for +: '" + this.typeName() + "' and '" + other.typeName() + "'");
    }

    public org.python.Object __add__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        return this.__add__(args, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __sub__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __sub__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        org.python.Object other = args.get(0);
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for -: '" + this.typeName() + "' and '" + other.typeName() + "'");
    }

    public org.python.Object __sub__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        return this.__sub__(args, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __mul__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __mul__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        org.python.Object other = args.get(0);
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for *: '" + this.typeName() + "' and '" + other.typeName() + "'");
    }

    public org.python.Object __mul__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        return this.__mul__(args, null, null, null);
    }


    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __truediv__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __truediv__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        org.python.Object other = args.get(0);
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for /: '" + this.typeName() + "' and '" + other.typeName() + "'");
    }

    public org.python.Object __truediv__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        return this.__truediv__(args, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __floordiv__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __floordiv__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        org.python.Object other = args.get(0);
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for //: '" + this.typeName() + "' and '" + other.typeName() + "'");
    }

    public org.python.Object __floordiv__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        return this.__floordiv__(args, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __mod__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __mod__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        org.python.Object other = args.get(0);
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for %: '" + this.typeName() + "' and '" + other.typeName() + "'");
    }

    public org.python.Object __mod__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        return this.__mod__(args, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __divmod__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __divmod__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        org.python.Object other = args.get(0);
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for divmod(): '" + this.typeName() + "' and '" + other.typeName() + "'");
    }

    public org.python.Object __divmod__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        return this.__divmod__(args, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __pow__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __pow__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        org.python.Object other = args.get(0);
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for ** or pow(): '" + this.typeName() + "' and '" + other.typeName() + "'");
    }

    public org.python.Object __pow__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        return this.__pow__(args, null, null, null);
    }

    public org.python.Object __pow__(org.python.Object other, org.python.Object modulus) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        args.add(modulus);
        return this.__pow__(args, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __lshift__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __lshift__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        org.python.Object other = args.get(0);
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for <<: '" + this.typeName() + "' and '" + other.typeName() + "'");
    }

    public org.python.Object __lshift__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        return this.__lshift__(args, null, null, null);
    }


    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rshift__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rshift__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        org.python.Object other = args.get(0);
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for >>: '" + this.typeName() + "' and '" + other.typeName() + "'");
    }

    public org.python.Object __rshift__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        return this.__rshift__(args, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __and__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __and__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        org.python.Object other = args.get(0);
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for &: '" + this.typeName() + "' and '" + other.typeName() + "'");
    }

    public org.python.Object __and__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        return this.__and__(args, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __xor__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __xor__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        org.python.Object other = args.get(0);
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for ^: '" + this.typeName() + "' and '" + other.typeName() + "'");
    }

    public org.python.Object __xor__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        return this.__xor__(args, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __or__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __or__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        org.python.Object other = args.get(0);
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for |: '" + this.typeName() + "' and '" + other.typeName() + "'");
    }

    public org.python.Object __or__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        return this.__or__(args, null, null, null);
    }


    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __radd__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __radd__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        throw new org.python.exceptions.AttributeError(this, "__radd__");
    }

    public org.python.Object __radd__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        return this.__radd__(args, null, null, null);
    }


    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rsub__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rsub__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        throw new org.python.exceptions.AttributeError(this, "__rsub__");
    }

    public org.python.Object __rsub__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        return this.__rsub__(args, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rmul__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rmul__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        throw new org.python.exceptions.AttributeError(this, "__rmul__");
    }

    public org.python.Object __rmul__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        return this.__rmul__(args, null, null, null);
    }


    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rtruediv__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rtruediv__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        throw new org.python.exceptions.AttributeError(this, "__rtruediv__");
    }

    public org.python.Object __rtruediv__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        return this.__rtruediv__(args, null, null, null);
    }


    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rfloordiv__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rfloordiv__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        throw new org.python.exceptions.AttributeError(this, "__rfloordiv__");
    }

    public org.python.Object __rfloordiv__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        return this.__rfloordiv__(args, null, null, null);
    }


    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rmod__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rmod__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        throw new org.python.exceptions.AttributeError(this, "__rmod__");
    }

    public org.python.Object __rmod__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        return this.__rmod__(args, null, null, null);
    }


    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rdivmod__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rdivmod__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        throw new org.python.exceptions.AttributeError(this, "__rdivmod__");
    }

    public org.python.Object __rdivmod__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        return this.__rdivmod__(args, null, null, null);
    }


    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rpow__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rpow__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        throw new org.python.exceptions.AttributeError(this, "__rpow__");
    }

    public org.python.Object __rpow__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        return this.__rpow__(args, null, null, null);
    }


    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rlshift__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rlshift__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        throw new org.python.exceptions.AttributeError(this, "__rlshift__");
    }

    public org.python.Object __rlshift__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        return this.__rlshift__(args, null, null, null);
    }


    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rrshift__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rrshift__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        throw new org.python.exceptions.AttributeError(this, "__rrshift__");
    }

    public org.python.Object __rrshift__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        return this.__rrshift__(args, null, null, null);
    }


    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rand__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rand__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        throw new org.python.exceptions.AttributeError(this, "__rand__");
    }

    public org.python.Object __rand__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        return this.__rand__(args, null, null, null);
    }


    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rxor__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __rxor__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        throw new org.python.exceptions.AttributeError(this, "__rxor__");
    }

    public org.python.Object __rxor__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        return this.__rxor__(args, null, null, null);
    }


    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __ror__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __ror__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        throw new org.python.exceptions.AttributeError(this, "__ror__");
    }

    public org.python.Object __ror__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        return this.__ror__(args, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public void __iadd__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __iadd__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        try {
            this.setValue(this.__add__(args.get(0)));
        } catch (org.python.exceptions.TypeError e) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for +=: '" + this.typeName() + "' and '" + args.get(0).typeName() + "'");
        }
    }

    public void __iadd__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        this.__iadd__(args, null, null, null);
    }


    @org.python.Method(
        __doc__ = ""
    )
    public void __isub__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __isub__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        try {
            this.setValue(this.__sub__(args.get(0)));
        } catch (org.python.exceptions.TypeError e) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for +=: '" + this.typeName() + "' and '" + args.get(0).typeName() + "'");
        }
    }

    public void __isub__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        this.__isub__(args, null, null, null);
    }


    @org.python.Method(
        __doc__ = ""
    )
    public void __imul__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __imul__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        try {
            this.setValue(this.__mul__(args.get(0)));
        } catch (org.python.exceptions.TypeError e) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for +=: '" + this.typeName() + "' and '" + args.get(0).typeName() + "'");
        }
    }

    public void __imul__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        this.__imul__(args, null, null, null);
    }


    @org.python.Method(
        __doc__ = ""
    )
    public void __itruediv__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __itruediv__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        try {
            this.setValue(this.__truediv__(args.get(0)));
        } catch (org.python.exceptions.TypeError e) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for +=: '" + this.typeName() + "' and '" + args.get(0).typeName() + "'");
        }
    }

    public void __itruediv__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        this.__itruediv__(args, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public void __ifloordiv__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __ifloordiv__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        try {
            this.setValue(this.__floordiv__(args.get(0)));
        } catch (org.python.exceptions.TypeError e) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for +=: '" + this.typeName() + "' and '" + args.get(0).typeName() + "'");
        }
    }

    public void __ifloordiv__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        this.__ifloordiv__(args, null, null, null);
    }


    @org.python.Method(
        __doc__ = ""
    )
    public void __imod__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __imod__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        try {
            this.setValue(this.__mod__(args.get(0)));
        } catch (org.python.exceptions.TypeError e) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for +=: '" + this.typeName() + "' and '" + args.get(0).typeName() + "'");
        }
    }

    public void __imod__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        this.__imod__(args, null, null, null);
    }


    @org.python.Method(
        __doc__ = ""
    )
    public void __ipow__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __ipow__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        try {
            this.setValue(this.__pow__(args.get(0)));
        } catch (org.python.exceptions.TypeError e) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for +=: '" + this.typeName() + "' and '" + args.get(0).typeName() + "'");
        }
    }

    public void __ipow__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        this.__ipow__(args, null, null, null);
    }


    @org.python.Method(
        __doc__ = ""
    )
    public void __ilshift__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __ilshift__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        try {
            this.setValue(this.__lshift__(args.get(0)));
        } catch (org.python.exceptions.TypeError e) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for +=: '" + this.typeName() + "' and '" + args.get(0).typeName() + "'");
        }
    }

    public void __ilshift__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        this.__ilshift__(args, null, null, null);
    }


    @org.python.Method(
        __doc__ = ""
    )
    public void __irshift__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __irshift__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        try {
            this.setValue(this.__rshift__(args.get(0)));
        } catch (org.python.exceptions.TypeError e) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for +=: '" + this.typeName() + "' and '" + args.get(0).typeName() + "'");
        }
    }

    public void __irshift__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        this.__irshift__(args, null, null, null);
    }


    @org.python.Method(
        __doc__ = ""
    )
    public void __iand__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __iand__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        try {
            this.setValue(this.__and__(args.get(0)));
        } catch (org.python.exceptions.TypeError e) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for +=: '" + this.typeName() + "' and '" + args.get(0).typeName() + "'");
        }
    }

    public void __iand__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        this.__iand__(args, null, null, null);
    }


    @org.python.Method(
        __doc__ = ""
    )
    public void __ixor__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __ixor__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }

        try {
            this.setValue(this.__xor__(args.get(0)));
        } catch (org.python.exceptions.TypeError e) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for +=: '" + this.typeName() + "' and '" + args.get(0).typeName() + "'");
        }
    }

    public void __ixor__(org.python.Object other) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(other);
        this.__ixor__(args, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public void __ior__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("wrapper __ior__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            this.__ior__(args.get(0));
        }
        else {
            throw new org.python.exceptions.TypeError("Expected 1 arguments, got " + args.size());
        }
    }

    public void __ior__(org.python.Object other) {
        throw new org.python.exceptions.AttributeError(this, "__ior__");
    }


    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __neg__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.AttributeError(this, "__neg__");
    }

    public org.python.Object __neg__() {
        return this.__neg__(null, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __pos__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.AttributeError(this, "__pos__");
    }

    public org.python.Object __pos__() {
        return this.__pos__(null, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __abs__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.AttributeError(this, "__abs__");
    }

    public org.python.Object __abs__() {
        return this.__abs__(null, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __invert__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.AttributeError(this, "__invert__");
    }

    public org.python.Object __invert__() {
        return this.__invert__(null, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __not__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        return new org.python.types.Bool(!((org.python.types.Bool) this.__bool__()).value);
    }

    public org.python.Object __not__() {
        return this.__not__(null, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __complex__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.AttributeError(this, "__complex__");
    }

    public org.python.Object __complex__(org.python.Object real, org.python.Object imag) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(2);
        args.add(real);
        args.add(imag);
        return this.__complex__(null, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __int__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.AttributeError(this, "__int__");
    }

    public org.python.Object __int__() {
        return this.__int__(null, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __float__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.AttributeError(this, "__float__");
    }

    public org.python.Object __float__() {
        return this.__float__(null, null, null, null);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __round__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.AttributeError(this, "__round__");
    }

    public org.python.Object __round__(org.python.Object ndigits) {
        java.util.List<org.python.Object> args = new java.util.ArrayList<org.python.Object>(1);
        args.add(ndigits);
        return this.__round__(args, null, null, null);
    }

    public org.python.Object __round__() {
        return this.__round__(null, null, null, null);
    }

    /**
     * Section 3.3.8 - With statement context
     */
    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __enter__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.AttributeError(this, "__enter__");
    }

    public org.python.Object __enter__() {
        throw new org.python.exceptions.AttributeError(this, "__enter__");
    }
    public org.python.Object __exit__(org.python.Object exc_type, org.python.Object exc_value, org.python.Object traceback) {
        throw new org.python.exceptions.AttributeError(this, "__exit__");
    }

    public org.python.Object __exit__() {
        throw new org.python.exceptions.AttributeError(this, "__exit__");
    }
}
