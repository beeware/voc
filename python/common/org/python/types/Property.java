package org.python.types;

public class Property extends org.python.types.Object {
    org.python.Object getter;
    org.python.Object setter;
    org.python.Object deleter;
    org.python.Object docstring;

    public Property(org.python.Object fget, org.python.Object fset, org.python.Object fdel, org.python.Object doc) {
        this.getter = fget;
        this.setter = fset;
        this.deleter = fdel;
        this.docstring = doc;
    }

    @org.python.Method(
        __doc__ = "Return repr(self)."
    )
    public org.python.Object __repr__() {
        // if (this.expression.getName().startswith("genexpr_"))
        return new org.python.types.Str(String.format("<%s at 0x%x>", this.typeName(), this.hashCode()));
    }

    @org.python.Method(
        __doc__ = "",
        args = {"instance", "klass"}
    )
    public org.python.Object __get__(org.python.Object instance, org.python.Object klass) {
        // System.out.println("Property __get__ on " + instance);
        if (this.getter != null) {
            try {
                return ((org.python.types.Function) this.getter).invoke(instance, null, null);
            } catch (java.lang.ClassCastException e) {
                throw new org.python.exceptions.TypeError("'" + this.getter.typeName() + "' object is not callable");
            }
        } else {
            throw new org.python.exceptions.AttributeError("can't get attribute");
        }
    }

    @org.python.Method(
        __doc__ = "",
        args = {"instance", "value"}
    )
    public void __set__(org.python.Object instance, org.python.Object value) {
        // System.out.println("Property __set__ on " + instance);
        if (this.setter != null) {
            try {
                ((org.python.types.Function) this.setter).invoke(instance, new org.python.Object [] { value }, null);
            } catch (java.lang.ClassCastException e) {
                throw new org.python.exceptions.TypeError("'" + this.setter.typeName() + "' object is not callable");
            }
        } else {
            throw new org.python.exceptions.AttributeError("can't set attribute");
        }
    }

    @org.python.Method(
        __doc__ = "",
        args = {"instance"}
    )
    public void __delete__(org.python.Object instance) {
        // System.out.println("Property __delete__ on " + instance);
        if (this.deleter != null) {
            try {
                ((org.python.types.Function) this.deleter).invoke(instance, null, null);
            } catch (java.lang.ClassCastException e) {
                throw new org.python.exceptions.TypeError("'" + this.deleter.typeName() + "' object is not callable");
            }
        } else {
            throw new org.python.exceptions.AttributeError("can't delete attribute");
        }
    }
}
