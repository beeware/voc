package org.python.stdlib.datetime;
import java.text.ParseException;
import java.text.DateFormatSymbols;
import java.util.Locale;
import java.text.SimpleDateFormat;
import org.python.types.Int;
import org.python.types.Str;
import org.python.types.Bool;
import org.python.types.List;
import org.python.types.NoneType;
import org.python.types.Object;
import java.util.Calendar;
import java.util.ArrayList;

public class Date extends org.python.types.Object {

    @org.python.Attribute
    public Int year;

    @org.python.Attribute
    public Int month;

    @org.python.Attribute
    public Int day;

    @org.python.Attribute
    public static final Date min = new Date(Int.getInt(1), Int.getInt(1), Int.getInt(1));

    @org.python.Attribute
    public static final Date max = new Date(Int.getInt(9999), Int.getInt(12), Int.getInt(31));

    @org.python.Method(
        __doc__ = "Date(args, kwargs) -> date" +
        "\n" +
        "Returns a Date object.\n",
        default_args = { "year", "month", "day" }
    )
    public Date(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super();

        if (args[0].toJava() == null || args[1].toJava() == null || args[2].toJava() == null)
            throw new org.python.exceptions.TypeError("an integer is required (got type NoneType)");

        this.year = Int.getInt(1);
        this.month = Int.getInt(1);
        this.day = Int.getInt(1);

        if (args[0] != null)
            this.year = (Int) args[0];
        if (args[1] != null)
            this.month = (Int) args[1];
        if (args[2] != null)
            this.day = (Int) args[2];

        if (this.year.value < 1 || this.year.value > 9999)
            throw new org.python.exceptions.ValueError("year " + this.year + " is out of range");
        if (this.month.value < 1 || this.month.value > 12)
            throw new org.python.exceptions.ValueError("month must be in 1..12");
        if (this.day.value < 1 || this.day.value > 31)
            throw new org.python.exceptions.ValueError("day is out of range for month");

        //TODO hantera dagar i udda/jämna månader, skottår

    }

    @org.python.Method(
        __doc__ = "Date(year, month, day) -> date",
        default_args = { "year", "month", "day" }
    )
    public Date(Int year, Int month, Int day) {
        super();
        this.year = year;
        this.month = month;
        this.day = day;
    }

    @org.python.Method(__doc__ = "ctime() -> time string")
    public Str ctime() {
        Str retStr = new Str();
        try {
            String month= (new DateFormatSymbols().getMonths()[(int)this.month.value-1]).substring(0,3);
            String dateString = String.format("%d-%d-%d", (int)this.year.value, (int)this.month.value, (int)this.day.value);
            java.util.Date date = new SimpleDateFormat("yyyy-M-d").parse(dateString);
            String dayOfWeek = (new SimpleDateFormat("EEEE", Locale.ENGLISH).format(date)).substring(0,3);
            retStr =  new Str(dayOfWeek + " " + month + " " +this.day.toJava()+ " " + "00:00:00" + " " + this.year.toJava());
        } catch (ParseException e) {
            e.printStackTrace();
        }
        return retStr;
    }

    @org.python.Method(__doc__ = "replace() -> object")
    public org.python.types.Object replace(org.python.Object[] args,
            java.util.Map<java.lang.String, org.python.Object> kwargs) {

        org.python.Object yearKwargs = kwargs.get("year");
        if (yearKwargs instanceof org.python.types.Int) {
            this.year = (Int) yearKwargs;
        }
        org.python.Object monthKwargs = kwargs.get("month");
        if (monthKwargs instanceof org.python.types.Int) {
            this.month = (Int) monthKwargs;
        }
        org.python.Object dayKwargs = kwargs.get("day");
        if (dayKwargs instanceof org.python.types.Int) {
            this.day = (Int) dayKwargs;
        }
        return this;
    }

    private static String filler(String input, int target) {
        int len = input.toString().length();
        String output = input;
        for (int i = len; i < target; i++) {
            output = "0" + output;
        }
        return output;
    }

    @org.python.Method(__doc__ = "today() -> date")
    public static org.python.types.Object today() {

        Calendar cal = Calendar.getInstance();

        int intMonth = cal.get(Calendar.MONTH);
        intMonth++;

        Int year = Int.getInt(cal.get(Calendar.YEAR));
        Int month = Int.getInt(intMonth);
        Int day = Int.getInt(cal.get(Calendar.DAY_OF_MONTH));

        org.python.stdlib.datetime.Date newDate = new org.python.stdlib.datetime.Date(year, month, day);

        return newDate;
    }

    @org.python.Method(__doc__ = "getTrimmedDateStrings() -> date string")
    private ArrayList getTrimmedDateStrings() {
        ArrayList retList = new ArrayList<String>();
        String year = this.year.toString();
        String month = this.month.toString();
        String day = this.day.toString();
        year = filler(year, 4);
        month = filler(month, 2);
        day = filler(day, 2);

        retList.add(day);
        retList.add(month);
        retList.add(year);

        return retList;
    }

    @org.python.Method(__doc__ = "isoformat() -> date string")
    public org.python.types.Str isoformat() {
        ArrayList dateStrings = getTrimmedDateStrings();
        return new org.python.types.Str(dateStrings.get(2) + "-" + dateStrings.get(1) + "-" + dateStrings.get(0));
    }

    @org.python.Method(__doc__ = "__repr__ -> date string")
    public org.python.types.Str __repr__() {
        ArrayList dateStrings = getTrimmedDateStrings();
        return new org.python.types.Str("datetime.date(" + dateStrings.get(2) + ", " + dateStrings.get(1) + ", " + dateStrings.get(0) + ")");
    }

    @org.python.Method(__doc__ = "__str__ -> date string")
    public org.python.types.Str __str__() {
        return isoformat();
    }
}