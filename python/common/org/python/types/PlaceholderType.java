package org.python.types;

class PlaceholderType extends org.python.types.Type {
    private java.util.ArrayList<org.python.Object> instances = new java.util.ArrayList<org.python.Object>();

    PlaceholderType(java.lang.Class klass) {
        super(org.python.types.Type.Origin.PLACEHOLDER, klass);
    }

    public void add_reference(org.python.Object instance) {
        instances.add(instance);
    }

    public void resolve(org.python.types.Type python_type) {
        for (org.python.Object obj : this.instances) {
            obj.__new__(python_type);
        }
    }
}
