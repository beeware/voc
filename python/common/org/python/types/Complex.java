package org.python.types;

import java.util.Locale;

public class Complex extends org.python.types.Object {
    @org.python.Attribute
    public org.python.types.Float real;
    @org.python.Attribute
    public org.python.types.Float imag;

    /**
     * A utility method to update the internal value of this object.
     *
     * Used by __i*__ operations to do an in-place operation.
     * obj must be of type org.python.types.Complex
     */
    public java.lang.Object toJava() {
        return this;
    }

    public org.python.Object byValue() {
        throw new org.python.exceptions.AttributeError("type object 'complex' has no attribute 'byValue'");
    }

    public int hashCode() {
        return this.hashCode();
    }

    public Complex(org.python.types.Float real_val, org.python.types.Float imag_val) {
        this.real = real_val;
        this.imag = imag_val;
    }

    public Complex(double real, double imag) {
        this.real = new org.python.types.Float(real);
        this.imag = new org.python.types.Float(imag);
    }

    public Complex(double imag) {
        this.real = new org.python.types.Float(0);
        this.imag = new org.python.types.Float(imag);
    }

    @org.python.Method(
            __doc__ = "complex(real[, imag]) -> complex number" +
                    "\n" +
                    "Create a complex number from a real part and an optional imaginary part.\n" +
                    "This is equivalent to (real + imag*1j) where imag defaults to 0.\n",
            default_args = {"real", "imag"}
    )
    public Complex(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        this.real = new org.python.types.Float(0);
        this.imag = new org.python.types.Float(0);

        if (args[0] instanceof org.python.types.Str && args[1] != null) {
            throw new org.python.exceptions.TypeError("complex() can't take second arg if first is a string");
        }

        if (args[1] instanceof org.python.types.Str) {
            throw new org.python.exceptions.TypeError("complex() second arg can't be a string");
        }

        if (args[0] instanceof org.python.types.Complex) {
            org.python.types.Complex real_cmplx_obj = (org.python.types.Complex) args[0];
            this.real = (org.python.types.Float) this.real.__add__(real_cmplx_obj.real);
            this.imag = (org.python.types.Float) this.imag.__add__(real_cmplx_obj.imag);
        } else {
            try {
                if (args[0] == null) {
                    this.real = new org.python.types.Float(0);
                } else {
                    this.real = ((org.python.types.Float) args[0].__float__());
                }
            } catch (org.python.exceptions.AttributeError e) {
                if (org.Python.VERSION < 0x03050300) {
                    throw new org.python.exceptions.TypeError(
                            "complex() argument must be a string or a number, not '" + args[0].typeName() + "'"
                    );
                } else {
                    throw new org.python.exceptions.TypeError(
                            "complex() first argument must be a string or a number, not '" + args[0].typeName() + "'"
                    );
                }
            } catch (org.python.exceptions.ValueError e) {
                throw new org.python.exceptions.ValueError("complex() arg is a malformed string");
            }
        }

        if (args[1] instanceof org.python.types.Complex) {
            org.python.types.Complex imag_cmplx_obj = (org.python.types.Complex) args[1];
            this.real = (org.python.types.Float) this.real.__sub__(imag_cmplx_obj.imag);
            this.imag = (org.python.types.Float) this.imag.__add__(imag_cmplx_obj.real);
        } else {
            try {
                if (args[1] == null) {
                    this.imag = new org.python.types.Float(0);
                } else {
                    this.imag = ((org.python.types.Float) args[1].__float__());
                }
            } catch (org.python.exceptions.AttributeError e) {
                if (org.Python.VERSION < 0x03040300) {
                    throw new org.python.exceptions.TypeError(
                            "complex() argument must be a string or a number, not '" + args[1].typeName() + "'"
                    );
                } else {
                    throw new org.python.exceptions.TypeError(
                            "complex() argument must be a string, a bytes-like object or a number, not '" +
                                    args[1].typeName() + "'"
                    );
                }
            }
        }
    }

    private String partToStr(org.python.types.Float x) {
        String x_str;
        if (x.value != 0.0) {
            String format = "%.17g";
            x_str = String.format(Locale.US, format, x.value);
            int dot_pos = x_str.indexOf(".");
            int e_pos = x_str.indexOf("e");
            if (dot_pos != -1) {
                // Remove trailing zeroes in the fractional part
                int last_zero = -1;
                int i;
                for (i = dot_pos + 1; i < x_str.length(); i++) {
                    char c = x_str.charAt(i);
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
                        last_zero -= 1;
                    }
                    x_str = x_str.substring(0, last_zero) + x_str.substring(i);
                }
            }
        } else if (x.isNegativeZero()) {
            x_str = "-0";
        } else {
            x_str = "0";
        }
        return x_str;
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
    public org.python.Object __repr__() {
        java.lang.StringBuilder buffer = new java.lang.StringBuilder();
        boolean real_present = true;
        if (this.real.value != 0) {
            buffer.append("(");
            if (((org.python.types.Bool) ((this.real).__int__().__eq__(this.real))).value) {
                buffer.append(((org.python.types.Str) this.real.__int__().__repr__()).value);
            } else {
                buffer.append(((org.python.types.Str) this.real.__repr__()).value);
            }
        } else {
            real_present = false;
        }
        if (this.real.value != 0 && this.imag.value >= 0) {
            buffer.append("+");
        }
        if (((org.python.types.Bool) ((this.imag).__int__().__eq__(this.imag))).value) {
            buffer.append(((org.python.types.Str) (this.imag).__int__().__repr__()).value);
        } else {
            buffer.append(((org.python.types.Str) (this.imag).__repr__()).value);
        }
        buffer.append("j");
        if (real_present) {
            buffer.append(")");
        }
        return new org.python.types.Str(buffer.toString());
    }

    @org.python.Method(
            __doc__ = "complex.__format__() -> str\n\nConvert to a string according to format_spec."
    )
    public org.python.Object __format__(org.python.Object format_string) {
        throw new org.python.exceptions.NotImplementedError("complex.__format__ has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "Return self<value.",
            args = {"other"}
    )
    public org.python.Object __lt__(org.python.Object other) {
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "Return self<=value.",
            args = {"other"}
    )
    public org.python.Object __le__(org.python.Object other) {
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "Return self==value.",
            args = {"other"}
    )
    public org.python.Object __eq__(org.python.Object other) {
        if (other instanceof org.python.types.Complex) {
            org.python.types.Complex other_obj = (org.python.types.Complex) other;
            return new org.python.types.Bool(
                    ((org.python.types.Bool) this.real.__eq__(other_obj.real)).value
                    && ((org.python.types.Bool) this.imag.__eq__(other_obj.imag)).value);
        } else if (other instanceof org.python.types.Float || other instanceof org.python.types.Int
                || other instanceof org.python.types.Bool) {
            return new org.python.types.Bool(
                    ((org.python.types.Bool) this.real.__eq__(other)).value
                    && ((org.python.types.Bool) this.imag.__eq__(new org.python.types.Int(0))).value);
        }
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "Return self>value.",
            args = {"other"}
    )
    public org.python.Object __gt__(org.python.Object other) {
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "Return self>=value.",
            args = {"other"}
    )
    public org.python.Object __ge__(org.python.Object other) {
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "self != 0"
    )
    public org.python.types.Bool __bool__() {
        // A complex number is "truthy" if either its real component or imaginary component are > 0
        return new org.python.types.Bool((this.real.value != 0.0) || (this.imag.value != 0.0));
    }

    public boolean __setattr_null(java.lang.String name, org.python.Object value) {
        // Builtin types can't have attributes set on them.
        return false;
    }

    @org.python.Method(
            __doc__ = "__dir__() -> list\ndefault dir() implementation"
    )
    public org.python.types.List __dir__() {
        throw new org.python.exceptions.NotImplementedError("complex.__dir__() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "Return self+value.",
            args = {"other"}
    )

    public org.python.Object __add__(org.python.Object other) {
        if (other instanceof org.python.types.Int || other instanceof org.python.types.Float) {
            return new org.python.types.Complex((org.python.types.Float) this.real.__add__(other), this.imag);
        } else if (other instanceof Bool) {
            if (!((org.python.types.Bool) other).value && this.real.isNegativeZero()) {
                return new org.python.types.Complex(new org.python.types.Float(0), this.imag);
            }
            return new org.python.types.Complex((org.python.types.Float) this.real.__add__(other), this.imag);
        } else if (other instanceof Complex) {
            org.python.types.Complex other_object = (org.python.types.Complex) other;
            return new org.python.types.Complex((org.python.types.Float) this.real.__add__(other_object.real), (org.python.types.Float) this.imag.__add__(other_object.imag));
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for +: 'complex' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "Return self-value.",
            args = {"other"}
    )
    public org.python.Object __sub__(org.python.Object other) {
        if (other instanceof org.python.types.Int || other instanceof org.python.types.Float) {
            return new org.python.types.Complex((org.python.types.Float) this.real.__sub__(other), this.imag);
        } else if (other instanceof Bool) {
            return new org.python.types.Complex((org.python.types.Float) this.real.__sub__(other), this.imag);
        } else if (other instanceof Complex) {
            org.python.types.Complex other_object = (org.python.types.Complex) other;
            return new org.python.types.Complex((org.python.types.Float) this.real.__sub__(other_object.real), (org.python.types.Float) this.imag.__sub__(other_object.imag));
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for -: 'complex' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "Return str(self)."
    )
    public org.python.Object __str__() {
        if (this.real.value != 0.0 || this.real.isNegativeZero()) {
            return new org.python.types.Str("(" + partToStr(this.real) + ((this.imag.value >= 0.0 && !this.imag.isNegativeZero()) ? "+" : "-") + partToStr(new org.python.types.Float(Math.abs(this.imag.value))) + "j)");
        } else {
            return new org.python.types.Str(partToStr(this.imag) + "j");
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __getitem__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("'complex' object is not subscriptable");
    }

    @org.python.Method(
            __doc__ = "Return self*value.",
            args = {"other"}
    )
    public org.python.Object __mul__(org.python.Object other) {
        if (other instanceof org.python.types.List || other instanceof org.python.types.Str || other instanceof org.python.types.Tuple || other instanceof org.python.types.Bytes || other instanceof org.python.types.ByteArray) {
            throw new org.python.exceptions.TypeError("can't multiply sequence by non-int of type '" + this.typeName() + "'");
        } else if (other instanceof org.python.types.Bool) {
            if (!((org.python.types.Bool) other).value && !this.real.isNegativeZero()) {
                return new org.python.types.Complex(new org.python.types.Float(0), new org.python.types.Float(0));
            } else if (this.real.isNegativeZero()) {
                return new org.python.types.Complex(new org.python.types.Float(0), (org.python.types.Float) this.imag.__mul__(other));
            }
            return new org.python.types.Complex((org.python.types.Float) this.real.__mul__(other), (org.python.types.Float) this.imag.__mul__(other));
        } else if (other instanceof org.python.types.Float) {
            if (((org.python.types.Float) other).value == 0.0 && !this.real.isNegativeZero()) {
                return new org.python.types.Complex(new org.python.types.Float(0), new org.python.types.Float(0));
            } else if (this.real.isNegativeZero()) {
                return new org.python.types.Complex(new org.python.types.Float(0), (org.python.types.Float) this.imag.__mul__(other));
            }
            return new org.python.types.Complex((org.python.types.Float) this.real.__mul__(other), (org.python.types.Float) this.imag.__mul__(other));
        } else if (other instanceof org.python.types.Int) {
            if (((org.python.types.Int) other).value == 0 && !this.real.isNegativeZero()) {
                return new org.python.types.Complex(new org.python.types.Float(0), new org.python.types.Float(0));
            } else if (this.real.isNegativeZero()) {
                return new org.python.types.Complex(new org.python.types.Float(0), (org.python.types.Float) this.imag.__mul__(other));
            }
            return new org.python.types.Complex((org.python.types.Float) this.real.__mul__(other), (org.python.types.Float) this.imag.__mul__(other));
        } else if (other instanceof org.python.types.Complex) {
            org.python.types.Complex other_obj = (org.python.types.Complex) other;
            org.python.types.Float real = (org.python.types.Float) this.real.__mul__(other_obj.real).__sub__(this.imag.__mul__(other_obj.imag));
            org.python.types.Float imag = (org.python.types.Float) this.real.__mul__(other_obj.imag).__add__(this.imag.__mul__(other_obj.real));
            return new org.python.types.Complex(real, imag);
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for *: 'complex' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "Return self/value.",
            args = {"other"}
    )
    public org.python.Object __truediv__(org.python.Object other) {
        if (other instanceof org.python.types.Int) {
            if (((org.python.types.Int) other).value == 0) {
                throw new org.python.exceptions.ZeroDivisionError("complex division by zero");
            } else if (this.real.isNegativeZero()) {
                return new org.python.types.Complex(this.real, (org.python.types.Float) this.imag.__truediv__(other));
            }
            return new org.python.types.Complex((org.python.types.Float) this.real.__truediv__(other), (org.python.types.Float) this.imag.__truediv__(other));
        } else if (other instanceof org.python.types.Bool) {
            if (!((Bool) other).value) {
                throw new org.python.exceptions.ZeroDivisionError("complex division by zero");
            }
            return new org.python.types.Complex(this.real, this.imag);
        } else if (other instanceof org.python.types.Float) {
            if (((Float) other).value == 0.0) {
                throw new org.python.exceptions.ZeroDivisionError("complex division by zero");
            } else if (this.real.isNegativeZero()) {
                return new org.python.types.Complex(this.real, (org.python.types.Float) this.imag.__truediv__(other));
            }
            return new org.python.types.Complex((org.python.types.Float) this.real.__truediv__(other), (org.python.types.Float) this.imag.__truediv__(other));
        } else if (other instanceof org.python.types.Complex) {
            org.python.types.Complex other_obj = (org.python.types.Complex) other;
            org.python.types.Complex result = new org.python.types.Complex(0, 0);
            double abs_breal = Math.abs(other_obj.real.value);
            double abs_bimag = Math.abs(other_obj.imag.value);
            if (abs_breal >= abs_bimag) {
                if (abs_breal == 0.0) {
                    throw new org.python.exceptions.ZeroDivisionError("complex division by zero");
                } else {
                    double ratio = other_obj.imag.value / other_obj.real.value;
                    double denom = other_obj.real.value + other_obj.imag.value * ratio;
                    result.real.value = (this.real.value + this.imag.value * ratio) / denom;
                    result.imag.value = (this.imag.value - this.real.value * ratio) / denom;
                }
            } else if (abs_bimag >= abs_breal) {
                double ratio = other_obj.real.value / other_obj.imag.value;
                double denom = other_obj.real.value * ratio + other_obj.imag.value;
                assert (other_obj.imag.value != 0.0);
                result.real.value = (this.real.value * ratio + this.imag.value) / denom;
                result.imag.value = (this.imag.value * ratio - this.real.value) / denom;
            } else {
                result.real.value = Double.NaN;
                result.imag.value = Double.NaN;
            }
            return result;
        }
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for /: 'complex' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "Return self//value.",
            args = {"other"}
    )
    public org.python.Object __floordiv__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("can't take floor of complex number.");
    }

    @org.python.Method(
            __doc__ = "Return self%value.",
            args = {"other"}
    )
    public org.python.Object __mod__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("can't mod complex numbers.");
    }

    @org.python.Method(
            __doc__ = "Return divmod(self, value).",
            args = {"other"}
    )
    public org.python.Object __divmod__(org.python.Object other) {

        throw new org.python.exceptions.TypeError("can't take floor or mod of complex number.");
    }

    private org.python.Object calCPow(org.python.types.Complex b) {
        org.python.types.Complex r = new org.python.types.Complex(0, 0);
        double vabs, len, at, phase;
        if (b.real.value == 0.0 && b.imag.value == 0) {
            r.real.value = 1.0;
            r.imag.value = 0.0;
        } else if (this.real.value == 0.0 && this.imag.value == 0.0) {
            if (b.imag.value != 0. || b.real.value < 0.) {
                throw new org.python.exceptions.ZeroDivisionError("0.0 to a negative or complex power");
            }
            r.real.value = 1.0;
            r.imag.value = 0.0;
        } else {
            vabs = Math.hypot(this.real.value, this.imag.value);
            len = Math.pow(vabs, b.real.value);
            at = Math.atan2(this.imag.value, this.real.value);
            phase = at * b.real.value;
            if (b.imag.value != 0.0) {
                len /= Math.exp(at * b.imag.value);
                phase += b.imag.value * Math.log(vabs);
            }
            r.real.value = len * Math.cos(phase);
            r.imag.value = len * Math.sin(phase);
        }
        return r;
    }

    private org.python.Object calUPow(long n) {
        org.python.types.Complex r, p;
        long mask = 1;
        r = new org.python.types.Complex(1, 0);
        p = this;
        while (mask > 0 && n >= mask) {
            if ((n & mask) != 0) {
                r = (org.python.types.Complex) r.__mul__(p);
            }
            mask <<= 1;
            p = (Complex) p.__mul__(p);
        }
        return r;
    }

    @org.python.Method(
            __doc__ = "Return pow(self, value, mod).",
            args = {"other"},
            default_args = {"modulo"}
    )
    public org.python.Object __pow__(org.python.Object other, org.python.Object modulo) {
        if (modulo == null) {
            if (other instanceof org.python.types.Bool) {
                if (((org.python.types.Bool) other).value) {
                    return this.__mul__(other);
                }
                return calCPow(new org.python.types.Complex(0, 0));
            } else if (other instanceof org.python.types.Int) {
                org.python.types.Int other_obj = (org.python.types.Int) other;
                if (other_obj.value > 100 || other_obj.value < -100) {
                    return calCPow(new org.python.types.Complex(other_obj.value, 0));
                } else if (other_obj.value > 0) {
                    return calUPow(other_obj.value);
                } else {
                    org.python.types.Complex c1 = new org.python.types.Complex(1, 0);
                    return c1.__truediv__(calUPow(-other_obj.value));
                }
            } else if (other instanceof org.python.types.Float) {
                org.python.types.Float other_obj = (org.python.types.Float) other;
                return calCPow(new org.python.types.Complex(other_obj.value, 0));
            } else if (other instanceof org.python.types.Complex) {
                org.python.types.Complex other_obj = (org.python.types.Complex) other;
                return calCPow(other_obj);
            }
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for ** or pow(): 'complex' and '" + other.typeName() + "'");
        }
        throw new org.python.exceptions.ValueError("complex modulo");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __lshift__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for <<: 'complex' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __rshift__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for >>: 'complex' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __and__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for &: 'complex' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __xor__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for ^: 'complex' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __or__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("unsupported operand type(s) for |: 'complex' and '" + other.typeName() + "'");
    }

    @org.python.Method(
            __doc__ = "Return value+self.",
            args = {"other"}
    )
    public org.python.Object __radd__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("complex.__radd__() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "Return value-self.",
            args = {"other"}
    )
    public org.python.Object __rsub__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("complex.__rsub__() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "Return value*self.",
            args = {"other"}
    )
    public org.python.Object __rmul__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("complex.__rmul__() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "Return value/self.",
            args = {"other"}
    )
    public org.python.Object __rtruediv__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("complex.__rtruediv__() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "Return value//self.",
            args = {"other"}
    )
    public org.python.Object __rfloordiv__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("complex.__rfloordiv__() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "Return value%self.",
            args = {"other"}
    )
    public org.python.Object __rmod__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("complex.__rmod__() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "Return divmod(value, self).",
            args = {"other"}
    )
    public org.python.Object __rdivmod__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("complex.__rdivmod__() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "Return pow(value, self, mod).",
            args = {"other"}
    )
    public org.python.Object __rpow__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("complex.__rpow__() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __rlshift__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("complex.__rlshift__() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __rrshift__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("complex.__rrshift__() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __rand__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("complex.__rand__() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __rxor__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("complex.__rxor__() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __ror__(org.python.Object other) {
        throw new org.python.exceptions.NotImplementedError("complex.__ror__() has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "-self"
    )
    public org.python.Object __neg__() {
        return new org.python.types.Complex((org.python.types.Float) this.real.__neg__(), (org.python.types.Float) this.imag.__neg__());
    }

    @org.python.Method(
            __doc__ = "+self"
    )
    public org.python.Object __pos__() {
        return new org.python.types.Complex(this.real, this.imag);
    }

    @org.python.Method(
            __doc__ = "abs(self)"
    )
    public org.python.Object __abs__() {
        double real = this.real.value;
        double imag = this.imag.value;
        return new org.python.types.Float(java.lang.Math.sqrt(real * real + imag * imag));
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __invert__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary ~: 'complex'");
    }

    @org.python.Method(
            __doc__ = "int(self)"
    )
    public org.python.Object __int__() {
        throw new org.python.exceptions.TypeError("can't convert complex to int");
    }

    @org.python.Method(
            __doc__ = "float(self)"
    )
    public org.python.Object __float__() {
        throw new org.python.exceptions.NotImplementedError("complex.__float__ has not been implemented.");
    }

    @org.python.Method(
            __doc__ = "complex.conjugate() -> complex\n\nReturn the complex conjugate of its argument. (3-4j).conjugate() == 3+4j."
    )
    public org.python.Object conjugate() {
        return new org.python.types.Complex(this.real, (org.python.types.Float) this.imag.__neg__());
    }
}
