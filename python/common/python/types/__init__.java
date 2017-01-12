package python.types;


@org.python.Module(
    __doc__ = "\nDefine names for built-in types that aren't directly accessible as a builtin.\n"
)
public class __init__ extends org.python.types.Module {
    static {
        // BuiltinFunctionType = org.python.types.Type.pythonType(org.python.types.BuiltinFunction.class);
        // BuiltinMethodType = org.python.types.Type.pythonType(org.python.types.BuiltinMethod.class);
        CodeType = org.python.types.Type.pythonType(org.python.types.Code.class);
        // DynamicClassAttribute = org.python.types.Type.pythonType(org.python.types.DynamicClassAttri.class);
        // FrameType = org.python.types.Type.pythonType(org.python.types.Frame.class);
        FunctionType = org.python.types.Type.pythonType(org.python.types.Function.class);
        GeneratorType = org.python.types.Type.pythonType(org.python.types.Generator.class);
        // GetSetDescriptorType = org.python.types.Type.pythonType(org.python.types.GetSetDescriptor.class);
        // LambdaType = org.python.types.Type.pythonType(org.python.types.Lambda.class);
        // MappingProxyType = org.python.types.Type.pythonType(org.python.types.MappingProxy.class);
        // MemberDescriptorType = org.python.types.Type.pythonType(org.python.types.MemberDescriptor.class);
        MethodType = org.python.types.Type.pythonType(org.python.types.Method.class);
        ModuleType = org.python.types.Type.pythonType(org.python.types.Module.class);
        // SimpleNamespace = org.python.types.Type.pythonType(org.python.types.SimpleNames.class);
        // TracebackType = org.python.types.Type.pythonType(org.python.types.Traceback.class);
    }

    private static long vm_start_time;

    // public static org.python.Object BuiltinFunctionType;
    // public static org.python.Object BuiltinMethodType;
    public static org.python.Object CodeType;
    // public static org.python.Object DynamicClassAttribute;
    // public static org.python.Object FrameType;
    public static org.python.Object FunctionType;
    public static org.python.Object GeneratorType;
    // public static org.python.Object GetSetDescriptorType;
    // public static org.python.Object LambdaType;
    // public static org.python.Object MappingProxyType;
    // public static org.python.Object MemberDescriptorType;
    public static org.python.Object MethodType;
    public static org.python.Object ModuleType;
    // public static org.python.Object SimpleNamespace;
    // public static org.python.Object TracebackType;
    // public static org.python.Object __builtins__;
    public static org.python.Object __cached__;

    @org.python.Attribute
    public static org.python.Object __file__ = new org.python.types.Str("python/common/python/types/__init__.java");

    @org.python.Attribute
    public static org.python.Object __loader__ = org.python.types.NoneType.NONE;  // TODO

    @org.python.Attribute
    public static org.python.Object __name__ = new org.python.types.Str("types");

    @org.python.Attribute
    public static org.python.Object __package__ = new org.python.types.Str("");

    @org.python.Attribute
    public static org.python.Object __spec__ = org.python.types.NoneType.NONE;  // TODO

    @org.python.Method(
        __doc__ = ""
    )
    public static org.python.Object _calculate_meta() {
        throw new org.python.exceptions.NotImplementedError("types._calculate_meta() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public static org.python.Object new_class() {
        throw new org.python.exceptions.NotImplementedError("types.new_class() has not been implemented.");
    }

    @org.python.Method(
        __doc__ = ""
    )
    public static org.python.Object prepare_class() {
        throw new org.python.exceptions.NotImplementedError("types.prepare_class() has not been implemented.");
    }

}