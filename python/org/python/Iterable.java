package org.python;


public interface Iterable {
    public org.python.Object __iter__();
    public org.python.Object __next__();
}
