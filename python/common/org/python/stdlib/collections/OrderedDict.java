package org.python.stdlib.collections;

// NOTE: The following methods has different implementation/representation in Python 3.4 and older version:
//       1. __iter__     (implemented as generator object in Python 3.4 and older version)
//       2. __reversed__ (implemented as generator object in Python 3.4 and older version)
//       3. keys         (implemented as KeysView object in Python 3.4, and as a list in Python 2.7)
//       4. values       (implemented as ValuesView object in Python 3.4, and as a list in Python 2.7)
//       5. items        (implemented as ItemsView object in Python 3.4, and as a list in Python 2.7)
// TODO: When the methods above are implemented to produce the same output as Python 3.4,
// TODO: uncomment and remove this line from `test_collections.py`: "Different type prior to Python 3.5"

public class OrderedDict extends org.python.types.Dict {

    private OrderedDict() {
        super();
        this.value = new java.util.LinkedHashMap<org.python.Object, org.python.Object>();
    }

    @org.python.Method(
        __doc__ = "Dictionary that remembers insertion order",
        default_args = {"iterable"}
    )
    public OrderedDict(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (args[0] == null) {
            this.value = new java.util.LinkedHashMap<>();
        } else {
            if (args[0] instanceof org.python.types.Dict) {
                this.value = new java.util.LinkedHashMap<>(
                    ((org.python.types.Dict) args[0]).value
                );
            } else {
                org.python.Object iterator = org.Python.iter(args[0]);
                java.util.Map<org.python.Object, org.python.Object> generated = new java.util.LinkedHashMap<>();
                try {
                    while (true) {
                        org.python.Object next = iterator.__next__();
                        java.util.List<org.python.Object> data;
                        if (next instanceof org.python.types.Tuple) {
                            data = ((org.python.types.Tuple) next).value;
                        } else if (next instanceof org.python.types.List) {
                            data = ((org.python.types.List) next).value;
                        } else if (next instanceof org.python.types.Str) {
                            org.python.types.Str str = ((org.python.types.Str) next);
                            data = new java.util.ArrayList<org.python.Object>();
                            for (int i = 0; i < ((org.python.types.Int) str.__len__()).value; i++) {
                                data.add(str.__getitem__(org.python.types.Int.getInt(i)));
                            }
                        } else {
                            throw new org.python.exceptions.TypeError(
                                "'" + next.typeName() + "' object is not iterable"
                            );
                        }

                        if (data.size() > 2) {
                            throw new org.python.exceptions.ValueError("too many values to unpack (expected 2)");
                        } else if (data.size() < 2) {
                            throw new org.python.exceptions.ValueError("need more than 1 value to unpack");
                        }

                        generated.put(data.get(0), data.get(1));
                    }
                } catch (org.python.exceptions.StopIteration si) {
                }
                this.value = generated;
            }
        }

        for (java.util.Map.Entry<java.lang.String, org.python.Object> entry : kwargs.entrySet()) {
            org.python.types.Str key = new org.python.types.Str(entry.getKey());
            this.value.put(key, entry.getValue());
        }
    }

    @org.python.Method(
            __doc__ = "Return repr(self)."
    )
    public org.python.types.Str __repr__() {
        if (this.value.isEmpty()) {
            return new org.python.types.Str("OrderedDict()");
        } else {
            java.lang.StringBuilder buffer = new java.lang.StringBuilder("OrderedDict([");
            boolean first = true;
            for (org.python.Object key : this.value.keySet()) {
                if (first) {
                    first = false;
                } else {
                    buffer.append(", ");
                }
                org.python.Object val = this.value.get(key);
                if (val.toJava() instanceof org.python.internals.Scope) {
                    buffer.append(
                        String.format("(%s, {...})", key.__repr__())
                    );
                } else {
                    buffer.append(
                        String.format("(%s, %s)", key.__repr__(), val.__repr__())
                    );
                }
            }
            buffer.append("])");
            return new org.python.types.Str(buffer.toString());
        }
    }

    @org.python.Method(
            __doc__ = "Return self==value.",
            args = {"other"}
    )
    public org.python.Object __eq__(org.python.Object other) {
        if (other instanceof org.python.stdlib.collections.OrderedDict) {
            org.python.stdlib.collections.OrderedDict od = (org.python.stdlib.collections.OrderedDict) other;
            return org.python.types.Bool.getBool(java.util.Arrays.equals(
                this.value.entrySet().toArray(), od.value.entrySet().toArray()
            ));
        } else {
            return super.__eq__(other);
        }
    }

    @org.python.Method(
            __doc__ = "Implement iter(self)."
    )
    public org.python.Object __iter__() {
        return new org.python.stdlib.collections.OrderedDict_Iterator(this);
    }

    @org.python.Method(
            __doc__ = "od.__reversed__() <==> reversed(od)"
    )
    public org.python.Object __reversed__() {
        return org.python.stdlib.collections.OrderedDict_Iterator.get_reverse_keyIterator(this.value.keySet());
    }

    @org.python.Method(
            __doc__ = "od.copy() -> dict -- a shallow copy of od"
    )
    public org.python.Object copy() {
        org.python.stdlib.collections.OrderedDict od = new org.python.stdlib.collections.OrderedDict();
        for (org.python.Object key: this.value.keySet()) {
            od.value.put(key, this.value.get(key));
        }

        return od;
    }

    @org.python.Method(
            __doc__ =
                "OD.fromkeys(S[, v]) -> New ordered dictionary with keys from S.\n" +
                "        If not specified, the value defaults to None.\n",
            args = {"iterable"},
            default_args = {"value"}
    )
    public static org.python.Object fromkeys(org.python.Object iterable, org.python.Object value) {
        org.python.stdlib.collections.OrderedDict result = new org.python.stdlib.collections.OrderedDict();
        try {
            org.python.Object iter = iterable.__iter__();
            if (value == null) {
                value = org.python.types.NoneType.NONE;
            }
            while (true) {
                result.__setitem__(iter.__next__(), value);
            }
        } catch (org.python.exceptions.AttributeError e) {
            throw new org.python.exceptions.TypeError("'" + iterable.typeName() + "' object is not iterable");
        } catch (org.python.exceptions.StopIteration e) {
        }

        return result;
    }

    @org.python.Method(
          __doc__ = ""
    )
    public org.python.Object items() {
        return new org.python.stdlib.collections.OrderedDictItems(this);
    }

    @org.python.Method(
          __doc__ = ""
    )
    public org.python.Object keys() {
        return new org.python.stdlib.collections.OrderedDictKeys(this);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object values() {
        return new org.python.stdlib.collections.OrderedDictValues(this);
    }

    public org.python.Object popitem() {
        return this.popitem(org.python.types.Bool.TRUE);
    }

    @org.python.Method(
            __doc__ =
                "Remove and return a (key, value) pair from the dictionary.\n" +
                "\n" +
                "Pairs are returned in LIFO order if last is true or FIFO order if false.",
            default_args = {"last"}
    )
    public org.python.Object popitem(org.python.Object last) {
        if (this.value.size() == 0) {
            throw new org.python.exceptions.KeyError(new org.python.types.Str("dictionary is empty"));
        }

        org.python.Object key;
        org.python.Object[] keys = this.value.keySet().toArray(new org.python.Object[this.value.size()]);
        if (last == null || ((org.python.types.Bool) last).value) {
            key = keys[this.value.size() - 1];
        } else {
            key = keys[0];
        }

        org.python.Object value = this.value.remove(key);

        java.util.List<org.python.Object> item_pair = new java.util.ArrayList<org.python.Object>();
        item_pair.add(key);
        item_pair.add(value);
        return new org.python.types.Tuple(item_pair);

    }

    @org.python.Method(
            __doc__ = "",
            default_args = {"iterable"},
            kwargs = "kwargs"
    )
    public org.python.Object update(org.python.Object iterable, org.python.types.Dict kwargs) {
        if (iterable == null) {
            if (kwargs != null) {
                // kwargs is not recommended prior to Python version 3.6 as order of keyword argument is not preserved
                org.python.Object iterator = org.Python.iter(kwargs);
                while (true) {
                    try {
                        org.python.Object key = iterator.__next__();
                        org.python.Object value = kwargs.value.get(key);
                        this.value.put(key, value);
                    } catch (org.python.exceptions.StopIteration si) {
                        break;
                    }
                }
            }
        } else if (iterable instanceof org.python.types.Dict) {
            org.python.Object iterator = org.Python.iter(iterable);
            while (true) {
                try {
                    org.python.Object key = iterator.__next__();
                    org.python.Object value = iterable.__getitem__(key);
                    this.value.put(key, value);
                } catch (org.python.exceptions.StopIteration si) {
                    break;
                }
            }
        } else {
            org.python.Object iterator = org.Python.iter(iterable);
            java.util.List<org.python.Object> pair;
            while (true) {
                try {
                    org.python.Object next = iterator.__next__();
                    if (next instanceof org.python.types.List) {
                        pair = ((org.python.types.List) next).value;
                    } else if (next instanceof org.python.types.Tuple) {
                        pair = ((org.python.types.Tuple) next).value;
                    } else if (next instanceof org.python.types.Str) {
                        throw new org.python.exceptions.ValueError("need more than 1 value to unpack");
                    } else {
                        throw new org.python.exceptions.TypeError(
                            "'" + next.typeName() + "' object is not iterable"
                        );
                    }

                    if (pair.size() > 2) {
                        throw new org.python.exceptions.ValueError("too many values to unpack (expected 2)");
                    } else if (pair.size() < 2) {
                        throw new org.python.exceptions.ValueError("need more than 1 value to unpack");
                    }

                    org.python.Object key = pair.get(0);
                    org.python.Object value = pair.get(1);
                    this.value.put(key, value);
                } catch (org.python.exceptions.StopIteration si) {
                    break;
                }
            }
        }

        return org.python.types.NoneType.NONE;
    }

    @org.python.Method(
            __doc__ =
                "Move an existing element to the end (or beginning if last==False).\n" +
                "\n" +
                "        Raises KeyError if the element does not exist.\n" +
                "        When last=True, acts like a fast version of self[key]=self.pop(key).\n",
            args = {"key"},
            default_args = {"last"}
    )
    public void move_to_end(org.python.Object key, org.python.Object last) {
        org.python.Object value = this.pop(key, null);

        if (last == null || ((org.python.types.Bool) last).value) {
            this.__setitem__(key, value);
        } else {
            java.util.LinkedHashMap<org.python.Object, org.python.Object> map = new java.util.LinkedHashMap<>();
            map.put(key, value);
            map.putAll(this.value);
            this.value = map;
        }
    }
}
