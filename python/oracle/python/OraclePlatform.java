package python;

class OraclePlatform implements python.PythonPlatform {
    public OraclePlatform() {}

    public long clock() {
        java.lang.management.ThreadMXBean tmxb = java.lang.management.ManagementFactory.getThreadMXBean();
        return tmxb.getCurrentThreadCpuTime();
    }

}