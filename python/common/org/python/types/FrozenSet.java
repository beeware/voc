package org.python.types;

public class FrozenSet extends org.python.types.Object {
    @org.python.Method(
            __doc__ = "frozenset() -> empty frozenset object" +
                    "frozenset(iterable) -> frozenset object\n" +
                    "\n" +
                    "Build an immutable unordered collection of unique elements.\n"
    )
    public FrozenSet(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'frozenset' not implemented");
    }
}
