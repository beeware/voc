package org.python.stdlib.datetime;

public class Time extends org.python.types.Object {

    public final org.python.types.Int hour;
    public final org.python.types.Int minute;
    public final org.python.types.Int second;
    public final org.python.types.Int microsecond;

    // @org.python.Method(
    //     __doc__ = "Time TODO",
    //     default_args = {}
    // )
    // public Time(org.python.types.Int hour, org.python.types.Int minute, org.python.types.Int second, org.python.types.Int microsecond, org.python.types.Str tzinfo) {
    //     this.hour = hour;
    //     this.minute = minute;
    //     this.second = second;
    //     this.microsecond = microsecond;
    //     this.tzinfo = tzinfo;
    // }

    @org.python.Method(
        __doc__ = "Time TODO",
        default_args = {}
    )
    public Time(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super();
        this.hour = null;
        this.minute = null;
        this.second = null;
        this.microsecond = null;
    }

     public Time(int hour, int minute, int second, int microsecond) {
         this.hour = org.python.types.Int.getInt(hour);
         this.minute = org.python.types.Int.getInt(minute);
         this.second = org.python.types.Int.getInt(second);
         this.microsecond = org.python.types.Int.getInt(microsecond);
     }

    // public Time(org.python.types.Int hour, org.python.types.Int minute, org.python.types.Int second) {
    //     this.hour = hour;
    //     this.minute = minute;
    //     this.second = second;
    // }

    // public Time(org.python.types.Int hour, org.python.types.Int minute) {
    //     this.hour = hour;
    //     this.minute = minute;
    // }

    // public Time(org.python.types.Int hour) {
    //     this.hour = hour;
    // }
}

