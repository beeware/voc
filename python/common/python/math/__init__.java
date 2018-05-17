package python.math;

import java.math.BigInteger;
import java.math.BigDecimal;
import python.errorfunction.math_erf;
import python.gammafunction.math_gamma;

@org.python.Module(
        __doc__ = ""
)
public class __init__ extends org.python.types.Module {
    public __init__() {
        super();
    }

    @org.python.Attribute
    public static org.python.Object pi = new org.python.types.Float(Math.PI);

    @org.python.Attribute
    public static org.python.Object e = new org.python.types.Float(Math.E);

    // @org.python.Attribute
    // public static org.python.Object inf = new org.python.types.Float(Double.POSITIVE_INFINITY);

    // @org.python.Attribute
    // public static org.python.Object nan = new org.python.types.Float(Double.NaN);

    private static double toFloatValue(org.python.Object v) {
        if (v instanceof org.python.types.Float) {
            return ((org.python.types.Float) v).value;
        } else if (v instanceof org.python.types.Int) {
            return (new org.python.types.Float(((org.python.types.Int) v).value)).value;
        } else {
            if (org.Python.VERSION < 0x03060000) {
                throw new org.python.exceptions.TypeError("a float is required");
            } else {
                throw new org.python.exceptions.TypeError("must be real number, not " + v.typeName());
            }
        }
    }



    private static boolean exceptNaN(double result, double arg) {
        return (Double.isNaN(result) && !Double.isNaN(arg));
    }

    private static boolean exceptInf(double result, double arg) {
        return (Double.isInfinite(result) && !Double.isInfinite(arg));
    }

    private static boolean isIntegral(double v) {
        return Math.ceil(v) - v == 0;
    }


    @org.python.Method(
            __doc__ = "",
            args = {"v"}
    )
    public static org.python.Object erf(org.python.Object v) {
        double result = math_erf.erf(toFloatValue(v));
        return new org.python.types.Float(result);
    }

    @org.python.Method(
            __doc__ = "",
            args = {"v"}
    )
    public static org.python.Object erfc(org.python.Object v) {
        double result = math_erf.erfc(toFloatValue(v));
        return new org.python.types.Float(result);
    }

    @org.python.Method(
            __doc__ = "",
            args = {"v"}
    )
    public static org.python.Object gamma(org.python.Object v) {
        double result = math_gamma.gamma(toFloatValue(v));
        return new org.python.types.Float(result);
    }

    @org.python.Method(
            __doc__ = "",
            args = {"v"}
    )
    public static org.python.Object lgamma(org.python.Object v) {
        double result = math_gamma.lgamma(toFloatValue(v));
        return new org.python.types.Float(result);
    }

    @org.python.Method(
            __doc__ = "",
            args = {"v"}
    )
    public static org.python.Object expm1(org.python.Object v) {

        double result = 0.0;
        result = Math.expm1(toFloatValue(v));
        if (Double.isInfinite(result)) {
            throw new org.python.exceptions.OverflowError("math range error");
        } else {
            return new org.python.types.Float(result);
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"v"}
    )
    public static org.python.Object acos(org.python.Object v) {
        org.python.types.Float r = new org.python.types.Float(Math.acos(toFloatValue(v)));
        if (Double.isNaN(r.value)) {
            throw new org.python.exceptions.ValueError("math domain error");
        } else {
            return r;
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"arg"}
    )
    public static org.python.Object cos(org.python.Object arg) {
        double v = toFloatValue(arg);
        if (exceptNaN(Math.cos(v), v)) {
            throw new org.python.exceptions.ValueError("math domain error");
        } else {
            return new org.python.types.Float(Math.cos(v));
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"v"}
    )
    public static org.python.Object acosh(org.python.Object v) {
        double y = toFloatValue(v);
        if (y < 1.0) {
            throw new org.python.exceptions.ValueError("math domain error");
        } else {
            if (y < 2.) {
                final double u = y - 1.;
                double s = Math.sqrt(u * (2. + u));
                return new org.python.types.Float(Math.log1p(u + s));
            } else if (y < 0x1p27) {
                final double u = 1. / y;
                double t = Math.sqrt((1. + u) * (1. - u));
                return new org.python.types.Float(Math.log(y * (1. + t)));
            } else {
                return new org.python.types.Float(Math.log(y) + Math.log1p(2));
            }
        }
    }


    @org.python.Method(
            __doc__ = "",
            args = {"v"}
    )
    public static org.python.Object asin(org.python.Object v) {
        org.python.types.Float r = new org.python.types.Float(Math.asin(toFloatValue(v)));
        if (Double.isNaN(r.value)) {
            throw new org.python.exceptions.ValueError("math domain error");
        } else {
            return r;
        }
    }


    @org.python.Method(
            __doc__ = "",
            args = {"arg"}
    )
    public static org.python.Object asinh(org.python.Object arg) {
        double v = toFloatValue(arg);
        if (isnan(v) || isinf(v)) {
            return arg;
        }

        final double ln2 = 6.93147180559945286227e-01;
        final double large = 1 << 28;
        final double small = 1.0 / (1 << 28);
        boolean sign = false;

        if (v < 0) {
            v = -v;
            sign = true;
        }

        double temp;
        if (v > large) {
            temp = log(v) + ln2;
        } else if (v > 2) {
            temp = log(2 * v + 1 / (Math.sqrt(v * v + 1) + v));
        } else if (v < small) {
            temp = v;
        } else {
            temp = Math.log1p(v + v * v / (1 + Math.sqrt(1 + v * v)));
        }

        return new org.python.types.Float(sign ? -temp : temp);
    }


    @org.python.Method(
            __doc__ = "",
            args = {"arg"}
    )
    public static org.python.Object sin(org.python.Object arg) {
        double v = toFloatValue(arg);
        if (exceptNaN(Math.sin(v), v)) {
            throw new org.python.exceptions.ValueError("math domain error");
        } else {
            return new org.python.types.Float(Math.sin(v));
        }
    }


    @org.python.Method(
            __doc__ = "",
            args = {"v"}
    )
    public static org.python.Object atan(org.python.Object v) {

        org.python.types.Float r = new org.python.types.Float(Math.atan(toFloatValue(v)));
        if (Double.isNaN(r.value)) {
            throw new org.python.exceptions.ValueError("math domain error");
        } else {
            return r;
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"v", "w"}
    )
    public static org.python.Object atan2(org.python.Object v, org.python.Object w) {
        return new org.python.types.Float(Math.atan(toFloatValue(v) / toFloatValue(w)));
    }


    @org.python.Method(
            __doc__ = "",
            args = {"v"}
    )
    public static org.python.Object atanh(org.python.Object v) {
        double absy = Math.abs(toFloatValue(v));
        if (absy >= 1.0) {
            throw new org.python.exceptions.ValueError("math domain error");
        } else {
            double u = (absy + absy) / (1. - absy);
            double x = 0.5 * Math.log1p(u);
            return new org.python.types.Float(Math.copySign(x, toFloatValue(v)));
        }
    }


    @org.python.Method(
            __doc__ = "",
            args = {"arg"}
    )
    public static org.python.Object tan(org.python.Object arg) {
        double v = toFloatValue(arg);
        if (exceptNaN(Math.tan(v), v)) {
            throw new org.python.exceptions.ValueError("math domain error");
        } else {
            return new org.python.types.Float(Math.tan(v));
        }
    }


    @org.python.Method(
            __doc__ = "",
            args = {"v"}
    )
    public static org.python.Object fsum(org.python.Object v) {
        if (v instanceof org.python.types.Str) {
            toFloatValue(v);
        }
        if (!(v instanceof org.python.types.Tuple) && !(v instanceof org.python.types.List)) {
            throw new org.python.exceptions.TypeError("'" + v.typeName() + "' object is not iterable");
        } else {
            java.util.List l;
            if (v instanceof org.python.types.Tuple) {
                l = new java.util.ArrayList<org.python.Object>(((org.python.types.Tuple) v).value);
            } else {
                l = new java.util.ArrayList<org.python.Object>(((org.python.types.List) v).value);
            }
            BigDecimal sum = new BigDecimal(0);
            for (int i = 0; i < l.size(); i++) {
                BigDecimal t = new BigDecimal(toFloatValue(((org.python.Object) l.get(i))));
                sum = sum.add(t);
            }
            return new org.python.types.Float(sum.doubleValue());
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"v"}
    )
    public static org.python.Object ceil(org.python.Object v) {
        if (v instanceof org.python.types.Int || v instanceof org.python.types.Float) {
            return new org.python.types.Int((int) Math.ceil(toFloatValue(v)));
        } else {
            try {
                org.python.Object[] args = new org.python.Object[1];
                java.util.Map<java.lang.String, org.python.Object> kwargs = new java.util.HashMap<java.lang.String, org.python.Object>();
                org.python.Object oper = v.__getattribute__("__ceil__");
                return (org.python.Object) ((org.python.types.Method) oper).invoke(args, kwargs);
            } catch (org.python.exceptions.AttributeError e) {
                if (org.Python.VERSION < 0x03060000) {
                    throw new org.python.exceptions.TypeError("a float is required");
                } else {
                    throw new org.python.exceptions.TypeError("must be real number, not " + v.typeName());
                }
            }
        }
    }


    @org.python.Method(
            __doc__ = "",
            args = {"arg"}
    )
    public static org.python.Object cosh(org.python.Object arg) {
        double v = toFloatValue(arg);
        if (exceptInf(Math.cosh(v), v)) {
            throw new org.python.exceptions.OverflowError("math range error");
        }
        return new org.python.types.Float(Math.cosh(v));
    }

    @org.python.Method(
            __doc__ = "",
            args = {"arg"}
    )
    public static org.python.Object sinh(org.python.Object arg) {
        double v = toFloatValue(arg);
        if (exceptInf(Math.sinh(v), v)) {
            throw new org.python.exceptions.OverflowError("math range error");
        }
        return new org.python.types.Float(Math.sinh(v));
    }

    @org.python.Method(
            __doc__ = "",
            args = {"arg"}
    )
    public static org.python.Object tanh(org.python.Object arg) {
        double v = toFloatValue(arg);
        if (exceptInf(Math.tanh(v), v)) {
            throw new org.python.exceptions.OverflowError("math range error");
        }
        return new org.python.types.Float(Math.tanh(v));
    }


    @org.python.Method(
            __doc__ = "",
            args = {"arg"}
    )
    public static org.python.Object sqrt(org.python.Object arg) {
        double v = toFloatValue(arg);
        if (exceptNaN(Math.sqrt(v), v)) {
            throw new org.python.exceptions.ValueError("math domain error");
        } else {
            return new org.python.types.Float(Math.sqrt(v));
        }
    }


    @org.python.Method(
            __doc__ = "",
            args = {"arg1", "arg2"}
    )
    public static org.python.Object gcd(org.python.Object arg1, org.python.Object arg2) {
        if (org.Python.VERSION < 0x03050000) {
            throw new org.python.exceptions.AttributeError("'module' object has no attribute 'gcd'");
        } else {
            if (!(arg1 instanceof org.python.types.Int)) {
                throw new org.python.exceptions.TypeError("'" + arg1.typeName() + "' object cannot be interpreted as an integer");
            } else if (!(arg2 instanceof org.python.types.Int)) {
                throw new org.python.exceptions.TypeError("'" + arg2.typeName() + "' object cannot be interpreted as an integer");
            } else {
                long m = Math.abs(((org.python.types.Int) arg1).value);
                long n = Math.abs(((org.python.types.Int) arg2).value);
                long h = 1;
                long p = m * n;
                for (long i = 2; i < p; i++) {
                    if ((m % i == 0) && (n % i == 0)) {
                        h = i;
                    }
                }
                return new org.python.types.Int(h);
            }
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"v"}
    )
    public static org.python.Object fabs(org.python.Object v) {
        return new org.python.types.Float(Math.abs(toFloatValue(v)));
    }

    @org.python.Method(
            __doc__ = "",
            args = {"a1", "a2"}
    )
    public static org.python.Object fmod(org.python.Object a1, org.python.Object a2) {
        double v = toFloatValue(a1);
        double w = toFloatValue(a2);
        if (isnan(v) || isnan(w)) {
            return new org.python.types.Float(Double.NaN);
        }
        if (isinf(w)) {
            return a1;
        }
        if (w == 0.0) {
            throw new org.python.exceptions.ValueError("math domain error");
        }
        if (isinf(v) && w == 0.0) {
            throw new org.python.exceptions.ValueError("math domain error");
        }
        return new org.python.types.Float(v % w);
    }



    @org.python.Method(
            __doc__ = "",
            args = {"v"}
    )
    public static org.python.Object exp(org.python.Object v) {
        double r = Math.exp(toFloatValue(v));
        if (exceptInf(r, toFloatValue(v))) {
            throw new org.python.exceptions.OverflowError("math range error");
        } else {
            return new org.python.types.Float(r);
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"v"}
    )
    public static org.python.Object floor(org.python.Object v) {
        if (v instanceof org.python.types.Int || v instanceof org.python.types.Float) {
            return new org.python.types.Int((int) Math.floor(toFloatValue(v)));
        } else {
            try {
                org.python.Object[] args = new org.python.Object[1];
                java.util.Map<java.lang.String, org.python.Object> kwargs = new java.util.HashMap<java.lang.String, org.python.Object>();
                org.python.Object oper = v.__getattribute__("__floor__");
                return (org.python.Object) ((org.python.types.Method) oper).invoke(args, kwargs);
            } catch (org.python.exceptions.AttributeError e) {
                if (org.Python.VERSION < 0x03060000) {
                    throw new org.python.exceptions.TypeError("a float is required");
                } else {
                    throw new org.python.exceptions.TypeError("must be real number, not " + v.typeName());
                }
            }
        }
    }


    @org.python.Method(
            __doc__ = "",
            args = {"v"},
            default_args = {"base"}
    )
    public static org.python.Object log(org.python.Object v, org.python.Object base) {
        double b = 0.0;
        if (base instanceof org.python.types.Float || base instanceof org.python.types.Int) {
            b = toFloatValue(base);
        } else if (base == null) {
            b = 0.0;
        }
        double doubleValue;
        doubleValue = log(toFloatValue(v));
        return (b == 0.0) ? new org.python.types.Float(doubleValue) : new org.python.types.Float(applyLoggedBase(doubleValue, b));
    }

    private static double log(double v) {
        if (v <= 0.) {
            throw new org.python.exceptions.ValueError("math domain error");
        } else {
            return Math.log(v);
        }
    }


    private static double applyLoggedBase(double loggedValue, double base) {

        double loggedBase;
        loggedBase = log(base);
        return loggedValue / loggedBase;
    }

    @org.python.Method(
            __doc__ = "",
            args = {"v"}
    )
    public static org.python.Object log10(org.python.Object v) {
        if (toFloatValue(v) <= 0.) {
            throw new org.python.exceptions.ValueError("math domain error");
        } else {
            return new org.python.types.Float(Math.log10(toFloatValue(v)));
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"v"}
    )
    public static org.python.Object log2(org.python.Object v) {
        if (toFloatValue(v) <= 0.) {
            throw new org.python.exceptions.ValueError("math domain error");
        } else {
            return log(v, new org.python.types.Float(2));
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"v"}
    )
    public static org.python.Object log1p(org.python.Object v) {
        if (toFloatValue(v) <= -1.) {
            throw new org.python.exceptions.ValueError("math domain error");
        } else {
            return new org.python.types.Float(Math.log1p(toFloatValue(v)));
        }
    }



    @org.python.Method(
            __doc__ = "",
            args = {"v", "w"}
    )
    public static org.python.Object copysign(org.python.Object v, org.python.Object w) {
        return new org.python.types.Float(Math.copySign(toFloatValue(v), toFloatValue(w)));
    }



    public static boolean isnan(double v) {
        return Double.isNaN(v);
    }

    public static boolean isinf(double v) {
        return Double.isInfinite(v);
    }

    private static boolean isninf(double v) {
        return v == Double.NEGATIVE_INFINITY;
    }

    @org.python.Method(
            __doc__ = "",
            args = {"v"}
    )
    public static org.python.Object modf(org.python.Object v) {
        double r = toFloatValue(v);
        if (isnan(r)) {
            java.util.List temp = new java.util.ArrayList<org.python.Object>();
            temp.add(new org.python.types.Float(r));
            temp.add(new org.python.types.Float(r));
            return new org.python.types.Tuple(temp);
        }
        if (isinf(r)) {
            double first = 0.0;
            if (isninf(r)) {
                first = -0.0;
            }
            java.util.List temp = new java.util.ArrayList<org.python.Object>();
            temp.add(new org.python.types.Float(first));
            temp.add(new org.python.types.Float(r));
            return new org.python.types.Tuple(temp);
        }
        double w = r % (1.0);
        r -= w;
        java.util.List temp = new java.util.ArrayList<org.python.Object>();
        temp.add(new org.python.types.Float(w));
        if (r == -0d) {
            temp.add(new org.python.types.Float(-r));
        } else {
            temp.add(new org.python.types.Float(r));
        }
        return new org.python.types.Tuple(temp);
    }

    @org.python.Method(
            __doc__ = "",
            args = {"v"}
    )
    public static org.python.Object frexp(org.python.Object v) {
        int exponent;
        double mantissa;
        double x = toFloatValue(v);
        exponent = Math.getExponent(x);
        switch (exponent) {

            default:
                exponent = exponent + 1;
                mantissa = Math.scalb(x, -exponent);
                break;

            case 1024:
                mantissa = x;
                exponent = 0;
                break;

            case -1023:
                if (x == 0.) {
                    mantissa = x;
                    exponent = 0;
                } else {
                    exponent = Math.getExponent(x * 0x1p52) - 51;
                    mantissa = Math.scalb(x, -exponent);
                }
                break;
        }
        java.util.List temp = new java.util.ArrayList<org.python.Object>();
        temp.add(new org.python.types.Float(mantissa));
        temp.add(new org.python.types.Int((int) exponent));
        return new org.python.types.Tuple(temp);
    }

    @org.python.Method(
            __doc__ = "",
            args = {"v", "wObj"}
    )
    public static org.python.Object ldexp(org.python.Object v, org.python.Object wObj) {
        double r = toFloatValue(v);
        double w = 0.0;
        if (!(wObj instanceof org.python.types.Int)) {
            throw new org.python.exceptions.TypeError("Expected an int as second argument to ldexp.");
        } else {
            w = toFloatValue(wObj);
        }
        if (w < Integer.MIN_VALUE) {
            w = Integer.MIN_VALUE;
        } else if (w > Integer.MAX_VALUE) {
            w = Integer.MAX_VALUE;
        }
        double result = Math.scalb(r, (int) w);
        if (exceptInf(result, r)) {
            throw new org.python.exceptions.OverflowError("math range error");
        } else {
            return new org.python.types.Float(result);
        }

    }

    @org.python.Method(
            __doc__ = "",
            args = {"v", "w"}
    )
    public static org.python.Object hypot(org.python.Object v, org.python.Object w) {
        double x = toFloatValue(v);
        double y = toFloatValue(w);
        double mag = Math.hypot(x, y);
        if (Double.isInfinite(mag) && !(Double.isInfinite(x) || Double.isInfinite(y))) {
            throw new org.python.exceptions.OverflowError("math range error");
        }
        return new org.python.types.Float(mag);
    }

    @org.python.Method(
            __doc__ = "",
            args = {"v"}
    )
    public static org.python.Object radians(org.python.Object v) {
        return new org.python.types.Float(Math.toRadians(toFloatValue(v)));
    }

    @org.python.Method(
            __doc__ = "",
            args = {"v"}
    )
    public static org.python.Object degrees(org.python.Object v) {
        return new org.python.types.Float(Math.toDegrees(toFloatValue(v)));
    }



    @org.python.Method(
            __doc__ = "",
            args = {"arg"}
    )
    public static org.python.Object factorial(org.python.Object arg) {
        double v = 0.0;
        if (arg instanceof org.python.types.Float) {
            v = ((org.python.types.Float) arg).value;
        } else if (arg instanceof org.python.types.Int) {
            v = (new org.python.types.Float(((org.python.types.Int) arg).value)).value;
        } else {
            throw new org.python.exceptions.TypeError("an integer is required (got type " + arg.typeName() + ")");
        }
        if ((v - ((int) v)) != 0.0) {
            throw new org.python.exceptions.ValueError("factorial() only accepts integral values");
        } else if (v <= 0.0) {
            throw new org.python.exceptions.ValueError("factorial() not defined for negative values");
        } else if (v == 0.0 || v == 1.0) {
            return new org.python.types.Float(1);
        } else if (v < 0.0 || isnan(v) || isinf(v)) {
            throw new org.python.exceptions.ValueError("math domain error");
        } else if (!isIntegral(v)) {
            throw new org.python.exceptions.ValueError("math domain error");
        } else {
            long value = (long) v;
            BigInteger bi = new BigInteger(Long.toString(value));
            for (long l = value - 1; l > 1; l--) {         // this implementation doesn't work for large numbers
                bi = bi.multiply(new BigInteger(Long.toString(l)));  // this needs work
            }
            return new org.python.types.Int(bi.intValue());
        }
    }

    /*@org.python.Method(
            __doc__ = "",
            args = {"arg"}
    )
    public static org.python.Object trunc(org.python.Object arg) {
        return arg.__trunc__();
    }*/





    @org.python.Method(
            __doc__ = "",
            args = {"v"}
    )
    public static org.python.Object isnan(org.python.Object v) {
        return new org.python.types.Bool(Double.isNaN(toFloatValue(v)));
    }

    @org.python.Method(
            __doc__ = "",
            args = {"v"}
    )
    public static org.python.Object isinf(org.python.Object v) {
        return new org.python.types.Bool(Double.isInfinite(toFloatValue(v)));
    }

    @org.python.Method(
            __doc__ = "",
            args = {"v"}
    )
    public static org.python.Object isfinite(org.python.Object v) {
        return new org.python.types.Bool(!(Double.isInfinite(toFloatValue(v))));
    }


    @org.python.Method(
            __doc__ = "",
            args = {"a1", "a2"}
    )
    public static org.python.Object pow(org.python.Object a1, org.python.Object a2) {
        double v = toFloatValue(a1);
        double w = toFloatValue(a2);
        if (w == 0.0) {
            return new org.python.types.Float(1);
        }
        if (v == 1.0) {
            return a1;
        }
        if (isnan(v) || isnan(w)) {
            return new org.python.types.Float(Double.NaN);
        }
        if (v == 0.0) {
            if (w == 0.0) {
                return new org.python.types.Float(1);
            } else if (w > 0.0 || w == Double.POSITIVE_INFINITY) {
                return new org.python.types.Float(0.0);
            } else {
                throw new org.python.exceptions.ValueError("math domain error");
            }
        }
        if (v == Double.NEGATIVE_INFINITY) {
            if (w == Double.NEGATIVE_INFINITY) {
                return new org.python.types.Float(0);
            }
            if (isinf(w)) {
                return new org.python.types.Float(Double.POSITIVE_INFINITY);
            }
            if (w == 0.0) {
                return new org.python.types.Float(1);
            }
            if (w > 0.0) {
                if (isOdd(w)) {
                    return new org.python.types.Float(Double.NEGATIVE_INFINITY);
                }
                return new org.python.types.Float(Double.POSITIVE_INFINITY);
            }
            if (isOdd(w)) {
                return new org.python.types.Float(-0.0);
            }
            return new org.python.types.Float(0.0);
        }
        if (w == Double.NEGATIVE_INFINITY) {
            if (v < 0.0) {
                if (v == -1.0) {
                    return new org.python.types.Float(1.0);
                }
                if (v < -1.0) {
                    return new org.python.types.Float(0.0);
                }
                return new org.python.types.Float(Double.POSITIVE_INFINITY);
            }
        }
        if (w == Double.POSITIVE_INFINITY) {
            if (v < 0.0) {
                if (v == -1.0) {
                    return new org.python.types.Float(1.0);
                }
                if (v < -1.0) {
                    return new org.python.types.Float(Double.POSITIVE_INFINITY);
                }
                return new org.python.types.Float(0.0);
            }
        }
        if (v < 0.0 && !isIntegral(w)) {
            throw new org.python.exceptions.ValueError("math domain error");
        }
        return new org.python.types.Float(Math.pow(v, w));
    }

    private static boolean isOdd(double v) {
        return isIntegral(v) && v % 2 != 0.0;
    }
}
