package python;

import android.os.Debug;


public class AndroidPlatform implements python.PythonPlatform {
    public AndroidPlatform() {}

    public long clock() {
        return Debug.threadCpuTimeNanos();
    }

    public void debug(java.lang.String msg) {
        android.util.Log.d("VOC", msg);
    }

    public void debug(java.lang.String msg, java.lang.Object obj) {
        android.util.Log.d("VOC", msg + " " + obj);
    }
}