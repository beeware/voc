package org.python.stdlib.sys;

public class VersionInfo extends org.python.types.Object {
    org.python.Object major;
    org.python.Object minor;
    org.python.Object micro;
    org.python.Object releaselevel;
    org.python.Object serial;
    public static final java.lang.String PYTHON_TYPE_NAME = "sys.version_info";

    public VersionInfo(int major, int minor, int micro, int releaselevel, int serial) {
        this.major = new org.python.types.Int(major);
        this.minor = new org.python.types.Int(minor);
        this.micro = new org.python.types.Int(micro);
        switch (releaselevel) {
            case 0x0a:
                this.releaselevel = new org.python.types.Str("alpha");
                break;
            case 0x0b:
                this.releaselevel = new org.python.types.Str("beta");
                break;
            case 0x0c:
                this.releaselevel = new org.python.types.Str("candidate");
                break;
            case 0x0f:
                this.releaselevel = new org.python.types.Str("final");
                break;
            default:
                this.releaselevel = new org.python.types.Str("unknown");
                break;
        }
        this.serial = new org.python.types.Int(serial);
    }

    @org.python.Method(
            __doc__ = "Return repr(self)."
    )
    public org.python.Object __repr__() {
        return new org.python.types.Str(
                java.lang.String.format(
                        "sys.version_info(major=%x, minor=%x, micro=%x, releaselevel='%s', serial=%x)",
                        ((org.python.types.Int) (this.major)).value,
                        ((org.python.types.Int) (this.minor)).value,
                        ((org.python.types.Int) (this.micro)).value,
                        this.releaselevel.__str__().toString(),
                        ((org.python.types.Int) (this.serial)).value
                )
        );
    }

    //  '__add__',
    //  '__class__',
    //  '__contains__',
    //  '__delattr__',
    //  '__dir__',
    //  '__doc__',
    //  '__eq__',
    //  '__format__',
    //  '__ge__',
    //  '__getattribute__',
    //  '__getitem__',
    //  '__getnewargs__',
    //  '__gt__',
    //  '__hash__',
    //  '__init__',
    //  '__iter__',
    //  '__le__',
    //  '__len__',
    //  '__lt__',
    //  '__mul__',
    //  '__ne__',
    //  '__new__',
    //  '__reduce__',
    //  '__reduce_ex__',
    //  '__repr__',
    //  '__rmul__',
    //  '__setattr__',
    //  '__sizeof__',
    //  '__str__',
    //  '__subclasshook__',
    //  'count',
    //  'index',
    //  'n_fields',
    //  'n_sequence_fields',
    //  'n_unnamed_fields',
    //  'serial',
}
