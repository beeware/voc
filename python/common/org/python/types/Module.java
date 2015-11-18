package org.python.types;

public class Module extends org.python.types.Object {

    public java.lang.Class klass;

    protected Module() {}

    public Module(java.lang.Class klass) {
        this.klass = klass;
    }

    public org.python.types.Str __repr__() {
        return new org.python.types.Str(String.format("<module '%s' from '%s'>", org.Python.pythonTypeName(this.getClass()), this.getClass()));
    }

    @SuppressWarnings("unchecked")
    public org.python.Object __getattribute__(java.lang.String name) {
        org.python.Object value;
        try {
            // First try the normal approach attribute
            value = super.__getattribute__(name);
        } catch (org.python.exceptions.AttributeError e) {
            // System.out.println("MODULE NO ATTRIBUTE");
            value = org.Python.builtins.get(name);

            if (value == null) {
                throw new org.python.exceptions.NameError(name);
            }
        }

        return value;
    }
}


