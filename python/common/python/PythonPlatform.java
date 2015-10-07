package python;

interface PythonPlatform {
    /**
     * Return the number of CPU nanoseconds that this thread has consumed.
     */
    public long clock();

}