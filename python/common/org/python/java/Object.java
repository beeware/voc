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
}
