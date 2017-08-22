package org.python.types;


public class Reversed extends Object implements org.python.Object {
    org.python.Object sequence;
    long index;

    public Reversed(org.python.Object sequence) {
        this.sequence = sequence;
        this.index = ((Int) sequence.__len__()).value - 1;
    }

    @org.python.Method(
            __doc__ = "Implement iter(self)."
    )
    public org.python.Object __iter__() {
        return this;
    }

    @org.python.Method(
            __doc__ = "Implement next(self)."
    )
    public org.python.Object __next__() {
        if (this.index < 0) {
            throw new org.python.exceptions.StopIteration();
        }
        org.python.Object item = this.sequence.__getitem__(new Int(this.index));
        this.index--;
        return item;
    }
}
