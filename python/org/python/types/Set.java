package org.python.types;

public class Set extends org.python.types.Object {
    public java.util.Set<org.python.Object> value;

    /**
     * Return the python name for this class.
     */
    public java.lang.String getPythonName() {
        return "set";
    }

    /**
     * A utility method to update the internal value of this object.
     *
     * Used by __i*__ operations to do an in-place operation.
     * obj must be of type org.python.types.Set
     */
    void setValue(org.python.Object obj) {
        this.value = ((org.python.types.Set) obj).value;
    }

    public Set(java.util.Set<org.python.Object> set) {
        super();
        this.value = set;
    }

    // public org.python.Object __new__() {
    //     throw new org.python.exceptions.NotImplementedError("set.__new__() has not been implemented");
    // }

    // public org.python.Object __init__() {
    //     throw new org.python.exceptions.NotImplementedError("set.__init__() has not been implemented");
    // }

    public org.python.types.Str __repr__() {
        java.lang.StringBuilder buffer = new java.lang.StringBuilder("{");
        boolean first = true;
        for (org.python.Object obj: this.value) {
            if (first) {
                first = false;
            } else {
                buffer.append(", ");
            }
            buffer.append(obj.__repr__());
        }
        buffer.append("}");
        return new org.python.types.Str(buffer.toString());
    }

    public org.python.types.Str __format__() {
        throw new org.python.exceptions.NotImplementedError("set.__format__() has not been implemented");
    }

    public org.python.Object __lt__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("set.__lt__() has not been implemented");
    }

    public org.python.Object __le__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("set.__le__() has not been implemented");
    }

    public org.python.Object __eq__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("set.__eq__() has not been implemented");
    }

    public org.python.Object __ne__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("set.__ne__() has not been implemented");
    }

    public org.python.Object __gt__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("set.__gt__() has not been implemented");
    }

    public org.python.Object __ge__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("set.__ge__() has not been implemented");
    }

    public org.python.Object __getattribute__(java.lang.String name) {
        throw new org.python.exceptions.NotImplementedError("set.__getattribute__() has not been implemented");
    }

    public void __setattr__(java.lang.String name, org.python.Object value) {
        throw new org.python.exceptions.NotImplementedError("set.__setattr__() has not been implemented");
    }

    public void __delattr__(java.lang.String name) {
        throw new org.python.exceptions.NotImplementedError("set.__delattr__() has not been implemented");
    }

    public org.python.types.List __dir__() {
        throw new org.python.exceptions.NotImplementedError("set.__dir__() has not been implemented");
    }

    public org.python.types.Int __len__() {
        throw new org.python.exceptions.NotImplementedError("set.__len__() has not been implemented");
    }

    public org.python.Iterable __iter__() {
        throw new org.python.exceptions.NotImplementedError("set.__iter__() has not been implemented");
    }

    public org.python.Object __contains__() {
        throw new org.python.exceptions.NotImplementedError("set.__contains__() has not been implemented");
    }

    public org.python.Object __sub__() {
        throw new org.python.exceptions.NotImplementedError("set.__sub__() has not been implemented");
    }

    public org.python.Object __and__() {
        throw new org.python.exceptions.NotImplementedError("set.__and__() has not been implemented");
    }

    public org.python.Object __xor__() {
        throw new org.python.exceptions.NotImplementedError("set.__xor__() has not been implemented");
    }

    public org.python.Object __or__() {
        throw new org.python.exceptions.NotImplementedError("set.__or__() has not been implemented");
    }

    public org.python.Object __rsub__() {
        throw new org.python.exceptions.NotImplementedError("set.__rsub__() has not been implemented");
    }

    public org.python.Object __rand__() {
        throw new org.python.exceptions.NotImplementedError("set.__rand__() has not been implemented");
    }

    public org.python.Object __rxor__() {
        throw new org.python.exceptions.NotImplementedError("set.__rxor__() has not been implemented");
    }

    public org.python.Object __ror__() {
        throw new org.python.exceptions.NotImplementedError("set.__ror__() has not been implemented");
    }

    public org.python.Object __isub__() {
        throw new org.python.exceptions.NotImplementedError("set.__isub__() has not been implemented");
    }

    public org.python.Object __iand__() {
        throw new org.python.exceptions.NotImplementedError("set.__iand__() has not been implemented");
    }

    public org.python.Object __ixor__() {
        throw new org.python.exceptions.NotImplementedError("set.__ixor__() has not been implemented");
    }

    public org.python.Object __ior__() {
        throw new org.python.exceptions.NotImplementedError("set.__ior__() has not been implemented");
    }


}