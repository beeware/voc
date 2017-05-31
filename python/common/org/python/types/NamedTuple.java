package org.python.types;

public class NamedTuple extends org.python.types.Object {
    public org.python.types.Str typeName;
    public class subTuple extends org.python.types.Object {
        public java.util.Set<org.python.Object> fieldNames;
        public subTuple(java.util.List<org.python.Object> fields) {
            this.fieldNames = new java.util.HashSet<org.python.Object>(fields);
        }
    }
    boolean verbose;
    boolean rename;

    @org.python.Method(
            __doc__ = "namedtuple(typeName, listOfFieldNames) -> new namedtuple object" +
                    "\n" +
                    "Returns a new tuple subclass named typename.\n",
            default_args = {"name", "fields"}
    )

    public NamedTuple(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super();
        if (args.length == 0) {
            throw new org.python.exceptions.TypeError("namedtuple() missing 2 required positional arguments: 'typename' and 'field_names'");
        } else if (args.length == 1) {
            throw new org.python.exceptions.TypeError("namedtuple() missing 1 required positional argument: 'typename' and 'field_names'");
        } else if (args.length > 2) {
            throw new org.python.exceptions.TypeError("namedtuple() takes from 2 to 4 positional arguments but " + args.length + " were given");
        } else {
            if (args[0] instanceof org.python.types.Str) {
                org.python.types.Str name = (org.python.types.Str) (args[0]);
                if (name.value.length() > 0) {
                    this.typeName = name;
                } else {
                    throw new org.python.exceptions.TypeError("Type names and field names must be valid identifiers");
                }
            } else {
                throw new org.python.exceptions.TypeError("Type names and field names must be valid identifiers");
            }
            this.verbose = false;
            this.rename = false;
            if (args[1] instanceof org.python.types.List) {
                org.python.types.List l = (org.python.types.List) (args[1]);
                java.util.List<org.python.Object> l1 = l.value;
                subTuple tuple = new subTuple((java.util.List<org.python.Object>) l1);
            } else if (args[1] instanceof org.python.types.Str) {
                java.util.List<org.python.Object> l1 = new java.util.ArrayList<org.python.Object>();
                l1.add(args[1]);
                subTuple tuple = new subTuple((java.util.List<org.python.Object>) l1);
            } else {
                throw new org.python.exceptions.TypeError("Type names and field names must be valid identifiers");
            }
        }

    }

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.types.Str __repr__() {
        // Representation of an empty set is different
        return new org.python.types.Str("<class '__main__." + this.typeName + "'>");
    }
}

    // @org.python.Method(
    //         __doc__ = ""
    // )
    // public org.python.types.Str __repr__() {
    //     // Representation of an empty set is different
    //     if (this.value.size() == 0) {
    //         return new org.python.types.Str("frozenset()");
    //     }

    //     java.lang.StringBuilder buffer = new java.lang.StringBuilder("frozenset({");
    //     boolean first = true;
    //     for (org.python.Object obj : this.value) {
    //         if (first) {
    //             first = false;
    //         } else {
    //             buffer.append(", ");
    //         }
    //         buffer.append(obj.__repr__());
    //     }
    //     buffer.append("})");
    //     return new org.python.types.Str(buffer.toString());
    // }


    // @org.python.Method(
    //         __doc__ = ""
    // )
    // public org.python.types.Int __len__() {
    //     return new org.python.types.Int(this.value.size());
    // }
