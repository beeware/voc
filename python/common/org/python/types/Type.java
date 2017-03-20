package org.python.types;

public class Type extends org.python.types.Object implements org.python.Callable {
    public enum Origin {
        PLACEHOLDER,  // Dummy entry to resolve circular dependencies
        BUILTIN,      // A type provided as part of Python itself.
        PYTHON,       // A type defined in Python code
        JAVA,         // A type defined in Java
        EXTENSION     // A type defined in Python, extending a Java base class
    }

    public java.lang.String PYTHON_TYPE_NAME;
    private static java.util.Map<java.lang.Class, org.python.types.Type> known_types = new java.util.HashMap<java.lang.Class, org.python.types.Type>();
    public java.lang.reflect.Constructor constructor;
    public java.lang.Class klass;

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

            // Declare the type, and install it the known types list
            // (Replacing any placeholders)
            python_type = declarePythonType(java_class);

            // Since we have a freshly created type, resolve
            // any placeholders that referenced this type.
            // These will have been created as a consequence of
            // calling the constructor for this type.
            placeholder.resolve(python_type);
        }
        // System.out.println("GOT TYPE " + java_class + " " + python_type.origin);
        return python_type;
    }

    public static org.python.types.Type pythonType(java.lang.String java_class_name) {
        try {
            return pythonType(java.lang.Thread.currentThread().getContextClassLoader().loadClass(java_class_name.replace("/", ".")));
        } catch (ClassNotFoundException e) {
            throw new org.python.exceptions.RuntimeError("Unknown Class " + java_class_name);
        }
    }

    public static org.python.types.Type declarePythonType(
            org.python.Object name,
            org.python.Object bases,
            org.python.Object dict
    ) {
        java.util.Map<org.python.Object, org.python.Object> from_dict = ((org.python.types.Dict) dict).value;
        java.util.Map<java.lang.String, org.python.Object> to_dict = new java.util.HashMap<java.lang.String, org.python.Object>();
        for (org.python.Object k : from_dict.keySet()) {
            to_dict.put(k.toString(), from_dict.get(k));
        }

        return org.python.types.Type.declarePythonType(
                org.python.types.Object.class,
                ((org.python.types.Str) name).value,
                ((org.python.types.Tuple) bases).value,
                to_dict
        );
    }

    public static org.python.types.Type declarePythonType(
            java.lang.String name,
            java.util.List<org.python.Object> bases,
            java.util.Map<java.lang.String, org.python.Object> dict
    ) {
        return org.python.types.Type.declarePythonType(org.python.types.Object.class, name, bases, dict);
    }

    public static org.python.types.Type declarePythonType(
            java.lang.Class java_class
    ) {
        return org.python.types.Type.declarePythonType(java_class, null, null, null);
    }

    public static org.python.types.Type declarePythonType(
            java.lang.Class java_class,
            java.lang.String name,
            java.util.List<org.python.Object> bases,
            java.util.Map<java.lang.String, org.python.Object> dict
    ) {
        org.python.types.Type python_type;
        // System.out.println("DECLARE " + java_class + " as " + name + " with bases " + bases + " and dict " + dict);

        // Construct the new type, and store it in the types table.
        // Any type implementing org.python.Object is a Python type;
        // otherwise, wrap it as a native Java type.
        if (org.python.Object.class.isAssignableFrom(java_class)) {
            if (java_class.getName().startsWith("org.python.types")
                    || java_class.getName().startsWith("org.python.stdlib")) {
                python_type = new org.python.types.Type(Origin.BUILTIN, java_class);
                org.Python.initializeModule(java_class, python_type.__dict__);
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

        // Set the name of the class.
        if (name != null) {
            python_type.PYTHON_TYPE_NAME = name;
        }

        // Set __base__ and __bases__ for the type
        if (bases != null && bases.size() > 0) {
            python_type.__dict__.put("__base__", bases.get(0));
            python_type.__dict__.put("__bases__", new org.python.types.Tuple(bases));
        }

        // Update the dictionary of the type.
        if (dict != null) {
            python_type.__dict__.putAll(dict);
        }

        // Register the type.
        org.python.types.Type placeholder = known_types.put(java_class, python_type);

        if (placeholder != null && placeholder.__dict__ != null) {
            python_type.__dict__.putAll(placeholder.__dict__);
        }

        // System.out.println("FINISHED DECLARING " + java_class + " as " + name + "; " + python_type.__dict__);
        return python_type;
    }

    /**
     * Convert a Java instance into the a Python-wrapped type.
     *
     * This means converting:
     *    * `null` into a None
     *    * Returning any object that already implements org.python.Object as itself.
     *    * Returning the existing VOC wrapper if one exists
     *    * Wrapping any other object in a newly created org.python.java.Object wrapper.
     */
    public static org.python.Object toPython(java.lang.Object value) {
        if (value == null) {
            return org.python.types.NoneType.NONE;
        } else {
            if (value.getClass() == java.lang.Boolean.TYPE
                    || value.getClass() == java.lang.Boolean.class) {
                return new org.python.types.Bool((java.lang.Boolean) value);
            } else if (value.getClass() == java.lang.Byte.TYPE
                    || value.getClass() == java.lang.Byte.class) {
                return new org.python.types.Int((java.lang.Byte) value);
            } else if (value.getClass() == java.lang.Character.TYPE
                    || value.getClass() == java.lang.Character.class) {
                return new org.python.types.Str((java.lang.Character) value);
            } else if (value.getClass() == java.lang.Short.TYPE
                    || value.getClass() == java.lang.Short.class) {
                return new org.python.types.Int((java.lang.Short) value);
            } else if (value.getClass() == java.lang.Integer.TYPE
                    || value.getClass() == java.lang.Integer.class) {
                return new org.python.types.Int((java.lang.Integer) value);
            } else if (value.getClass() == java.lang.Long.TYPE
                    || value.getClass() == java.lang.Long.class) {
                return new org.python.types.Int((java.lang.Long) value);
            } else if (value.getClass() == java.lang.Float.TYPE
                    || value.getClass() == java.lang.Float.class) {
                return new org.python.types.Float((java.lang.Float) value);
            } else if (value.getClass() == java.lang.Double.TYPE
                    || value.getClass() == java.lang.Double.class) {
                return new org.python.types.Float((java.lang.Double) value);
            } else if (value.getClass() == java.lang.String.class) {
                return new org.python.types.Str((java.lang.String) value);
            } else if (org.python.Object.class.isAssignableFrom(value.getClass())) {
                return (org.python.Object) value;
            } else {
                try {
                    // Check to see if a __VOC__ field exists on the object.
                    // If it does, that field will contain the wrapper object.
                    // However, if this is the first time the object has been
                    // referenced (e.g., during construction), we may need to
                    // create the wrapper.
                    java.lang.reflect.Field field = value.getClass().getField("__VOC__");
                    org.python.Object wrapper = (org.python.Object) field.get(value);
                    if (wrapper == null) {
                        wrapper = new org.python.java.Object(value);
                        field.set(value, wrapper);
                    }
                    return wrapper;
                } catch (java.lang.NoSuchFieldException nsf) {
                    return new org.python.java.Object(value);
                } catch (java.lang.IllegalAccessException e) {
                    throw new org.python.exceptions.RuntimeError("Illegal access to __VOC__ attribute");
                }
            }
        }
    }

    public static java.lang.Object toJava(java.lang.Class<?> klass, org.python.Object value) {
        if (value == null) {
            return value;
        } else {
            if (klass == java.lang.Float.TYPE || klass == java.lang.Float.class) {
                return ((java.lang.Number) value.toJava()).floatValue();
            } else if (klass == java.lang.Long.TYPE || klass == java.lang.Long.class) {
                return ((java.lang.Number) value.toJava()).longValue();
            } else if (klass == java.lang.Integer.TYPE || klass == java.lang.Integer.class) {
                return ((java.lang.Number) value.toJava()).intValue();
            } else if (klass == java.lang.Short.TYPE || klass == java.lang.Short.class) {
                return ((java.lang.Number) value.toJava()).shortValue();
            } else if (klass == java.lang.Byte.TYPE || klass == java.lang.Byte.class) {
                return ((java.lang.Number) value.toJava()).byteValue();
            } else {
                return value.toJava();
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
        }

        if (origin == Origin.BUILTIN || origin == Origin.PYTHON || origin == Origin.EXTENSION) {
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
        if (this.klass == null) {
            return new org.python.types.Str(
                    String.format("<...type 0x%x (%s) is being initialized...>",
                            this.hashCode(),
                            this.origin
                    )
            );
        }
        return new org.python.types.Str(
                String.format("<class '%s'%s>",
                        org.Python.typeName(this.klass),
                        this.origin == Origin.PLACEHOLDER ? " (placeholder)" : ""
                )
        );
    }

    public org.python.Object __getattribute_null(java.lang.String name) {
        // System.out.println("GETATTRIBUTE CLASS " + this.klass.getName() + " " + name + " " + this.origin);
        // System.out.println("CLASS ATTRS " + this.__dict__);
        org.python.Object value = this.__dict__.get(name);
        if (value == null) {
            // We need to differentiate between "doesn't exist in the __dict__", and
            // exists, but has a value of null.
            if (!this.__dict__.containsKey(name)) {
                // The class attributes didn't contain a value for the attribute
                // name. Introspect on the object class to see if a field
                // with the given name exists, caching either the Field instance,
                // or an AttributeError representation of the NoSuchFieldException.
                try {
                    java.lang.reflect.Field field = this.klass.getDeclaredField(name);

                    // A field exists. Check that the attribute
                    // should be exposed to the Python namespace.
                    org.python.Attribute annotation =
                            (org.python.Attribute) field.getAnnotation(org.python.Attribute.class);
                    if (annotation != null) {
                        value = new org.python.java.Field(field);
                    } else {
                        value = null;
                    }
                } catch (java.lang.NoSuchFieldException e) {
                    value = null;
                }
                this.__dict__.put(name, value);
            }
        }

        // If the result of the lookup is an AttributeError, there's
        // no local field; so defer to the base type chain.
        if (value == null) {
            if (this.__dict__.get("__bases__") != null) {
                for (org.python.Object base : ((org.python.types.Tuple) this.__dict__.get("__bases__")).value) {
                    value = base.__getattribute_null(name);
                    if (value != null) {
                        break;
                    }
                }
            }
        }

        // If we still don't have a value, look for a global
        // variable defined at the module level.
        if (value == null) {
            // System.out.println("CLASS ATTRS " + this.klass);
            // System.out.println("__dict__ " + this.__dict__);
            org.python.Object module_name = this.__dict__.get("__module__");
            if (module_name != null) {
                org.python.Object module = python.sys.__init__.modules.__getitem__(module_name);
                value = module.__getattribute_null(name);
            }
        }

        // If we don't have a module attribute, look for a builtin.
        if (value == null) {
            // System.out.println("Look for attribute in builtins " + name);
            value = org.Python.builtins.get(name);
        }

        // System.out.println("GETATTRIBUTE CLASS " + this.klass.getName() + " " + name + " = " + value);
        return value;
    }

    public void __setattr__(java.lang.String name, org.python.Object value) {
        if (!this.__setattr_null(name, value)) {
            throw new org.python.exceptions.TypeError("Can't set new attributes on built-in type '" + org.Python.typeName(this.klass) + "'");
        }
    }

    public boolean __setattr_null(java.lang.String name, org.python.Object value) {
        // System.out.println("SETATTRIBUTE TYPE " + name + " = " + value);
        // System.out.println("class __dict__ = " + this.__dict__);

        // Can't set attributes of builtin types.
        if (this.origin == Origin.BUILTIN) {
            return false;
        }

        this.__dict__.put(name, value);
        return true;
    }

    public org.python.Object invoke(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        try {
            // org.Python.debug("Constructor:", this.constructor);
            // org.Python.debug("     Origin:", this.origin);
            // org.Python.debug("       Type:", this);
            // for (org.python.Object arg: args) {
            //     org.Python.debug("            arg: ", arg);
            // }
            // org.Python.debug("         kwargs: ", kwargs);

            if (this.constructor != null) {
                org.python.Method annotation = (org.python.Method) this.constructor.getAnnotation(org.python.Method.class);
                org.python.Object[] adjusted_args;

                if (annotation != null && origin == Origin.BUILTIN) {
                    java.lang.String[] arg_names = annotation.args();
                    java.lang.String[] default_arg_names = annotation.default_args();
                    boolean has_varargs = annotation.varargs().equals("");
                    int a;
                    java.lang.String arg_name;
                    org.python.Object arg;
                    int n_args = arg_names.length + default_arg_names.length;

                    adjusted_args = new org.python.Object[arg_names.length + default_arg_names.length];

                    if (args.length < n_args) {
                        // Take as many positional arguments as have been literally provided
                        for (a = 0; a < args.length; a++) {
                            adjusted_args[a] = args[a];
                        }

                        // Populate the rest from kwargs
                        for (a = args.length; a < n_args; a++) {
                            if (a < arg_names.length) {
                                arg_name = arg_names[a];
                            } else {
                                arg_name = default_arg_names[a - arg_names.length];
                            }

                            arg = kwargs.remove(arg_name);
                            if (arg == null && a < arg_names.length) {
                                throw new org.python.exceptions.TypeError(
                                        this.PYTHON_TYPE_NAME + " constructor missing positional argument '" +
                                                arg_name + "'"
                                );
                            }
                            adjusted_args[a] = arg;
                        }
                    } else {
                        for (a = 0; a < n_args; a++) {
                            adjusted_args[a] = args[a];
                        }

                        for (a = n_args; a < args.length; a++) {
                            if (a < arg_names.length) {
                                arg_name = arg_names[a];
                            } else {
                                arg_name = default_arg_names[a - arg_names.length];
                            }
                            kwargs.put(arg_name, args[a]);
                        }
                    }
                } else {
                    adjusted_args = args;
                }

                // for (org.python.Object arg: adjusted_args) {
                //     org.Python.debug("            adj arg: ", arg);
                // }
                // org.Python.debug("         adj kwargs: ", kwargs);

                return (org.python.Object) this.constructor.newInstance(adjusted_args, kwargs);
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
        // } finally {
            //     System.out.println("CONSTRUCTOR DONE");
        }
    }
}
