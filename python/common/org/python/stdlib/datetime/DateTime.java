package org.python.stdlib.datetime;

import org.python.types.Int;
import org.python.types.Str;

import java.time.LocalDateTime;
import java.time.Instant;
import java.time.ZoneOffset;

public class DateTime extends org.python.types.Object {

	//Class Attributes
    @org.python.Attribute
    public static Int MIN_YEAR = Int.getInt(1);
    @org.python.Attribute
    public static Int MAX_YEAR = Int.getInt(9999);

    @org.python.Attribute
    public static Int MIN_MONTH = Int.getInt(1);
    @org.python.Attribute
    public static Int MAX_MONTH = Int.getInt(12);

    @org.python.Attribute
    public static Int MIN_DAY = Int.getInt(1);
    @org.python.Attribute
    public static Int MAX_DAY = Int.getInt(31);

    @org.python.Attribute
    public static Int MIN_HOUR = Int.getInt(0);
    @org.python.Attribute
    public static Int MAX_HOUR = Int.getInt(23);

    @org.python.Attribute
    public static Int MIN_MIN = Int.getInt(0);
    @org.python.Attribute
    public static Int MAX_MIN = Int.getInt(59);

    @org.python.Attribute
    public static Int MIN_SEC = Int.getInt(0);
    @org.python.Attribute
    public static Int MAX_SEC = Int.getInt(59);

    @org.python.Attribute
    public static Int MIN_MS = Int.getInt(0);
    @org.python.Attribute
    public static Int MAX_MS = Int.getInt(999999);

    @org.python.Attribute
    public static DateTime min = new DateTime((int) MIN_YEAR.value, (int) MIN_MONTH.value, (int) MIN_DAY.value, (int) MIN_HOUR.value, (int) MIN_MIN.value, (int) MIN_SEC.value, (int) MIN_MS.value);

    @org.python.Attribute
    public static DateTime max = new DateTime((int) MAX_YEAR.value, (int) MAX_MONTH.value, (int) MAX_DAY.value, (int) MAX_HOUR.value, (int) MAX_MIN.value, (int) MAX_SEC.value, (int) MAX_MS.value);


	//Instance Attributes
    public Int year;
    public Int month;
    public Int day;
    public Int hour;
    public Int minute;
    public Int second;
    public Int ms;
    public Str tzinfo;


	@org.python.Method(
        __doc__ = "Main DateTime Constructor",
        default_args = {}
    )

    public DateTime(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
        super();

		//Init temp variables
		Int yearTemp = null;
		Int monthTemp = null;
		Int dayTemp = null;
        Int hourTemp = Int.getInt(0);
        Int minTemp = Int.getInt(0);
        Int secTemp = Int.getInt(0);
        Int msTemp = Int.getInt(0);

		//Too few arguments
        if ((args.length + kwargs.size()) < 3) {
            throw new org.python.exceptions.TypeError("Too few arguments.");
        }

		//Too many arguments
        if ((args.length + kwargs.size()) > 7) {
            throw new org.python.exceptions.TypeError("Too many arguments.");
        }

		//Set and validate all arguments

		//Year
		String strYear = "year";
		yearTemp = ((kwargs.get(strYear) == null && args.length >= 1) ? (Int) args[0] : (Int) kwargs.get(strYear));
		if (yearTemp==null) {
			throw new org.python.exceptions.TypeError("Required argument 'year' not found");
		}
		checkIntType(strYear, yearTemp);
		checkIntRange(strYear, yearTemp, MIN_YEAR, MAX_YEAR);

		//Month
		String strMonth = "month";
		monthTemp = ((kwargs.get(strMonth) == null && args.length >= 2) ? (Int) args[1] : (Int) kwargs.get(strMonth));
		if (monthTemp==null) {
			throw new org.python.exceptions.TypeError("Required argument 'month' not found");
		}
		checkIntType(strMonth, monthTemp);
		checkIntRange(strMonth, monthTemp, MIN_MONTH, MAX_MONTH);

		//Day
		String strDay = "day";
		dayTemp = ((kwargs.get(strDay) == null && args.length >= 3) ? (Int) args[2] : (Int) kwargs.get(strDay));
		if (dayTemp==null) {
						throw new org.python.exceptions.TypeError("Required argument 'day' not found");
		}
		checkIntType(strDay, dayTemp);
		checkIntRange(strDay, dayTemp, MIN_DAY, MAX_DAY);

		//Hour
		String strHour = "hour";
		hourTemp = ((kwargs.get(strHour) == null && args.length >= 4) ? (Int) args[3] : (Int) kwargs.get(strHour));
		if (hourTemp!=null) {
			checkIntType(strHour, hourTemp);
			checkIntRange(strHour, hourTemp, MIN_HOUR, MAX_HOUR);
		}

		//Minutes
		String strMin = "minute";
		minTemp = ((kwargs.get(strMin) == null && args.length >= 5) ? (Int) args[4] : (Int) kwargs.get(strMin));
		if (minTemp!=null) {
			checkIntType(strMin, minTemp);
			checkIntRange(strMin, minTemp, MIN_MIN, MAX_MIN);
		}

		//Second
		String strSec = "second";
		secTemp = ((kwargs.get(strSec) == null && args.length >= 6) ? (Int) args[5] : (Int) kwargs.get(strSec));
		if (secTemp!=null) {
			checkIntType(strSec, secTemp);
			checkIntRange(strSec, secTemp, MIN_SEC, MAX_SEC);
		}

		//MicroSecond
		String strMs = "microsecond";
		msTemp = ((kwargs.get(strMs) == null && args.length >= 7) ? (Int) args[6] : (Int) kwargs.get(strMs));
		if (msTemp!=null) {
			checkIntType(strMs, msTemp);
			checkIntRange(strMs, msTemp, MIN_MS, MAX_MS);
		}

		//Final assignment
		this.year = yearTemp;
        this.month = monthTemp;
        this.day = dayTemp;
        this.hour = hourTemp;
        this.minute = minTemp;
        this.second = secTemp;
        this.ms = msTemp;
		this.tzinfo = null;
	}

	@org.python.Method(
        __doc__ = "2nd DateTime Constructor",
        default_args = {}
    )
    public DateTime(int year, int month, int day, int hour, int min, int sec, int ms) {
        this.year = org.python.types.Int.getInt(year);
        this.month = org.python.types.Int.getInt(month);
        this.day = org.python.types.Int.getInt(day);
        this.hour = org.python.types.Int.getInt(hour);
        this.minute = org.python.types.Int.getInt(min);
        this.second = org.python.types.Int.getInt(sec);
        this.ms = org.python.types.Int.getInt(ms);
        this.tzinfo = null;
    }


	@org.python.Method(
        __doc__ = "Checks a variable if it is of type Integers",
        default_args = {}
    )
	private void checkIntType(String varName, org.python.types.Object var) {
		if (!(var instanceof org.python.types.Int)) {
			throw new org.python.exceptions.TypeError("Wrong '" + varName + "'-type");
		}
	}

	@org.python.Method(
        __doc__ = "Checks a variable if it is in a specific range of Integers",
        default_args = {}
    )
	private void checkIntRange(String varName, org.python.types.Int var, org.python.types.Int min, org.python.types.Int max) {
        if (var.value < min.value || var.value > max.value) {
            throw new org.python.exceptions.ValueError(varName + " is Out of range");
        }
	}


	//Instance Methods
    @org.python.Method(
            __doc__ = "Return date object with same year, month and day."
    )
    public Date date() {
        int year = (int) this.year.value;
        int month = (int) this.month.value;
        int day = (int) this.day.value;

        return new org.python.stdlib.datetime.Date(year, month, day);
    }

    @org.python.Method(
            __doc__ = "Return time object with same hour, minute, second and microsecond."
    )
    public Time time() {
        int hour = (int) this.hour.value;
        int min = (int) this.minute.value;
        int sec = (int) this.second.value;
        int ms = (int) this.ms.value;

        return new org.python.stdlib.datetime.Time(hour, min, sec, ms);
    }


	//Class Methods
    @org.python.Method(
            __doc__ = "Return the UTC datetime corresponding to the POSIX timestamp."
    )
    public DateTime utcfromtimestamp(Integer timeStamp) {
        Instant i = Instant.ofEpochMilli(timeStamp*1000);
        LocalDateTime ldt = LocalDateTime.ofInstant(i, ZoneOffset.UTC);

        int year = ldt.getYear();
        int month = ldt.getMonthValue();
        int day = ldt.getDayOfMonth();
        int hour = ldt.getHour();
        int min = ldt.getMinute();
        int sec = ldt.getSecond();
        int ms = ldt.getNano() / 1000;

        return new DateTime(year, month, day, hour, min, sec, ms);
    }

	//Get instance attributes
    @org.python.Method(
            __doc__ = "Return getattr(self, name)"
    )
    public org.python.Object __getattribute__(java.lang.String input) {
        if (input.equals("year")) {
            return this.year;
        }
        if (input.equals("month")) {
            return this.month;
        }
        if (input.equals("day")) {
            return this.day;
        }
        if (input.equals("hour")) {
            return this.hour;
        }
        if (input.equals("minute")) {
            return this.minute;
        }
        if (input.equals("second")) {
            return this.second;
        }
        if (input.equals("microsecond")) {
            return this.ms;
        }
        return super.__getattribute__(input);
    };
}


