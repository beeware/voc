package org.python.stdlib.collections;

public class OrderedDictItems extends org.python.types.DictItems{
    static {
        org.python.types.Type.declarePythonType(OrderedDictItems.class, "odict_items", null, null);
    }

    OrderedDictItems(org.python.stdlib.collections.OrderedDict odict) {
        super(odict);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __reversed__() {
        return org.python.stdlib.collections.OrderedDict_Iterator.get_reverse_itemIterator(this.value);
    }
}
