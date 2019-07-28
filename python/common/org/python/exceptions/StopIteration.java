package org.python.exceptions;

public class StopIteration extends org.python.exceptions.Exception {
    @org.python.Attribute()
    public org.python.Object value;

    /**
     * StopIteration is a singleton instance for performance reasons, introduced in
     * PR #881 (https://github.com/beeware/voc/pull/881/). This results in a non-trivial
     * performance improvement for nested loops. However, this also means that the equality
     * comparison between StopIteration instances will always be true.
     */
    public static final org.python.exceptions.StopIteration STOPITERATION = new org.python.exceptions.StopIteration();

    private StopIteration() {
        super("");
        this.value = org.python.types.NoneType.NONE;
    }

    public StopIteration(org.python.Object value) {
        super();
        this.value = value;
    }

    public StopIteration(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super(args, kwargs);
    }
}
