package org;

import java.util.Hashtable;

import org.python.PyObject;
import org.python.exceptions.NotImplementedError;
import org.python.exceptions.TypeError;


public class Python {
    public static Hashtable<String, PyObject> globals;

    static {
        globals = new Hashtable<String, PyObject>();
    }

    public static void __import__() {
        throw new NotImplementedError("Builtin function '__import__' not implemented");
    }

    public static void abs() {
        throw new NotImplementedError("Builtin function 'abs' not implemented");
    }

    public static void all() {
        throw new NotImplementedError("Builtin function 'all' not implemented");
    }

    public static void any() {
        throw new NotImplementedError("Builtin function 'any' not implemented");
    }

    public static void ascii() {
        throw new NotImplementedError("Builtin function 'ascii' not implemented");
    }

    public static void bin() {
        throw new NotImplementedError("Builtin function 'bin' not implemented");
    }

    public static void bool() {
        throw new NotImplementedError("Builtin function 'bool' not implemented");
    }

    public static void bytearray() {
        throw new NotImplementedError("Builtin function 'bytearray' not implemented");
    }

    public static void bytes() {
        throw new NotImplementedError("Builtin function 'bytes' not implemented");
    }

    public static void callable() {
        throw new NotImplementedError("Builtin function 'callable' not implemented");
    }

    public static void chr() {
        throw new NotImplementedError("Builtin function 'callable' not implemented");
    }

    public static void classmethod() {
        throw new NotImplementedError("Builtin function 'classmethod' not implemented");
    }

    public static void compile() {
        throw new NotImplementedError("Builtin function 'compile' not implemented");
    }

    public static void complex() {
        throw new NotImplementedError("Builtin function 'complex' not implemented");
    }

    public static void copyright() {
        throw new NotImplementedError("Builtin function 'copyright' not implemented");
    }

    public static void credits() {
        throw new NotImplementedError("Builtin function 'credits' not implemented");
    }

    public static void delattr() {
        throw new NotImplementedError("Builtin function 'delattr' not implemented");
    }

    public static void dict() {
        throw new NotImplementedError("Builtin function 'dict' not implemented");
    }

    public static void dir() {
        throw new NotImplementedError("Builtin function 'dir' not implemented");
    }

    public static void divmod() {
        throw new NotImplementedError("Builtin function 'divmod' not implemented");
    }

    public static void dreload() {
        throw new NotImplementedError("Builtin function 'dreload' not implemented");
    }

    public static void enumerate() {
        throw new NotImplementedError("Builtin function 'enumerate' not implemented");
    }

    public static void eval() {
        throw new NotImplementedError("Builtin function 'eval' not implemented");
    }

    public static void exec() {
        throw new NotImplementedError("Builtin function 'exec' not implemented");
    }

    public static void filter() {
        throw new NotImplementedError("Builtin function 'filter' not implemented");
    }

    public static PyObject float_cast(PyObject obj) {
        return new PyObject((float) obj.value);
    }

    public static void format() {
        throw new NotImplementedError("Builtin function 'format' not implemented");
    }

    public static void frozenset() {
        throw new NotImplementedError("Builtin function 'frozenset' not implemented");
    }

    public static void getattr() {
        throw new NotImplementedError("Builtin function 'getattr' not implemented");
    }

    public static PyObject globals() {
        return new PyObject(Python.globals);
    }

    public static void hasattr() {
        throw new NotImplementedError("Builtin function 'hasattr' not implemented");
    }

    public static PyObject hash(PyObject obj) {
        return new PyObject(obj.hashCode());
    }

    public static void help() {
        throw new NotImplementedError("Builtin function 'help' not implemented");
    }

    public static PyObject hex(PyObject obj) {
        return new PyObject(String.format("0x%x", obj.value));
    }

    public static void id() {
        throw new NotImplementedError("Builtin function 'id' not implemented");
    }

    public static void input() {
        throw new NotImplementedError("Builtin function 'input' not implemented");
    }

    public static PyObject int_cast(PyObject obj) {
        return new PyObject((int) obj.value);
    }

    public static void intern() {
        throw new NotImplementedError("Builtin function 'intern' not implemented");
    }

    public static void isinstance() {
        throw new NotImplementedError("Builtin function 'isinstance' not implemented");
    }

    public static void issubclass() {
        throw new NotImplementedError("Builtin function 'issubclass' not implemented");
    }

    public static void iter() {
        throw new NotImplementedError("Builtin function 'iter' not implemented");
    }

    public static void len() {
        throw new NotImplementedError("Builtin function 'input' not implemented");
    }

    public static void license() {
        throw new NotImplementedError("Builtin function 'license' not implemented");
    }

    public static void list() {
        throw new NotImplementedError("Builtin function 'list' not implemented");
    }

    public static void locals() {
        throw new NotImplementedError("Builtin function 'locals' not implemented");
    }

    public static void map() {
        throw new NotImplementedError("Builtin function 'input' not implemented");
    }

    public static void max() {
        throw new NotImplementedError("Builtin function 'max' not implemented");
    }

    public static void memoryview() {
        throw new NotImplementedError("Builtin function 'memoryview' not implemented");
    }

    public static void min() {
        throw new NotImplementedError("Builtin function 'min' not implemented");
    }

    public static void next() {
        throw new NotImplementedError("Builtin function 'next' not implemented");
    }

    public static void object() {
        throw new NotImplementedError("Builtin function 'object' not implemented");
    }

    public static PyObject oct(PyObject obj) {
        return new PyObject(String.format("0o%o", obj.value));
    }

    public static void open() {
        throw new NotImplementedError("Builtin function 'open' not implemented");
    }

    public static PyObject ord(PyObject obj) {
        if (obj.type == String.class) {
            int length = ((String) obj.value).length();
            if (length != 1) {
                return new PyObject((int) ((String) obj.value).charAt(0));
            } else {
                throw new TypeError("ord() expected string of length 1, but string of length " + length + " found");
            }
        } else {
            throw new TypeError("ord() expected string of length 1, but " + obj.type + " found");
        }
    }

    public static PyObject pow(PyObject x, PyObject y) {
        return x.__pow__(y);
    }

    public static void print(PyObject... args) {
        StringBuilder buffer = new StringBuilder();
        for (int i = 0; i < args.length; i++) {
            buffer.append(args[i]);
            if (i != args.length - 1) {
                buffer.append(" ");
            }
        }
        System.out.println(buffer.toString());
    }

    public static void property() {
        throw new NotImplementedError("Builtin function 'property' not implemented");
    }

    public static void range() {
        throw new NotImplementedError("Builtin function 'range' not implemented");
    }

    public static void repr() {
        throw new NotImplementedError("Builtin function 'repr' not implemented");
    }

    public static void reversed() {
        throw new NotImplementedError("Builtin function 'reversed' not implemented");
    }

    public static void round() {
        throw new NotImplementedError("Builtin function 'round' not implemented");
    }

    public static void set() {
        throw new NotImplementedError("Builtin function 'set' not implemented");
    }

    public static void setattr() {
        throw new NotImplementedError("Builtin function 'setattr' not implemented");
    }

    public static void slice() {
        throw new NotImplementedError("Builtin function 'input' not implemented");
    }

    public static void sorted() {
        throw new NotImplementedError("Builtin function 'sorted' not implemented");
    }

    public static void staticmethod() {
        throw new NotImplementedError("Builtin function 'staticmethod' not implemented");
    }

    public static PyObject str(PyObject obj) {
        return new PyObject((String) obj.value);
    }

    public static PyObject sum(PyObject iterable, int start) {
        throw new NotImplementedError("Builtin function 'sum' not implemented");
    }

    public static PyObject sum(PyObject iterable, PyObject start) {
        return sum(iterable, (int) start.value);
    }

    public static PyObject sum(PyObject iterable) {
        return sum(iterable, 0);
    }

    public static void super_call() {
        throw new NotImplementedError("Builtin function 'super' not implemented");
    }

    public static void tuple() {
        throw new NotImplementedError("Builtin function 'tuple' not implemented");
    }

    public static void type() {
        throw new NotImplementedError("Builtin function 'type' not implemented");
    }

    public static void vars() {
        throw new NotImplementedError("Builtin function 'vars' not implemented");
    }

    public static void zip() {
        throw new NotImplementedError("Builtin function 'zip' not implemented");
    }
}
