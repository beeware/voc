package python;

import android.os.Debug;


class AndroidPlatform implements python.PythonPlatform {
    public AndroidPlatform() {}

    public long clock() {
        return Debug.threadCpuTimeNanos();
    }

}