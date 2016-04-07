package org.python.types;

public class Float extends org.python.types.Object {
    public double value;

    /**
     * A utility method to update the internal value of this object.
     *
     * Used by __i*__ operations to do an in-place operation.
     * obj must be of type org.python.types.Float
     */
    void setValue(org.python.Object obj) {
        this.value = ((org.python.types.Float) obj).value;
    }

    public java.lang.Object toJava() {
        return this.value;
    }

    public org.python.Object byValue() {
        return new org.python.types.Float(this.value);
    }

    public int hashCode() {
        return new java.lang.Double(this.value).hashCode();
    }

    public Float(float value) {
        super();
        this.value = (double) value;
    }

    public Float(double value) {
        super();
        this.value = value;
    }

    // public org.python.Object __new__() {
    //     throw new org.python.exceptions.NotImplementedError("float.__new__() has not been implemented.");
    // }

    // public org.python.Object __init__() {
    //     throw new org.python.exceptions.NotImplementedError("float.__init__() has not been implemented.");
    // }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Str __repr__() {
        return new org.python.types.Str(java.lang.Double.toString(this.value));
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Str __format__(org.python.Object format_string) {
        throw new org.python.exceptions.NotImplementedError("float.__format__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __lt__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            long other_val = ((org.python.types.Int) other).value;
            return new org.python.types.Bool(this.value < ((double) other_val));
        } else if (other instanceof org.python.types.Float) {
            double other_val = ((org.python.types.Float) other).value;
            return new org.python.types.Bool(this.value < other_val);
        } else if (other instanceof org.python.types.Bool) {
            if (((org.python.types.Bool) other).value) {
                return new org.python.types.Bool(this.value < 1.0);
            }
            else {
                return new org.python.types.Bool(this.value < 0.0);
            }
        }
        throw new org.python.exceptions.TypeError("unorderable types: float() < " + other.typeName() + "()");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __le__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("float.__le__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __eq__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            return new org.python.types.Bool(this.value == ((double)((org.python.types.Int) other).value));
        } else if (other instanceof Float) {
            return new org.python.types.Bool(this.value == ((org.python.types.Float) other).value);
        } else if (other instanceof Bool) {
            return new org.python.types.Bool(
                (this.value == 0.0 && !((org.python.types.Bool) other).value)
                || (this.value != 0.0 && ((org.python.types.Bool) other).value)
            );
        }
        else if (other instanceof org.python.types.Str) {
            return new org.python.types.Bool(false);
        }
        throw new org.python.exceptions.TypeError("unorderable types: float() == " + other.typeName() + "()");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __ne__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("float.__ne__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __gt__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("float.__gt__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __ge__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("float.__ge__() has not been implemented.");
        
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Bool __bool__() {
        return new org.python.types.Bool(this.value != 0.0);
    }

    public boolean __setattr_null(java.lang.String name, org.python.Object value) {
        // Builtin types can't have attributes set on them.
        return false;
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.List __dir__() {
        throw new org.python.exceptions.NotImplementedError("float.__dir__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __add__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("float.__add__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __sub__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            long other_val = ((org.python.types.Int) other).value;
            return new org.python.types.Float(this.value - ((double) other_val));
        } else if (other instanceof org.python.types.Float) {
            double other_val = ((org.python.types.Float) other).value;
            return new org.python.types.Float(this.value - other_val);
        } else if (other instanceof org.python.types.Bool) {
            if (((org.python.types.Bool) other).value) {
                return new org.python.types.Float(this.value - 1.0);
            }
            return new org.python.types.Float(this.value);
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for /: 'float' and '" + other.typeName() + "'");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __mul__(org.python.Object other) {

        if (other instanceof org.python.types.Str) {
            throw new org.python.exceptions.TypeError("can't multiply sequence by non-int of type '" + "float" + "'");
        } else if (other instanceof org.python.types.Int) {
            return new org.python.types.Float(this.value * ((org.python.types.Int) other).value);
        } else if (other instanceof org.python.types.Float) {
            return new org.python.types.Float(((double) this.value) * ((org.python.types.Float) other).value);
        } else if (other instanceof org.python.types.Bool) {
            return new org.python.types.Float(this.value * (((org.python.types.Bool) other).value ? 1 : 0));
        }      
                
        throw new org.python.exceptions.NotImplementedError("float.__mul__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __truediv__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            long other_val = ((org.python.types.Int) other).value;
            if (other_val == 0) {
                throw new org.python.exceptions.ZeroDivisionError("float division by zero");
            }
            return new org.python.types.Float(this.value / ((double) other_val));
        } else if (other instanceof org.python.types.Float) {
            double other_val = ((org.python.types.Float) other).value;
            if (other_val == 0.0) {
                throw new org.python.exceptions.ZeroDivisionError("float division by zero");
            }
            return new org.python.types.Float(this.value / other_val);
        } else if (other instanceof org.python.types.Bool) {
            if (((org.python.types.Bool) other).value) {
                return new org.python.types.Float(this.value);
            }
            else {
                throw new org.python.exceptions.ZeroDivisionError("float division by zero");
            }
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for /: 'float' and '" + other.typeName() + "'");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __floordiv__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("float.__floordiv__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __mod__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("float.__mod__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __divmod__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("float.__divmod__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __pow__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("float.__pow__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __radd__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("float.__radd__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rsub__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("float.__rsub__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rmul__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("float.__rmul__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rtruediv__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("float.__rtruediv__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rfloordiv__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("float.__rfloordiv__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rmod__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("float.__rmod__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rdivmod__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("float.__rdivmod__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rpow__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("float.__rpow__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __neg__() {
        throw new org.python.exceptions.NotImplementedError("float.__neg__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __pos__() {
        throw new org.python.exceptions.NotImplementedError("float.__pos__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __abs__() {
        if (this.value < 0.0) {
            return new org.python.types.Float(-this.value);
        } else {
            return new org.python.types.Float(this.value);
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Int __int__() {
        return new org.python.types.Int((int) this.value);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Float __float__() {
        return new org.python.types.Float(this.value);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __round__(org.python.Object ndigits) {
        throw new org.python.exceptions.NotImplementedError("float.__round__() has not been implemented.");
    }

}
