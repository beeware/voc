package org.python.types;

public class FrozenSet extends org.python.types.Object {
    public java.util.Set<org.python.Object> value;

    @org.python.Method(
            __doc__ = "frozenset() -> empty frozenset object" +
                    "frozenset(iterable) -> frozenset object\n" +
                    "\n" +
                    "Build an immutable unordered collection of unique elements.\n",
            default_args = {"iterable"}
            )
    public FrozenSet(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        if (args[0] == null) {
            this.value = java.util.Collections.emptySet();
        } else {
            if (args[0] instanceof org.python.types.Set) {
                this.value = java.util.Collections.unmodifiableSet(
                        ((org.python.types.Set) args[0]).value
                );
            } else if (args[0] instanceof org.python.types.List) {
                this.value = java.util.Collections.unmodifiableSet(
                        new java.util.HashSet<org.python.Object>(
                        ((org.python.types.List) args[0]).value)
                );
            } else if (args[0] instanceof org.python.types.Tuple) {
                this.value = java.util.Collections.unmodifiableSet(
                        new java.util.HashSet<org.python.Object>(
                        ((org.python.types.Tuple) args[0]).value)
                );
            } else if (org.Python.iter(args[0]) instanceof org.python.Iterable) {
                org.python.Iterable iterator = org.Python.iter(args[0]);
                java.util.Set<org.python.Object> generated = new java.util.HashSet<org.python.Object>();
                try {
                    while (true) {
                        org.python.Object next = iterator.__next__();
                        generated.add(next);
                    }
                } catch (org.python.exceptions.StopIteration si) {
                }
                this.value = java.util.Collections.unmodifiableSet(generated);
            } else {
                java.lang.StringBuilder buffer = new java.lang.StringBuilder("'");
                buffer.append(args[0].typeName());
                buffer.append("' object is not iterable");

                throw new org.python.exceptions.TypeError(buffer.toString());
            }
        }
    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.types.Str __repr__() {
        // Representation of an empty set is different
        if (this.value.size() == 0) {
            return new org.python.types.Str("frozenset()");
        }

        java.lang.StringBuilder buffer = new java.lang.StringBuilder("frozenset({");
        boolean first = true;
        for (org.python.Object obj : this.value) {
            if (first) {
                first = false;
            } else {
                buffer.append(", ");
            }
            buffer.append(obj.__repr__());
        }
        buffer.append("})");
        return new org.python.types.Str(buffer.toString());
    }


    @org.python.Method(
            __doc__ = ""
    )
    public org.python.types.Int __len__() {
        return new org.python.types.Int(this.value.size());
    }
}
