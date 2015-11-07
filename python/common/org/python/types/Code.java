package org.python.types;

public class Code extends org.python.types.Object {

    /**
     * A utility method to update the internal value of this object.
     *
     * Used by __i*__ operations to do an in-place operation.
     * obj must be of type org.python.types.Class
     */
    void setValue(org.python.Object obj) {
        org.python.types.Object object = (org.python.types.Object) obj;
        this.attrs.put("co_argcount", object.attrs.get("co_argcount"));
        this.attrs.put("co_cellvars", object.attrs.get("co_cellvars"));
        this.attrs.put("co_code", object.attrs.get("co_code"));
        this.attrs.put("co_consts", object.attrs.get("co_consts"));
        this.attrs.put("co_filename", object.attrs.get("co_filename"));
        this.attrs.put("co_firstlineno", object.attrs.get("co_firstlineno"));
        this.attrs.put("co_flags", object.attrs.get("co_flags"));
        this.attrs.put("co_freevars", object.attrs.get("co_freevars"));
        this.attrs.put("co_kwonlyargcount", object.attrs.get("co_kwonlyargcount"));
        this.attrs.put("co_lnotab", object.attrs.get("co_lnotab"));
        this.attrs.put("co_name", object.attrs.get("co_name"));
        this.attrs.put("co_names", object.attrs.get("co_names"));
        this.attrs.put("co_nlocals", object.attrs.get("co_nlocals"));
        this.attrs.put("co_stacksize", object.attrs.get("co_stacksize"));
        this.attrs.put("co_varnames", object.attrs.get("co_varnames"));
    }

    public Code() {
        super();
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

        this.attrs.put("co_argcount", co_argcount);
        this.attrs.put("co_cellvars", co_cellvars);
        this.attrs.put("co_code", co_code);
        this.attrs.put("co_consts", co_consts);
        this.attrs.put("co_filename", co_filename);
        this.attrs.put("co_firstlineno", co_firstlineno);
        this.attrs.put("co_flags", co_flags);
        this.attrs.put("co_freevars", co_freevars);
        this.attrs.put("co_kwonlyargcount", co_kwonlyargcount);
        this.attrs.put("co_lnotab", co_lnotab);
        this.attrs.put("co_name", co_name);
        this.attrs.put("co_names", co_names);
        this.attrs.put("co_nlocals", co_nlocals);
        this.attrs.put("co_stacksize", co_stacksize);
        this.attrs.put("co_varnames", co_varnames);
    }

    public org.python.types.Str __repr__() {
        return new org.python.types.Str(
            String.format("<%s object at %x, file \"%s\", line %s>",
                org.Python.pythonTypeName(this),
                this.hashCode(),
                this.attrs.get("co_filename"),
                this.attrs.get("co_firstlineno")
            )
        );
    }
}