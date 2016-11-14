package python.time;


public class __init__ extends org.python.types.Module {
    public __init__() {
        super();
        vm_start_time = python.platform.__init__.impl.clock();
    }


    private static long vm_start_time;

    public static org.python.types.Str _STRUCT_TM_ITEMS;
    public static org.python.types.Str __doc__;
    public static org.python.types.Str __file__;
    public static org.python.types.Str __loader__;
    public static org.python.types.Str __name__;
    public static org.python.types.Str __package__;
    public static org.python.types.Str __spec__;

    public static org.python.types.Int altzone;

    @org.python.Method(
        __doc__ = ""
    )
    public static org.python.Object asctime() {
        throw new org.python.exceptions.NotImplementedError("time.asctime() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = "clock() -> floating point number\n" +
            "\n" +
            "Return the CPU time or real time since the start of the process or since\n" +
            "the first call to clock().  This has as much precision as the system\n" +
            "records.\n"
    )
    public static org.python.Object clock() {
        long current_time = python.platform.__init__.impl.clock() - vm_start_time;

        // thread time is in nanoseconds; convert to seconds.
        return new org.python.types.Float(current_time / 1000000000.0);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public static org.python.Object ctime() {
        throw new org.python.exceptions.NotImplementedError("time.ctime() has not been implemented.");
    }

    public static org.python.types.Int daylight;

    @org.python.Method(
        __doc__ = ""
    )
    public static org.python.Object get_clock_info() {
        throw new org.python.exceptions.NotImplementedError("time.get_clock_info() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public static org.python.Object gmtime() {
        throw new org.python.exceptions.NotImplementedError("time.gmtime() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public static org.python.Object localtime() {
        throw new org.python.exceptions.NotImplementedError("time.localtime() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public static org.python.Object mktime() {
        throw new org.python.exceptions.NotImplementedError("time.mktime() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public static org.python.Object monotonic() {
        throw new org.python.exceptions.NotImplementedError("time.monotonic() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public static org.python.Object perf_counter() {
        throw new org.python.exceptions.NotImplementedError("time.perf_counter() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public static org.python.Object process_time() {
        throw new org.python.exceptions.NotImplementedError("time.process_time() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = "sleep(seconds)\n" +
            "\n" +
            "Delay execution for a given number of seconds.  The argument may be\n" +
            "a floating point number for subsecond precision.\n",
        args = {"seconds"}
    )
    public static org.python.Object sleep(org.python.Object seconds) {
        try {
            java.lang.Thread.sleep((int) (org.Python.float_cast(seconds).value * 1000.0));
        } catch(ClassCastException e) {
            throw new org.python.exceptions.TypeError("a float is required");
        } catch(InterruptedException ex) {
            Thread.currentThread().interrupt();
        }
        return org.python.types.NoneType.NONE;
    }

    @org.python.Method(
        __doc__ = ""
    )
    public static org.python.Object strftime() {
        throw new org.python.exceptions.NotImplementedError("time.strftime() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public static org.python.Object strptime() {
        throw new org.python.exceptions.NotImplementedError("time.strptime() has not been implemented.");
    }

    // public static org.python.Object struct_time;

    @org.python.Method(
        __doc__ = "time() -> floating point number\n" +
            "\n" +
            "Return the current time in seconds since the Epoch.\n" +
            "Fractions of a second may be present if the system clock provides them.\n"
    )
    public static org.python.types.Float time() {
        return new org.python.types.Float(System.currentTimeMillis() / 1000.0);
    }

    public static org.python.types.Int timezone;

    public static org.python.types.Tuple tzname;

    @org.python.Method(
        __doc__ = ""
    )
    public static org.python.Object tzset() {
        throw new org.python.exceptions.NotImplementedError("time.tzset() has not been implemented.");
    }
}
