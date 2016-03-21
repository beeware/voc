package org.python.types;

public class NoneType extends org.python.types.Object {
    public static org.python.Object NONE = new org.python.types.NoneType();
    public static final java.lang.String PYTHON_TYPE_NAME = "NoneType";

    NoneType() {}

    @org.python.Method(
        __doc__=""
    )
    public org.python.Object __pos__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary +: 'NoneType'");
    }

    @org.python.Method(
        __doc__=""
    )
    public org.python.Object __neg__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary -: 'NoneType'");
    }

    @org.python.Method(
        __doc__=""
    )
    public org.python.Object __invert__() {
        throw new org.python.exceptions.TypeError("bad operand type for unary ~: 'NoneType'");
    }


    @org.python.Method(
        __doc__=""
    )
    public org.python.Object __bool__() {
        return new org.python.types.Bool(false);
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __ge__(org.python.Object other) {
        if(other instanceof org.python.types.Bool) {
            throw new org.python.exceptions.TypeError("unorderable types: NoneType() >= bool()");
        } else if(other instanceof org.python.types.Float) {
            throw new org.python.exceptions.TypeError("unorderable types: NoneType() >= float()");
        } else if(other instanceof org.python.types.Int) {
            throw new org.python.exceptions.TypeError("unorderable types: NoneType() >= int()");
        } else if(other instanceof org.python.types.Str) {
            throw new org.python.exceptions.TypeError("unorderable types: NoneType() >= str()");
        } else if(other instanceof org.python.types.List) {
            throw new org.python.exceptions.TypeError("unorderable types: NoneType() >= list()");
        } else if(other instanceof org.python.types.Set) {
            throw new org.python.exceptions.TypeError("unorderable types: NoneType() >= set()");
        } else if(other instanceof org.python.types.Tuple) {
            throw new org.python.exceptions.TypeError("unorderable types: NoneType() >= tuple()");
        } else if(other instanceof org.python.types.Dict) {
            throw new org.python.exceptions.TypeError("unorderable types: NoneType() >= dict()");
        }

        throw new Error();
    }

        @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __gt__(org.python.Object other) {
        if(other instanceof org.python.types.Bool) {
            throw new org.python.exceptions.TypeError("unorderable types: NoneType() > bool()");
        } else if(other instanceof org.python.types.Float) {
            throw new org.python.exceptions.TypeError("unorderable types: NoneType() > float()");
        } else if(other instanceof org.python.types.Int) {
            throw new org.python.exceptions.TypeError("unorderable types: NoneType() > int()");
        } else if(other instanceof org.python.types.Str) {
            throw new org.python.exceptions.TypeError("unorderable types: NoneType() > str()");
        } else if(other instanceof org.python.types.List) {
            throw new org.python.exceptions.TypeError("unorderable types: NoneType() > list()");
        } else if(other instanceof org.python.types.Set) {
            throw new org.python.exceptions.TypeError("unorderable types: NoneType() > set()");
        } else if(other instanceof org.python.types.Tuple) {
            throw new org.python.exceptions.TypeError("unorderable types: NoneType() > tuple()");
        } else if(other instanceof org.python.types.Dict) {
            throw new org.python.exceptions.TypeError("unorderable types: NoneType() > dict()");
        }

        throw new Error();
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __lt__(org.python.Object other) {
        if(other instanceof org.python.types.Bool) {
            throw new org.python.exceptions.TypeError("unorderable types: NoneType() < bool()");
        } else if(other instanceof org.python.types.Float) {
            throw new org.python.exceptions.TypeError("unorderable types: NoneType() < float()");
        } else if(other instanceof org.python.types.Int) {
            throw new org.python.exceptions.TypeError("unorderable types: NoneType() < int()");
        } else if(other instanceof org.python.types.Str) {
            throw new org.python.exceptions.TypeError("unorderable types: NoneType() < str()");
        } else if(other instanceof org.python.types.List) {
            throw new org.python.exceptions.TypeError("unorderable types: NoneType() < list()");
        } else if(other instanceof org.python.types.Set) {
            throw new org.python.exceptions.TypeError("unorderable types: NoneType() < set()");
        } else if(other instanceof org.python.types.Tuple) {
            throw new org.python.exceptions.TypeError("unorderable types: NoneType() < tuple()");
        } else if(other instanceof org.python.types.Dict) {
            throw new org.python.exceptions.TypeError("unorderable types: NoneType() < dict()");
        }

        throw new Error();
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __le__(org.python.Object other) {
        if(other instanceof org.python.types.Bool) {
            throw new org.python.exceptions.TypeError("unorderable types: NoneType() <= bool()");
        } else if(other instanceof org.python.types.Float) {
            throw new org.python.exceptions.TypeError("unorderable types: NoneType() <= float()");
        } else if(other instanceof org.python.types.Int) {
            throw new org.python.exceptions.TypeError("unorderable types: NoneType() <= int()");
        } else if(other instanceof org.python.types.Str) {
            throw new org.python.exceptions.TypeError("unorderable types: NoneType() <= str()");
        } else if(other instanceof org.python.types.List) {
            throw new org.python.exceptions.TypeError("unorderable types: NoneType() <= list()");
        } else if(other instanceof org.python.types.Set) {
            throw new org.python.exceptions.TypeError("unorderable types: NoneType() <= set()");
        } else if(other instanceof org.python.types.Tuple) {
            throw new org.python.exceptions.TypeError("unorderable types: NoneType() <= tuple()");
        } else if(other instanceof org.python.types.Dict) {
            throw new org.python.exceptions.TypeError("unorderable types: NoneType() <= dict()");
        }

        throw new Error();
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __mul__(org.python.Object other) {
        if(other instanceof org.python.types.Bool) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for *: 'NoneType' and 'bool'");
        } else if(other instanceof org.python.types.Float) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for *: 'NoneType' and 'float'");
        } else if(other instanceof org.python.types.Int) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for *: 'NoneType' and 'int'");
        } else if(other instanceof org.python.types.Str) {
            throw new org.python.exceptions.TypeError("can't multiply sequence by non-int of type 'NoneType'");
        } else if(other instanceof org.python.types.List) {
            throw new org.python.exceptions.TypeError("can't multiply sequence by non-int of type 'NoneType'");
        } else if(other instanceof org.python.types.Set) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for *: 'NoneType' and 'set'");
        } else if(other instanceof org.python.types.Tuple) {
            throw new org.python.exceptions.TypeError("can't multiply sequence by non-int of type 'NoneType'");
        } else if(other instanceof org.python.types.Dict) {
            throw new org.python.exceptions.TypeError("unsupported operand type(s) for *: 'NoneType' and 'dict'");
        }

        throw new Error();
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.Object __getitem__(org.python.Object other) {
        throw new org.python.exceptions.TypeError("'NoneType' object is not subscriptable");
    }

    public java.lang.Object toJava() {
        return null;
    }

    @org.python.Method(
        __doc__ = ""
    )
    public org.python.types.Str __repr__() {
        return new org.python.types.Str("None");
    }

    public boolean __setattr_null(java.lang.String name, org.python.Object value) {
        return false;
    }
}