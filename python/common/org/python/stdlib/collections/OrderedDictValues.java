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
        return org.python.stdlib.collections.OrderedDict_Iterator.get_reverse_valueIterator(this.value);
    }
}
