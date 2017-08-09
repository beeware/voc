package org.python.types;

public class Property extends org.python.types.Object {
    org.python.Object fget;
    org.python.Object fset;
    org.python.Object fdel;
    org.python.Object doc;

    public Property(org.python.Object fget, org.python.Object fset, org.python.Object fdel, org.python.Object doc) {
        this.fget = fget;
        this.fset = fset;
        this.fdel = fdel;
        this.doc = doc;
    }

    @org.python.Method(
            __doc__ = "Return repr(self)."
    )
    public org.python.Object __repr__() {
        // if (this.expression.getName().startswith("genexpr_"))
        return new org.python.types.Str(String.format("<%s object at 0x%x>", this.typeName(), this.hashCode()));
    }

    @org.python.Method(
            __doc__ = "Return an attribute of instance, which is of type owner.",
            args = {"instance", "klass"}
    )
    public org.python.Object __get__(org.python.Object instance, org.python.Object klass) {
        // System.out.println("Property __get__ on " + instance);
        if (this.fget != null) {
            try {
                return ((org.python.types.Function) this.fget).invoke(instance, null, null);
            } catch (java.lang.ClassCastException e) {
                throw new org.python.exceptions.TypeError("'" + this.fget.typeName() + "' object is not callable");
            }
        } else {
            throw new org.python.exceptions.AttributeError("can't get attribute");
        }
    }

    @org.python.Method(
            __doc__ = "Set an attribute of instance to value.",
            args = {"instance", "value"}
    )
    public void __set__(org.python.Object instance, org.python.Object value) {
        // System.out.println("Property __set__ on " + instance);
        if (this.fset != null) {
            try {
                ((org.python.types.Function) this.fset).invoke(instance, new org.python.Object[]{value}, null);
            } catch (java.lang.ClassCastException e) {
                throw new org.python.exceptions.TypeError("'" + this.fset.typeName() + "' object is not callable");
            }
        } else {
            throw new org.python.exceptions.AttributeError("can't set attribute");
        }
    }

    @org.python.Method(
            __doc__ = "Delete an attribute of instance.",
            args = {"instance"}
    )
    public void __delete__(org.python.Object instance) {
        // System.out.println("Property __delete__ on " + instance);
        if (this.fdel != null) {
            try {
                ((org.python.types.Function) this.fdel).invoke(instance, null, null);
            } catch (java.lang.ClassCastException e) {
                throw new org.python.exceptions.TypeError("'" + this.fdel.typeName() + "' object is not callable");
            }
        } else {
            throw new org.python.exceptions.AttributeError("can't delete attribute");
        }
    }

    @org.python.Method(
            __doc__ = "Descriptor to change the setter on a property.",
            args = {"fn"}
    )
    public org.python.Object setter(org.python.Object fn) {
        // Duplicate the property, substituting the new setter.
        return new org.python.types.Property(this.fget, fn, this.fdel, this.doc);
    }

    @org.python.Method(
            __doc__ = "Descriptor to change the deleter on a property.",
            args = {"fn"}
    )
    public org.python.Object deleter(org.python.Object fn) {
        // Duplicate the property, substituting the new deleter.
        return new org.python.types.Property(this.fget, this.fset, fn, this.doc);
    }
}
