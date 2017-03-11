package org.python.types;

public class MemoryView extends org.python.types.Object {
    @org.python.Method(
            __doc__ = "memoryview(object)" +
                    "\n" +
                    "Create a new memoryview object which references the given object.\n"
    )
    public MemoryView(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        throw new org.python.exceptions.NotImplementedError("Builtin function 'memoryview' not implemented");
    }
}
