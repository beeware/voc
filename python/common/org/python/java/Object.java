package org.python.java;

public class Object extends org.python.types.Object {
    static
    // public static org.python.Object convert(java.lang.Object java) {
    //     if (java instanceof java.lang.String) {
    //         return new org.python.types.Str((java.lang.String) java);
    //     } else {
    //         return new org.python.java.Object(java);
    //     }
    // }

    public java.lang.Object object;

    public int hashCode() {
        return this.object.hashCode();
    }

    public java.lang.Object toJava() {
        return this.object;
    }

    public Object(java.lang.Object object) {
        super(org.python.types.Type.Origin.JAVA, object.getClass());
        this.object = object;
    }

    public org.python.types.Str __repr__() {
        return new org.python.types.Str(String.format("<Native %s object at 0x>", this.object.getClass(), this.object.hashCode()));
    }

    public org.python.types.Str __str__() {
        return new org.python.types.Str(this.object.toString());
    }

    public org.python.Object __getattribute__(java.lang.String name) {
        // System.out.println("GETATTRIBUTE NATIVE OBJECT " + this + " " + name);
        // Look for a cached attribute.
        org.python.Object value = this.attrs.get(name);

        if (value == null) {
            // Look for a cached class-level attribute.
            org.python.types.Type klass = (org.python.types.Type) this.attrs.get("__class__");
            value = klass.__getattribute__(name).__get__(this, klass);
        }

        return value;
    }

    public void __setattr__(java.lang.String name, org.python.Object value) {
        // System.out.println("SETATTRIBUTE NATIVE OBJECT " + this + " " + name + " = " + value);
        try {
            org.python.Object attr = this.__getattribute__(name);

            if (attr instanceof org.python.java.Attribute) {
                ((org.python.java.Attribute) attr).__set__(this, value);
            }
        } catch(org.python.exceptions.AttributeError e) {
        }

        this.attrs.put(name, value);
    }

}
