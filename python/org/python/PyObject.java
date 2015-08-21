package org.python;

import java.lang.reflect.Type;
import java.util.Hashtable;
import java.util.Set;
import java.util.Map;
import java.util.ArrayList;

public class PyObject {
    public static Hashtable<String, PyObject> globals;

    // public static Hashtable<String, PyObject> locals;

    public Type type;
    public Object value;

    static {
        globals = new Hashtable<String, PyObject>();
        // locals = new Hashtable<String, PyObject>();
    }

    /**
     * Copy Constructor
     */
    public PyObject(Object v, Type t) {
        value = v;
        type = t;
    }

    public PyObject() {
        type = Object.class;
        value = new Hashtable<String, PyObject>();
    }

    public PyObject(byte v) {
        type = Integer.class;
        value = (long)v;
    }

    public PyObject(short v) {
        type = Integer.class;
        value = (long)v;
    }

    public PyObject(int v) {
        type = Integer.class;
        value = (long)v;
    }

    public PyObject(long v) {
        type = Integer.class;
        value = v;
    }

    public PyObject(float v) {
        type = Float.class;
        value = (double)v;
    }

    public PyObject(double v) {
        type = Float.class;
        value = v;
    }

    public PyObject(char v) {
        type = String.class;
        value = Character.toString(v);
    }

    public PyObject(String v) {
        type = String.class;
        value = v;
    }

    public PyObject(Map v) {
        type = Map.class;
        value = v;
    }

    public PyObject(Set v) {
        type = Set.class;
        value = v;
    }

    public PyObject(ArrayList v) {
        type = ArrayList.class;
        value = v;
    }

    /**
     * Proxy Java object methods onto their Python counterparts.
     */

    public boolean equals(PyObject other) {
        return __equals__(other);
    }

    public int compareTo(PyObject other) {
        if (__lt__(other)) {
            return -1;
        } else if (__gt__(other)) {
            return 1;
        }
        return 0;
    }

    public String toString() {
        return __str__();
    }

    /**
     * Python interface compatibility
     */

    public void __setattr__(String attr, PyObject v) {
        // value.put(attr, v);
    }

    public PyObject __getattr__(String attr) {
        // return value.get(attr);
        return null;
    }

    public String __repr__() {
        return "<PyObject>";
    }

    public String __str__() {
        return __repr__();
    }

    public boolean __equals__(PyObject other) {
        return false;
    }

    public boolean __hash__(PyObject other) {
        return false;
    }

    public boolean __lt__(PyObject other) {
        return false;
    }

    public boolean __lte__(PyObject other) {
        return false;
    }

    public boolean __gt__(PyObject other) {
        return false;
    }

    public boolean __gte__(PyObject other) {
        return false;
    }

    public PyObject add(PyObject other) {
        return null;
    }

    public PyObject subtract(PyObject other) {
        return null;
    }

    public PyObject multiply(PyObject other) {
        return null;
    }

    public PyObject floordivide(PyObject other) {
        return null;
    }

    public PyObject truedivide(PyObject other) {
        return null;
    }

    public PyObject modulo(PyObject other) {
        return null;
    }

    public PyObject power(PyObject other) {
        return null;
    }

    public PyObject lshift(PyObject other) {
        return null;
    }

    public PyObject rshift(PyObject other) {
        return null;
    }

    public PyObject and(PyObject other) {
        return null;
    }

    public PyObject xor(PyObject other) {
        return null;
    }

    public PyObject or(PyObject other) {
        return null;
    }

    public void inplace_add(PyObject other) {
        this.value = this.add(other).value;
    }

    public void inplace_subtract(PyObject other) {
        this.value = this.subtract(other).value;
    }

    public void inplace_multiply(PyObject other) {
        this.value = this.multiply(other).value;
    }

    public void inplace_floordivide(PyObject other) {
        this.value = this.floordivide(other).value;
    }

    public void inplace_truedivide(PyObject other) {
        this.value = this.truedivide(other).value;
    }

    public void inplace_modulo(PyObject other) {
        this.value = this.modulo(other).value;
    }

    public void inplace_power(PyObject other) {
        this.value = this.power(other).value;
    }

    public void inplace_lshift(PyObject other) {
        this.value = this.lshift(other).value;
    }

    public void inplace_rshift(PyObject other) {
        this.value = this.rshift(other).value;
    }

    public void inplace_and(PyObject other) {
        this.value = this.and(other).value;
    }

    public void inplace_xor(PyObject other) {
        this.value = this.xor(other).value;
    }

    public void inplace_or(PyObject other) {
        this.value = this.or(other).value;
    }

    public void __setitem__(PyObject k, PyObject v) {
    }

    public PyObject __getitem__(PyObject k) {
        return null;
    }

    public void delete_subscr(PyObject k) {
    }

}
