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
            __doc__ = "Dictionary that remembers insertion order'\n" +
                      "An inherited dict maps keys to values.\n" +
                      "The inherited dict provides __getitem__, __len__, __contains__, and get.\n" +
                      "The remaining methods are order-aware.\n" +
                      "Big-O running times for all methods are the same as regular dictionaries.\n" +
                      "\n" +
                      "The internal self.__map dict maps keys to links in a doubly linked list.\n" +
                      "The circular doubly linked list starts and ends with a sentinel element.\n" +
                      "The sentinel element never gets deleted (this simplifies the algorithm).\n" +
                      "The sentinel is in self.__hardroot with a weakref proxy in self.__root.\n" +
                      "The prev links are weakref proxies (to prevent circular references).\n" +
                      "Individual links are kept alive by the hard reference in self.__map.\n" +
                      "Those hard references disappear when a key is deleted from an OrderedDict.",
            varargs = "args",
            kwargs = "kwargs"
    )
    public static org.python.Object OrderedDict(org.python.types.Tuple args, org.python.types.Dict kwargs) {
        throw new org.python.exceptions.NotImplementedError("OrderedDict has not been implemented");
    }

    @org.python.Method(
            __doc__= "Returns a new subclass of tuple with named fields.\n" +
                     "\n",
            args = {"typename", "field_names"}
    )
    public static org.python.Object namedtuple(org.python.Object typename, org.python.Object field_names) {
        throw new org.python.exceptions.NotImplementedError("namedtuple has not been implemented");
    }

    @org.python.Method(
            __doc__= "Dict subclass for counting hashable items.  Sometimes called a bag\n" +
                     "or multiset.  Elements are stored as dictionary keys and their counts\n" +
                     "are stored as dictionary values.\n" +
                     "\n" +
                     "# References:\n" +
                     "#   http://en.wikipedia.org/wiki/Multiset\n" +
                     "#   http://www.gnu.org/software/smalltalk/manual-base/html_node/Bag.html\n" +
                     "#   http://www.demo2s.com/Tutorial/Cpp/0380__set-multiset/Catalog0380__set-multiset.htm\n" +
                     "#   http://code.activestate.com/recipes/259174/\n" +
                     "#   Knuth, TAOCP Vol. II section 4.6.3",
            varargs = "args",
            kwargs = "kwargs"
    )
    public static org.python.Object Counter(org.python.types.Tuple args, org.python.types.Dict kwargs) {
        throw new org.python.exceptions.NotImplementedError("Counter has not been implemented");
    }

    @org.python.Method(
            __doc__= "A ChainMap groups multiple dicts (or other mappings) together\n" +
                     "to create a single, updateable view.\n" +
                     "\n" +
                     "The underlying mappings are stored in a list.  That list is public and can\n" +
                     "be accessed or updated using the *maps* attribute.  There is no other\n" +
                     "state.\n" +
                     "\n" +
                     "Lookups search the underlying mappings successively until a key is found.\n" +
                     "In contrast, writes, updates, and deletions only operate on the first\n" +
                     "mapping.",
            varargs = "maps"
    )
    public static org.python.Object ChainMap(org.python.types.Tuple maps) {
        throw new org.python.exceptions.NotImplementedError("ChainMap has not been implemented");
    }

    @org.python.Method(
        __doc__= "",
        varargs = "args",
        kwargs = "kwargs"
    )
    public static org.python.Object UserDict(org.python.types.Tuple args, org.python.types.Dict kwargs) {
        throw new org.python.exceptions.NotImplementedError("UserDict has not been implemented");
    }

    @org.python.Method(
        __doc__= "",
        default_args = {"initlist"}
    )
    public static org.python.Object UserList(org.python.Object initlist) {
        if (initlist == null) {
            initlist = org.python.types.NoneType.NONE;
        }
        throw new org.python.exceptions.NotImplementedError("UserList has not been implemented");
    }

    @org.python.Method(
        __doc__= "",
        args = {"seq"}
    )
    public static org.python.Object UserString(org.python.Object seq) {
        throw new org.python.exceptions.NotImplementedError("UserString has not been implemented");
    }

    @org.python.Method(
        __doc__= "",
        varargs = "args",
        kwargs = "kwargs"
    )
    public static org.python.Object defaultdict(org.python.types.Tuple args, org.python.types.Dict kwargs) {
        org.python.Object default_factory = org.python.types.NoneType.NONE;
        if (!args.value.isEmpty()) {
            default_factory = args.value.get(0);
            args.value = new java.util.ArrayList<>(args.value); // convert Arrays$ArrayList to ArrayList to call `remove`
            args.value.remove(0);
        }

        // convert parameter types
        org.python.Object[] _args = new org.python.Object[1];
        if (!args.value.isEmpty()) {
            _args = args.value.toArray(new org.python.Object[args.value.size()]);
        }

        java.util.Map<String, org.python.Object> _kwargs = new java.util.HashMap<>();
        if (!kwargs.value.isEmpty()) {
            for (java.util.Map.Entry<org.python.Object, org.python.Object> entry : kwargs.value.entrySet()) {
                org.python.Object key = entry.getKey();
                _kwargs.put(((org.python.types.Str) key).value, kwargs.value.get(key));
            }
        }

        return new org.python.stdlib.collections.DefaultDict(default_factory, _args, _kwargs);
    }

    @org.python.Method(
        __doc__= "",
        default_args = {"iterable", "maxlen"}
    )
    public static org.python.Object deque(org.python.Object iterable, org.python.Object maxlen) {
        if (iterable == null) {
            iterable = org.python.types.NoneType.NONE;
        }
        if (maxlen == null) {
            maxlen = org.python.types.NoneType.NONE;
        }
        throw new org.python.exceptions.NotImplementedError("deque has not been implemented");
    }

}
