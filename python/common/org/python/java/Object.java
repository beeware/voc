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
        super();
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
            // System.out.println("CLASS ATTRS " + klass.attrs);
            org.python.Object attr = klass.attrs.get(name);

            if (attr == null) {
                // java.lang.Map doesn't differentiate between "doesn't exist"
                // and "value is null"; so since we know the value is null, check
                // to see if it is an explicit null (i.e., attribute doesn't exist)
                if (klass.attrs.containsKey(name)) {
                    throw new org.python.exceptions.AttributeError(this, name);
                } else {
                    try {
                        attr = new org.python.java.Function(this.object.getClass(), name);
                        klass.attrs.put(name, attr);
                        value = attr.__get__(this, org.python.types.Type.pythonType(this.getClass()));
                        this.attrs.put(name, value);
                    } catch (org.python.exceptions.AttributeError fe) {
                        try {
                            attr = new org.python.java.Attribute(this.object.getClass(), name);
                            klass.attrs.put(name, attr);
                            value = attr;
                        } catch (org.python.exceptions.AttributeError ae) {
                            // Field does not exist. Record this fact,
                            // and raise an AttributError.
                            klass.attrs.put(name, null);
                            throw new org.python.exceptions.AttributeError(this, name);
                        }
                    }
                }
            }
        }

        return value.__get__(this, org.python.types.Type.pythonType(this.getClass()));
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
