package org.python.types;

public class Float extends org.python.types.Object {
    private static final long NEGATIVE_ZERO_RAW_BITS = Double.doubleToRawLongBits(-0.0);
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
        if (other instanceof org.python.types.Int) {
            return new org.python.types.Bool(this.value <= ((double)((org.python.types.Int) other).value));
        } else if (other instanceof Float) {
            return new org.python.types.Bool(this.value <= ((org.python.types.Float) other).value);
        } else if(other instanceof Bool) {
            if (((org.python.types.Bool) other).value) {
                return new org.python.types.Bool(this.value <= 1.0);
            }
            else {
                return new org.python.types.Bool(this.value <= 0.0);
            }
        }
        throw new org.python.exceptions.TypeError("unorderable types: float() <= " + other.typeName() + "()");
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
            if (((org.python.types.Bool) other).value) {
                return new org.python.types.Bool(this.value == 1.0);
            }
            else {
                return new org.python.types.Bool(this.value == 0.0);
            }
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
        if (other instanceof org.python.types.Int) {
            return new org.python.types.Bool(this.value > ((double)((org.python.types.Int) other).value));
        } else if (other instanceof Float) {
            return new org.python.types.Bool(this.value > ((org.python.types.Float) other).value);
        } else if(other instanceof Bool) {
            if (((org.python.types.Bool) other).value) {
                return new org.python.types.Bool(this.value > 1.0);
            }
            else {
                return new org.python.types.Bool(this.value > 0.0);
            }
        }
        throw new org.python.exceptions.TypeError("unorderable types: float() > " + other.typeName() + "()");
    }
    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __ge__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            return new org.python.types.Bool(this.value >= ((double)((org.python.types.Int) other).value));
        } else if (other instanceof Float) {
            return new org.python.types.Bool(this.value >= ((org.python.types.Float) other).value);
        } else if(other instanceof Bool) {
            if (((org.python.types.Bool) other).value) {
                return new org.python.types.Bool(this.value >= 1.0);
            }
            else {
                return new org.python.types.Bool(this.value >= 0.0);
            }
        }
        throw new org.python.exceptions.TypeError("unorderable types: float() >= " + other.typeName() + "()");
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
        if (other instanceof org.python.types.Int) {
            long other_val = ((org.python.types.Int) other).value;
            return new org.python.types.Float(this.value + ((double) other_val));
        } else if (other instanceof org.python.types.Bool) {
            if (((org.python.types.Bool) other).value) {
                return new org.python.types.Float(this.value + 1.0);
            }
            return new org.python.types.Float(this.value);
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for +: 'float' and '" + other.typeName() + "'");
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
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for -: 'float' and '" + other.typeName() + "'");
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
        } else if (other instanceof org.python.types.Dict) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for *: 'float' and '" + other.typeName() + "'");
        } else if (other instanceof org.python.types.NoneType) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for *: 'float' and '" + other.typeName() + "'");
        } else if (other instanceof org.python.types.Set) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for *: 'float' and '" + other.typeName() + "'");
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
        if (other instanceof org.python.types.Int) {
            if (((org.python.types.Int) other).value == 0) {
                throw new org.python.exceptions.ZeroDivisionError("float divmod()");
            }
            return new org.python.types.Float(Math.floor((double) this.value / ((org.python.types.Int) other).value));
        } else if (other instanceof org.python.types.Float) {
            if (((org.python.types.Float) other).value == 0.0) {
                throw new org.python.exceptions.ZeroDivisionError("float divmod()");
            }
            return new org.python.types.Float(Math.floor(this.value / ((org.python.types.Float) other).value));
        } else if (other instanceof org.python.types.Bool) {
            if (((org.python.types.Bool) other).value) {
                return new org.python.types.Float(Math.floor(this.value));
            } else {
                throw new org.python.exceptions.ZeroDivisionError("float divmod()");
            }
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for //: 'float' and '" + other.typeName() + "'");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __mod__(org.python.Object other) {
        try {
            if (other instanceof org.python.types.Bool) {
                if (((org.python.types.Bool) other).value) {
                    return new org.python.types.Float(this.value - Math.floor(this.value));
                } else {
                    throw new org.python.exceptions.ZeroDivisionError("integer division or modulo by zero");
                }
            } else if (other instanceof org.python.types.Int) {
                long other_val = ((org.python.types.Int) other).value;
                if (other_val == 0) {
                    throw new org.python.exceptions.ZeroDivisionError("integer division or modulo by zero");
                } else {
                    double result = this.value % other_val;
                    if (other_val > 0 && result < 0) {
                        // second operand is positive, ensure that result is positive
                        result += other_val;
                    } else if (other_val < 0 && result > 0) {
                        // second operand is negative, ensure that result is negative
                        result += other_val; // subtract other_val, which is negative
                    }
                    if (other_val < 0 && result >= 0
                            && Double.doubleToRawLongBits(result) != NEGATIVE_ZERO_RAW_BITS) {
                        result *= -1;
                    }
                    return new org.python.types.Float(result);
                }
            } else if (other instanceof org.python.types.Float) {
                double other_val = ((org.python.types.Float) other).value;
                if (other_val == 0.0) {
                    throw new org.python.exceptions.ZeroDivisionError("float modulo");
                } else {
                    double result = ((double) this.value) % other_val;
                    if (other_val > 0.0 && result < 0.0) {
                        // second operand is positive, ensure that result is positive
                        result += other_val;
                    } else if (other_val < 0.0 && result > 0.0) {
                        // second operand is negative, ensure that result is negative
                        result += other_val; // subtract other_val, which is negative
                    }
                    // edge case where adding -0.0 to 0.0 doesn't yield the expected -0.0
                    // do this only if it is definitely not -0.0 already
                    if (other_val < 0.0 && result >= 0.0
                            && Double.doubleToRawLongBits(result) != NEGATIVE_ZERO_RAW_BITS) {
                        result *= -1;
                    }
                    return new org.python.types.Float(result);
                }
            }
        } catch (org.python.exceptions.TypeError e) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for %: 'int' and '" + other.typeName() + "'");
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for %: 'int' and '" + other.typeName() + "'");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __divmod__(org.python.Object other) {
        try {
            java.util.List<org.python.Object> data = new java.util.ArrayList<>();
            data.add(this.__floordiv__(other));
            data.add(this.__mod__(other));
            return new org.python.types.Tuple(data);
        } catch (org.python.exceptions.TypeError ae) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for divmod(): '" + this.typeName() + "' and '" + other.typeName() + "'");
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __pow__(org.python.Object other, org.python.Object modulo) {
        if (modulo != null) {
            throw new org.python.exceptions.NotImplementedError("float.__pow__() with modulo has not been implemented");
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
                return new org.python.types.Float(java.lang.Math.pow(this.value, other_val));
            }
        } else if (other instanceof org.python.types.Float) {
            double other_val = ((org.python.types.Float) other).value;
            if (this.value == 0 && other_val < 0.0) {
                throw new org.python.exceptions.ZeroDivisionError("0.0 cannot be raised to a negative power");
            }
            // TODO: if this.value < 0 && other_val is not an integer, this will be a Complex result, so change this.value to Complex and delegate it out
            // return (new org.python.types.Complex(this.value, 0)).__pow__(other, modulo);
            return new org.python.types.Float(java.lang.Math.pow(this.value, other_val));
        } else if (other instanceof org.python.types.Bool) {
            if (((org.python.types.Bool) other).value) {
                return new org.python.types.Float(this.value);
            } else {
                return new org.python.types.Float(1);
            }
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for ** or pow(): 'float' and '" + other.typeName() + "'");
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
        return new org.python.types.Float(-this.value);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __pos__() {
        return new org.python.types.Float(this.value);
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
