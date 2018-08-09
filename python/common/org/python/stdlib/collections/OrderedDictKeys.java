package org.python.stdlib.collections;

public class OrderedDictKeys extends org.python.types.DictKeys {
    static {
        org.python.types.Type.declarePythonType(OrderedDictKeys.class, "odict_keys", null, null);
    }

    OrderedDictKeys(org.python.stdlib.collections.OrderedDict odict) {
        super(odict);
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object __reversed__() {
        if (org.Python.VERSION < 0x03050000) {
            throw new org.python.exceptions.TypeError("argument to reversed() must be a sequence");
        }

        return org.python.stdlib.collections.OrderedDict_Iterator.get_reverse_keyIterator(this.value);
    }
}
