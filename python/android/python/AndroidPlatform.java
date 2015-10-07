package python;

class AndroidPlatform implements python.PythonPlatform {
    public AndroidPlatform() {}

    public long clock() {
        throw new org.python.exceptions.NotImplementedError("Android platform not implemented yet");
    }

}