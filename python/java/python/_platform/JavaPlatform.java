package python._platform;

import java.lang.management.ManagementFactory;
import java.lang.management.ThreadMXBean;

public class JavaPlatform implements python.PlatformInterface {
    private org.python.stdlib._io.TextIOWrapper _stderr;
    private org.python.stdlib._io.TextIOWrapper _stdout;
    private org.python.stdlib._io.TextIOWrapper _stdin;

    public JavaPlatform() {
        _stderr = new org.python.stdlib._io.TextIOWrapper(System.err);
        _stdout = new org.python.stdlib._io.TextIOWrapper(System.out);
        _stdin = new org.python.stdlib._io.TextIOWrapper(System.in);
    }

    public long clock() {
        ThreadMXBean tmxb = ManagementFactory.getThreadMXBean();
        return tmxb.getCurrentThreadCpuTime();
    }

    public void debug(java.lang.String msg) {
        System.out.println("DEBUG " + msg);
    }

    public void debug(java.lang.String msg, java.lang.Object obj) {
        System.out.println("DEBUG " + msg + ": " + obj);
    }

    public org.python.Object getPlatform() {
        java.lang.String os_name = System.getProperty("os.name");
        java.lang.String py_name;
        if (os_name.startsWith("Windows")) {
            py_name = "win32";
        } else if (os_name.equals("Mac OS X")) {
            py_name = "darwin";
        } else if (os_name.equals("Linux")) {
            py_name = "linux";
        } else {
            System.out.println(os_name);
            py_name = "unknown";
        }

        return new org.python.types.Str(py_name);
    }

    public org.python.Object stderr() {
        return _stderr;
    }

    public org.python.Object stdout() {
        return _stdout;
    }

    public org.python.Object stdin() {
        return _stdin;
    }

    public org.python.Object args() {
        // java.util.regex.Pattern cmdline_pattern = java.util.regex.Pattern.compile("(\"[^\"]*\"|[^\"]+)(\\s+|$)");
        java.util.regex.Pattern cmdline_pattern = java.util.regex.Pattern.compile("\\s+");
        java.lang.String[] cmdline_args = cmdline_pattern.split(System.getProperty("sun.java.command"));
        java.util.List<org.python.Object> arg_list = new java.util.ArrayList<org.python.Object>();
        for (String arg : cmdline_args) {
            arg_list.add(new org.python.types.Str(arg));
        }

        return new org.python.types.List(arg_list);
    }
}
