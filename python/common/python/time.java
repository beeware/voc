package python;


public class time extends org.python.types.Module {

    static {
        vm_start_time = python.platform.impl.clock();
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
    public static org.python.Object asctime(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("time.asctime() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public static org.python.Object clock(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("clock() takes no keyword arguments");
        }
        if (args.length == 0) {
            long current_time = python.platform.impl.clock() - vm_start_time;

            // thread time is in nanoseconds; convert to seconds.
            return new org.python.types.Float(current_time / 1000000000.0);
        } else {
            throw new org.python.exceptions.TypeError("clock() takes no arguments (" + args.length + " given)");
        }
    }

    @org.python.Method(
        __doc__ = ""
    )
    public static org.python.Object ctime(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("time.ctime() has not been implemented.");
    }

    public static org.python.types.Int daylight;

    @org.python.Method(
        __doc__ = ""
    )
    public static org.python.Object get_clock_info(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("time.get_clock_info() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public static org.python.Object gmtime(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("time.gmtime() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public static org.python.Object localtime(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("time.localtime() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public static org.python.Object mktime(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("time.mktime() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public static org.python.Object monotonic(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("time.monotonic() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public static org.python.Object perf_counter(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("time.perf_counter() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public static org.python.Object process_time(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("time.process_time() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public static org.python.Object sleep(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (kwargs.size() != 0) {
            throw new org.python.exceptions.TypeError("sleep() takes no keyword arguments");
        }
        if (args.length == 1) {
            try {
                java.lang.Thread.sleep((int) (org.Python.float_cast(args, kwargs).value * 1000.0));
            } catch(ClassCastException e) {
                throw new org.python.exceptions.TypeError("a float is required");
            } catch(InterruptedException ex) {
                Thread.currentThread().interrupt();
            }
        } else {
            throw new org.python.exceptions.TypeError("sleep() takes exactly 1 argument (" + args.length + " given)");
        }
        return org.python.types.NoneType.NONE;
    }

    @org.python.Method(
        __doc__ = ""
    )
    public static org.python.Object strftime(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("time.strftime() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public static org.python.Object strptime(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("time.strptime() has not been implemented.");
    }

    // public static org.python.Object struct_time;

    @org.python.Method(
        __doc__ = ""
    )
    public static org.python.types.Float time(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        return new org.python.types.Float(System.currentTimeMillis() / 1000.0);
    }

    public static org.python.types.Int timezone;

    public static org.python.types.Tuple tzname;

    @org.python.Method(
        __doc__ = ""
    )
    public static org.python.Object tzset(org.python.Object [] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("time.tzset() has not been implemented.");
    }
}
