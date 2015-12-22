package python;

import java.lang.management.ManagementFactory;
import java.lang.management.ThreadMXBean;


public class JavaPlatform implements python.PythonPlatform {
    public JavaPlatform() {}

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

}