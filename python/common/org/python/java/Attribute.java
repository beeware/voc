package org.python.java;


public class Attribute extends org.python.types.Object {
    java.lang.reflect.Field field;

    public Attribute(java.lang.Class klass, java.lang.String name) {
        super();
        try {
            this.field = klass.getField(name);
        } catch (java.lang.NoSuchFieldException e) {
            throw new org.python.exceptions.AttributeError(klass, name);
        }
    }

    public org.python.types.Str __repr__() {
        return new org.python.types.Str(
            String.format("<unbound native field %s>",
                this.field
            )
        );
    }

    public org.python.Object __get__(org.python.Object instance, org.python.types.Type klass) {
        try {
            return new org.python.java.Object(this.field.get(instance.toJava()));
        } catch (IllegalAccessException iae) {
            throw new org.python.exceptions.RuntimeError("Illegal access to native field " + this.field.getName());
        }
    }

    public void __set__(org.python.Object instance, org.python.Object value) {
        try {
            this.field.set(instance.toJava(), value.toJava());
        } catch (IllegalAccessException iae) {
            throw new org.python.exceptions.RuntimeError("Illegal access to native field " + this.field.getName());
        }
    }
}
