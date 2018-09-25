package python;
import java.util.ArrayList;
import java.util.List;

@org.python.Module(
        __doc__ = ""
)
public class re extends org.python.types.Module {

    @org.python.Method(
            __doc__ = "",
            args = {"pattern"}
    )
    public static String escape(org.python.Object pattern) {
		String inputStr = String.valueOf(pattern);
		ArrayList<Character> retStr = new ArrayList<Character>();
		
		for(char c: inputStr.toCharArray()) {
			if(!(Character.isLetter(c) || Character.isDigit(c))){
				retStr.add('\\');
			}
			retStr.add(c);
		}

		StringBuilder builder = new StringBuilder(retStr.size());
		for(Character ch: retStr){
			builder.append(ch);
		}

		//return builder.toString();
		return "bblaala";
    }

}
