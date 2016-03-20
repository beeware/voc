import os
from unittest import expectedFailure

from ..utils import TranspileTestCase


class TimeModuleTests(TranspileTestCase):

    #######################################################
    # _STRUCT_TM_ITEMS
    @expectedFailure
    def test__STRUCT_TM_ITEMS(self):
        self.assertCodeExecution("""
            import time
            print(time._STRUCT_TM_ITEMS)
            print('Done.')
            """)

    #######################################################
    # __doc__
    @expectedFailure
    def test___doc__(self):
        self.assertCodeExecution("""
            import time
            print(time.__doc__)
            print('Done.')
            """)

    #######################################################
    # __file__
    @expectedFailure
    def test___file__(self):
        self.assertCodeExecution("""
            import time
            print(time.__file__)
            print('Done.')
            """)

    #######################################################
    # __loader__
    @expectedFailure
    def test___loader__(self):
        self.assertCodeExecution("""
            import time
            print(time.__loader__)
            print('Done.')
            """)

    #######################################################
    # __name__
    @expectedFailure
    def test___name__(self):
        self.assertCodeExecution("""
            import time
            print(time.__name__)
            print('Done.')
            """)

    #######################################################
    # __package__
    @expectedFailure
    def test___package__(self):
        self.assertCodeExecution("""
            import time
            print(time.__package__)
            print('Done.')
            """)

    #######################################################
    # __spec__
    @expectedFailure
    def test___spec__(self):
        self.assertCodeExecution("""
            import time
            print(time.__spec__)
            print('Done.')
            """)

    #######################################################
    # altzone
    @expectedFailure
    def test_altzone(self):
        self.assertCodeExecution("""
            import time
            print(time.altzone)
            print('Done.')
            """)

    #######################################################
    # asctime
    @expectedFailure
    def test_asctime(self):
        self.assertCodeExecution("""
            import time
            print(time.asctime())
            print('Done.')
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
            print('Done.')
            """.format(sleepy_time=sleepy_time, diff_offset=diff_offset))

    #######################################################
    # ctime
    @expectedFailure
    def test_ctime(self):
        self.assertCodeExecution("""
            import time
            print(time.ctime())
            print('Done.')
            """)

    #######################################################
    # daylight
    @expectedFailure
    def test_daylight(self):
        self.assertCodeExecution("""
            import time
            print(time.daylight)
            print('Done.')
            """)

    #######################################################
    # get_clock_info
    @expectedFailure
    def test_get_clock_info(self):
        self.assertCodeExecution("""
            import time
            print(time.get_clock_info())
            print('Done.')
            """)

    #######################################################
    # gmtime
    @expectedFailure
    def test_gmtime(self):
        self.assertCodeExecution("""
            import time
            print(time.gmtime())
            print('Done.')
            """)

    #######################################################
    # localtime
    @expectedFailure
    def test_localtime(self):
        self.assertCodeExecution("""
            import time
            print(time.localtime())
            print('Done.')
            """)

    #######################################################
    # mktime
    @expectedFailure
    def test_mktime(self):
        self.assertCodeExecution("""
            import time
            print(time.mktime())
            print('Done.')
            """)

    #######################################################
    # monotonic
    @expectedFailure
    def test_monotonic(self):
        self.assertCodeExecution("""
            import time
            print(time.monotonic())
            print('Done.')
            """)

    #######################################################
    # perf_counter
    @expectedFailure
    def test_perf_counter(self):
        self.assertCodeExecution("""
            import time
            print(time.perf_counter())
            print('Done.')
            """)

    #######################################################
    # process_time
    @expectedFailure
    def test_process_time(self):
        self.assertCodeExecution("""
            import time
            print(time.process_time())
            print('Done.')
            """)

    #######################################################
    # sleep
    def test_sleep(self):
        self.assertCodeExecution("""
            import time
            print(time.sleep(1))
            print('Done.')
            """)

    #######################################################
    # strftime
    @expectedFailure
    def test_strftime(self):
        self.assertCodeExecution("""
            import time
            print(time.strftime())
            print('Done.')
            """)

    #######################################################
    # strptime
    @expectedFailure
    def test_strptime(self):
        self.assertCodeExecution("""
            import time
            print(time.strptime())
            print('Done.')
            """)

    #######################################################
    # struct_time
    @expectedFailure
    def test_struct_time(self):
        self.assertCodeExecution("""
            import time
            print(time.struct_time())
            print('Done.')
            """)

    #######################################################
    # time
    def test_time(self):
        self.assertCodeExecution("""
            import time
            print(int(time.time() / 10000))
            print('Done.')
            """)

    #######################################################
    # timezone
    @expectedFailure
    def test_timezone(self):
        self.assertCodeExecution("""
            import time
            print(time.timezone)
            print('Done.')
            """)

    #######################################################
    # tzname

    @expectedFailure
    def test_tzname(self):
        self.assertCodeExecution("""
            import time
            print(time.tzname)
            print('Done.')
            """)

    #######################################################
    # tzset
    @expectedFailure
    def test_tzset(self):
        self.assertCodeExecution("""
            import time
            print(time.tzset())
            print('Done.')
            """)
