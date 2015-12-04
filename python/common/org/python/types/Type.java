package org.python.types;

public class Type extends org.python.types.Object {
    public enum Origin {PLACEHOLDER, PYTHON, JAVA};

    private static java.util.Map<java.lang.Class, org.python.types.Type> known_types = new java.util.HashMap<java.lang.Class, org.python.types.Type>();

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
                python_type = new org.python.types.Type(java_class);
            } else {
                python_type = new org.python.java.Type(java_class);
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
            throw new org.python.exceptions.RuntimeError("Unknown Class");
        }
    }

    public static org.python.Object toPython(java.lang.Object value) {
        if (org.python.Object.class.isAssignableFrom(value.getClass())) {
            try {
                org.python.types.Type python_type = org.python.types.Type.pythonType(value.getClass());
                java.lang.reflect.Constructor constructor = python_type.klass.getConstructor(value.getClass());
                return (org.python.Object) constructor.newInstance(value);
            } catch (java.lang.NoSuchMethodException e) {
                throw new org.python.exceptions.RuntimeError("Couldn't find toPython() compatible constructor for " + value);
            } catch (java.lang.IllegalAccessException e) {
                throw new org.python.exceptions.RuntimeError("Invalid access to toPython() compatible constructor for " + value);
            } catch (java.lang.reflect.InvocationTargetException e) {
                try {
                    // e.getTargetException().printStackTrace();
                    // If the Java method raised an Python exception, re-raise that
                    // exception as-is. If it wasn"t a Python exception, wrap it
                    // as one and continue.
                    throw (org.python.exceptions.BaseException) e.getCause();
                } catch (ClassCastException java_e) {
                    throw new org.python.exceptions.RuntimeError(e.getCause().getMessage());
                }
            } catch (java.lang.InstantiationException e) {
                throw new org.python.exceptions.RuntimeError("Couldn't instantiate Python() compatible constructor for " + value);
            }
        } else {
            return new org.python.java.Object(value);
        }
    }


    public java.lang.Class klass;
    public Origin origin;

    /**
     * A utility method to update the internal value of this object.
     *
     * Used by __i*__ operations to do an in-place operation.
     * obj must be of type org.python.types.Type
     */
    void setValue(org.python.Object obj) {
        this.klass = ((org.python.types.Type) obj).klass;
    }

    public Type(java.lang.Class klass, Origin origin) {
        super(origin, null);
        if (origin != Origin.PLACEHOLDER) {
            this.klass = klass;

            this.attrs.put("__name__", new org.python.types.Str(this.klass.getName()));
            this.attrs.put("__qualname__", new org.python.types.Str(this.klass.getName()));
            // this.attrs.put("__module__", );

            org.Python.initializeModule(this.klass, this.attrs);
        }
    }

    public Type(java.lang.Class klass) {
        this(klass, Origin.PYTHON);
    }

    public void add_reference(org.python.Object instance) {
        throw new java.lang.RuntimeException("Can't add reference to normal type");
    }

    public org.python.types.Str __repr__() {
        return new org.python.types.Str(String.format("<class '%s'>", org.Python.typeName(this.klass)));
    }
}


class PlaceholderType extends org.python.types.Type {
    private java.util.ArrayList<org.python.Object> instances = new java.util.ArrayList<org.python.Object>();

    PlaceholderType(java.lang.Class klass) {
        super(klass, org.python.types.Type.Origin.PLACEHOLDER);
    }

    public void add_reference(org.python.Object instance) {
        instances.add(instance);
    }

    public void resolve(org.python.types.Type python_type) {
        for (org.python.Object obj: this.instances) {
            obj.__new__(python_type);
        }
    }
}
