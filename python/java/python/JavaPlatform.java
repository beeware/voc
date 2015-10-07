package python;

import java.lang.management.ManagementFactory;
import java.lang.management.ThreadMXBean;


class JavaPlatform implements python.PythonPlatform {
    public JavaPlatform() {}

    public long clock() {
        ThreadMXBean tmxb = ManagementFactory.getThreadMXBean();
        return tmxb.getCurrentThreadCpuTime();
    }

}