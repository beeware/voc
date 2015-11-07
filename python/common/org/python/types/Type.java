package org.python.types;

public class Type extends org.python.types.Object {
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

            // Construct the new type, and store it in the types table
            python_type = new org.python.types.Type(java_class);
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

    public java.lang.Class klass;

    /**
     * A utility method to update the internal value of this object.
     *
     * Used by __i*__ operations to do an in-place operation.
     * obj must be of type org.python.types.Type
     */
    void setValue(org.python.Object obj) {
        this.klass = ((org.python.types.Type) obj).klass;
    }

    Type(java.lang.Class klass, boolean empty) {
        super(empty);
        if (!empty) {
            this.klass = klass;

            this.attrs.put("__name__", new org.python.types.Str(this.klass.getName()));
            // this.attrs.put("__module__", );
            // this.attrs.put("__qualname__", );

            // Iterate over every method in the class, and if the
            // method is annotated for inclusion in the Python class,
            // add a function wrapper to the type definition.
            for (java.lang.reflect.Method method: klass.getMethods()) {
                // System.out.println("Found method " + method + " on type " + klass);
                java.lang.annotation.Annotation annotation = method.getAnnotation(org.python.Method.class);
                if (annotation != null) {
                    // System.out.println("Add method " + method + " to type " + klass);
                    this.attrs.put(
                        method.getName(),
                        new org.python.types.Function(method)
                    );
                }
            }
            // System.out.println("Methods added for type " + klass);
        }

    }

    Type(java.lang.Class klass) {
        this(klass, false);
    }

    public boolean is_placeholder() {
        return false;
    }

    public void add_reference(org.python.Object instance) {
        throw new java.lang.RuntimeException("Can't add reference to normal type");
    }

    public org.python.types.Str __repr__() {
        return new org.python.types.Str(String.format("<class '%s'>", org.Python.pythonTypeName(this.klass)));
    }
}


class PlaceholderType extends org.python.types.Type {
    private java.util.ArrayList<org.python.Object> instances = new java.util.ArrayList<org.python.Object>();

    PlaceholderType(java.lang.Class klass) {
        super(klass, true);
    }

    public boolean is_placeholder() {
        return true;
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
