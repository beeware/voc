package python;

@org.python.Module(
        __doc__ =
                "This module provides various functions to manipulate time values.\n" +
                        "\n" +
                        "There are two standard representations of time.  One is the number\n" +
                        "of seconds since the Epoch, in UTC (a.k.a. GMT).  It may be an integer\n" +
                        "or a floating point number (to represent fractions of seconds).\n" +
                        "The Epoch is system-defined; on Unix, it is generally January 1st, 1970.\n" +
                        "The actual value can be retrieved by calling gmtime(0).\n" +
                        "\n" +
                        "The other representation is a tuple of 9 integers giving local time.\n" +
                        "The tuple items are:\n" +
                        "  year (including century, e.g. 1998)\n" +
                        "  month (1-12)\n" +
                        "  day (1-31)\n" +
                        "  hours (0-23)\n" +
                        "  minutes (0-59)\n" +
                        "  seconds (0-59)\n" +
                        "  weekday (0-6, Monday is 0)\n" +
                        "  Julian day (day in the year, 1-366)\n" +
                        "  DST (Daylight Savings Time) flag (-1, 0 or 1)\n" +
                        "If the DST flag is 0, the time is given in the regular time zone;\n" +
                        "if it is 1, the time is given in the DST time zone;\n" +
                        "if it is -1, mktime() should guess based on the date and time.\n" +
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
)
public class time extends org.python.types.Module {
    public time() {
        super();
        vm_start_time = python.platform.impl.clock();
    }

    private static long vm_start_time;
    public static org.python.Object _STRUCT_TM_ITEMS;

    @org.python.Attribute
    public static org.python.Object __file__ = new org.python.types.Str("python/common/python/time.java");
    @org.python.Attribute
    public static org.python.Object __loader__ = org.python.types.NoneType.NONE;  // TODO
    @org.python.Attribute
    public static org.python.Object __name__ = new org.python.types.Str("time");
    @org.python.Attribute
    public static org.python.Object __package__ = new org.python.types.Str("");
    @org.python.Attribute
    public static org.python.Object __spec__ = org.python.types.NoneType.NONE;  // TODO
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
        long current_time = python.platform.impl.clock() - vm_start_time;

        // thread time is in nanoseconds; convert to seconds.
        return new org.python.types.Float(current_time / 1000000000.0);
    }

    @org.python.Method(
            __doc__ = "ctime(seconds) -> string\n\n" +
                      "Convert a time in seconds since the Epoch to a string in local time.\n" +
                      "This is equivalent to asctime(localtime(seconds)). When the time tuple is\n" +
                      "not present, current time as returned by localtime() is used.",
            default_args = {"seconds"}
    )
    public static org.python.Object ctime(org.python.Object seconds) {
        java.util.Date date;
        if ((seconds == null) || (seconds instanceof org.python.types.NoneType)) {
            long currentTimeInMillis = System.currentTimeMillis();
            date = new java.util.Date(currentTimeInMillis);
        } else {
            //Type checking the parameter
            if (!(seconds instanceof org.python.types.Int) && !(seconds instanceof org.python.types.Float)) {
                throw new org.python.exceptions.TypeError("an integer is required (got type " + seconds.typeName() + ")");
            }
            date = new java.util.Date(((org.python.types.Int) seconds.__int__()).value * 1000L);
        }
        java.text.SimpleDateFormat ft = new java.text.SimpleDateFormat("E MMM dd HH:mm:ss yyyy", java.util.Locale.ENGLISH);
        String padded_date = ft.format(date);
        if (Character.toString(padded_date.charAt(8)).equals("0")) {
            java.lang.StringBuilder sb = new StringBuilder();
            sb.append(padded_date.substring(0, 7));
            sb.append("  ");
            sb.append(padded_date.substring(9, padded_date.length()));
            padded_date = sb.toString();
        }
        return new org.python.types.Str(padded_date);
    }

    public static org.python.types.Int daylight;

    @org.python.Method(
            __doc__ = "get_clock_info(name: str) -> dict\n" +
                      "\n" +
                      "Get information of the specified clock.",
            args = {"name"}
    )
    public static org.python.Object get_clock_info(org.python.Object name) {
        try {
            if (((org.python.types.Str) name).value.equals("monotonic")) {
                return new org.python.stdlib.time.Namespace(
                    false, "java.lang.System.nanoTime()", true, compute_nanoTime_resolution()
                );
            }
            // TODO: complete this when more clock types are implemented
            throw new org.python.exceptions.ValueError("unknown clock");
        } catch (java.lang.ClassCastException e) {
            if (org.Python.VERSION < 0x03050000) {
                throw new org.python.exceptions.TypeError("must be str, not " + name.typeName());
            }
            throw new org.python.exceptions.TypeError("get_clock_info() argument 1 must be str, not " + name.typeName());
        }

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
            __doc__ = "monotonic() -> float\n" +
                      "\n" +
                      "Monotonic clock, cannot go backward."
    )
    public static org.python.Object monotonic() {
        return new org.python.types.Float(System.nanoTime() / 1000000000.0);
    }

    /**
     * Computes resolution of nanoTime in worst case scenario
     *
     * According to https://docs.oracle.com/javase/7/docs/api/java/lang/System.html#nanoTime(),
     * resolution of nanoTime is at least as good as that of currentTimeMillis()
     *
     * The algorithm to compute currentTimeMillis() resolution is adopted from
     * https://www.javaworld.com/article/2077327/core-java/my-kingdom-for-a-good-timer.html
     */
    private static double compute_nanoTime_resolution() {
        // JIT/hotspot warmup:
        for (int r = 0; r < 3000; ++r) {
            System.currentTimeMillis();
        }

        long time = System.currentTimeMillis();
        long time_prev = time;
        long total_delta = 0;
        int iteration = 5;

        for (int i = 0; i < iteration; ++i) {
            // Busy wait until system time changes:
            while (time == time_prev) {
                time = System.currentTimeMillis();
            }
            total_delta += (time - time_prev);
            time_prev = time;
        }

        return (total_delta / iteration) / 1000.0; // returns resolution in seconds
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
            java.lang.Thread.sleep((int) (((org.python.types.Float) seconds.__float__()).value * 1000.0));
        } catch (ClassCastException e) {
            throw new org.python.exceptions.TypeError("a float is required");
        } catch (InterruptedException ex) {
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
