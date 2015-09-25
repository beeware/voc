package org.python;


public interface Iterable {
    public org.python.types.Object __iter__();
    public org.python.types.Object __next__();
}
