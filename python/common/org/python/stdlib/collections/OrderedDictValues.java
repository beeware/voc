package org.python.stdlib.collections;

public class OrderedDictValues extends org.python.types.DictValues{
    static {
        org.python.types.Type.declarePythonType(OrderedDictValues.class, "odict_values", null, null);
    }

    OrderedDictValues(org.python.stdlib.collections.OrderedDict odict) {
        super(odict);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __reversed__() {
        if (org.Python.VERSION < 0x03050000) {
            throw new org.python.exceptions.TypeError("argument to reversed() must be a sequence");
        }

        return org.python.stdlib.collections.OrderedDict_Iterator.get_reverse_valueIterator(this.value);
    }
}
