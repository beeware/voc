package org.python.stdlib.datetime;
import org.python.types.Int;
import org.python.types.Str;

public class Date extends org.python.types.Object { 
    private org.python.types.Int year;
    private org.python.types.Int month;
    private org.python.types.Int day;
    
    @org.python.Method(
        __doc__ = "Time TODO",
        default_args = {"year","month","day"}
    )
    public Date(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super();

        this.year = Int.getInt(1);
        this.month = Int.getInt(1);
        this.day = Int.getInt(1);

        if(args[0] != null) this.year = (Int) args[0];
        if(args[1] != null) this.month = (Int) args[1];
        if(args[2] != null) this.day = (Int) args[2];

/*
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
*/
//        this.year = (Int) args[0];        
    }

    @org.python.Method(
        __doc__ = "Return repr(self).",
        default_args = {"year","month","day"}
    )
    public org.python.types.Object replace(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        
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

    @org.python.Method(
            __doc__ = "Return repr(self)."
    )
    public org.python.types.Str isoformat() {
        String year = this.year.toString();
        String month = this.month.toString();
        String day = this.day.toString();
        year = filler(year,4);
        month = filler(month,2);
        day = filler(day,2);

        //return this.year;
        return new org.python.types.Str(year+"-"+month+"-"+day);
    }

    private String filler(String input, int target) {
        int len = input.toString().length();
        String output = input;
        for (int i = len; i<target; i++) {
           output = "0"+output;
        }
        return output;
    }


    public Date(int year, int month, int day) {
        this.year = org.python.types.Int.getInt(year);
        this.month = org.python.types.Int.getInt(month);
        this.day = org.python.types.Int.getInt(day);
    }

    @org.python.Method(
            __doc__ = "Return repr(self)."
    )
    public org.python.types.Str __repr__() {
        return new org.python.types.Str("0002-02-02");
    }
}
