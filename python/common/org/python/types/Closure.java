package org.python.types;

public class Closure extends org.python.types.Object {

    public java.util.List<org.python.Object> default_args;
    public java.util.Map<java.lang.String, org.python.Object> default_kwargs;

    /**
     * A utility method to update the internal value of this object.
     *
     * Used by __i*__ operations to do an in-place operation.
     * obj must be of type org.python.types.Closure
     */
    void setValue(org.python.Object obj) {
    }

    // public Closure(
    //             java.util.List<org.python.Object> default_args,
    //             java.util.Map<java.lang.String, org.python.Object> default_kwargs
    //         ) {
    //     super();
    //     this.default_args = default_args;
    //     this.default_kwargs = default_kwargs;
    // }

    public Closure() {
        super();
    }

}