package org.python.types;

public class Type extends org.python.types.Object implements org.python.Callable {
    public enum Origin {PLACEHOLDER, BUILTIN, PYTHON, JAVA, EXTENSION};
    public java.lang.String PYTHON_TYPE_NAME;
    private static java.util.Map<java.lang.Class, org.python.types.Type> known_types = new java.util.HashMap<java.lang.Class, org.python.types.Type>();

    public java.lang.reflect.Constructor constructor;
    public java.lang.Class klass;
    public org.python.types.Type __base__;
    public org.python.types.Tuple __bases__;

    /**
     * Factory method to obtain Python classes from their Java counterparts
     */
    public static org.python.types.Type pythonType(java.lang.Class java_class) {
        // Look up the class in the known types table.
        org.python.types.Type python_type = known_types.get(java_class);
        if (python_type == null) {
            // If type isn't known, create and store a placeholder
            // so that recursive lookups have a termination condition.
            PlaceholderType placeholder = new PlaceholderType(java_class);
            known_types.put(java_class, placeholder);

            // Construct the new type, and store it in the types table.
            // Any type implementing org.python.Object is a Python type;
            // otherwise, wrap it as a native Java type.
            if (org.python.Object.class.isAssignableFrom(java_class)) {
                if (java_class.getName().startsWith("org.python.types.")) {
                    python_type = new org.python.types.Type(Origin.BUILTIN, java_class);
                } else {
                    python_type = new org.python.types.Type(Origin.PYTHON, java_class);
                }
            } else {
                try {
                    java_class.getDeclaredField("__VOC__");
                    python_type = new org.python.java.Type(Origin.EXTENSION, java_class);
                } catch (NoSuchFieldException e) {
                    python_type = new org.python.java.Type(Origin.JAVA, java_class);
                }
            }
            known_types.put(java_class, python_type);

            // Since we have a freshly created type, resolve
            // any placeholders that referenced this type.
            // These will have been created as a consequence of
            // calling the constructor for this type.
            placeholder.resolve(python_type);
        }
        return python_type;
    }

    public static org.python.types.Type pythonType(java.lang.String java_class_name) {
        try {
            return pythonType(java.lang.Class.forName(java_class_name.replace("/", ".")));
        } catch (ClassNotFoundException e) {
            throw new org.python.exceptions.RuntimeError("Unknown Class " + java_class_name);
        }
    }

    /**
     * Convert a Java instance into the a Python-wrapped type.
     *
     * This means converting:
     *    * `null` into a None
     *    * Returning any object that already implements org.python.Object as itself.
     *    * Wrapping any other object in a org.python.java.Object wrapper.
     */
    public static org.python.Object toPython(java.lang.Object value) {
        if (value == null) {
            return org.python.types.NoneType.NONE;
        } else {
            if (   value.getClass() == java.lang.Boolean.TYPE
                || value.getClass() == java.lang.Boolean.class) {
                return new org.python.types.Bool((java.lang.Boolean) value);
            } else if (   value.getClass() == java.lang.Byte.TYPE
                       || value.getClass() == java.lang.Byte.class) {
                return new org.python.types.Int((java.lang.Byte) value);
            } else if (   value.getClass() == java.lang.Character.TYPE
                       || value.getClass() == java.lang.Character.class) {
                return new org.python.types.Str((java.lang.Character) value);
            } else if (   value.getClass() == java.lang.Short.TYPE
                       || value.getClass() == java.lang.Short.class) {
                return new org.python.types.Int((java.lang.Short) value);
            } else if (   value.getClass() == java.lang.Integer.TYPE
                       || value.getClass() == java.lang.Integer.class) {
                return new org.python.types.Int((java.lang.Integer) value);
            } else if (   value.getClass() == java.lang.Long.TYPE
                       || value.getClass() == java.lang.Long.class) {
                return new org.python.types.Int((java.lang.Long) value);
            } else if (   value.getClass() == java.lang.Float.TYPE
                       || value.getClass() == java.lang.Float.class) {
                return new org.python.types.Float((java.lang.Float) value);
            } else if (   value.getClass() == java.lang.Double.TYPE
                       || value.getClass() == java.lang.Double.class) {
                return new org.python.types.Float((java.lang.Double) value);
            } else if (value.getClass() == java.lang.String.class) {
                return new org.python.types.Str((java.lang.String) value);
            } else if (org.python.Object.class.isAssignableFrom(value.getClass())) {
                return (org.python.Object) value;
            } else {
                return new org.python.java.Object(value);
            }
        }
    }


    /**
     * A utility method to update the internal value of this object.
     *
     * Used by __i*__ operations to do an in-place operation.
     * obj must be of type org.python.types.Type
     */
    void setValue(org.python.Object obj) {
        this.klass = ((org.python.types.Type) obj).klass;
    }

    public Type(Origin origin, java.lang.Class klass) {
        super(origin, null);

        if (origin != Origin.PLACEHOLDER) {
            this.klass = klass;

            this.attrs.put("__name__", new org.python.types.Str(this.klass.getName()));
            this.attrs.put("__qualname__", new org.python.types.Str(this.klass.getName()));
            // this.attrs.put("__module__", );
        }

        if (origin == Origin.BUILTIN) {
            org.Python.initializeModule(klass, this.attrs);
        } else if (origin == Origin.PYTHON || origin == Origin.EXTENSION) {
            try {
                this.constructor = this.klass.getConstructor(org.python.Object[].class, java.util.Map.class);
            } catch (java.lang.NoSuchMethodException e) {
                this.constructor = null;
            }
        }
    }

    public Type(java.lang.Class klass) {
        this(Origin.PYTHON, klass);
    }

    public void add_reference(org.python.Object instance) {
        throw new java.lang.RuntimeException("Can't add reference to normal type");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Str __repr__() {
        return new org.python.types.Str(String.format("<class '%s'>", org.Python.typeName(this.klass)));
    }

    public org.python.Object __getattribute_null(java.lang.String name) {
        // System.out.println("GETATTRIBUTE CLASS " + this.klass.getName() + " " + name);
        // System.out.println("CLASS ATTRS " + this.attrs);
        org.python.Object value = this.attrs.get(name);

        if (value == null) {
            // The class attributes didn't contain a value for the attribute
            // name. Introspect on the object class to see if a field
            // with the given name exists, caching either the Field instance,
            // or an AttributeError representation of the NoSuchFieldException.
            try {
                value = new org.python.java.Field(this.klass.getDeclaredField(name));
            } catch (java.lang.NoSuchFieldException e) {
                value = new org.python.exceptions.AttributeError(this.klass, name);
            }
            this.attrs.put(name, value);
        }

        // If the result of the lookup is an AttributeError, there's
        // no local field; so defer to the base type.
        if (value instanceof org.python.exceptions.AttributeError) {
            if (this.__base__ == null) {
                value = null;
            } else {
                value = this.__base__.__getattribute_null(name);
            }
        }
        // System.out.println("GETATTRIBUTE CLASS " + this.klass.getName() + " " + name + " = " + value);
        return value;
    }

    public void __setattr__(java.lang.String name, org.python.Object value) {
        if (!this.__setattr_null(name, value)) {
            throw new org.python.exceptions.TypeError("can't set attributes of built-in/extension type '" + org.Python.typeName(this.klass) + "'");
        }
    }

    public boolean __setattr_null(java.lang.String name, org.python.Object value) {
        // System.out.println("SETATTRIBUTE TYPE " + name + " = " + value);
        // System.out.println("class attrs = " + this.attrs);

        // Can't set attributes of builtin types.
        if (this.origin == Origin.BUILTIN) {
            return false;
        }

        this.attrs.put(name, value);
        return true;
    }

    public org.python.Object invoke(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        try {
            // org.Python.debug("Constructor:", this.constructor);
            // org.Python.debug("     Origin:", this.origin);
            // org.Python.debug("       Type:", this);
            // for (org.python.Object arg: args) {
            //     org.Python.debug("            arg: ", arg);
            // }
            // org.Python.debug("         kwargs: ", kwargs);

            if (this.constructor != null) {
                return (org.python.Object) this.constructor.newInstance(args, kwargs);
            } else {
                throw new org.python.exceptions.RuntimeError("No Python-compatible constructor for type " + this.klass);
            }
        } catch (java.lang.IllegalAccessException e) {
            throw new org.python.exceptions.RuntimeError("Illegal access to Java constructor " + this.constructor);
        } catch (java.lang.reflect.InvocationTargetException e) {
            try {
                // e.getTargetException().printStackTrace();
                // If the Java method raised an Python exception, re-raise that
                // exception as-is. If it wasn't a Python exception, wrap it
                // as one and continue.
                throw (org.python.exceptions.BaseException) e.getCause();
            } catch (ClassCastException java_e) {
                throw new org.python.exceptions.RuntimeError(e.getCause().toString());
            }
        } catch (java.lang.InstantiationException e) {
            throw new org.python.exceptions.RuntimeError(e.getCause().toString());
        } finally {
        //     System.out.println("CONSTRUCTOR DONE");
        }
    }
}
