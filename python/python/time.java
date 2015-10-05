package python;


public class time extends org.python.types.Module {

    public static org.python.types.Str _STRUCT_TM_ITEMS;
    public static org.python.types.Str __doc__;
    public static org.python.types.Str __file__;
    public static org.python.types.Str __loader__;
    public static org.python.types.Str __name__;
    public static org.python.types.Str __package__;
    public static org.python.types.Str __spec__;

    public static org.python.types.Int altzone;

    public static void asctime(org.python.Object [] args, java.util.Hashtable<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("time.asctime has not been implemented.");
    }

    public static void clock(org.python.Object [] args, java.util.Hashtable<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("tclockime. has not been implemented.");
    }

    public static void ctime(org.python.Object [] args, java.util.Hashtable<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("tctimeime. has not been implemented.");
    }

    public static org.python.types.Int daylight;

    public static void get_clock_info(org.python.Object [] args, java.util.Hashtable<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("time.get_clock_info has not been implemented.");
    }

    public static void gmtime(org.python.Object [] args, java.util.Hashtable<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("time.gmtime has not been implemented.");
    }

    public static void localtime(org.python.Object [] args, java.util.Hashtable<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("time.localtime has not been implemented.");
    }

    public static void mktime(org.python.Object [] args, java.util.Hashtable<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("time.mktime has not been implemented.");
    }

    public static void monotonic(org.python.Object [] args, java.util.Hashtable<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("time.monotonic has not been implemented.");
    }

    public static void perf_counter(org.python.Object [] args, java.util.Hashtable<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("time.perf_counter has not been implemented.");
    }

    public static void process_time(org.python.Object [] args, java.util.Hashtable<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("time.process_time has not been implemented.");
    }

    public static void sleep(org.python.Object [] args, java.util.Hashtable<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("tsleepime. has not been implemented.");
    }

    public static void strftime(org.python.Object [] args, java.util.Hashtable<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("time.strftime has not been implemented.");
    }

    public static void strptime(org.python.Object [] args, java.util.Hashtable<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("time.strptime has not been implemented.");
    }

    // public static void struct_time;

    public static org.python.types.Float time(org.python.Object [] args, java.util.Hashtable<java.lang.String, org.python.Object> kwargs) {
        return new org.python.types.Float(System.currentTimeMillis() / 1000.0);
    }

    public static org.python.types.Int timezone;

    public static org.python.types.Tuple tzname;

    public static void tzset(org.python.Object [] args, java.util.Hashtable<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("ttzsetime. has not been implemented.");
    }
}
