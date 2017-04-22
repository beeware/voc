package python;

public interface PlatformInterface {
    /**
     * Return the number of CPU nanoseconds that this thread has consumed.
     */
    public long clock();

    public void debug(java.lang.String msg);

    public void debug(java.lang.String msg, java.lang.Object obj);

    public org.python.Object getPlatform();

    public org.python.Object stderr();

    public org.python.Object stdout();

    public org.python.Object stdin();

    public org.python.Object args();
}
