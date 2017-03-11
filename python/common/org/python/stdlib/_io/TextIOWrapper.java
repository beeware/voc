package org.python.stdlib._io;

public class TextIOWrapper extends org.python.types.Object {
    public org.python.Object __VOC__;
    java.io.InputStream input;
    java.io.OutputStream output;

    public TextIOWrapper(java.io.InputStream istream) {
        super(org.python.types.Type.Origin.BUILTIN, null);
        this.input = istream;
    }

    public TextIOWrapper(java.io.OutputStream ostream) {
        super(org.python.types.Type.Origin.BUILTIN, null);
        this.output = ostream;
    }

    // @org.python.Method(
    //     __doc__ = "Create and return a new object.  See help(type) for accurate signature."
    // )
    // public org.python.Object __new__(org.python.Object klass) {
    //     org.python.types.Type cls = (org.python.types.Type) super.__new__(klass);
    //     System.out.println("__NEW__ TextIOWrapper");
    //     return cls;
    // }

    // '_CHUNK_SIZE',
    // '__class__',
    // '__del__',
    // '__delattr__',
    // '__dict__',
    // '__dir__',
    // '__doc__',
    // '__enter__',
    // '__eq__',
    // '__exit__',
    // '__format__',
    // '__ge__',
    // '__getattribute__',
    // '__getstate__',
    // '__gt__',
    // '__hash__',
    // '__init__',
    // '__iter__',
    // '__le__',
    // '__lt__',
    // '__ne__',
    // '__new__',
    // '__next__',
    // '__reduce__',
    // '__reduce_ex__',
    // '__repr__',
    // '__setattr__',
    // '__sizeof__',
    // '__str__',
    // '__subclasshook__',
    // '_checkClosed',
    // '_checkReadable',
    // '_checkSeekable',
    // '_checkWritable',
    // '_finalizing',
    // 'buffer',
    // 'close',
    // 'closed',
    // 'detach',
    // 'encoding',
    // 'errors',
    // 'fileno',

    @org.python.Method(
            __doc__ = ""
    )
    public org.python.Object flush() {
        try {
            output.flush();
        } catch (java.io.IOException e) {
            throw new org.python.exceptions.RuntimeError("Unable to flush output: " + e.toString());
        }
        return org.python.types.NoneType.NONE;
    }

    // 'isatty',
    // 'line_buffering',
    // 'name',
    // 'newlines',
    // 'read',
    // 'readable',
    // 'readline',
    // 'readlines',
    // 'seek',
    // 'seekable',
    // 'tell',
    // 'truncate',
    // 'writable',

    @org.python.Method(
            __doc__ = "",
            args = {"content"}
    )
    public org.python.Object write(org.python.Object content) {
        try {
            output.write(content.toString().getBytes("UTF-8"));
        } catch (java.io.IOException e) {
            throw new org.python.exceptions.RuntimeError("Unable to write output: " + e.toString());
        }
        return org.python.types.NoneType.NONE;
    }

    // 'writelines'
};
