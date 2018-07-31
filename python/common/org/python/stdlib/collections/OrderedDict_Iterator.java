package org.python.stdlib.collections;

class OrderedDict_Iterator extends org.python.types.Iterator {
    static {
        org.python.types.Type.declarePythonType(OrderedDict_Iterator.class, "odict_iterator", null, null);
    }

    OrderedDict_Iterator(org.python.stdlib.collections.OrderedDict odict) {
        this.iterator = odict.value.keySet().iterator();
    }

    private OrderedDict_Iterator() {
        this.iterator = null;
    }

    static OrderedDict_Iterator get_reverse_keyIterator(java.util.Set<org.python.Object> keySet) {
        org.python.stdlib.collections.OrderedDict_Iterator keyIterator =
            new org.python.stdlib.collections.OrderedDict_Iterator();
        java.util.LinkedList<org.python.Object> keyLinkedList = new java.util.LinkedList<>();
        keyLinkedList.addAll(keySet);
        keyIterator.iterator = keyLinkedList.descendingIterator();

        return keyIterator;
    }

    static OrderedDict_Iterator get_reverse_itemIterator(
            java.util.Set<java.util.Map.Entry<org.python.Object, org.python.Object>> entrySet) {
        org.python.stdlib.collections.OrderedDict_Iterator itemIterator =
            new org.python.stdlib.collections.OrderedDict_Iterator();
        java.util.LinkedList<org.python.Object> itemLinkedList = new java.util.LinkedList<>();
        for (java.util.Map.Entry<org.python.Object, org.python.Object> entry : entrySet) {
            java.util.List<org.python.Object> tmp = new java.util.ArrayList<org.python.Object>();
            tmp.add(entry.getKey());
            tmp.add(entry.getValue());
            itemLinkedList.add(new org.python.types.Tuple(tmp));
        }
        itemIterator.iterator = itemLinkedList.descendingIterator();

        return itemIterator;
    }

    static OrderedDict_Iterator get_reverse_valueIterator(java.util.Collection<org.python.Object> values) {
        org.python.stdlib.collections.OrderedDict_Iterator valueIterator =
            new org.python.stdlib.collections.OrderedDict_Iterator();
        java.util.LinkedList<org.python.Object> valueLinkedList = new java.util.LinkedList<>();
        valueLinkedList.addAll(values);
        valueIterator.iterator = valueLinkedList.descendingIterator();

        return valueIterator;
    }
}
