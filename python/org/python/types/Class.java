package org.python.types;

public class Class extends org.python.types.Object {
    public java.lang.Class value;

    /**
     * Return the python name for this class.
     */
    public java.lang.String getPythonName() {
        return "class";
    }

    /**
     * A utility method to update the internal value of this object.
     *
     * Used by __i*__ operations to do an in-place operation.
     * obj must be of type org.python.types.Class
     */
    void setValue(org.python.Object obj) {
        this.value = ((org.python.types.Class) obj).value;
    }

    public Class(java.lang.Class value) {
        super();
        this.value = value;

        // Iterate over all methods, adding the static ones as class attributes
        for (java.lang.reflect.Method method: value.getMethods()) {
            if (java.lang.reflect.Modifier.isStatic(method.getModifiers())) {
                attrs.put(method.getName(), new org.python.types.Function(method, false));
            }
        }
    }

}