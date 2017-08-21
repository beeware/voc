package python;

@org.python.Module(
        __doc__ =
                "The io module provides the Python interfaces to stream handling. The\n" +
                        "builtin open function is defined in this module.\n" +
                        "\n" +
                        "At the top of the I/O hierarchy is the abstract base class IOBase. It\n" +
                        "defines the basic interface to a stream. Note, however, that there is no\n" +
                        "separation between reading and writing to streams; implementations are\n" +
                        "allowed to raise an IOError if they do not support a given operation.\n" +
                        "\n" +
                        "Extending IOBase is RawIOBase which deals simply with the reading and\n" +
                        "writing of raw bytes to a stream. FileIO subclasses RawIOBase to provide\n" +
                        "an interface to OS files.\n" +
                        "\n" +
                        "BufferedIOBase deals with buffering on a raw byte stream (RawIOBase). Its\n" +
                        "subclasses, BufferedWriter, BufferedReader, and BufferedRWPair buffer\n" +
                        "streams that are readable, writable, and both respectively.\n" +
                        "BufferedRandom provides a buffered interface to random access\n" +
                        "streams. BytesIO is a simple stream of in-memory bytes.\n" +
                        "\n" +
                        "Another IOBase subclass, TextIOBase, deals with the encoding and decoding\n" +
                        "of streams into text. TextIOWrapper, which extends it, is a buffered text\n" +
                        "interface to a buffered raw stream (`BufferedIOBase`). Finally, StringIO\n" +
                        "is a in-memory stream for text.\n" +
                        "\n" +
                        "Argument names are not part of the specification, and only the arguments\n" +
                        "of open() are intended to be used as keyword arguments.\n" +
                        "\n" +
                        "data:\n" +
                        "\n" +
                        "DEFAULT_BUFFER_SIZE\n" +
                        "\n" +
                        "   An int containing the default buffer size used by the module's buffered\n" +
                        "   I/O classes. open() uses the file's blksize (as obtained by os.stat) if\n" +
                        "   possible.\n" +
                        "\n" +
                        "\n"
)
public class _io extends org.python.types.Module {
    @org.python.Method(
            __doc__ = "Create and return a new object.  See help(type) for accurate signature."
    )
    public org.python.Object __new__(org.python.Object klass) {
        org.python.types.Type cls = (org.python.types.Type) super.__new__(klass);
        return cls;
    }

    //'BlockingIOError',
    //'BufferedRWPair',
    //'BufferedRandom',
    //'BufferedReader',
    //'BufferedWriter',
    //'BytesIO',
    //'DEFAULT_BUFFER_SIZE',
    //'FileIO',
    //'IncrementalNewlineDecoder',
    //'StringIO',
    //'TextIOWrapper',
    //'UnsupportedOperation',
    //'_BufferedIOBase',
    //'_IOBase',
    //'_RawIOBase',
    //'_TextIOBase',
    @org.python.Attribute
    public static org.python.Object __loader__ = org.python.types.NoneType.NONE;  // TODO
    @org.python.Attribute
    public static org.python.Object __name__ = new org.python.types.Str("_io");
    @org.python.Attribute()
    public static org.python.Object __file__ = new org.python.types.Str("python/common/python/_io.java");
    @org.python.Attribute
    public static org.python.Object __package__ = new org.python.types.Str("");
    @org.python.Attribute
    public static org.python.Object __spec__ = org.python.types.NoneType.NONE;  // TODO

    //'open']
};
