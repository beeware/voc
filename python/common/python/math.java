package python;

import java.lang.Math;

@org.python.Module(
        __doc__ = "Math-things"
    )

public class math extends org.python.types.Module {

    @org.python.Method(
            __doc__ = "Returns the smallest integer larger than or equal to 'value'.",
            args = {"value"}
    )
    public static org.python.types.Object ceil(org.python.types.Object value) {
        int val = 0; 
        if(value instanceof org.python.types.Float) {
            val = (int) Math.ceil(((org.python.types.Float) value).value);
        }
        return org.python.types.Int.getInt(val);
    }

    @org.python.Method(
            __doc__ = "Returns the largest integer smaller than or equal to 'value'.",
            args = {"value"}
    )
    public static org.python.types.Object floor(org.python.types.Object value) {
        int val = 0; 
        if(value instanceof org.python.types.Float) {
            val = (int) Math.floor(((org.python.types.Float) value).value);
        }
        return org.python.types.Int.getInt(val);
    }
    
    @org.python.Method(
            __doc__ = "Returns the square-root of 'value'",
            args = {"value"}
    )
    public static org.python.types.Object sqrt(org.python.types.Object value) {
        double val = 0; 
        if(value instanceof org.python.types.Float) {
            val = Math.sqrt(((org.python.types.Float) value).value);
        } else if(value instanceof org.python.types.Int) {
            val = Math.sqrt((double)((org.python.types.Int) value).value);
        }
        return new org.python.types.Float(val);
    }
}