from ..utils import TranspileTestCase


class MathTests(TranspileTestCase):
    def test_acos(self):
        self.assertCodeExecution("""
            import math
            try:
                x = math.acos(23)
            except ValueError as err:
                print(err)

            x = math.acos(0.5)
            print(x)

            try:
                x = math.acos("ss")
            except TypeError as err:
                print(err)

            x = math.acos(-0.24)
            print(x)
            """)

    def test_acosh(self):
        self.assertCodeExecution("""
            import math
            try:
                x = math.acosh(-23)
            except ValueError as err:
                print(err)

            x = math.acosh(12)
            print(x)

            try:
                x = math.acosh("ss")
            except TypeError as err:
                print(err)
            """)

    def test_asin(self):
        self.assertCodeExecution("""
            import math
            try:
                x = math.asin(23)
            except ValueError as err:
                print(err)

            x = math.asin(0.3434)
            print(x)

            try:
                x = math.asin("ss")
            except TypeError as err:
                print(err)

            x = math.asin(-0.24)
            print(x)
            """)

    def test_asinh(self):
        self.assertCodeExecution("""
            import math
            try:
                x = math.asinh(-23)
            except ValueError as err:
                print(err)

            x = math.asinh(12)
            print(x)

            try:
                x = math.asinh("ss")
            except TypeError as err:
                print(err)
            """)

    def test_atan(self):
        self.assertCodeExecution("""
            import math
            try:
                x = math.atan("ss")
            except TypeError as err:
                print(err)

            x = math.atan(-0.4524)
            print(x)
            """)

    def test_atan2(self):
        self.assertCodeExecution("""
            import math
            try:
                x = math.atan2("ss","sd")
            except TypeError as err:
                print(err)

            x = math.atan2(10,3545)
            print(x)
            """)

    def test_atanh(self):
        self.assertCodeExecution("""
            import math
            try:
                x = math.atan("ss")
            except TypeError as err:
                print(err)

            x = math.atan(-0.4524)
            print(x)

            try:
                x = math.atanh(-23)
            except ValueError as err:
                print(err)
            """)

    def test_ceil(self):
        self.assertCodeExecution("""
            import math
            try:
                x = math.ceil("ss")
            except TypeError as err:
                print(err)

            x = math.ceil(-0.4524)
            print(x)
            """)
        self.assertCodeExecution("""
            import math
            class a:
                def __ceil__(self):
                    return "ceil"

            b = a()
            x = math.ceil(b)
            print(x)

            class c:
                pass

            d = c()
            try:
                x = math.ceil(d)
            except TypeError as err:
                print(err)

            """)

    def test_copysign(self):
        self.assertCodeExecution("""
            import math
            try:
                x = math.copysign("ss",34)
            except TypeError as err:
                print(err)

            try:
                x = math.copysign(34,"ss")
            except TypeError as err:
                print(err)

            try:
                x = math.copysign("d","ss")
            except TypeError as err:
                print(err)

            x = math.copysign(2,-0.4524)
            print(x)
            """)

    def test_cos(self):
        self.assertCodeExecution("""
            import math
            x = math.cos(23345)
            print(x)

            try:
                x = math.cos("ddf")
            except TypeError as err:
                print(err)
            """)

    def test_cosh(self):
        self.assertCodeExecution("""
            import math
            try:
                x = math.cosh(23345)
            except OverflowError as err:
                print(err)

            try:
                x = math.cosh("ddf")
            except TypeError as err:
                print(err)

            x = math.cosh(25)
            print(x)
            """)

    def test_degrees(self):
        self.assertCodeExecution("""
            import math
            x = math.degrees(23345)
            print(x)

            x = math.degrees(223.2)
            print(x)

            try:
                x = math.degrees("ddf")
            except TypeError as err:
                print(err)
            """)

    def test_e(self):
        self.assertCodeExecution("""
            import math
            x = math.e
            print(x)
            """)

    def test_erf(self):
        self.assertCodeExecution("""
            import math
            x = math.erf(23345)
            print(x)

            x = math.erf(-223.2)
            print(x)

            try:
                x = math.erfc("ddf")
            except TypeError as err:
                print(err)
            """)

    def test_erfc(self):
        self.assertCodeExecution("""
            import math
            x = math.erfc(23345)
            print(x)

            x = math.erfc(-223.2)
            print(x)

            try:
                x = math.erfc("ddf")
            except TypeError as err:
                print(err)
            """)

    def test_exp(self):
        self.assertCodeExecution("""
            import math
            try:
                x = math.exp(23345)
            except OverflowError as err:
                print(err)

            x = math.exp(-223.2)
            print(x)

            try:
                x = math.exp("ddf")
            except TypeError as err:
                print(err)
            """)

    def test_expm1(self):
        self.assertCodeExecution("""
            import math
            try:
                x = math.expm1(23345)
            except OverflowError as err:
                print(err)

            x = math.expm1(-223.2)
            print(x)

            x = math.expm1(223.2)
            print(x)

            try:
                x = math.expm1("ddf")
            except TypeError as err:
                print(err)
            """)

    def test_fabs(self):
        self.assertCodeExecution("""
            import math
            x = math.fabs(-2434.113)
            print(x)

            try:
                x = math.fabs("ddf")
            except TypeError as err:
                print(err)
            """)

    def test_factorial(self):
        self.assertCodeExecution("""
            import math
            try:
                x = math.factorial(-2434.113)
            except ValueError as err:
                print(err)

            try:
                x = math.factorial("ddf")
            except TypeError as err:
                print(err)

            try:
                x = math.factorial(24334.113)
            except ValueError as err:
                print(err)

            # x = math.factorial(45)
            # print(x)

            # x = math.factorial(435)
            # print(x)
            """)

    def test_fmod(self):
        self.assertCodeExecution("""
            import math
            x = math.fmod(-2434.113,244)
            print(x)

            try:
                x = math.fmod("ddf",34)
            except TypeError as err:
                print(err)
            """)

    def test_floor(self):
        self.assertCodeExecution("""
            import math
            x = math.floor(-2434.113)
            print(x)

            try:
                x = math.floor("33f")
            except TypeError as err:
                print(err)
            """)

        self.assertCodeExecution("""
            import math
            class a:
                def __floor__(self):
                    return "floor"

            b = a()
            x = math.floor(b)
            print(x)

            class c:
                pass

            d = c()
            try:
                x = math.floor(d)
            except TypeError as err:
                print(err)
            """)

    def test_frexp(self):
        self.assertCodeExecution("""
            import math
            x = math.frexp(-2434.113)
            print(x)

            x = math.frexp(24423.113)
            print(x)

            try:
                x = math.frexp("33f")
            except TypeError as err:
                print(err)
            """)

    def test_fsum(self):
        self.assertCodeExecution("""
            import math
            x = math.fsum([-2434.113,24,25,5,2.35,224])
            print(x)

            x = math.fsum([.1,.1,.1,.1,.1,.1,.1,.1,.1,.1])
            print(x)

            try:
                x = math.fsum("33f")
            except TypeError as err:
                print(err)

            try:
                x = math.fsum(3)
            except TypeError as err:
                print(err)
            """)

    def test_gamma(self):
        self.assertCodeExecution("""
            import math
            x = math.gamma(24)
            print(x)

            try:
                x = math.gamma(-2)
            except ValueError as err:
                print(err)

            try:
                x = math.gamma("33f")
            except TypeError as err:
                print(err)
            """)

    def test_gcd(self):
        self.assertCodeExecution("""
            import math
            try:
                x = math.gcd(24,34)
            except AttributeError as err:
                print(err)
            else:
                print(x)

            try:
                x = math.gcd(2.3,13)
            except TypeError as err:
                print(err)
            except AttributeError as err:
                print(err)

            try:
                x = math.gcd("33f",34)
            except TypeError as err:
                print(err)
            except AttributeError as err:
                print(err)
            """)

    def test_hypot(self):
        self.assertCodeExecution("""
            import math
            x = math.hypot(223432,3545.45)
            print(x)

            x = math.hypot(-0.233,23)
            print(x)

            try:
                x = math.hypot("33f",34)
            except TypeError as err:
                print(err)
            """)

    # def test_inf(self):
    #     self.assertCodeExecution("""
    #         import math
    #         x = math.inf
    #         print(x)
    #         """)

    def test_isfinite(self):
        self.assertCodeExecution("""
            import math
            x = math.isfinite(343545)
            print(x)

            try:
                x = math.isfinite("33f")
            except TypeError as err:
                print(err)

            x = math.isfinite(float('inf'))
            print(x)
            """)

    def test_isinf(self):
        self.assertCodeExecution("""
            import math
            x = math.isinf(343545)
            print(x)

            try:
                x = math.isinf("33f")
            except TypeError as err:
                print(err)

            x = math.isinf(float('inf'))
            print(x)
            """)

    def test_isnan(self):
        self.assertCodeExecution("""
            import math
            x = math.isnan(343545)
            print(x)

            try:
                x = math.isnan("33f")
            except TypeError as err:
                print(err)

            x = math.isnan(float('nan'))
            print(x)
            """)

    def test_ldexp(self):
        self.assertCodeExecution("""
            import math
            x = math.ldexp(34,32)
            print(x)

            try:
                x = math.ldexp("sf",23)
            except TypeError as err:
                print(err)

            try:
                x = math.ldexp("sf",23)
            except TypeError as err:
                print(err)
            """)

    def test_lgamma(self):
        self.assertCodeExecution("""
            import math
            x = math.lgamma(24)
            print(x)

            x = math.lgamma(-324.2)
            print(x)

            try:
                x = math.lgamma(-2)
            except ValueError as err:
                print(err)

            try:
                x = math.lgamma("33f")
            except TypeError as err:
                print(err)
            """)

    def test_log(self):
        self.assertCodeExecution("""
            import math
            x = math.log(23432)
            print(x)

            try:
                x = math.log(-23)
            except ValueError as err:
                print(err)

            try:
                x = math.log("sf")
            except TypeError as err:
                print(err)
            """)

    def test_log10(self):
        self.assertCodeExecution("""
            import math
            x = math.log10(23432)
            print(x)

            try:
                x = math.log10(-23)
            except ValueError as err:
                print(err)

            try:
                x = math.log10("sf")
            except TypeError as err:
                print(err)
            """)

    def test_log1p(self):
        self.assertCodeExecution("""
            import math
            x = math.log1p(23432)
            print(x)

            try:
                x = math.log1p(-23)
            except ValueError as err:
                print(err)

            try:
                x = math.log1p("sf")
            except TypeError as err:
                print(err)
            """)

    def test_log2(self):
        self.assertCodeExecution("""
            import math
            x = math.log2(2343)
            print(x)
            """)

        self.assertCodeExecution("""
            import math
            try:
                x = math.log2(-23)
            except ValueError as err:
                print(err)

            try:
                x = math.log2("sf")
            except TypeError as err:
                print(err)
            """)

    def test_modf(self):
        self.assertCodeExecution("""
            import math
            x = math.modf(353.324)
            print(x)
            """)

        self.assertCodeExecution("""
            import math
            x = math.modf(-2.35224)
            print(x)
            """)

        self.assertCodeExecution("""
            import math
            try:
                x = math.modf("sf")
            except TypeError as err:
                print(err)
            """)

    # def test_nan(self):
    #     self.assertCodeExecution("""
    #         import math
    #         x = math.nan
    #         print(x)
    #         """)

    def test_pi(self):
        self.assertCodeExecution("""
            import math
            x = math.pi
            print(x)
            """)

    def test_pow(self):
        self.assertCodeExecution("""
            import math
            x = math.pow(234,34)
            print(x)

            x = math.pow(-234,-34)
            print(x)

            try:
                x = math.pow(-23,-12.3)
            except ValueError as err:
                print(err)

            try:
                x = math.pow("sf",23)
            except TypeError as err:
                print(err)
            """)

    def test_radians(self):
        self.assertCodeExecution("""
            import math
            x = math.radians(353.3)
            print(x)

            x = math.radians(-0.35224)
            print(x)

            try:
                x = math.radians("sf")
            except TypeError as err:
                print(err)
            """)

    def test_sin(self):
        self.assertCodeExecution("""
            import math
            x = math.sin(23345)
            print(x)

            try:
                x = math.sin("ddf")
            except TypeError as err:
                print(err)
            """)

    def test_sinh(self):
        self.assertCodeExecution("""
            import math
            try:
                x = math.sinh(23345)
            except OverflowError as err:
                print(err)

            try:
                x = math.sinh("ddf")
            except TypeError as err:
                print(err)

            x = math.sinh(25)
            print(x)
            """)

    def test_sqrt(self):
        self.assertCodeExecution("""
            import math
            x = math.sqrt(23345)
            print(x)

            try:
                x = math.sqrt("ddf")
            except TypeError as err:
                print(err)

            x = math.sqrt(435.455)
            print(x)
            """)

    def test_tan(self):
        self.assertCodeExecution("""
            import math
            x = math.tan(23345)
            print(x)

            try:
                x = math.tan("ddf")
            except TypeError as err:
                print(err)
            """)

    def test_tanh(self):
        self.assertCodeExecution("""
            import math
            x = math.tanh(2)
            print(x)

            x = math.tanh(-3.34)
            print(x)

            try:
                x = math.tanh("ddf")
            except TypeError as err:
                print(err)

            x = math.tanh(25)
            print(x)
            """)
