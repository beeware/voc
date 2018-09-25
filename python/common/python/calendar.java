package python;
import java.lang.Math;

@org.python.Module(
        __doc__ = ""
)
public class calendar extends org.python.types.Module {

    @org.python.Method(
            __doc__ = "",
            args = {"x", "y"}
    )
    public static org.python.Object leapdays(org.python.Object x, org.python.Object y) {
		if(x instanceof org.python.types.Str || y instanceof org.python.types.Str){
			throw new org.python.exceptions.TypeError(
				"unsupported operand type(s) for -=: 'str' and 'int'");
		}

		long x_ = ((org.python.types.Int) x.__int__()).value-1;
		long y_ = ((org.python.types.Int) y.__int__()).value-1;
		
		org.python.types.Int result = org.python.types.Int.getInt((Math.floorDiv(y_, org.python.types.Int.getInt(4).value) - 
				Math.floorDiv(x_, org.python.types.Int.getInt(4).value)) -
				(Math.floorDiv(y_, org.python.types.Int.getInt(100).value) - 
				Math.floorDiv(x_, org.python.types.Int.getInt(100).value)) +
				(Math.floorDiv(y_, org.python.types.Int.getInt(400).value) - 
				Math.floorDiv(x_, org.python.types.Int.getInt(400).value)));
		
		if(x instanceof org.python.types.Float || y instanceof org.python.types.Float){
			return ((org.python.types.Float) result.__float__());
		}
		else{
			return result;
		}
        
   }
}
