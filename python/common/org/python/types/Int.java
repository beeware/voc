package org.python.types;


public class Int extends org.python.types.Object {
    public long value;

    /**
     * A utility method to update the internal value of this object.
     *
     * Used by __i*__ operations to do an in-place operation.
     * obj must be of type org.python.types.Int
     */
    void setValue(org.python.Object obj) {
        this.value = ((org.python.types.Int) obj).value;
    }

    public java.lang.Object toJava() {
        return this.value;
    }

    public org.python.Object byValue() {
        return new org.python.types.Int(this.value);
    }

    public int hashCode() {
        return new java.lang.Long(this.value).hashCode();
    }

    public Int(byte value) {
        this.value = (long) value;
    }

    public Int(short value) {
        this.value = (long) value;
    }

    public Int(int value) {
        this.value = (long) value;
    }

    public Int(long value) {
        this.value = value;
    }

    // public org.python.Object __new__() {
    //     throw new org.python.exceptions.NotImplementedError("int.__new__() has not been implemented");
    // }

    // public org.python.Object __init__() {
    //     throw new org.python.exceptions.NotImplementedError("int.__init__() has not been implemented");
    // }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Str __repr__() {
        return new org.python.types.Str(java.lang.Long.toString(this.value));
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Str __format__(org.python.Object format_str) {
        throw new org.python.exceptions.NotImplementedError("int.__format__() has not been implemented");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __lt__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            return new org.python.types.Bool(this.value < ((org.python.types.Int) other).value);
        } else if (other instanceof Float) {
            return new org.python.types.Bool(((double) this.value) < ((org.python.types.Float) other).value);
        }
        throw new org.python.exceptions.TypeError("unorderable types: int() < " + other.typeName() + "()");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __le__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            return new org.python.types.Bool(this.value <= ((org.python.types.Int) other).value);
        } else if (other instanceof Float) {
            return new org.python.types.Bool(((double) this.value) <= ((org.python.types.Float) other).value);
        }
        throw new org.python.exceptions.TypeError("unorderable types: int() <= " + other.typeName() + "()");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __eq__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            return new org.python.types.Bool(this.value == ((org.python.types.Int) other).value);
        } else if (other instanceof Float) {
            return new org.python.types.Bool(((double) this.value) == ((org.python.types.Float) other).value);
        } else if (other instanceof Bool) {
            return new org.python.types.Bool(
                (this.value == 0 && !((org.python.types.Bool) other).value)
                || (this.value != 0 && ((org.python.types.Bool) other).value)
            );
        }
        throw new org.python.exceptions.TypeError("unorderable types: int() == " + other.typeName() + "()");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __ne__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            return new org.python.types.Bool(this.value != ((org.python.types.Int) other).value);
        } else if (other instanceof Float) {
            return new org.python.types.Bool(((double) this.value) != ((org.python.types.Float) other).value);
        }
        throw new org.python.exceptions.TypeError("unorderable types: int() != " + other.typeName() + "()");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __gt__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            return new org.python.types.Bool(this.value > ((org.python.types.Int) other).value);
        } else if (other instanceof Float) {
            return new org.python.types.Bool(((double) this.value) > ((org.python.types.Float) other).value);
        }
        throw new org.python.exceptions.TypeError("unorderable types: int() > " + other.typeName() + "()");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __ge__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            return new org.python.types.Bool(this.value >= ((org.python.types.Int) other).value);
        } else if (other instanceof Float) {
            return new org.python.types.Bool(((double) this.value) >= ((org.python.types.Float) other).value);
        }
        throw new org.python.exceptions.TypeError("unorderable types: int() >= " + other.typeName() + "()");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Bool __bool__() {
        return new org.python.types.Bool(this.value);
    }

    public boolean __setattr_null(java.lang.String name, org.python.Object value) {
        // Builtin types can't have attributes set on them.
        return false;
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.List __dir__() {
        throw new org.python.exceptions.NotImplementedError("int.__dir__() has not been implemented");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __add__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            return new org.python.types.Int(this.value + ((org.python.types.Int) other).value);
        } else if (other instanceof org.python.types.Float) {
            return new org.python.types.Float(((double) this.value) + ((org.python.types.Float) other).value);
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for +: 'int' and '" + other.typeName() + "'");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __sub__(org.python.Object other) {
        if (other instanceof org.python.types.Str) {
            return other.__sub__(this);
        } else if (other instanceof org.python.types.Int) {
            return new org.python.types.Int(this.value - ((org.python.types.Int) other).value);
        } else if (other instanceof org.python.types.Float) {
            return new org.python.types.Float(((double) this.value) - ((org.python.types.Float) other).value);
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for -: 'int' and '" + other.typeName() + "'");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __mul__(org.python.Object other) {
        if (other instanceof org.python.types.Str) {
            return other.__mul__(this);
        } else if (other instanceof org.python.types.Int) {
            return new org.python.types.Int(this.value * ((org.python.types.Int) other).value);
        } else if (other instanceof org.python.types.Float) {
            return new org.python.types.Float(((double) this.value) * ((org.python.types.Float) other).value);
        } else if (other instanceof org.python.types.List) {
            return other.__mul__(this);
        } else if (other instanceof org.python.types.Tuple) {
            return other.__mul__(this);
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for *: 'int' and '" + other.typeName() + "'");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __truediv__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            return new org.python.types.Float(this.value / ((double)((org.python.types.Int) other).value));
        } else if (other instanceof org.python.types.Float) {
            return new org.python.types.Float(this.value / ((org.python.types.Float) other).value);
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for /: 'int' and '" + other.typeName() + "'");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __floordiv__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            return new org.python.types.Int(this.value / ((org.python.types.Int) other).value);
        } else if (other instanceof org.python.types.Float) {
            return new org.python.types.Int(this.value / ((long) ((org.python.types.Float) other).value));
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for //: 'int' and '" + other.typeName() + "'");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __mod__(org.python.Object other) {
        try {
            if (other instanceof org.python.types.Bool) {
                if (((org.python.types.Bool) other).value) {
                    return new org.python.types.Int(0);
                } else {
                    throw new org.python.exceptions.ZeroDivisionError("integer division or modulo by zero");
                }
            } else if (other instanceof org.python.types.Int) {
                long other_val = ((org.python.types.Int) other).value;
                if (other_val == 0) {
                    throw new org.python.exceptions.ZeroDivisionError("integer division or modulo by zero");
                }
                return new org.python.types.Int(this.value % other_val);
            } else if (other instanceof org.python.types.Float) {
                double other_val = ((org.python.types.Float) other).value;
                if (other_val == 0.0) {
                    throw new org.python.exceptions.ZeroDivisionError("float modulo");
                }
                return new org.python.types.Float(((double) this.value) % other_val);
            }
        } catch (org.python.exceptions.TypeError e) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for %: 'int' and '" + other.typeName() + "'");
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for %: 'int' and '" + other.typeName() + "'");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __divmod__(java.util.List<org.python.Object> args, java.util.Map<java.lang.String, org.python.Object> kwargs, java.util.List<org.python.Object> default_args, java.util.Map<java.lang.String, org.python.Object> default_kwargs) {
        throw new org.python.exceptions.NotImplementedError("int.__divmod__() has not been implemented");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __pow__(org.python.Object other, org.python.Object modulo) {
        if (modulo != null) {
            throw new org.python.exceptions.NotImplementedError("int.__pow__() with modulo has not been implemented");
        }

        if (other instanceof org.python.types.Int) {
            long other_val = ((org.python.types.Int) other).value;
            if (other_val < 0) {
                if (this.value == 0) {
                    throw new org.python.exceptions.ZeroDivisionError("0.0 cannot be raised to a negative power");
                }

                double result = 1.0;
                for (long count = 0; count < -other_val; count++) {
                    result *= this.value;
                }
                return new org.python.types.Float(1.0 / result);
            } else {
                long result = 1;
                for (long count = 0; count < other_val; count++) {
                    result *= this.value;
                }
                return new org.python.types.Int(result);
            }
        } else if (other instanceof org.python.types.Float) {
            double other_val = ((org.python.types.Float) other).value;
            if (this.value == 0 && other_val < 0.0) {
                throw new org.python.exceptions.ZeroDivisionError("0.0 cannot be raised to a negative power");
            }
            return new org.python.types.Float(java.lang.Math.pow((double) this.value, other_val));
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for ** or pow(): 'int' and '" + other.typeName() + "'");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __lshift__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("int.__lshift__() has not been implemented");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rshift__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("int.__rshift__() has not been implemented");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __and__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("int.__and__() has not been implemented");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __xor__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("int.__xor__() has not been implemented");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __or__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("int.__or__() has not been implemented");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __radd__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("int.__radd__() has not been implemented");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rsub__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("int.__rsub__() has not been implemented");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rmul__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("int.__rmul__() has not been implemented");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rtruediv__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("int.__rtruediv__() has not been implemented");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rfloordiv__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("int.__rfloordiv__() has not been implemented");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rmod__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("int.__rmod__() has not been implemented");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rdivmod__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("int.__rdivmod__() has not been implemented");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rpow__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("int.__rpow__() has not been implemented");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rlshift__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("int.__rlshift__() has not been implemented");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rrshift__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("int.__rrshift__() has not been implemented");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rand__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("int.__rand__() has not been implemented");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __rxor__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("int.__rxor__() has not been implemented");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __ror__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("int.__ror__() has not been implemented");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __neg__() {
        if (this.value < 0) {
            return new org.python.types.Int(this.value);
        } else {
            return new org.python.types.Int(-this.value);
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __pos__() {
        if (this.value < 0) {
            return new org.python.types.Int(-this.value);
        } else {
            return new org.python.types.Int(this.value);
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __abs__() {
        if (this.value < 0) {
            return new org.python.types.Int(-this.value);
        } else {
            return new org.python.types.Int(this.value);
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __invert__() {
        throw new org.python.exceptions.NotImplementedError("int.__invert__() has not been implemented");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Int __int__() {
        return new org.python.types.Int(this.value);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Float __float__() {
        return new org.python.types.Float((float) this.value);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __round__(org.python.Object ndigits) {
        throw new org.python.exceptions.NotImplementedError("int.__round__() has not been implemented");
    }

}