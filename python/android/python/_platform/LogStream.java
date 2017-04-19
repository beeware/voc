package python._platform;

public class LogStream extends java.io.OutputStream {
    protected java.lang.String tag;
    protected byte[] buf;
    protected int size;
    protected int count;
    protected int priority;

    public LogStream(int priority, java.lang.String tag, int size) {
        this.tag = tag;
        this.priority = priority;
        this.size = size;

        buf = new byte[size];
    }

    public void write(int b) {
        if (b != '\n') {
            buf[count] = (byte) b;
            count++;
        }

        if (b == '\n' || count == size) {
            android.util.Log.println(priority, tag, new java.lang.String(buf, 0, count));
            count = 0;
        }
    }
}
