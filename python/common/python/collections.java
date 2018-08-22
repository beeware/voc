package python;

@org.python.Module(
        __doc__ =
            "This module implements specialized container datatypes providing\n" +
            "alternatives to Python's general purpose built-in containers, dict,\n" +
            "list, set, and tuple.\n" +
                "\n" +
                "* namedtuple   factory function for creating tuple subclasses with named fields\n" +
                "* deque        list-like container with fast appends and pops on either end\n" +
                "* ChainMap     dict-like class for creating a single view of multiple mappings\n" +
                "* Counter      dict subclass for counting hashable objects\n" +
                "* OrderedDict  dict subclass that remembers the order entries were added\n" +
                "* defaultdict  dict subclass that calls a factory function to supply missing values\n" +
                "* UserDict     wrapper around dictionary objects for easier dict subclassing\n" +
                "* UserList     wrapper around list objects for easier list subclassing\n" +
                "* UserString   wrapper around string objects for easier string subclassing\n" +
                "\n"
)
public class collections extends org.python.types.Module {
    public collections() {
        super();
    }

    static {
        OrderedDict = org.python.types.Type.pythonType(org.python.stdlib.collections.OrderedDict.class);
        // Counter = org.python.types.Type.pythonTypeorg.python.stdlib.collections.Counter.class);
        // ChainMap = org.python.types.Type.pythonTypeorg.python.stdlib.collections.ChainMap.class);
        // UserDict = org.python.types.Type.pythonTypeorg.python.stdlib.collections.UserDict.class);
        // UserList = org.python.types.Type.pythonTypeorg.python.stdlib.collections.UserList.class);
        // UserString = org.python.types.Type.pythonTypeorg.python.stdlib.collections.UserString.class);
        defaultdict = org.python.types.Type.pythonType(org.python.stdlib.collections.DefaultDict.class);
        // deque = org.python.stdlib.collections.Deque.class;
    }

    @org.python.Attribute
    public static org.python.Object OrderedDict;
    // @org.python.Attribute
    // public static org.python.Object Counter;
    // @org.python.Attribute
    // public static org.python.Object ChainMap;
    // @org.python.Attribute
    // public static org.python.Object UserDict;
    // @org.python.Attribute
    // public static org.python.Object UserList;
    // @org.python.Attribute
    // public static org.python.Object UserString;
    @org.python.Attribute
    public static org.python.Object defaultdict;
    // @org.python.Attribute
    // public static org.python.Object deque;

    @org.python.Attribute()
    public static org.python.Object __file__ = new org.python.types.Str("python/common/python/collections.java");
    @org.python.Attribute
    public static org.python.Object __loader__ = org.python.types.NoneType.NONE;  // TODO
    @org.python.Attribute
    public static org.python.Object __name__ = new org.python.types.Str("collections");
    @org.python.Attribute
    public static org.python.Object __package__ = new org.python.types.Str("collections");
    @org.python.Attribute()
    public static org.python.Object __path__;
    @org.python.Attribute
    public static org.python.Object __spec__ = org.python.types.NoneType.NONE;  // TODO
    @org.python.Attribute()
    public static org.python.Object _bootstrap;
    @org.python.Attribute()
    public static org.python.Object _imp;

    @org.python.Method(
            __doc__ = "Returns a new subclass of tuple with named fields.\n" +
                "\n",
            args = {"typename", "field_names"}
    )
    public static org.python.Object namedtuple(org.python.Object typename, org.python.Object field_names) {
        throw new org.python.exceptions.NotImplementedError("namedtuple has not been implemented");
    }
}
