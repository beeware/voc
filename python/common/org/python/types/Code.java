package org.python.types;

public class Code extends org.python.types.Object {
    @org.python.Attribute
    org.python.types.Int co_argcount;

    @org.python.Attribute
    org.python.types.Tuple co_cellvars;

    @org.python.Attribute
    org.python.types.Bytes co_code;

    @org.python.Attribute
    org.python.types.Tuple co_consts;

    @org.python.Attribute
    org.python.types.Str co_filename;

    @org.python.Attribute
    org.python.types.Int co_firstlineno;

    @org.python.Attribute
    org.python.types.Int co_flags;

    @org.python.Attribute
    org.python.types.Tuple co_freevars;

    @org.python.Attribute
    org.python.types.Int co_kwonlyargcount;

    @org.python.Attribute
    org.python.types.Bytes co_lnotab;

    @org.python.Attribute
    org.python.types.Str co_name;

    @org.python.Attribute
    org.python.types.Tuple co_names;

    @org.python.Attribute
    org.python.types.Int co_nlocals;

    @org.python.Attribute
    org.python.types.Int co_stacksize;

    @org.python.Attribute
    org.python.types.Tuple co_varnames;

    /**
     * A utility method to update the internal value of this object.
     *
     * Used by __i*__ operations to do an in-place operation.
     * obj must be of type org.python.types.Class
     */
    void setValue(org.python.Object obj) {
        org.python.types.Object object = (org.python.types.Object) obj;
        this.co_argcount = (org.python.types.Int) object.__getattribute__("co_argcount");
        this.co_cellvars = (org.python.types.Tuple) object.__getattribute__("co_cellvars");
        this.co_code = (org.python.types.Bytes) object.__getattribute__("co_code");
        this.co_consts = (org.python.types.Tuple) object.__getattribute__("co_consts");
        this.co_filename = (org.python.types.Str) object.__getattribute__("co_filename");
        this.co_firstlineno = (org.python.types.Int) object.__getattribute__("co_firstlineno");
        this.co_flags = (org.python.types.Int) object.__getattribute__("co_flags");
        this.co_freevars = (org.python.types.Tuple) object.__getattribute__("co_freevars");
        this.co_kwonlyargcount = (org.python.types.Int) object.__getattribute__("co_kwonlyargcount");
        this.co_lnotab = (org.python.types.Bytes) object.__getattribute__("co_lnotab");
        this.co_name = (org.python.types.Str) object.__getattribute__("co_name");
        this.co_names = (org.python.types.Tuple) object.__getattribute__("co_names");
        this.co_nlocals = (org.python.types.Int) object.__getattribute__("co_nlocals");
        this.co_stacksize = (org.python.types.Int) object.__getattribute__("co_stacksize");
        this.co_varnames = (org.python.types.Tuple) object.__getattribute__("co_varnames");
    }

    public Code(
            org.python.types.Int co_argcount,
            org.python.types.Tuple co_cellvars,
            org.python.types.Bytes co_code,
            org.python.types.Tuple co_consts,
            org.python.types.Str co_filename,
            org.python.types.Int co_firstlineno,
            org.python.types.Int co_flags,
            org.python.types.Tuple co_freevars,
            org.python.types.Int co_kwonlyargcount,
            org.python.types.Bytes co_lnotab,
            org.python.types.Str co_name,
            org.python.types.Tuple co_names,
            org.python.types.Int co_nlocals,
            org.python.types.Int co_stacksize,
            org.python.types.Tuple co_varnames
    ) {
        super();

        this.co_argcount = co_argcount;
        this.co_cellvars = co_cellvars;
        this.co_code = co_code;
        this.co_consts = co_consts;
        this.co_filename = co_filename;
        this.co_firstlineno = co_firstlineno;
        this.co_flags = co_flags;
        this.co_freevars = co_freevars;
        this.co_kwonlyargcount = co_kwonlyargcount;
        this.co_lnotab = co_lnotab;
        this.co_name = co_name;
        this.co_names = co_names;
        this.co_nlocals = co_nlocals;
        this.co_stacksize = co_stacksize;
        this.co_varnames = co_varnames;
    }

    public org.python.types.Str __repr__() {
        java.lang.String location;
        if (this.co_filename == null) {
            location = "builtin function";
        } else {
            location = String.format("file \"%s\", line %s", this.co_filename, this.co_firstlineno);
        }
        return new org.python.types.Str(
                String.format("<%s object at 0x%x, %s>",
                        this.typeName(),
                        this.hashCode(),
                        location
                )
        );
    }
}
