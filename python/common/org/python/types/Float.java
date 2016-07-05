package org.python.types;
import java.util.Locale;

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
        double value = this.value;
        String result;
        if (Double.isNaN(value)) {
            result = "nan";
        } else if (Double.isInfinite(value)) {
            if (value > 0) {
                result = "inf";
            } else {
                result = "-inf";
            }
        } else {
            result = java.lang.Double.toString(this.value);
            String format = "%.17g";
            result = String.format(Locale.US, format, value);
            int dot_pos = result.indexOf(".");
            int e_pos = result.indexOf("e");
            if (dot_pos != -1) {
                // Remove trailing zeroes in the fractional part
                int last_zero = -1;
                int i;
                for (i = dot_pos + 1; i < result.length(); i++) {
                    char c = result.charAt(i);
                    if (i == e_pos) {
                        break;
                    } else if (c == '0') {
                        if (last_zero == -1) {
                            last_zero = i;
                        }
                    } else {
                        last_zero = -1;
                    }
                }
                if (last_zero != -1) {
                    if (last_zero == dot_pos + 1) {
                        // Everything after the dot is zeros
                        if (e_pos == -1) {
                            // If there's no "e", leave ".0" at the end
                            last_zero += 1;
                        } else {
                            // If there is an "e", nuke the dot as well
                            last_zero -= 1;
                        }
                    }
                    result = result.substring(0, last_zero) + result.substring(i);
                }
            }
        }
        return new org.python.types.Str(result);
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
            } else {
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
        } else if (other instanceof Bool) {
            if (((org.python.types.Bool) other).value) {
                return new org.python.types.Bool(this.value <= 1.0);
            } else {
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
        } else if (other instanceof org.python.types.Float) {
            return new org.python.types.Bool(this.value == ((org.python.types.Float) other).value);
        } else if (other instanceof org.python.types.Bool) {
            if (((org.python.types.Bool) other).value) {
                return new org.python.types.Bool(this.value == 1.0);
            } else {
                return new org.python.types.Bool(this.value == 0.0);
            }
        } else if (other instanceof org.python.types.NoneType) {
            return new org.python.types.Bool(false);
        } else if (other instanceof org.python.types.Str) {
            return new org.python.types.Bool(false);
        }
        throw new org.python.exceptions.TypeError("unorderable types: float() == " + other.typeName() + "()");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __ne__(org.python.Object other) {
        if (other instanceof org.python.types.Int || other instanceof org.python.types.Float ||
                other instanceof org.python.types.Bool || other instanceof org.python.types.NoneType ||
                other instanceof org.python.types.Str) {
            if (((org.python.types.Bool) this.__eq__((org.python.Object) other)).value) {
                return new org.python.types.Bool(false);
            } else if (!((org.python.types.Bool) this.__eq__((org.python.Object) other)).value) {
                return new org.python.types.Bool(true);
            }
        }
        throw new org.python.exceptions.TypeError("unorderable types: float() == " + other.typeName() + "()");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __gt__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            return new org.python.types.Bool(this.value > ((double)((org.python.types.Int) other).value));
        } else if (other instanceof Float) {
            return new org.python.types.Bool(this.value > ((org.python.types.Float) other).value);
        } else if (other instanceof Bool) {
            if (((org.python.types.Bool) other).value) {
                return new org.python.types.Bool(this.value > 1.0);
            } else {
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
        } else if (other instanceof Bool) {
            if (((org.python.types.Bool) other).value) {
                return new org.python.types.Bool(this.value >= 1.0);
            } else {
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
            } else {
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
                    throw new org.python.exceptions.ZeroDivisionError("float modulo");
                }
            } else if (other instanceof org.python.types.Int) {
                long other_val = ((org.python.types.Int) other).value;
                if (other_val == 0) {
                    throw new org.python.exceptions.ZeroDivisionError("float modulo");
                } else {
                    // Reference: http://stackoverflow.com/a/4412200
                    // This translates to (a % b + b) %b
                    // This expression works as the result of (a % b) is necessarily lower than b,
                    // no matter if a is positive or negative. Adding b takes care of the negative
                    // values of a, since (a % b) is a negative value between -b and 0, (a % b + b)
                    // is necessarily lower than b and positive. The last modulo is there in case a
                    // was positive to begin with, since if a is positive (a % b + b) would become
                    // larger than b. Therefore, (a % b + b) % b turns it into smaller than b again
                    // (and doesn't affect negative a values).
                    double result = (((((double) this.value) % other_val) + other_val) % other_val);
                    return new org.python.types.Float(result);
                }
            } else if (other instanceof org.python.types.Float) {
                double other_val = ((org.python.types.Float) other).value;
                if (other_val == 0.0) {
                    throw new org.python.exceptions.ZeroDivisionError("float modulo");
                } else {
                    double result = (((((double) this.value) % other_val) + other_val) % other_val);
                    return new org.python.types.Float(result);
                }
            }
        } catch (org.python.exceptions.TypeError e) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for %: 'float' and '" + other.typeName() + "'");
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for %: 'float' and '" + other.typeName() + "'");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __divmod__(org.python.Object other) {
        try {
            java.util.List<org.python.Object> data = new java.util.ArrayList<org.python.Object>();
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
    public org.python.Object __iadd__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            long other_val = ((org.python.types.Int) other).value;
            return new org.python.types.Float(this.value += ((double) other_val));
        } else if (other instanceof org.python.types.Bool) {
            if (((org.python.types.Bool) other).value) {
                return new org.python.types.Float(this.value += 1.0);
            }
            return new org.python.types.Float(this.value);
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for +=: 'float' and '" + other.typeName() + "'");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __ilshift__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for <<=: 'float' and '" + other.typeName() + "'");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __irshift__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for >>=: 'float' and '" + other.typeName() + "'");
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
        if(ndigits instanceof org.python.types.Int) {
            long wholeNumber;
            double fractionalPart;
            if (((org.python.types.Int)ndigits).value != 0) {
                throw new org.python.exceptions.NotImplementedError("float.__round__() with ndigits has not been implemented");
            } else {
                wholeNumber = (long) this.value;
                fractionalPart = this.value - wholeNumber;
            }
            int sign;
            if (wholeNumber >= 0) {
                sign = 1;
            } else {
                sign = -1;
            }
            if (Math.abs(fractionalPart) < 0.5) {
                return new org.python.types.Int(sign * Math.abs(wholeNumber));
            } else if (Math.abs(fractionalPart) > 0.5) {
                return new org.python.types.Int(sign * (Math.abs(wholeNumber) + 1));
            } else {
                if (wholeNumber % 2 == 0) {
                    return new org.python.types.Int(sign * Math.abs(wholeNumber));
                } else {
                    return new org.python.types.Int(sign * (Math.abs(wholeNumber) + 1));
                }
            }
        } else {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for round(): 'float' and '" + ndigits.typeName() + "'");
        }
    }


    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __invert__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary ~: 'float'");
    }


    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Str hex() {
        String result;
        if (Double.isNaN(this.value)) {
            result = "nan";
        } else if (Double.isInfinite(this.value)) {
            if (this.value > 0) {
                result = "inf";
            } else {
                result = "-inf";
            }
        } else {
            long bits = Double.doubleToLongBits(this.value);
            StringBuilder buffer = new StringBuilder();
            boolean sign = (bits >> 63) != 0;
            long exponent = (bits >> 52) & 0x7ffL;
            long mantissa = bits & 0x000fffffffffffffL;
            if (sign) {
                buffer.append("-");
            }
            buffer.append("0x");
            String hexMantissa = Long.toHexString(mantissa);
            if (exponent == 0) {
                buffer.append("0.");
            } else {
                buffer.append("1.");
            }
            if (exponent == 0 && mantissa == 0) {
                // for some reason the matissa is not padded in this case
                buffer.append(hexMantissa);
                buffer.append("p+0");
            } else {
                buffer.append("0000000000000".substring(hexMantissa.length()));
                buffer.append(hexMantissa);
                if (exponent == 0) {
                    exponent = -1022;
                } else {
                    exponent -= 1023;
                }
                if (exponent >= 0) {
                    buffer.append("p+");
                    buffer.append(Long.toString(exponent));
                } else {
                    buffer.append("p-");
                    buffer.append(Long.toString(-exponent));
                }
            }
            result = buffer.toString();
        }
        return new org.python.types.Str(result);
    }
}
