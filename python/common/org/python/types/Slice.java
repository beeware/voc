package org.python.types;

public class Slice extends org.python.types.Object {
    org.python.types.Int start;
    org.python.types.Int stop;
    org.python.types.Int step;

    public Slice(org.python.Object stop) {
        this(new org.python.types.Int(0), stop, new org.python.types.Int(1));
    }

    public Slice(org.python.Object start, org.python.Object stop) {
        this(start, stop, new org.python.types.Int(1));
    }

    public Slice(org.python.Object start, org.python.Object stop, org.python.Object step) {
        super();
        if (start instanceof org.python.types.Int) {
            this.__dict__.put("start", start);
            this.start = (org.python.types.Int) start;
        } else if (start instanceof org.python.types.NoneType) {
            this.__dict__.put("start", start);
        } else {
            org.python.Object index_object;
            try {
                index_object = start.__index__();
            } catch (org.python.exceptions.TypeError | org.python.exceptions.AttributeError error) {
                throw new org.python.exceptions.TypeError("slice indices must be integers or None or have an __index__ method");
            }
            if (index_object instanceof org.python.types.Int) {
                this.__dict__.put("start", start);
                this.start = (org.python.types.Int) index_object;
            } else {
                throw new org.python.exceptions.TypeError("TypeError: __index__ returned non-int (type " + index_object.typeName() + ")");
            }
        }

        if (stop instanceof org.python.types.Int) {
            this.__dict__.put("stop", stop);
            this.stop = (org.python.types.Int) stop;
        } else if (stop instanceof org.python.types.NoneType) {
            this.__dict__.put("stop", stop);
        } else {
            org.python.Object index_object;
            try {
                index_object = stop.__index__();
            } catch (org.python.exceptions.TypeError | org.python.exceptions.AttributeError error) {
                throw new org.python.exceptions.TypeError("slice indices must be integers or None or have an __index__ method");
            }
            if (index_object instanceof org.python.types.Int) {
                this.__dict__.put("stop", stop);
                this.stop = (org.python.types.Int) index_object;
            } else {
                throw new org.python.exceptions.TypeError("TypeError: __index__ returned non-int (type " + index_object.typeName() + ")");
            }
        }

        if (step instanceof org.python.types.Int) {
            this.step = (org.python.types.Int) step;
            if (this.step.value == 0) {
                throw new org.python.exceptions.ValueError("slice step cannot be zero");
            } else {
                this.__dict__.put("step", step);
            }
        } else if (step instanceof org.python.types.NoneType) {
            this.__dict__.put("step", step);
        } else {
            org.python.Object index_object;
            try {
                index_object = step.__index__();
            } catch (org.python.exceptions.TypeError | org.python.exceptions.AttributeError error) {
                throw new org.python.exceptions.TypeError("slice indices must be integers or None or have an __index__ method");
            }
            if (index_object instanceof org.python.types.Int) {
                this.__dict__.put("step", step);
                this.step = (org.python.types.Int) index_object;
            } else {
                throw new org.python.exceptions.TypeError("TypeError: __index__ returned non-int (type " + index_object.typeName() + ")");
            }
        }
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __ge__(org.python.Object other) {
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __gt__(org.python.Object other) {
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __eq__(org.python.Object other) {
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __lt__(org.python.Object other) {
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }

    @org.python.Method(
            __doc__ = "",
            args = {"other"}
    )
    public org.python.Object __le__(org.python.Object other) {
        return org.python.types.NotImplementedType.NOT_IMPLEMENTED;
    }
}
