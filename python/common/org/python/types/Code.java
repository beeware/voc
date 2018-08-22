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
