From: http://docs.oracle.com/javase/specs/jvms/se7/html/jvms-4.html

4.2. The Internal Form of Names

4.2.1. Binary Class and Interface Names

Class and interface names that appear in class file structures are always represented in a fully qualified form known as binary names (JLS §13.1). Such names are always represented as CONSTANT_Utf8_info structures (§4.4.7) and thus may be drawn, where not further constrained, from the entire Unicode codespace. Class and interface names are referenced from those CONSTANT_NameAndType_info structures (§4.4.6) which have such names as part of their descriptor (§4.3), and from all CONSTANT_Class_info structures (§4.4.1).

For historical reasons, the syntax of binary names that appear in class file structures differs from the syntax of binary names documented in JLS §13.1. In this internal form, the ASCII periods (.) that normally separate the identifiers which make up the binary name are replaced by ASCII forward slashes (/). The identifiers themselves must be unqualified names (§4.2.2).

For example, the normal binary name of class Thread is java.lang.Thread. In the internal form used in descriptors in the class file format, a reference to the name of class Thread is implemented using a CONSTANT_Utf8_info structure representing the string java/lang/Thread.

4.2.2. Unqualified Names

Names of methods, fields, and local variables are stored as unqualified names. An unqualified name must not contain any of the ASCII characters . ; [ / (that is, period or semicolon or left square bracket or forward slash).

Method names are further constrained so that, with the exception of the special method names <init> and <clinit> (§2.9), they must not contain the ASCII characters < or > (that is, left angle bracket or right angle bracket).

Note that a field name or interface method name may be <init> or <clinit>, but no method invocation instruction may reference <clinit> and only the invokespecial instruction (§invokespecial) may reference <init>.

