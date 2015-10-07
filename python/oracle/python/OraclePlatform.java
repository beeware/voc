package python;

import java.lang.management.ManagementFactory;
import java.lang.management.ThreadMXBean;


class OraclePlatform implements python.PythonPlatform {
    public OraclePlatform() {}

    public long clock() {
        ThreadMXBean tmxb = ManagementFactory.getThreadMXBean();
        return tmxb.getCurrentThreadCpuTime();
    }

}