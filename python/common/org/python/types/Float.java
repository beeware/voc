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
    public org.python.types.Str __repr__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("float.__repr__ doesn't take keyword arguments");
        } else if (args != null && args.size() != 0) {
            throw new org.python.exceptions.TypeError("Expected 0 arguments, got " + args.size());
        }

        return new org.python.types.Str(java.lang.Double.toString(this.value));
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Str __format__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("float.__format__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __lt__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("float.__lt__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 argument, got " + args.size());
        }

        org.python.Object other = args.get(0);
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
    public org.python.Object __le__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("float.__le__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __eq__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("float.__eq__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 argument, got " + args.size());
        }

        org.python.Object other = args.get(0);
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
        throw new org.python.exceptions.TypeError("unorderable types: float() == " + other.typeName() + "()");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __ne__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("float.__ne__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __gt__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("float.__gt__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __ge__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("float.__ge__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Bool __bool__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("float.__bool__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __getattribute__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("float.__getattribute__() has not been implemented.");
    }

    public void __setattr__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("float.__setattr__() has not been implemented.");
    }

    public void __delattr__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("float.__delattr__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.List __dir__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("float.__dir__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __add__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("float.__add__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __sub__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("float.__sub__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 argument, got " + args.size());
        }

        org.python.Object other = args.get(0);
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
    public org.python.Object __mul__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("float.__mul__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __truediv__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("float.__truediv__ doesn't take keyword arguments");
        } else if (args == null || args.size() != 1) {
            throw new org.python.exceptions.TypeError("Expected 1 argument, got " + args.size());
        }

        org.python.Object other = args.get(0);
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
    public org.python.Object __floordiv__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("float.__floordiv__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __mod__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("float.__mod__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __divmod__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("float.__divmod__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __pow__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("float.__pow__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __radd__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("float.__radd__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rsub__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("float.__rsub__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rmul__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("float.__rmul__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rtruediv__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("float.__rtruediv__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rfloordiv__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("float.__rfloordiv__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rmod__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("float.__rmod__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rdivmod__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("float.__rdivmod__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rpow__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("float.__rpow__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __neg__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("float.__neg__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __pos__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("float.__pos__() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __abs__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        if (kwargs != null && kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("float.__abs__ doesn't take keyword arguments");
        } else if (args != null && args.size() != 0) {
            throw new org.python.exceptions.TypeError("Expected 0 arguments, got " + args.size());
        }

        if (this.value < 0.0) {
            return new org.python.types.Float(-this.value);
        } else {
            return new org.python.types.Float(this.value);
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Int __int__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        return new org.python.types.Int((int) this.value);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Float __float__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        return new org.python.types.Float(this.value);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __round__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("float.__round__() has not been implemented.");
    }
}