package python;

public interface Platform {
    /**
     * Return the number of CPU nanoseconds that this thread has consumed.
     */
    public long clock();

    public void debug(java.lang.String msg);

    public void debug(java.lang.String msg, java.lang.Object obj);
}