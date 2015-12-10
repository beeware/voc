package org.python.java;


public class Field extends org.python.types.Object {
    java.lang.reflect.Field field;

    public Field(java.lang.reflect.Field field) {
        super();
        this.field = field;
    }

    public org.python.types.Str __repr__() {
        return new org.python.types.Str(
            String.format("<unbound native field %s>",
                this.field
            )
        );
    }

    public org.python.Object __get__(org.python.Object instance, org.python.Object klass) {
        try {
            return (org.python.Object) this.field.get(instance.toJava());
        } catch (IllegalAccessException iae) {
            throw new org.python.exceptions.RuntimeError("Illegal access to native field " + this.field.getName());
        }
    }

    public void __set__(org.python.Object instance, org.python.Object value) {
        try {
            this.field.set(instance.toJava(), value);
        } catch (IllegalAccessException iae) {
            throw new org.python.exceptions.RuntimeError("Illegal access to native field " + this.field.getName());
        }
    }
}
