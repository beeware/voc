import os
import sys
from unittest import expectedFailure

from ..utils import TranspileTestCase, NotImplementedToExpectedFailure


class TimeModuleTests(NotImplementedToExpectedFailure, TranspileTestCase):

    #######################################################
    # _STRUCT_TM_ITEMS
    @expectedFailure
    def test__STRUCT_TM_ITEMS(self):
        self.assertCodeExecution("""
            import time
            print(time._STRUCT_TM_ITEMS)
            """)

    #######################################################
    # __doc__
    def test___doc__(self):
        if sys.hexversion > 0x03060400:
            # Docstring was truncated in Python 3.6.4
            substitutions = {
                '': [
                    "\n" +
                    "Variables:\n" +
                    "\n" +
                    "timezone -- difference in seconds between UTC and local standard time\n" +
                    "altzone -- difference in  seconds between UTC and local DST time\n" +
                    "daylight -- whether local time should reflect DST\n" +
                    "tzname -- tuple of (standard time zone name, DST time zone name)\n" +
                    "\n" +
                    "Functions:\n" +
                    "\n" +
                    "time() -- return current time in seconds since the Epoch as a float\n" +
                    "clock() -- return CPU time since process start as a float\n" +
                    "sleep() -- delay for a number of seconds given as a float\n" +
                    "gmtime() -- convert seconds since Epoch to UTC tuple\n" +
                    "localtime() -- convert seconds since Epoch to local time tuple\n" +
                    "asctime() -- convert time tuple to string\n" +
                    "ctime() -- convert time in seconds to string\n" +
                    "mktime() -- convert local time tuple to seconds since Epoch\n" +
                    "strftime() -- convert time tuple to string according to format specification\n" +
                    "strptime() -- parse string to time tuple according to format specification\n" +
                    "tzset() -- change the local timezone"
                ]
            }
        else:
            substitutions = None

        self.assertCodeExecution(
            """
            import time
            print(time.__doc__)
            """,
            substitutions=substitutions
        )

    #######################################################
    # __file__
    @expectedFailure
    def test___file__(self):
        self.assertCodeExecution("""
            import time
            print(time.__file__)
            """)

    #######################################################
    # __loader__
    @expectedFailure
    def test___loader__(self):
        self.assertCodeExecution("""
            import time
            print(time.__loader__)
            """)

    #######################################################
    # __name__
    def test___name__(self):
        self.assertCodeExecution("""
            import time
            print(time.__name__)
            """)

    #######################################################
    # __package__
    def test___package__(self):
        self.assertCodeExecution("""
            import time
            print(time.__package__)
            """)

    #######################################################
    # __spec__
    @expectedFailure
    def test___spec__(self):
        self.assertCodeExecution("""
            import time
            print(time.__spec__)
            """)

    #######################################################
    # altzone
    @expectedFailure
    def test_altzone(self):
        self.assertCodeExecution("""
            import time
            print(time.altzone)
            """)

    #######################################################
    # asctime
    @expectedFailure
    def test_asctime(self):
        self.assertCodeExecution("""
            import time
            print(time.asctime())
            """)

    #######################################################
    # clock
    def test_clock(self):
        # Since we can't know exactly what CPU time will be used,
        # and CPU time will vary between implementations,
        # this test validates that clock returns a float < 0.01s
        sleepy_time = 1
        diff_offset = sleepy_time if os.name == 'nt' else 0
        # On Windows, time.clock includes the time spent in time.sleep
        # however on Unix it does not.
        self.assertCodeExecution("""
            import time
            start = time.clock()
            time.sleep({sleepy_time})
            end = time.clock()
            diff = end - start - {diff_offset}
            print(type(diff))
            print(diff < 0.1)
            """.format(sleepy_time=sleepy_time, diff_offset=diff_offset))

    #######################################################
    # ctime
    def test_ctime(self):
        self.assertCodeExecution("""
            import time
            print(time.ctime()[:10], time.ctime()[-4:])
            """)

    def test_ctime_with_parameter(self):
        self.assertCodeExecution("""
            import time
            print(time.ctime(0))
            print(time.ctime(1000))
            now = time.time()
            print(time.ctime((now - (now % 3600))))
            print(time.ctime(1000.67))
            try:
                time.ctime('today')
            except Exception as e:
                print(e)
            try:
                time.ctime([1,2])
            except Exception as e:
                print(e)
            try:
                time.ctime((1,2))
            except Exception as e:
                print(e)
            time.ctime(None)
        """)

    #######################################################
    # daylight
    @expectedFailure
    def test_daylight(self):
        self.assertCodeExecution("""
            import time
            print(time.daylight)
            """)

    #######################################################
    # get_clock_info
    def test_get_clock_info_monotonic(self):
        self.assertCodeExecution("""
            import time

            mono_info = time.get_clock_info('monotonic')
            print(mono_info.adjustable)
            # monotonic clock is implemented using System.nanoTime() in Java
            # print(mono_info.implementation)
            print(mono_info.monotonic)
            # java implementation has much higher resolution due to
            # JVM's high-resolution time source
            # print(mono_info.resolution)

            try:
                time.get_clock_info(123)
            except TypeError as e:
                print(e)
            """)

    @expectedFailure
    def test_get_clock_info(self):
        self.assertCodeExecution("""
            import time

            print(time.get_clock_info('clock'))
            print(time.get_clock_info('perf_counter'))
            print(time.get_clock_info('process_time'))
            print(time.get_clock_info('time'))
            """)

    #######################################################
    # gmtime
    @expectedFailure
    def test_gmtime(self):
        self.assertCodeExecution("""
            import time
            print(time.gmtime())
            """)

    #######################################################
    # localtime
    @expectedFailure
    def test_localtime(self):
        self.assertCodeExecution("""
            import time
            print(time.localtime())
            """)

    #######################################################
    # mktime
    @expectedFailure
    def test_mktime(self):
        self.assertCodeExecution("""
            import time
            print(time.mktime())
            """)

    #######################################################
    # monotonic
    def test_monotonic(self):
        # test to make sure that time elapsed between two consecutive
        # monotonic clockticks is within the range of
        # [monotonic resolution - ε, monotonic resolution + ε], where ε = 0.001
        self.assertCodeExecution("""
            import time

            now = time.monotonic()
            prev = now
            while now == prev:
                now = time.monotonic()

            diff = now-prev
            delta = abs(diff- time.get_clock_info('monotonic').resolution)
            print(delta < 0.001)
            """)

    #######################################################
    # perf_counter
    @expectedFailure
    def test_perf_counter(self):
        self.assertCodeExecution("""
            import time
            print(time.perf_counter())
            """)

    #######################################################
    # process_time
    @expectedFailure
    def test_process_time(self):
        self.assertCodeExecution("""
            import time
            print(time.process_time())
            """)

    #######################################################
    # sleep
    def test_sleep(self):
        self.assertCodeExecution("""
            import time
            print(time.sleep(1))
            """)

    #######################################################
    # strftime
    @expectedFailure
    def test_strftime(self):
        self.assertCodeExecution("""
            import time
            print(time.strftime())
            """)

    #######################################################
    # strptime
    @expectedFailure
    def test_strptime(self):
        self.assertCodeExecution("""
            import time
            print(time.strptime())
            """)

    #######################################################
    # struct_time
    @expectedFailure
    def test_struct_time(self):
        self.assertCodeExecution("""
            import time
            print(time.struct_time())
            """)

    #######################################################
    # time
    def test_time(self):
        self.assertCodeExecution("""
            import time
            print(int(time.time() / 10000))
            """)

    #######################################################
    # timezone
    @expectedFailure
    def test_timezone(self):
        self.assertCodeExecution("""
            import time
            print(time.timezone)
            """)

    #######################################################
    # tzname

    @expectedFailure
    def test_tzname(self):
        self.assertCodeExecution("""
            import time
            print(time.tzname)
            """)

    #######################################################
    # tzset
    @expectedFailure
    def test_tzset(self):
        self.assertCodeExecution("""
            import time
            print(time.tzset())
            """)

    not_implemented_versions = {
        'test_clock': (3.7, )
    }
