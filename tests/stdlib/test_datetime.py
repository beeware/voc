from unittest import expectedFailure

from ..utils import TranspileTestCase


class DatetimeModuleTests(TranspileTestCase):

 #######################################################

    # @expectedFailure
    def test_datetime_simple(self):
        self.assertCodeExecution("""
            import datetime
            d = datetime.datetime(2018, 10, 10)
            """)

    # @expectedFailure
    def test_datetime_simple2(self):
        self.assertCodeExecution("""
            import datetime
            d = datetime.datetime(1990,5,10)
            """)

    # @expectedFailure
    def test_datetime_simple3(self):
        self.assertCodeExecution("""
            import datetime
            d = datetime.datetime(1995,3,10)
            """)

    # @expectedFailure
    def test_datetime_simple_kwargs(self):
        self.assertCodeExecution("""
            import datetime
            d = datetime.datetime(year=2018, month=10, day=10)
            """)

    # @expectedFailure
    def test_datetime_simple_kwargs2(self):
        self.assertCodeExecution("""
            import datetime
            d = datetime.datetime(year=1990, month=5, day=10)
            """)

    # @expectedFailure
    def test_datetime_simple_kwargs3(self):
        self.assertCodeExecution("""
            import datetime
            d = datetime.datetime(year=1995, month=3, day=10)
            """)

    # @expectedFailure
    def test_datetime_simple_kwargs4(self):
        self.assertCodeExecution("""
            import datetime
            d = datetime.datetime(year = 1995, month = 1, day = 1, hour = 1)
            """)

    # @expectedFailure
    def test_datetime_simple_kwargs5(self):
        self.assertCodeExecution("""
            import datetime
            d = datetime.datetime(year = 1995, month = 1, day = 1, hour = 1, minute = 1)
            """)

    # @expectedFailure
    def test_datetime_simple_kwargs6(self):
        self.assertCodeExecution("""
            import datetime
            d = datetime.datetime(year = 1995, month = 1, day = 1, hour = 1, minute = 1, second = 1)
            """)


    # @expectedFailure
    def test_datetime_simple_kwargs7(self):
        self.assertCodeExecution("""
            import datetime
            d = datetime.datetime(year = 1995, month = 1, day = 1, hour = 1, minute = 1, second = 1, microsecond = 1)
            """)


    @expectedFailure
    def test_datetime_few_arg(self):
        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime(1,1))
            """)

    @expectedFailure
    def test_datetime_few_arg2(self):
        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime(1))
            """)

    @expectedFailure
    def test_datetime_many_arg(self):
        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime(2000,1,1,1,1,1,1,1,1))
            """)

    @expectedFailure
    def test_datetime_many_arg2(self):
        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime(1990,11,11,1,1,1,1,1,1))
            """)

    @expectedFailure
    def test_datetime_wrong_yeartype(self):
        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime("2018",1,1))
            """)

    @expectedFailure
    def test_datetime_year_too_low(self):
        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime(-1,1,1))
            """)

    @expectedFailure
    def test_datetime_year_too_high(self):
        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime(122018,1,1))
            """)

    @expectedFailure
    def test_datetime_wrong_monthtype(self):
        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime(2018,"1",1))
            """)

    @expectedFailure
    def test_datetime_month_too_low(self):
        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime(1990,-1,1))
            """)

    @expectedFailure
    def test_datetime_month_too_high(self):
        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime(1990,31,1))
            """)

    @expectedFailure
    def test_datetime_wrong_daytype(self):
        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime(2018,1,"1"))
            """)

    @expectedFailure
    def test_datetime_day_too_low(self):
        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime(1990,1,-1))
            """)

    @expectedFailure
    def test_datetime_day_too_high(self):
        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime(1990,31,41))
            """)

    @expectedFailure
    def test_datetime_hour_too_low(self):
        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime(1990,1,1,-1))
            """)

    @expectedFailure
    def test_datetime_hour_too_high(self):
        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime(1990,1,1,25))
            """)

    @expectedFailure
    def test_datetime_wrong_mintype(self):
        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime(2018,1,1,1,"1"))
            """)

    @expectedFailure
    def test_datetime_min_too_low(self):
        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime(1990,1,1,1,-1))
            """)

    @expectedFailure
    def test_datetime_min_too_high(self):
        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime(1990,1,1,1,61))
            """)


    @expectedFailure
    def test_datetime_wrong_sectype(self):
        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime(2018,1,1,1,1,"1"))
            """)

    @expectedFailure
    def test_datetime_sec_too_low(self):
        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime(1990,1,1,1,1,-1))
            """)

    @expectedFailure
    def test_datetime_sec_too_high(self):
        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime(1990,1,1,1,1,61))
            """)

    @expectedFailure
    def test_datetime_wrong_mstype(self):
        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime(2018,1,1,1,1,1,"1"))
            """)

    @expectedFailure
    def test_datetime_ms_too_low(self):
        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime(2018,1,1,1,1,1,-11))
            """)

    @expectedFailure
    def test_datetime_ms_too_high(self):
        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime(2018,1,1,1,1,1,1000000))
            """)

    # @expectedFailure
    # One test with 240.000 different inputs using args
    def test_datetime_all_conc_args(self):
        self.assertCodeExecution("""            
            import datetime
            for year in range(1, 10000, 1000):
                for month in range(1, 12, 3):
                    for day in range(1, 28, 6):
                        for hour in range(0, 23, 4):
                            for min in range(0, 59, 18):
                                for sec in range(0, 59, 12):
                                    for ms in range(0, 1000000, 100000):
                                        d = datetime.datetime(year,month,day,hour,min,sec,ms)
            """)


    # @expectedFailure
    # One test with 240.000 different inputs using kwargs
    def test_datetime_all_conc_kwargs(self):
        self.assertCodeExecution("""            
            import datetime
            for y in range(1, 10000, 1000):
                for m in range(1, 12, 3):
                    for d in range(1, 28, 6):
                        for h in range(0, 23, 4):
                            for min in range(0, 59, 18):
                                for sec in range(0, 59, 12):
                                    for ms in range(0, 1000000, 100000):
                                        date = datetime.datetime(year = y, month = m, day = d, hour = h, minute = min, second = sec, microsecond = ms)
            """)

    @expectedFailure
    def test_datetime_utcfromtimestamp(self):
        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime.utcfromtimestamp(0))
            """)

        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime.utcfromtimestamp(1234567890))
            """)

        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime.utcfromtimestamp(1234567890.123))
            """)

        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime.utcfromtimestamp(-1234567890))
            """)

        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime.utcfromtimestamp(-1234567890.123))
            """)

    @expectedFailure
    def test_datetime_utcfromtimestamp_errors(self):

        self.assertCodeExecution("""
            import datetime
            try 
                print(datetime.datetime.utcfromtimestamp(100000000000))
            except TypeError as e:
                print(e)
            """)

        self.assertCodeExecution("""
            import datetime
            try 
                print(datetime.datetime.utcfromtimestamp(-100000000000))
            except ValueError as e:
                print(e)
            """)

        self.assertCodeExecution("""
            import datetime
            try
                print(datetime.datetime.utcfromtimestamp('0'))
            except ValueError as e:
                print(e)
            """)

    # @expectedFailure
    def test_datetime_class_attributes(self):
        self.assertCodeExecution("""
            import datetime
            d = datetime.datetime.min
            """)

        self.assertCodeExecution("""
            import datetime
            d = datetime.datetime.max
            """)

    # @expectedFailure
    def test_datetime_instance_get_attributes(self):

        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime(2018, 1, 1).year)
        """)

        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime(2018, 1, 1).month)
        """)

        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime(2018, 1, 1).day)
        """)

        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime(2018, 1, 1, 1).hour)
        """)

        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime(2018, 1, 1, 1, 1).minute)
        """)

        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime(2018, 1, 1, 1, 1, 1).second)
        """)

        self.assertCodeExecution("""
            import datetime
            print(datetime.datetime(2018, 1, 1, 1, 1, 1, 1).microsecond)
        """)

    @expectedFailure
    def test_datetime_instance_set_attributes(self):

        self.assertCodeExecution("""
            import datetime
            y = datetime.datetime(2018, 1, 1)
            try:
                y.year = 2017
            except AttributeError as e:
                print(e)
        """)

        self.assertCodeExecution("""
            import datetime
            m = datetime.datetime(2018, 1, 1)
            try:
                m.month = 2
            except AttributeError as e:
                print (e)
        """)

        self.assertCodeExecution("""
            import datetime
            d = datetime.datetime(2018, 1, 1)
            try:
                d.day = 2
            except AttributeError as e:
                print(e)
        """)

        self.assertCodeExecution("""
            import datetime
            h = datetime.datetime(2018, 1, 1, 1)
            try:
                h.hour = 2
            except AttributeError as e
                print(e)
        """)

        self.assertCodeExecution("""
            import datetime
            m = datetime.datetime(2018, 1, 1, 1, 1)
            try:
                m.minute = 2
            except AttributeError as e
                print(e)
        """)

        self.assertCodeExecution("""
            import datetime
            s = datetime.datetime(2018, 1, 1, 1, 1, 1)
            try:
                s.second = 2
            except AttributeError as e
                print(e)
        """)

        self.assertCodeExecution("""
            import datetime
            m = datetime.datetime(2018, 1, 1, 1, 1, 1, 1)
            try:
                m.microsecond = 2
            except AttributeError as e
                print(e)
        """)

        self.assertCodeExecution("""
            import datetime
            t = datetime.datetime(2018, 1, 1)
            try:
                t.tzinfo = 1
            except AttributeError as e
                print(e)
        """)

    # @expectedFailure
    def test_datetime_instance_method_date(self):
        self.assertCodeExecution("""
            import datetime
            d = datetime.datetime(2018, 1, 1).date
        """)

    # @expectedFailure
    def test_datetime_instance_method_time(self):
        self.assertCodeExecution("""
            import datetime
            d = datetime.datetime(2018, 1, 1, 1, 1, 1, 1).time
        """)


class DateTests(TranspileTestCase):

    # @expectedFailure
    def test_Date(self):
        self.assertCodeExecution("""
            from datetime import date
            d = date(1,1,1)
            """)

    # @expectedFailure
    def test_date_isoformat_kwargs(self):
        self.assertCodeExecution("""
            from datetime import date
            d = date(year=2,month=1,day=1)
            print(d.isoformat())
            """)

    # @expectedFailure
    def test_date_isoformat_args(self):
        self.assertCodeExecution("""
            from datetime import date
            d = date(2,1,1)
            print(d.isoformat())
            """)

    @expectedFailure
    def test_date_replace_all(self):
        self.assertCodeExecution("""
            from datetime import date
            d = date(1,1,1)
            print(d.replace(2,2,2))
            """)

    @expectedFailure
    def test_date_replace_year(self):
        self.assertCodeExecution("""
            from datetime import date
            d = date(1,1,1)
            print(d.replace(year=2019))
            """)

    @expectedFailure
    def test_date_replace_month(self):
        self.assertCodeExecution("""
            from datetime import date
            d = date(1,1,1)
            print(d.replace(month=10))
            """)

    @expectedFailure
    def test_date_replace_day(self):
        self.assertCodeExecution("""
            from datetime import date
            d = date(1,1,1)
            print(d.replace(day=30))
            """)
            

class TimedeltaTests(TranspileTestCase):

    def test_creation(self):
        self.assertCodeExecution("""
            import datetime
            print(datetime.timedelta(seconds=20))
            print(datetime.timedelta(minutes=30))
            print(datetime.timedelta(hours=20))

            print(datetime.timedelta(days=20))
            print(datetime.timedelta(weeks=20))
            print(datetime.timedelta(microseconds=20))
            print(datetime.timedelta(milliseconds=20))
            
            #  Carrying over milliseconds to seconds
            print(datetime.timedelta(microseconds=1, minutes=1, seconds=1, milliseconds=11111, hours=1))
            #  TODO: Carrying over to days
            #  print(datetime.timedelta(microseconds=1, minutes=1, seconds=1, milliseconds=111111111111, hours=1))
            """)


class TimeTests(TranspileTestCase):

    def test___new__(self):
        self.assertCodeExecution("""
            from datetime import time
            t = time()
            """)

    # @expectedFailure
    def test_hour(self):
        self.assertCodeExecution("""
            from datetime import time
            t = time()
            print(t.hour)
            """)

    # @expectedFailure
    def test_minute(self):
        self.assertCodeExecution("""
            from datetime import time
            t = time()
            print(t.minute)
            """)

    # @expectedFailure
    def test_second(self):
        self.assertCodeExecution("""
            from datetime import time
            t = time()
            print(t.second)
            """)

    # @expectedFailure
    def test_microsecond(self):
        self.assertCodeExecution("""
            from datetime import time
            t = time()
            print(t.microsecond)
            """)

    # @expectedFailure
    def test_tzinfo(self):
        self.assertCodeExecution("""
            from datetime import time
            t = time()
            print(t.tzinfo)
            """)
