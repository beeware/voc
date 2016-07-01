package org.python.java;


public class Object extends org.python.types.Object {

    public java.lang.Object object;

    public int hashCode() {
        return this.object.hashCode();
    }

    public java.lang.Object toJava() {
        return this.object;
    }

    public java.lang.Object toObject() {
        return this.object;
    }

    public Object(java.lang.Object object) {
        this(org.python.types.Type.Origin.JAVA, object);
    }

    public Object(org.python.types.Type.Origin origin, java.lang.Object object) {
        super(origin, object.getClass());
        // System.out.println("JAVA WRAPPER FOR " + object.getClass());
        this.object = object;
        try {
            java.lang.reflect.Field voc_field = this.object.getClass().getField("__VOC__");
            voc_field.set(this.object, this);
        } catch (NoSuchFieldException e) {
            // System.out.println("NO __VOC__ FIELD");
        } catch (java.lang.IllegalAccessException e) {
            throw new org.python.exceptions.RuntimeError("Illegal access to __VOC__ field for " + this.object.getClass());
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Str __repr__() {
        return new org.python.types.Str(String.format("<Native %s object at 0x%x>", this.object.getClass().getName(), this.object.hashCode()));
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Str __str__() {
        return new org.python.types.Str(this.object.toString());
    }

    // @org.python.Method(
    //     __doc__ = ""
    // )
    // public org.python.Object __getattribute__(java.lang.String name) {
    //     // System.out.println("GETATTRIBUTE NATIVE OBJECT " + this + " " + name);
    //     // Look for a cached attribute.
    //     org.python.Object value = this.__dict__.get(name);

    //     if (value == null) {
    //         // Look for a cached class-level attribute.
    //         org.python.types.Type klass = (org.python.types.Type) this.__dict__.get("__class__");
    //         value = klass.__getattribute__(name).__get__(this, klass);
    //     }

    //     return value;
    // }

    // @org.python.Method(
    //     __doc__ = ""
    // )
    // public void __setattr__(java.lang.String name, org.python.Object value) {
    //     // System.out.println("SETATTRIBUTE NATIVE OBJECT " + this + " " + name + " = " + value);
    //     try {
    //         org.python.Object attr = this.__getattribute__(name);

    //         if (attr instanceof org.python.types.Attribute) {
    //             ((org.python.java.Attribute) attr).__set__(this, value);
    //         }
    //     } catch(org.python.exceptions.AttributeError e) {
    //     }

    //     this.__dict__.put(name, value);
    // }

}
