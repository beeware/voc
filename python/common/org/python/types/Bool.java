package org.python.types;

public class Bool extends org.python.types.Object {
    public boolean value;
    public static org.python.Object TRUE = new org.python.types.Bool(true);
    public static org.python.Object FALSE = new org.python.types.Bool(false);

    /**
     * A utility method to update the internal value of this object.
     *
     * Used by __i*__ operations to do an in-place operation.
     * obj must be of type org.python.types.Bool
     */
    void setValue(org.python.Object obj) {
        this.value = ((org.python.types.Bool) obj).value;
    }

    public java.lang.Object toJava() {
        return this.value;
    }

    public org.python.Object byValue() {
        return new org.python.types.Bool(this.value);
    }

    public int hashCode() {
        return new java.lang.Boolean(this.value).hashCode();
    }

    public Bool(boolean bool) {
        super();
        this.value = bool;
    }

    public Bool(long int_val) {
        super();
        this.value = int_val != 0;
    }

    @org.python.Method(
            __doc__ = "bool(x) -> bool" +
                    "\n" +
                    "Returns True when the argument x is true, False otherwise.\n" +
                    "The builtins True and False are the only two instances of the class bool.\n" +
                    "The class bool is a subclass of the class int, and cannot be subclassed.\n",
            default_args = {"x"}
    )
    public Bool(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (args[0] == null) {
            this.value = false;
        } else {
            this.value = args[0].toBoolean();
        }
    }
    // public org.python.Object __new__() {
    //     throw new org.python.exceptions.NotImplementedError("bool.__new__() has not been implemented.");
    // }

    // public org.python.Object __init__() {
    //     throw new org.python.exceptions.NotImplementedError("bool.__init__() has not been implemented.");
    // }

    @org.python.Method(
            __doc__ = "Return repr(self)."
    )
    public org.python.types.Str __repr__() {
        if (this.value) {
            return new org.python.types.Str("True");
        } else {
            return new org.python.types.Str("False");
        }
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.types.Str __format__(org.python.Object format_string) {
        throw new org.python.exceptions.NotImplementedError("'bool'.__format__ has not been implemented.");
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.types.Str __getitem__(org.python.Object format_string) {
        throw new org.python.exceptions.TypeError("'bool' object is not subscriptable");
    }

    @org.python.Method(
            __doc__ = "Return self<value.",
            args = {"other"}
    )
    public org.python.Object __lt__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            return new org.python.types.Bool((((org.python.types.Bool) this).value ? 1 : 0) < ((org.python.types.Int) other).value);
        } else if (other instanceof org.python.types.Bool) {
            return new org.python.types.Bool((((org.python.types.Bool) this).value ? 1 : 0) < (((org.python.types.Bool) other).value ? 1 : 0));
        }
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "Return self<=value.",
            args = {"other"}
    )
    public org.python.Object __le__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            return new org.python.types.Bool((((org.python.types.Bool) this).value ? 1 : 0) <= ((org.python.types.Int) other).value);
        } else if (other instanceof org.python.types.Bool) {
            return new org.python.types.Bool((((org.python.types.Bool) this).value ? 1 : 0) <= (((org.python.types.Bool) other).value ? 1 : 0));
        }
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "Return self==value.",
            args = {"other"}
    )
    public org.python.Object __eq__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            return new org.python.types.Bool((((org.python.types.Bool) this).value ? 1 : 0) == ((org.python.types.Int) other).value);
        } else if (other instanceof org.python.types.Bool) {
            return new org.python.types.Bool((((org.python.types.Bool) this).value ? 1 : 0) == (((org.python.types.Bool) other).value ? 1 : 0));
        }
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "Return self>value.",
            args = {"other"}
    )
    public org.python.Object __gt__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            return new org.python.types.Bool((((org.python.types.Bool) this).value ? 1 : 0) > ((org.python.types.Int) other).value);
        } else if (other instanceof org.python.types.Bool) {
            return new org.python.types.Bool((((org.python.types.Bool) this).value ? 1 : 0) > (((org.python.types.Bool) other).value ? 1 : 0));
        }
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "Return self>=value.",
            args = {"other"}
    )
    public org.python.Object __ge__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            return new org.python.types.Bool((((org.python.types.Bool) this).value ? 1 : 0) >= ((org.python.types.Int) other).value);
        } else if (other instanceof org.python.types.Bool) {
            return new org.python.types.Bool((((org.python.types.Bool) this).value ? 1 : 0) >= (((org.python.types.Bool) other).value ? 1 : 0));
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
        throw new org.python.exceptions.NotImplementedError("bool.__dir__() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "Return self+value.",
            args = {"other"}
    )

    public org.python.Object __add__(org.python.Object other) {
        if (other instanceof org.python.types.Bool) {
            return new org.python.types.Int((((org.python.types.Bool) this).value ? 1 : 0) + (((org.python.types.Bool) other).value ? 1 : 0));
        } else if (other instanceof org.python.types.Int) {
            return new org.python.types.Int((((org.python.types.Bool) this).value ? 1 : 0) + ((org.python.types.Int) other).value);
        } else if (other instanceof org.python.types.Float) {
            return new org.python.types.Float((((org.python.types.Bool) this).value ? 1 : 0) + ((org.python.types.Float) other).value);
        } else if (other instanceof org.python.types.Complex) {
            org.python.types.Complex cmplx = new org.python.types.Complex(((org.python.types.Bool) this).value ? 1 : 0, 0);
            org.python.types.Complex other_cmplx = (org.python.types.Complex) other;
            return new org.python.types.Complex(cmplx.real.value + other_cmplx.real.value, other_cmplx.imag.value);
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for +: 'bool' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "Return self-value.",
            args = {"other"}
    )
    public org.python.Object __sub__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            return new org.python.types.Int((((org.python.types.Bool) this).value ? 1 : 0) - ((org.python.types.Int) other).value);
        } else if (other instanceof org.python.types.Bool) {
            return new org.python.types.Int((((org.python.types.Bool) this).value ? 1 : 0) - (((org.python.types.Bool) other).value ? 1 : 0));
        } else if (other instanceof org.python.types.Float) {
            return new org.python.types.Float((((org.python.types.Bool) this).value ? 1.0 : 0.0) - (((org.python.types.Float) other).value));
        } else if (other instanceof org.python.types.Complex) {
            org.python.types.Complex cmplx = new org.python.types.Complex(((org.python.types.Bool) this).value ? 1 : 0, 0);
            org.python.types.Complex other_cmplx = (org.python.types.Complex) other;
            return cmplx.__sub__(other_cmplx);
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for -: 'bool' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "Return self*value.",
            args = {"other"}
    )
    public org.python.Object __mul__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            return new org.python.types.Int((((org.python.types.Bool) this).value ? 1 : 0) * ((org.python.types.Int) other).value);
        } else if (other instanceof org.python.types.Bool) {
            return new org.python.types.Int((((org.python.types.Bool) this).value ? 1 : 0) * (((org.python.types.Bool) other).value ? 1 : 0));
        } else if (other instanceof org.python.types.Float) {
            return new org.python.types.Float((((org.python.types.Bool) this).value ? 1.0 : 0.0) * (((org.python.types.Float) other).value));
        } else if (other instanceof org.python.types.Complex) {
            org.python.types.Complex cmplx = new org.python.types.Complex(((org.python.types.Bool) this).value ? 1 : 0, 0);
            org.python.types.Complex other_cmplx = (org.python.types.Complex) other;
            return cmplx.__mul__(other_cmplx);
        } else if (other instanceof org.python.types.Str) {
            if (((org.python.types.Bool) this).value) {
                return new org.python.types.Str(((org.python.types.Str) other).value);
            } else {
                return new org.python.types.Str("");
            }
        } else if (other instanceof org.python.types.List) {
            return other.__mul__(this);
        } else if (other instanceof org.python.types.Tuple) {
            return other.__mul__(this);
        } else if (other instanceof org.python.types.ByteArray) {
            return other.__mul__(this);
        } else if (other instanceof org.python.types.Bytes) {
            return other.__mul__(this);
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for *: 'bool' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "Return self/value.",
            args = {"other"}
    )
    public org.python.Object __truediv__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            return new org.python.types.Int(this.value ? 1 : 0).__truediv__(other);
        } else if (other instanceof org.python.types.Bool) {
            org.python.types.Float other_value = new org.python.types.Float((((org.python.types.Bool) other).value ? 1.0 : 0.0));
            if (other_value.value == 0.0) {
                throw new org.python.exceptions.ZeroDivisionError("division by zero");
            } else {
                org.python.types.Float value = new org.python.types.Float((((org.python.types.Bool) this).value ? 1.0 : 0.0));
                return value.__truediv__(other);
            }
        } else if (other instanceof org.python.types.Float) {
            org.python.types.Float other_value = (org.python.types.Float) other;
            if (other_value.value == 0.0) {
                throw new org.python.exceptions.ZeroDivisionError("float division by zero");
            } else {
                org.python.types.Float value = new org.python.types.Float((((org.python.types.Bool) this).value ? 1.0 : 0.0));
                return value.__truediv__(other);
            }
        } else if (other instanceof org.python.types.Complex) {
            org.python.types.Complex cmplx = new org.python.types.Complex(((org.python.types.Bool) this).value ? 1 : 0, 0);
            org.python.types.Complex other_cmplx = (org.python.types.Complex) other;
            return cmplx.__truediv__(other_cmplx);
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for /: 'bool' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "Return self//value.",
            args = {"other"}
    )
    public org.python.Object __floordiv__(org.python.Object other) {
        try {
            return new org.python.types.Int(this.value ? 1 : 0).__floordiv__(other);
        } catch (org.python.exceptions.TypeError ae) {
            if (other instanceof org.python.types.Complex) {
                throw new org.python.exceptions.TypeError("can't take floor of complex number.");
            } else {
                throw new org.python.exceptions.TypeError("unsupported operand type(s) for //: '" + this.typeName() + "' and '" + other.typeName() + "'");
            }
        }
    }

    @org.python.Method(
            __doc__ = "Return self%value.",
            args = {"other"}
    )
    public org.python.Object __mod__(org.python.Object other) {
        if (other instanceof org.python.types.Bool) {
            boolean other_val = ((org.python.types.Bool) other).value;
            if (!other_val) {
                throw new org.python.exceptions.ZeroDivisionError("integer division or modulo by zero");
            }
            if (this.value) {
                return new org.python.types.Int(0);
            } else {
                if (org.Python.VERSION < 0x03060000) {
                    return new org.python.types.Bool(false);
                } else {
                    return new org.python.types.Int(0);
                }
            }
        } else if (other instanceof org.python.types.Int) {
            long other_val = ((org.python.types.Int) other).value;
            if (other_val == 0) {
                throw new org.python.exceptions.ZeroDivisionError("integer division or modulo by zero");
            }

            if (!this.value) {
                if (org.Python.VERSION < 0x03060000) {
                    return new org.python.types.Bool(false);
                } else {
                    return new org.python.types.Int(0);
                }
            } else if (other_val > 1) {
                if (org.Python.VERSION < 0x03060000) {
                    return new org.python.types.Bool(this.value);
                } else {
                    return new org.python.types.Int(1);
                }
            }
        } else if (other instanceof org.python.types.Complex) {
            throw new org.python.exceptions.TypeError("can't mod complex numbers.");
        }
        try {
            return new org.python.types.Int(this.value ? 1 : 0).__mod__(other);
        } catch (org.python.exceptions.TypeError ae) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for %: 'bool' and '" + other.typeName() + "'");
        }
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
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for divmod(): 'bool' and '" + other.typeName() + "'");
        }
    }

    @org.python.Method(
            __doc__ = "Return pow(self, value, mod).",
            args = {"other"},
            default_args = {"modulo"}
    )
    public org.python.Object __pow__(org.python.Object other, org.python.Object modulo) {
        try {
            return new org.python.types.Int(this.value ? 1 : 0).__pow__(other, modulo);
        } catch (org.python.exceptions.TypeError e) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for ** or pow(): 'bool' and '" + other.typeName() + "'");
        }
    }

    @org.python.Method(
            __doc__ = "Return self<<value.",
            args = {"other"}
    )
    public org.python.Object __lshift__(org.python.Object other) {
        if (other instanceof org.python.types.Bool) {
            return new org.python.types.Int((((org.python.types.Bool) this).value ? 1 : 0) << (((org.python.types.Bool) other).value ? 1 : 0));
        } else if (other instanceof org.python.types.Int) {
            long other_val = ((org.python.types.Int) other).value;
            if (other_val < 0) {
                throw new org.python.exceptions.ValueError("negative shift count");
            }
            return new org.python.types.Int((((org.python.types.Bool) this).value ? 1 : 0) << other_val);
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for <<: 'bool' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "Return self>>value.",
            args = {"other"}
    )
    public org.python.Object __rshift__(org.python.Object other) {
        if (other instanceof org.python.types.Bool) {
            return new org.python.types.Int((((org.python.types.Bool) this).value ? 1 : 0) >> (((org.python.types.Bool) other).value ? 1 : 0));
        } else if (other instanceof org.python.types.Int) {
            long other_val = ((org.python.types.Int) other).value;
            if (other_val < 0) {
                throw new org.python.exceptions.ValueError("negative shift count");
            }
            return new org.python.types.Int((((org.python.types.Bool) this).value ? 1 : 0) >> other_val);
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for >>: 'bool' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "Return self&value.",
            args = {"other"}
    )
    public org.python.Object __and__(org.python.Object other) {
        if (other instanceof org.python.types.Bool) {
            return new org.python.types.Bool(
                    (((org.python.types.Bool) this).value ? 1 : 0) &
                            (((org.python.types.Bool) other).value ? 1 : 0)
            );
        }

        if (other instanceof org.python.types.Int) {
            return new org.python.types.Int(
                    (((org.python.types.Bool) this).value ? 1 : 0) &
                            ((org.python.types.Int) other).value
            );
        }

        throw new org.python.exceptions.TypeError("unsupported operand type(s) for &: 'bool' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "Return self^value.",
            args = {"other"}
    )
    public org.python.Object __xor__(org.python.Object other) {
        if (other instanceof org.python.types.Bool) {
            return new org.python.types.Bool((((org.python.types.Bool) this).value ? 1 : 0) ^ (((org.python.types.Bool) other).value ? 1 : 0));
        } else if (other instanceof org.python.types.Int) {
            long operand1 = this.value ? 1L : 0L;
            long operand2 = ((org.python.types.Int) other).value;
            return new org.python.types.Int(operand1 ^ operand2);
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for ^: 'bool' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "Return self|value.",
            args = {"other"}
    )
    public org.python.Object __or__(org.python.Object other) {
        if (other instanceof org.python.types.Bool) {
            return new org.python.types.Bool((((org.python.types.Bool) this).value ? 1 : 0) | (((org.python.types.Bool) other).value ? 1 : 0));
        }
        if (other instanceof org.python.types.Int) {
            return new org.python.types.Int((((org.python.types.Bool) this).value ? 1 : 0) | ((org.python.types.Int) other).value);
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for |: 'bool' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "Return value+self.",
            args = {"other"}
    )
    public org.python.Object __radd__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("bool.__radd__() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "Return value-self.",
            args = {"other"}
    )
    public org.python.Object __rsub__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("bool.__rsub__() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "Return value*self.",
            args = {"other"}
    )
    public org.python.Object __rmul__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("bool.__rmul__() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "Return value/self.",
            args = {"other"}
    )
    public org.python.Object __rtruediv__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("bool.__rtruediv__() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "Return value//self.",
            args = {"other"}
    )
    public org.python.Object __rfloordiv__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("bool.__rfloordiv__() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "Return value%self.",
            args = {"other"}
    )
    public org.python.Object __rmod__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("bool.__rmod__() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "Return divmod(value, self).",
            args = {"other"}
    )
    public org.python.Object __rdivmod__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("bool.__rdivmod__() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "Return pow(value, self, mod).",
            args = {"other"}
    )
    public org.python.Object __rpow__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("bool.__rpow__() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "Return value<<self.",
            args = {"other"}
    )
    public org.python.Object __rlshift__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("bool.__rlshift__() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "Return value>>self.",
            args = {"other"}
    )
    public org.python.Object __rrshift__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("bool.__rrshift__() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "Return value&self.",
            args = {"other"}
    )
    public org.python.Object __rand__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("bool.__rand__() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "Return value^self.",
            args = {"other"}
    )
    public org.python.Object __rxor__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("bool.__rxor__() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "Return value|self.",
            args = {"other"}
    )
    public org.python.Object __ror__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("bool.__ror__() has not been implemented.");

    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __ilshift__(org.python.Object other) {
        int this_val = (((org.python.types.Bool) this).value ? 1 : 0);
        if (other instanceof org.python.types.Bool) {
            this_val <<= (((org.python.types.Bool) other).value ? 1 : 0);
            return new org.python.types.Int(this_val);
        } else if (other instanceof org.python.types.Int) {
            long other_val = ((org.python.types.Int) other).value;
            if (other_val < 0) {
                throw new org.python.exceptions.ValueError("negative shift count");
            }
            this_val <<= other_val;
            return new org.python.types.Int(this_val);
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for <<=: 'bool' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __irshift__(org.python.Object other) {
        int this_val = (((org.python.types.Bool) this).value ? 1 : 0);
        if (other instanceof org.python.types.Bool) {
            this_val >>= (((org.python.types.Bool) other).value ? 1 : 0);
            return new org.python.types.Int(this_val);
        } else if (other instanceof org.python.types.Int) {
            long other_val = ((org.python.types.Int) other).value;
            if (other_val < 0) {
                throw new org.python.exceptions.ValueError("negative shift count");
            }
            this_val >>= other_val;
            return new org.python.types.Int(this_val);
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for >>=: 'bool' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "-self"
    )
    public org.python.Object __neg__() {
        return new org.python.types.Int(this.value ? -1 : 0);
    }

    @org.python.Method(
            __doc__ = "+self"
    )
    public org.python.Object __pos__() {
        return new org.python.types.Int(this.value ? 1 : 0);
    }

    @org.python.Method(
            __doc__ = "abs(self)"
    )
    public org.python.Object __abs__() {
        return new org.python.types.Int(this.value ? 1 : 0);
    }

    @org.python.Method(
            __doc__ = "~self"
    )
    public org.python.Object __invert__() {
        return new org.python.types.Int(this.value ? -2 : -1);
    }

    @org.python.Method(
            __doc__ = "int(self)"
    )
    public org.python.types.Int __int__() {
        return new org.python.types.Int(this.value ? 1 : 0);
    }

    @org.python.Method(
            __doc__ = "float(self)"
    )
    public org.python.types.Float __float__() {
        return new org.python.types.Float(this.value ? 1 : 0);
    }

    @org.python.Method(
            __doc__ = "Rounding an Integral returns itself.\nRounding with an ndigits argument also returns an integer."
    )
    public org.python.Object __round__(org.python.Object ndigits) {
        if (ndigits instanceof org.python.types.Int) {
            return new org.python.types.Int(this.value ? 1 : 0);
        }
        throw new org.python.exceptions.TypeError("'" + ndigits.typeName() + "' object cannot be interpreted as an integer");
    }

    @org.python.Method(
            __doc__ = "Return self converted to an integer, if self is suitable for use as an index into a list."
    )
    public org.python.Object __index__() {
        return new org.python.types.Int(this.value ? 1 : 0);
    }
}
