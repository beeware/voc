package python;

@org.python.Module(
        __doc__ =
                "math"
)
public class math extends org.python.types.Module {
    public math() {
        super();
    }

    @org.python.Attribute
    public static org.python.Object __file__ = new org.python.types.Str("python/common/python/math.java");
    @org.python.Attribute
    public static org.python.Object __loader__ = org.python.types.NoneType.NONE;  // TODO
    @org.python.Attribute
    public static org.python.Object __name__ = new org.python.types.Str("math");
    @org.python.Attribute
    public static org.python.Object __package__ = new org.python.types.Str("");
    @org.python.Attribute
    public static org.python.Object __spec__ = org.python.types.NoneType.NONE;  // TODO

    @org.python.Method(
            __doc__ = "",
            args = {"number"}
    )
    public static org.python.Object sqrt(org.python.Object number) {
        double d = ((org.python.types.Float) number.__float__()).value;

        if (d < 0) throw new org.python.exceptions.ValueError("math domain error");

        return new org.python.types.Float(Math.sqrt(d));
    }

}
