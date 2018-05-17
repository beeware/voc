package python.gammafunction;


public class math_gamma {
    static final double pi = 3.141592653589793238462643383279502884197;
    static final double sqrtpi = 1.772453850905516027298167483341145182798;
    static final int LANCZOS_N = 13;
    static final double lanczos_g = 6.024680040776729583740234375;
    static final double lanczos_g_minus_half = 5.524680040776729583740234375;
    static final double[] lanczos_num_coeffs = new double[] {
            23531376880.410759688572007674451636754734846804940,
            42919803642.649098768957899047001988850926355848959,
            35711959237.355668049440185451547166705960488635843,
            17921034426.037209699919755754458931112671403265390,
            6039542586.3520280050642916443072979210699388420708,
            1439720407.3117216736632230727949123939715485786772,
            248874557.86205415651146038641322942321632125127801,
            31426415.585400194380614231628318205362874684987640,
            2876370.6289353724412254090516208496135991145378768,
            186056.26539522349504029498971604569928220784236328,
            8071.6720023658162106380029022722506138218516325024,
            210.82427775157934587250973392071336271166969580291,
            2.5066282746310002701649081771338373386264310793408
            };
    static final double[] lanczos_den_coeffs = new double[] {
            0.0, 39916800.0, 120543840.0, 150917976.0, 105258076.0, 45995730.0,
            13339535.0, 2637558.0, 357423.0, 32670.0, 1925.0, 66.0, 1.0
            };
    static final int NGAMMA_INTEGRAL = 23;
    static final double[] gamma_integral = new double[] {
            1.0, 1.0, 2.0, 6.0, 24.0, 120.0, 720.0, 5040.0, 40320.0, 362880.0,
            3628800.0, 39916800.0, 479001600.0, 6227020800.0, 87178291200.0,
            1307674368000.0, 20922789888000.0, 355687428096000.0,
            6402373705728000.0, 121645100408832000.0, 2432902008176640000.0,
            51090942171709440000.0, 1124000727777607680000.0,
            };

    static double sinpi(double x) {
        double y;
        double r;
        int n;

        y = Math.abs(x) % 2.0;
        n = (int) Math.round(2.0 * y);

        assert ((0 <= n) && (n <= 4));

        switch (n) {
            case 0:
                r = Math.sin(pi * y);

                break;

            case 1:
                r = Math.cos(pi * (y - 0.5));

                break;

            case 2:
                r = Math.sin(pi * (1.0 - y));

                break;

            case 3:
                r = -Math.cos(pi * (y - 1.5));

                break;

            case 4:
                r = Math.sin(pi * (y - 2.0));

                break;

            default:
                assert (false);
                r = 3;
        }

        return Math.copySign(1.0, x) * r;
    }

    static double lanczos_sum(double x) {
        double num = 0.0;
        double den = 0.0;
        int i;

        assert (x > 0.0);

        if (x < 5.0) {
            for (i = LANCZOS_N; --i >= 0;) {
                num = (num * x) + lanczos_num_coeffs[i];
                den = (den * x) + lanczos_den_coeffs[i];
            }
        } else {
            for (i = 0; i < LANCZOS_N; i++) {
                num = (num / x) + lanczos_num_coeffs[i];
                den = (den / x) + lanczos_den_coeffs[i];
            }
        }

        return num / den;
    }

    public static double gamma(double x) {
        double absx;
        double r;
        double y;
        double z;
        double sqrtpow;

        if (Double.isNaN(x)) {
            return x;
        }

        if (Double.isInfinite(x)) {
            if (x > 0.0) {
                return x;
            }

            throw new org.python.exceptions.ValueError("math domain error");
        }

        if (x == 0.0) {
            throw new org.python.exceptions.ValueError("math domain error");
        }

        if (x == Math.floor(x)) {
            if (x < 0.0) {
                throw new org.python.exceptions.ValueError("math domain error");
            }

            if (x <= NGAMMA_INTEGRAL) {
                return gamma_integral[(int) x - 1];
            }
        }

        absx = Math.abs(x);

        if (absx < 1e-20) {
            r = 1.0 / x;

            if (Double.isInfinite(r)) {
                throw new org.python.exceptions.OverflowError("math range error");
            }

            return r;
        }

        if (absx > 200.0) {
            if (x < 0.0) {
                return 0.0 / sinpi(x);
            } else {
                throw new org.python.exceptions.OverflowError("math range error");
            }
        }

        y = absx + lanczos_g_minus_half;

        if (absx > lanczos_g_minus_half) {
            double q = y - absx;
            z = q - lanczos_g_minus_half;
        } else {
            double q = y - lanczos_g_minus_half;
            z = q - absx;
        }

        z = (z * lanczos_g) / y;

        if (x < 0.0) {
            r = (-pi / sinpi(absx) / absx * Math.exp(y)) / lanczos_sum(absx);
            r -= (z * r);

            if (absx < 140.0) {
                r /= Math.pow(y, absx - 0.5);
            } else {
                sqrtpow = Math.pow(y, (absx / 2.0) - 0.25);
                r /= sqrtpow;
                r /= sqrtpow;
            }
        } else {
            r = lanczos_sum(absx) / Math.exp(y);
            r += (z * r);

            if (absx < 140.0) {
                r *= Math.pow(y, absx - 0.5);
            } else {
                sqrtpow = Math.pow(y, (absx / 2.0) - 0.25);
                r *= sqrtpow;
                r *= sqrtpow;
            }
        }

        if (Double.isInfinite(r)) {
            throw new org.python.exceptions.OverflowError("math range error");
        }

        return r;
    }

    public static double lgamma(double x) {
        double r;
        double absx;

        if (Double.isNaN(x)) {
            return x;
        }

        if (Double.isInfinite(x)) {
            return Double.POSITIVE_INFINITY;
        }

        if ((x == Math.floor(x)) && (x <= 2.0)) {
            if (x <= 0.0) {
                throw new org.python.exceptions.ValueError("math domain error");
            } else {
                return 0.0;
            }
        }

        absx = Math.abs(x);

        if (absx < 1e-20) {
            return -Math.log(absx);
        }

        if (x > 0.0) {
            r = Math.log(lanczos_sum(x)) - lanczos_g +
                ((x - 0.5) * (Math.log((x + lanczos_g) - 0.5) - 1));
        } else {
            r = Math.log(pi) - Math.log(Math.abs(sinpi(absx))) -
                Math.log(absx) -
                (Math.log(lanczos_sum(absx)) - lanczos_g +
                ((absx - 0.5) * (Math.log((absx + lanczos_g) - 0.5) - 1)));
        }

        if (Double.isInfinite(r)) {
            throw new org.python.exceptions.OverflowError("math range error");
        }

        return r;
    }
}
