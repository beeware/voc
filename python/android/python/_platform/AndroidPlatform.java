package python._platform;

import android.os.Debug;

public class AndroidPlatform implements python.PlatformInterface {
    private org.python.stdlib._io.TextIOWrapper _stderr;
    private org.python.stdlib._io.TextIOWrapper _stdout;
    private org.python.stdlib._io.TextIOWrapper _stdin;

    public AndroidPlatform() {
        _stderr = new org.python.stdlib._io.TextIOWrapper(new LogStream(android.util.Log.ERROR, "Python", 1024));
        _stdout = new org.python.stdlib._io.TextIOWrapper(new LogStream(android.util.Log.INFO, "Python", 1024));
        // _stdin = new org.python.stdlib._io.TextIOWrapper(System.in);
    }

    public long clock() {
        return Debug.threadCpuTimeNanos();
    }

    public void debug(java.lang.String msg) {
        android.util.Log.i("Python", msg);
    }

    public void debug(java.lang.String msg, java.lang.Object obj) {
        android.util.Log.i("Python", msg + " " + obj);
    }

    public org.python.Object getPlatform() {
        return new org.python.types.Str("android");
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
        return new org.python.types.List();
    }
}
