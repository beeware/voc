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

    @org.python.Method(
            name = "int",
            __doc__ = "int(x=0) -> integer" +
                    "int(x, base=10) -> integer\n" +
                    "\n" +
                    "Convert a number or string to an integer, or return 0 if no arguments\n" +
                    "are given.  If x is a number, return x.__int__().  For floating point\n" +
                    "numbers, this truncates towards zero.\n" +
                    "\n" +
                    "If x is not a number or if base is given, then x must be a string,\n" +
                    "bytes, or bytearray instance representing an integer literal in the\n" +
                    "given base.  The literal can be preceded by '+' or '-' and be surrounded\n" +
                    "by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\n" +
                    "Base 0 means to interpret the base from the string as an integer literal.\n" +
                    "\n" +
                    "  >>> int('0b100', base=0)\n" +
                    "  4\n",
            default_args = {"x", "base"}
    )
    public Int(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (args[0] == null) {
            this.value = 0;
        } else if (args[1] == null) {
            try {
                this.value = ((org.python.types.Int) args[0].__int__()).value;
            } catch (org.python.exceptions.AttributeError ae) {
                if (org.Python.VERSION < 0x03040300) {
                    throw new org.python.exceptions.TypeError(
                            "int() argument must be a string or a number, not '" + args[0].typeName() + "'"
                    );
                } else {
                    throw new org.python.exceptions.TypeError(
                            "int() argument must be a string, a bytes-like object or a number, not '" +
                                    args[0].typeName() + "'"
                    );
                }
            }
        } else if (args.length > 3) {
            throw new org.python.exceptions.NotImplementedError("int() with a base is not implemented");
        }
    }

    // public org.python.Object __new__() {
    //     throw new org.python.exceptions.NotImplementedError("int.__new__() has not been implemented");
    // }

    // public org.python.Object __init__() {
    //     throw new org.python.exceptions.NotImplementedError("int.__init__() has not been implemented");
    // }

    @org.python.Method(
            __doc__ = "Return repr(self)."
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
    public org.python.types.Str __getitem__(org.python.Object format_str) {
        throw new org.python.exceptions.TypeError("'int' object is not subscriptable");
    }

    @org.python.Method(
            __doc__ = "Return self<value.",
            args = {"other"}
    )
    public org.python.Object __lt__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            return new org.python.types.Bool(this.value < ((org.python.types.Int) other).value);
        } else if (other instanceof org.python.types.Bool) {
            return new org.python.types.Bool(((double) this.value) < (((org.python.types.Bool) other).value ? 1 : 0));
        }
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "Return self<=value.",
            args = {"other"}
    )
    public org.python.Object __le__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            return new org.python.types.Bool(this.value <= ((org.python.types.Int) other).value);
        } else if (other instanceof org.python.types.Bool) {
            return new org.python.types.Bool(((double) this.value) <= (((org.python.types.Bool) other).value ? 1 : 0));
        }
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "Return self==value.",
            args = {"other"}
    )
    public org.python.Object __eq__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            return new org.python.types.Bool(this.value == ((org.python.types.Int) other).value);
        } else if (other instanceof org.python.types.Bool) {
            org.python.types.Bool temp = (org.python.types.Bool) other;
            if (this.value == 1 && temp.value) {
                return new org.python.types.Bool(1);
            }
            if (this.value == 0 && !temp.value) {
                return new org.python.types.Bool(1);
            }
            return new org.python.types.Bool(0);
        }
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "Return self>value.",
            args = {"other"}
    )
    public org.python.Object __gt__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            return new org.python.types.Bool(this.value > ((org.python.types.Int) other).value);
        } else if (other instanceof org.python.types.Bool) {
            return new org.python.types.Bool(((double) this.value) > (((org.python.types.Bool) other).value ? 1 : 0));
        }
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "Return self>=value.",
            args = {"other"}
    )
    public org.python.Object __ge__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            return new org.python.types.Bool(this.value >= ((org.python.types.Int) other).value);
        } else if (other instanceof org.python.types.Bool) {
            return new org.python.types.Bool(((double) this.value) >= (((org.python.types.Bool) other).value ? 1 : 0));
        }
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "self != 0"
    )
    public org.python.types.Bool __bool__() {
        return new org.python.types.Bool(this.value);
    }

    public boolean __setattr_null(java.lang.String name, org.python.Object value) {
        // Builtin types can't have attributes set on them.
        return false;
    }

    @org.python.Method(
            __doc__ = "__dir__() -> list\ndefault dir() implementation"
    )
    public org.python.types.List __dir__() {
        throw new org.python.exceptions.NotImplementedError("int.__dir__() has not been implemented");
    }

    @org.python.Method(
            __doc__ = "Return self+value.",
            args = {"other"}
    )
    public org.python.Object __add__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            return new org.python.types.Int(this.value + ((org.python.types.Int) other).value);
        } else if (other instanceof org.python.types.Float) {
            return new org.python.types.Float(((double) this.value) + ((org.python.types.Float) other).value);
        } else if (other instanceof org.python.types.Bool) {
            return new org.python.types.Int(this.value + (((org.python.types.Bool) other).value ? 1 : 0));
        } else if (other instanceof org.python.types.Complex) {
            org.python.types.Complex other_cmplx_object = (org.python.types.Complex) other;
            return new org.python.types.Complex((org.python.types.Float) this.__add__(other_cmplx_object.real), (org.python.types.Float) (new org.python.types.Float(0)).__add__(other_cmplx_object.imag));
        } else {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for +: 'int' and '" + other.typeName() + "'");
        }
    }

    @org.python.Method(
            __doc__ = "Return self-value.",
            args = {"other"}
    )
    public org.python.Object __sub__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            return new org.python.types.Int(this.value - ((org.python.types.Int) other).value);
        } else if (other instanceof org.python.types.Float) {
            return new org.python.types.Float(((double) this.value) - ((org.python.types.Float) other).value);
        } else if (other instanceof org.python.types.Bool) {
            return new org.python.types.Int(this.value - (((org.python.types.Bool) other).value ? 1 : 0));
        } else if (other instanceof org.python.types.Complex) {
            org.python.types.Complex other_cmplx_object = (org.python.types.Complex) other;
            return new org.python.types.Complex((org.python.types.Float) this.__sub__(other_cmplx_object.real), (org.python.types.Float) (new org.python.types.Float(0)).__sub__(other_cmplx_object.imag));
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for -: 'int' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "Return self*value.",
            args = {"other"}
    )
    public org.python.Object __mul__(org.python.Object other) {
        if (other instanceof org.python.types.Str) {
            return other.__mul__(this);
        } else if (other instanceof org.python.types.Int) {
            return new org.python.types.Int(this.value * ((org.python.types.Int) other).value);
        } else if (other instanceof org.python.types.Float) {
            return new org.python.types.Float(((double) this.value) * ((org.python.types.Float) other).value);
        } else if (other instanceof org.python.types.Complex) {
            return ((org.python.types.Complex) other).__mul__(this);
        } else if (other instanceof org.python.types.Bool) {
            return new org.python.types.Int(this.value * (((org.python.types.Bool) other).value ? 1 : 0));
        } else if (other instanceof org.python.types.List) {
            return other.__mul__(this);
        } else if (other instanceof org.python.types.Tuple) {
            return other.__mul__(this);
        } else if (other instanceof org.python.types.Bytes) {
            byte[] other_value = ((org.python.types.Bytes) other).value;
            int value = Math.max(0, (int) this.value);
            int len = other_value.length;
            byte[] bytes = new byte[value * len];
            for (int i = 0; i < value; i++) {
                System.arraycopy(other_value, 0, bytes, i * len, len);
            }
            return new org.python.types.Bytes(bytes);
        } else if (other instanceof org.python.types.ByteArray) {
            byte[] other_value = ((org.python.types.ByteArray) other).value;
            int value = Math.max(0, (int) this.value);
            int len = other_value.length;
            byte[] bytes = new byte[value * len];
            for (int i = 0; i < value; i++) {
                System.arraycopy(other_value, 0, bytes, i * len, len);
            }
            return new org.python.types.ByteArray(bytes);
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for *: 'int' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "Return self/value.",
            args = {"other"}
    )
    public org.python.Object __truediv__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            if (((org.python.types.Int) other).value == 0) {
                throw new org.python.exceptions.ZeroDivisionError("division by zero");
            }
            return new org.python.types.Float((double) this.value / ((org.python.types.Int) other).value);
        } else if (other instanceof org.python.types.Float) {
            if (((org.python.types.Float) other).value == 0.0) {
                throw new org.python.exceptions.ZeroDivisionError("float division by zero");
            }
            return new org.python.types.Float(this.value / ((org.python.types.Float) other).value);
        } else if (other instanceof org.python.types.Complex) {
            if (((org.python.types.Complex) other).real.value == 0.0 && ((org.python.types.Complex) other).imag.value == 0.0) {
                throw new org.python.exceptions.ZeroDivisionError("complex division by zero");
            }
            org.python.types.Complex cmplx_obj = new org.python.types.Complex((double) this.value, 0.0);
            org.python.types.Complex other_cmplx_obj = (org.python.types.Complex) other;
            return cmplx_obj.__truediv__(other_cmplx_obj);

        } else if (other instanceof org.python.types.Bool) {
            if (((org.python.types.Bool) other).value) {
                return new org.python.types.Float(this.value);
            } else {
                throw new org.python.exceptions.ZeroDivisionError("division by zero");
            }
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for /: 'int' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "Return self//value.",
            args = {"other"}
    )
    public org.python.Object __floordiv__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            if (((org.python.types.Int) other).value == 0) {
                throw new org.python.exceptions.ZeroDivisionError("integer division or modulo by zero");
            }
            return new org.python.types.Int((long) Math.floor((double) this.value / ((org.python.types.Int) other).value));
        } else if (other instanceof org.python.types.Float) {
            if (((org.python.types.Float) other).value == 0.0) {
                throw new org.python.exceptions.ZeroDivisionError("float divmod()");
            }
            return new org.python.types.Float(Math.floor(this.value / ((org.python.types.Float) other).value));
        } else if (other instanceof org.python.types.Bool) {
            if (((org.python.types.Bool) other).value) {
                return new org.python.types.Int(this.value);
            } else {
                throw new org.python.exceptions.ZeroDivisionError("integer division or modulo by zero");
            }
        } else if (other instanceof org.python.types.Complex) {
            throw new org.python.exceptions.TypeError("can't take floor of complex number.");
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for //: '" + this.typeName() + "' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "Return self%value.",
            args = {"other"}
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
                } else {
                    long result = this.value % other_val;
                    if (other_val > 0 && result < 0) {
                        // second operand is positive, ensure that result is positive
                        result += other_val;
                    } else if (other_val < 0 && result > 0) {
                        // second operand is negative, ensure that result is negative
                        result += other_val; // subtract other_val, which is negative
                    }
                    return new org.python.types.Int(result);
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
                    // edge case where operands are 0 and -0.0:
                    // need to force sign to negative as adding -0.0 to 0.0 doesn't yield the expected -0.0
                    if (other_val < 0.0 && result >= 0.0) {
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
            __doc__ = "Return divmod(self, value).",
            args = {"other"}
    )
    public org.python.Object __divmod__(org.python.Object other) {
        try {
            java.util.List<org.python.Object> data = new java.util.ArrayList<org.python.Object>();
            data.add(this.__floordiv__(other));
            data.add(this.__mod__(other));
            return new org.python.types.Tuple(data);
        } catch (org.python.exceptions.TypeError ae) {
            throw new org.python.exceptions.TypeError(
                    "unsupported operand type(s) for divmod(): '" + this.typeName() + "' and '" + other.typeName() + "'"
            );
        }
    }
    @org.python.Method(
            __doc__ = "Return pow(self, other, mod).",
            args = {"other"},
            default_args = {"modulo"}
    )
    public org.python.Object __pow__(org.python.Object other, org.python.Object modulo) {
        if (modulo != null) {
            /* if exponent is not int and modulo specified raise TypeError*/
            if (other instanceof org.python.types.Float) {
                throw new org.python.exceptions.TypeError("pow() 3rd argument not allowed unless all arguments are integers");
            }
            if (other instanceof org.python.types.Int || other instanceof org.python.types.Bool) {
                long this_val = ((org.python.types.Int) this).value;
                long other_val = ((org.python.types.Int) other).value;
                long modulo_val = ((org.python.types.Int) modulo).value;
                /* if exponent is negative raise TypeError*/
                if (other_val < 0) {
                    if (org.Python.VERSION < 0x03050000) {
                        throw new org.python.exceptions.TypeError(
                                "pow() 2nd argument cannot be negative when 3rd argument specified"
                        );
                    } else {
                        throw new org.python.exceptions.ValueError(
                                "pow() 2nd argument cannot be negative when 3rd argument specified"
                        );
                    }
                }
                /* if modulus == 0: raise ValueError() */
                if (modulo_val == 0) {
                    throw new org.python.exceptions.ValueError("pow() 3rd argument cannot be 0");
                }
                /* if modulus == 1:
                       return 0 */
                if (modulo_val == 1) {
                    return new org.python.types.Int(0);
                }
                /* if base < 0:
                       base = base % modulus */
                if (this_val < 0) {
                    this_val = this_val % modulo_val;
                }
                /* At this point a, b, and c are guaranteed non-negative UNLESS
                c is NULL, in which case a may be negative. */
                long result = 1;
                this_val = this_val % modulo_val;
                while (other_val != 0) {
                    if (other_val % 2 == 1) {
                        result = (result * this_val) % modulo_val;
                    }
                    this_val = (this_val * this_val) % modulo_val;
                    other_val /= 2;
                }
                return new org.python.types.Int(result);
            }
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for pow(): 'int', '" + other.typeName() + "', 'int");
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
            if (this.value < 0 && Math.floor(other_val) != other_val) {
                // The result will be complex, so make it a complex type instead
                return (new org.python.types.Complex(this.value, 0)).__pow__(other, modulo);
            }
            return new org.python.types.Float(java.lang.Math.pow((double) this.value, other_val));
        } else if (other instanceof org.python.types.Complex) {
            org.python.types.Complex cmplx_obj = new org.python.types.Complex((double) this.value, 0.0);
            org.python.types.Complex other_cmplx_obj = (org.python.types.Complex) other;
            return cmplx_obj.__pow__(other_cmplx_obj, null);
        } else if (other instanceof org.python.types.Bool) {
            if (((org.python.types.Bool) other).value) {
                return new org.python.types.Int(this.value);
            } else {
                return new org.python.types.Int(1);
            }
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for ** or pow(): 'int' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "Return self<<value.",
            args = {"other"}
    )
    public org.python.Object __lshift__(org.python.Object other) {
        if (other instanceof org.python.types.Bool) {
            return new org.python.types.Int(this.value << (((org.python.types.Bool) other).value ? 1 : 0));
        } else if (other instanceof org.python.types.Int) {
            long other_val = ((org.python.types.Int) other).value;
            if (other_val < 0) {
                throw new org.python.exceptions.ValueError("negative shift count");
            }
            return new org.python.types.Int(this.value << other_val);
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for <<: 'int' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "Return self>>value.",
            args = {"other"}
    )
    public org.python.Object __rshift__(org.python.Object other) {
        if (other instanceof org.python.types.Bool) {
            return new org.python.types.Int(this.value >> (((org.python.types.Bool) other).value ? 1 : 0));
        } else if (other instanceof org.python.types.Int) {
            long other_val = ((org.python.types.Int) other).value;
            if (other_val < 0) {
                throw new org.python.exceptions.ValueError("negative shift count");
            }
            return new org.python.types.Int(this.value >> other_val);
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for >>: 'int' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "Return self&value.",
            args = {"other"}
    )
    public org.python.Object __and__(org.python.Object other) {
        if (other instanceof org.python.types.Bool) {
            return new org.python.types.Int(this.value & (((org.python.types.Bool) other).value ? 1 : 0));
        } else if (other instanceof org.python.types.Int) {
            return new org.python.types.Int(this.value & ((org.python.types.Int) other).value);
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for &: 'int' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "Return self^value.",
            args = {"other"}
    )
    public org.python.Object __xor__(org.python.Object other) {
        if (other instanceof org.python.types.Bool) {
            return new org.python.types.Int(this.value ^ (((org.python.types.Bool) other).value ? 1 : 0));
        } else if (other instanceof org.python.types.Int) {
            return new org.python.types.Int(this.value ^ ((org.python.types.Int) other).value);
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for ^: 'int' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "Return self|value.",
            args = {"other"}
    )
    public org.python.Object __or__(org.python.Object other) {
        if (other instanceof org.python.types.Bool) {
            return new org.python.types.Int(this.value | (((org.python.types.Bool) other).value ? 1 : 0));
        } else if (other instanceof org.python.types.Int) {
            return new org.python.types.Int(this.value | ((org.python.types.Int) other).value);
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for |: 'int' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "Return value+self.",
            args = {"other"}
    )
    public org.python.Object __radd__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("int.__radd__() has not been implemented");
    }

    @org.python.Method(
            __doc__ = "Return value-self.",
            args = {"other"}
    )
    public org.python.Object __rsub__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("int.__rsub__() has not been implemented");
    }

    @org.python.Method(
            __doc__ = "Return value*self.",
            args = {"other"}
    )
    public org.python.Object __rmul__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("int.__rmul__() has not been implemented");
    }

    @org.python.Method(
            __doc__ = "Return value/self.",
            args = {"other"}
    )
    public org.python.Object __rtruediv__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("int.__rtruediv__() has not been implemented");
    }

    @org.python.Method(
            __doc__ = "Return value//self.",
            args = {"other"}
    )
    public org.python.Object __rfloordiv__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("int.__rfloordiv__() has not been implemented");
    }

    @org.python.Method(
            __doc__ = "Return value%self.",
            args = {"other"}
    )
    public org.python.Object __rmod__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("int.__rmod__() has not been implemented");
    }

    @org.python.Method(
            __doc__ = "Return divmod(value, self).",
            args = {"other"}
    )
    public org.python.Object __rdivmod__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("int.__rdivmod__() has not been implemented");
    }

    @org.python.Method(
            __doc__ = "Return pow(value, self, mod).",
            args = {"other"}
    )
    public org.python.Object __rpow__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("int.__rpow__() has not been implemented");
    }

    @org.python.Method(
            __doc__ = "Return value<<self.",
            args = {"other"}
    )
    public org.python.Object __rlshift__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("int.__rlshift__() has not been implemented");
    }

    @org.python.Method(
            __doc__ = "Return value>>self.",
            args = {"other"}
    )
    public org.python.Object __rrshift__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("int.__rrshift__() has not been implemented");
    }

    @org.python.Method(
            __doc__ = "Return value&self.",
            args = {"other"}
    )
    public org.python.Object __rand__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("int.__rand__() has not been implemented");
    }

    @org.python.Method(
            __doc__ = "Return value^self.",
            args = {"other"}
    )
    public org.python.Object __rxor__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("int.__rxor__() has not been implemented");
    }

    @org.python.Method(
            __doc__ = "Return value|self.",
            args = {"other"}
    )
    public org.python.Object __ror__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("int.__ror__() has not been implemented");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __imod__(org.python.Object other) {
        if (other instanceof org.python.types.Bool) {
            return this.__mod__(other);
        } else if (other instanceof org.python.types.Int) {
            return this.__mod__(other);
        } else if (other instanceof org.python.types.Float) {
            return this.__mod__(other);
        } else if (other instanceof org.python.types.Complex) {
            throw new org.python.exceptions.TypeError("can't mod complex numbers.");
        } else {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for %=: 'int' and '" + other.typeName() + "'");
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __imul__(org.python.Object other) {
        if (other instanceof org.python.types.Str) {
            return this.__mul__(other);
        } else if (other instanceof org.python.types.Bool) {
            return this.__mul__(other);
        } else if (other instanceof org.python.types.Int) {
            return this.__mul__(other);
        } else if (other instanceof org.python.types.Float) {
            return this.__mul__(other);
        } else if (other instanceof org.python.types.Complex) {
            return this.__mul__(other);
        } else if (other instanceof org.python.types.ByteArray) {
            return this.__mul__(other);
        } else if (other instanceof org.python.types.Bytes) {
            return this.__mul__(other);
        } else if (other instanceof org.python.types.Tuple) {
            return this.__mul__(other);
        } else if (other instanceof org.python.types.List) {
            return this.__mul__(other);
        } else {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for *=: 'int' and '" + other.typeName() + "'");
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __ilshift__(org.python.Object other) {
        if (other instanceof org.python.types.Bool) {
            this.value <<= (((org.python.types.Bool) other).value ? 1 : 0);
            return new org.python.types.Int(this.value);
        } else if (other instanceof org.python.types.Int) {
            long other_val = ((org.python.types.Int) other).value;
            if (other_val < 0) {
                throw new org.python.exceptions.ValueError("negative shift count");
            }
            this.value <<= other_val;
            return new org.python.types.Int(this.value);
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for <<=: 'int' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __ipow__(org.python.Object other) {
        if (other instanceof org.python.types.Str) {
            return this.__pow__(other, null);
        } else if (other instanceof org.python.types.Bool) {
            return this.__pow__(other, null);
        } else if (other instanceof org.python.types.Int) {
            return this.__pow__(other, null);
        } else if (other instanceof org.python.types.Float) {
            return this.__pow__(other, null);
        } else if (other instanceof org.python.types.Complex) {
            return this.__pow__(other, null);
        } else if (other instanceof org.python.types.Tuple) {
            return this.__pow__(other, null);
        } else if (other instanceof org.python.types.List) {
            return this.__pow__(other, null);
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for ** or pow(): 'int' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __itruediv__(org.python.Object other) {
        if (other instanceof org.python.types.Int || other instanceof org.python.types.Float || other instanceof org.python.types.Bool || other instanceof org.python.types.Complex) {
            return this.__truediv__(other);
        } else {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for /=: 'int' and '" + other.typeName() + "'");
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __ifloordiv__(org.python.Object other) {
        if (other instanceof org.python.types.Int || other instanceof org.python.types.Float || other instanceof org.python.types.Bool || other instanceof org.python.types.Complex) {
            return this.__floordiv__(other);
        } else {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for //=: 'int' and '" + other.typeName() + "'");
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __irshift__(org.python.Object other) {
        if (other instanceof org.python.types.Bool) {
            this.value >>= (((org.python.types.Bool) other).value ? 1 : 0);
            return new org.python.types.Int(this.value);
        } else if (other instanceof org.python.types.Int) {
            long other_val = ((org.python.types.Int) other).value;
            if (other_val < 0) {
                throw new org.python.exceptions.ValueError("negative shift count");
            }
            this.value >>= other_val;
            return new org.python.types.Int(this.value);
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for >>=: 'int' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "-self"
    )
    public org.python.Object __neg__() {
        return new org.python.types.Int(-this.value);
    }

    @org.python.Method(
            __doc__ = "+self"
    )
    public org.python.Object __pos__() {
        return new org.python.types.Int(this.value);
    }

    @org.python.Method(
            __doc__ = "abs(self)"
    )
    public org.python.Object __abs__() {
        return new org.python.types.Int(Math.abs(this.value));
    }

    @org.python.Method(
            __doc__ = "~self"
    )
    public org.python.Object __invert__() {
        return new org.python.types.Int(-(this.value + 1));
    }

    @org.python.Method(
            __doc__ = "int(self)"
    )
    public org.python.Object __int__() {
        return new org.python.types.Int(this.value);
    }

    @org.python.Method(
            __doc__ = "float(self)"
    )
    public org.python.Object __float__() {
        return new org.python.types.Float((float) this.value);
    }

    @org.python.Method(
            __doc__ = "Rounding an Integral returns itself.\nRounding with an ndigits argument also returns an integer."
    )
    public org.python.Object __round__(org.python.Object ndigits) {
        if (ndigits instanceof org.python.types.Int) {
            return new org.python.types.Int(this.value);
        }
        throw new org.python.exceptions.TypeError("'" + ndigits.typeName() + "' object cannot be interpreted as an integer");
    }
}
