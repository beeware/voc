package org.python.types;

public class Str extends org.python.types.Object {
    public java.lang.String value;

    /**
     * A utility method to update the internal value of this object.
     *
     * Used by __i*__ operations to do an in-place operation.
     * obj must be of type org.python.types.Str
     */
    void setValue(org.python.Object obj) {
        this.value = ((org.python.types.Str) obj).value;
    }

    public Str(java.lang.String str) {
        this.value = str;
    }

    // public org.python.Object __new__() {
    //     throw new org.python.exceptions.NotImplementedError("str.__new__() has not been implemented.");
    // }

    // public org.python.Object __init__() {
    //     throw new org.python.exceptions.NotImplementedError("str.__init__() has not been implemented.");
    // }

    public org.python.types.Str __repr__() {
        return new org.python.types.Str("'" + this.value + "'");
    }

    public org.python.types.Str __str__() {
        return new org.python.types.Str(this.value);
    }

    public org.python.types.Str __format__() {
        throw new org.python.exceptions.NotImplementedError("str.__format__() has not been implemented.");
    }

    public org.python.types.Int __int__() {
        try {
            return new org.python.types.Int(Long.parseLong(this.value));
        } catch (NumberFormatException e) {
            throw new org.python.exceptions.ValueError("invalid literal for int() with base 10: '" + this.value + "'");
        }
    }

    public org.python.types.Float __float__() {
        try {
            return new org.python.types.Float(Double.parseDouble(this.value));
        } catch (NumberFormatException e) {
            throw new org.python.exceptions.ValueError("could not convert string to float: '" + this.value + "'");
        }
    }

    public org.python.Object __lt__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("str.__lt__() has not been implemented.");
    }

    public org.python.Object __le__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("str.__le__() has not been implemented.");
    }

    public org.python.Object __eq__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("str.__eq__() has not been implemented.");
    }

    public org.python.Object __ne__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("str.__ne__() has not been implemented.");
    }

    public org.python.Object __gt__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("str.__gt__() has not been implemented.");
    }

    public org.python.Object __ge__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("str.__ge__() has not been implemented.");
    }

    public org.python.Object __getattribute__(java.lang.String name) {
        throw new org.python.exceptions.NotImplementedError("str.__getattribute__() has not been implemented.");
    }

    public void __setattr__(java.lang.String name, org.python.Object value) {
        throw new org.python.exceptions.NotImplementedError("str.__setattr__() has not been implemented.");
    }

    public void __delattr__(java.lang.String name) {
        throw new org.python.exceptions.NotImplementedError("str.__delattr__() has not been implemented.");
    }

    public org.python.types.List __dir__() {
        throw new org.python.exceptions.NotImplementedError("str.__dir__() has not been implemented.");
    }

    public org.python.types.Int __len__() {
        throw new org.python.exceptions.NotImplementedError("str.__len__() has not been implemented.");
    }

    public org.python.Object __getitem__(org.python.Object index) {
        throw new org.python.exceptions.NotImplementedError("str.__getitem__() has not been implemented.");
    }

    public org.python.Iterable __iter__() {
        throw new org.python.exceptions.NotImplementedError("str.__iter__() has not been implemented.");
    }

    public org.python.types.Bool __contains__() {
        throw new org.python.exceptions.NotImplementedError("str.__contains__() has not been implemented.");
    }

    public org.python.Object __add__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("str.__add__() has not been implemented.");
    }

    public org.python.Object __mul__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            long other_int = ((org.python.types.Int)other).value;
            if (other_int < 1) {
                return new Str("");
            }
            java.lang.StringBuffer res = new java.lang.StringBuffer(value.length() * (int)other_int);
            for (int i = 0; i < other_int; i++) {
                res.append(value);
            }
            return new Str(res.toString());
        }
        throw new org.python.exceptions.NotImplementedError("str.__mul__() has not been implemented.");
    }

    public org.python.Object __mod__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("str.__mod__() has not been implemented.");
    }

    public org.python.Object __rmul__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("str.__rmul__() has not been implemented.");
    }

    public org.python.Object __rmod__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("str.__rmod__() has not been implemented.");
    }

}
