package org.python.types;

public class FrozenSet extends org.python.types.Object {
    public java.util.Set<org.python.Object> value;

    @org.python.Method(
            __doc__ = "frozenset() -> empty frozenset object" +
                    "frozenset(iterable) -> frozenset object\n" +
                    "\n" +
                    "Build an immutable unordered collection of unique elements.\n"
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
            } else {
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
            }
        }
    }


    @org.python.Method(
            __doc__ = ""
    )
    public org.python.types.Int __len__() {
        return new org.python.types.Int(this.value.size());
    }
}
