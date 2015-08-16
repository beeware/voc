from .constants import Fieldref, Methodref, String, Integer, Long

# From: https://en.wikipedia.org/wiki/Java_bytecode_instruction_listings
# Reference" http://docs.oracle.com/javase/specs/jvms/se7/html/jvms-6.html#jvms-6.2

##########################################################################
# 6.2. Opcodes
##########################################################################

class Opcode:
    def __init__(self, code):
        self.code = code

    def __len__(self):
        return 1

    def write(self, writer):
        writer.write_u1(self.code)
        self.write_extra(writer)

    def write_extra(self, writer):
        pass

    def resolve(self, constant_pool):
        pass


class AALOAD(Opcode):
    def __init__(self):
        super(AALOAD, self).__init__(0x32)
# arrayref, index → value
# Load onto the stack a reference from an array

class AASTORE(Opcode):
    def __init__(self):
        super(AASTORE, self).__init__(0x53)
# arrayref, index, value →
# Store into a reference in an array

class ACONST_NULL(Opcode):
    def __init__(self):
        super(ACONST_NULL, self).__init__(0x01)
# → null
# Push a null reference onto the stack


class ALOAD(Opcode):
    # Load a reference onto the stack from a local variable #index
    # Args(1): index
    # Stack: → objectref
    def __init__(self, var):
        super(ALOAD, self).__init__(0x19)

    def write_extra(self, writer):
        writer.write_u1(self.var)


class ALOAD_0(Opcode):
    # Load a reference onto the stack from local variable 0
    # Stack: → objectref

    def __init__(self):
        super(ALOAD_0, self).__init__(0x2a)


class ALOAD_1(Opcode):
    def __init__(self):
        super(ALOAD_1, self).__init__(0x2b)
# → objectref
# Load a reference onto the stack from local variable 1

class ALOAD_2(Opcode):
    def __init__(self):
        super(ALOAD_2, self).__init__(0x2c)
# → objectref
# Load a reference onto the stack from local variable 2

class ALOAD_3(Opcode):
    def __init__(self):
        super(ALOAD_3, self).__init__(0x2d)
# → objectref
# Load a reference onto the stack from local variable 3

class ANEWARRAY(Opcode):
    def __init__(self):
        super(ANEWARRAY, self).__init__(0xbd)
# 2: indexbyte1, indexbyte2
# count → arrayref
# Create a new array of references of length count and component type identified
# by the class reference index (indexbyte1 << 8 + indexbyte2) in the constant
# pool

class ARETURN(Opcode):
    def __init__(self):
        super(ARETURN, self).__init__(0xb0)
# objectref → [empty]
# Return a reference from a method

class ARRAYLENGTH(Opcode):
    def __init__(self):
        super(ARRAYLENGTH, self).__init__(0xbe)
# arrayref → length
# Get the length of an array

class ASTORE(Opcode):
    def __init__(self):
        super(ASTORE, self).__init__(0x3a)
# 1: index
# objectref →
# Store a reference into a local variable #index

class ASTORE_0(Opcode):
    def __init__(self):
        super(ASTORE_0, self).__init__(0x4b)
# objectref →
# Store a reference into local variable 0

class ASTORE_1(Opcode):
    def __init__(self):
        super(ASTORE_1, self).__init__(0x4c)
# objectref →
# Store a reference into local variable 1

class ASTORE_2(Opcode):
    def __init__(self):
        super(ASTORE_2, self).__init__(0x4d)
# objectref →
# Store a reference into local variable 2

class ASTORE_3(Opcode):
    def __init__(self):
        super(ASTORE_3, self).__init__(0x4e)
# objectref →
# Store a reference into local variable 3

class ATHROW(Opcode):
    def __init__(self):
        super(ATHROW, self).__init__(0xbf)
# objectref → [empty], objectref
# Throws an error or exception (notice that the rest of the stack is cleared,
# leaving only a reference to the Throwable)

class BALOAD(Opcode):
    def __init__(self):
        super(BALOAD, self).__init__(0x33)
# arrayref, index → value
# Load a byte or Boolean value from an array

class BASTORE(Opcode):
    def __init__(self):
        super(BASTORE, self).__init__(0x54)
# arrayref, index, value →
# Store a byte or Boolean value into an array

class BIPUSH(Opcode):
    def __init__(self):
        super(BIPUSH, self).__init__(0x10)
# 1: byte → value
# Push a byte onto the stack as an integer value

class BREAKPOINT(Opcode):
    def __init__(self):
        super(BREAKPOINT, self).__init__(0xca)
# Reserved for breakpoints in Java debuggers; should not appear in any class file

class CALOAD(Opcode):
    def __init__(self):
        super(CALOAD, self).__init__(0x34)
# arrayref, index → value
# Load a char from an array

class CASTORE(Opcode):
    def __init__(self):
        super(CASTORE, self).__init__(0x55)
# arrayref, index, value →
# Store a char into an array

class CHECKCAST(Opcode):
    def __init__(self):
        super(CHECKCAST, self).__init__(0xc0)
# 2: indexbyte1, indexbyte2
# objectref → objectref
# Checks whether an objectref is of a certain type, the class reference of which
# is in the constant pool at index (indexbyte1 << 8 + indexbyte2)

class D2F(Opcode):
    def __init__(self):
        super(D2F, self).__init__(0x90)
# value → result
# Convert a double to a float

class D2I(Opcode):
    def __init__(self):
        super(D2I, self).__init__(0x8e)
# value → result
# Convert a double to an int

class D2L(Opcode):
    def __init__(self):
        super(D2L, self).__init__(0x8f)
# value → result
# Convert a double to a long

class DADD(Opcode):
    def __init__(self):
        super(DADD, self).__init__(0x63)
# value1, value2 → result
# Add two doubles

class DALOAD(Opcode):
    def __init__(self):
        super(DALOAD, self).__init__(0x31)
# arrayref, index → value
# Load a double from an array

class DASTORE(Opcode):
    def __init__(self):
        super(DASTORE, self).__init__(0x52)
# arrayref, index, value →
# Store a double into an array

class DCMPG(Opcode):
    def __init__(self):
        super(DCMPG, self).__init__(0x98)
# value1, value2 → result
# Compare two doubles

class DCMPL(Opcode):
    def __init__(self):
        super(DCMPL, self).__init__(0x97)
# value1, value2 → result
# Compare two doubles

class DCONST_0(Opcode):
    def __init__(self):
        super(DCONST_0, self).__init__(0x0e)
# → 0.0
# Push the constant 0.0 onto the stack

class DCONST_1(Opcode):
    def __init__(self):
        super(DCONST_1, self).__init__(0x0f)
# → 1.0
# Push the constant 1.0 onto the stack

class DDIV(Opcode):
    def __init__(self):
        super(DDIV, self).__init__(0x6f)
# value1, value2 → result
# Divide two doubles

class DLOAD(Opcode):
    def __init__(self):
        super(DLOAD, self).__init__(0x18)
# 1: index
# → value
# Load a double value from a local variable #index

class DLOAD_0(Opcode):
    def __init__(self):
        super(DLOAD_0, self).__init__(0x26)
# → value
# Load a double from local variable 0

class DLOAD_1(Opcode):
    def __init__(self):
        super(DLOAD_1, self).__init__(0x27)
# → value
# Load a double from local variable 1

class DLOAD_2(Opcode):
    def __init__(self):
        super(DLOAD_2, self).__init__(0x28)
# → value
# Load a double from local variable 2

class DLOAD_3(Opcode):
    def __init__(self):
        super(DLOAD_3, self).__init__(0x29)
# → value
# Load a double from local variable 3

class DMUL(Opcode):
    def __init__(self):
        super(DMUL, self).__init__(0x6b)
# value1, value2 → result multiply two doubles

class DNEG(Opcode):
    def __init__(self):
        super(DNEG, self).__init__(0x77)
# value → result  negate a double

class DREM(Opcode):
    def __init__(self):
        super(DREM, self).__init__(0x73)
# value1, value2 → result get the remainder from a division between two doubles

class DRETURN(Opcode):
    def __init__(self):
        super(DRETURN, self).__init__(0xaf)
# value → [empty] return a double from a method

class DSTORE(Opcode):
    def __init__(self):
        super(DSTORE, self).__init__(0x39)
# 1: index
# value →
# Store a double value into a local variable #index

class DSTORE_0(Opcode):
    def __init__(self):
        super(DSTORE_0, self).__init__(0x47)
# value →
# Store a double into local variable 0

class DSTORE_1(Opcode):
    def __init__(self):
        super(DSTORE_1, self).__init__(0x48)
# value →
# Store a double into local variable 1

class DSTORE_2(Opcode):
    def __init__(self):
        super(DSTORE_2, self).__init__(0x49)
# value →
# Store a double into local variable 2

class DSTORE_3(Opcode):
    def __init__(self):
        super(DSTORE_3, self).__init__(0x4a)
# value →
# Store a double into local variable 3

class DSUB(Opcode):
    def __init__(self):
        super(DSUB, self).__init__(0x67)
# value1, value2 → result subtract a double from another

class DUP(Opcode):
    def __init__(self):
        super(DUP, self).__init__(0x59)
# value → value, value    duplicate the value on top of the stack

class DUP_X1(Opcode):
    def __init__(self):
        super(DUP_X1, self).__init__(0x5a)
# value2, value1 → value1, value2, value1
# Insert a copy of the top value into the stack two values from the top. value1
# and value2 must not be of the type double or long.

class DUP_X2(Opcode):
    def __init__(self):
        super(DUP_X2, self).__init__(0x5b)
# value3, value2, value1 → value1, value3, value2, value1
# Insert a copy of the top value into the stack two (if value2 is double or long
# it takes up the entry of value3, too) or three values (if value2 is neither
# double nor long) from the top

class DUP2(Opcode):
    def __init__(self):
        super(DUP2, self).__init__(0x5c)
# {value2, value1} → {value2, value1}, {value2, value1}
# Duplicate top two stack words (two values, if value1 is not double nor long; a
# single value, if value1 is double or long)

class DUP2_X1(Opcode):
    def __init__(self):
        super(DUP2_X1, self).__init__(0x5d)
# value3, {value2, value1} → {value2, value1}, value3, {value2, value1}
# Duplicate two words and insert beneath third word (see explanation above)

class DUP2_X2(Opcode):
    def __init__(self):
        super(DUP2_X2, self).__init__(0x5e)
# {value4, value3}, {value2, value1} → {value2, value1}, {value4, value3}, {value2, value1}
# Duplicate two words and insert beneath fourth word

class F2D(Opcode):
    def __init__(self):
        super(F2D, self).__init__(0x8d)
# value → result
# Convert a float to a double

class F2I(Opcode):
    def __init__(self):
        super(F2I, self).__init__(0x8b)
# value → result
# Convert a float to an int

class F2L(Opcode):
    def __init__(self):
        super(F2L, self).__init__(0x8c)
# value → result
# Convert a float to a long

class FADD(Opcode):
    def __init__(self):
        super(FADD, self).__init__(0x62)
# value1, value2 → result add two floats

class FALOAD(Opcode):
    def __init__(self):
        super(FALOAD, self).__init__(0x30)
# arrayref, index → value
# Load a float from an array

class FASTORE(Opcode):
    def __init__(self):
        super(FASTORE, self).__init__(0x51)
# arrayref, index, value →
# Store a float in an array

class FCMPG(Opcode):
    def __init__(self):
        super(FCMPG, self).__init__(0x96)
# value1, value2 → result
# Compare two floats

class FCMPL(Opcode):
    def __init__(self):
        super(FCMPL, self).__init__(0x95)
# value1, value2 → result
# Compare two floats

class FCONST_0(Opcode):
    def __init__(self):
        super(FCONST_0, self).__init__(0x0b)
# → 0.0f
# Push 0.0f on the stack

class FCONST_1(Opcode):
    def __init__(self):
        super(FCONST_1, self).__init__(0x0c)
# → 1.0f
# Push 1.0f on the stack

class FCONST_2(Opcode):
    def __init__(self):
        super(FCONST_2, self).__init__(0x0d)
# → 2.0f
# Push 2.0f on the stack

class FDIV(Opcode):
    def __init__(self):
        super(FDIV, self).__init__(0x6e)
# value1, value2 → result
# Divide two floats

class FLOAD(Opcode):
    def __init__(self):
        super(FLOAD, self).__init__(0x17)
# 1: index
# → value
# Load a float value from a local variable #index

class FLOAD_0(Opcode):
    def __init__(self):
        super(FLOAD_0, self).__init__(0x22)
# → value
# Load a float value from local variable 0

class FLOAD_1(Opcode):
    def __init__(self):
        super(FLOAD_1, self).__init__(0x23)
# → value
# Load a float value from local variable 1

class FLOAD_2(Opcode):
    def __init__(self):
        super(FLOAD_2, self).__init__(0x24)
# → value
# Load a float value from local variable 2

class FLOAD_3(Opcode):
    def __init__(self):
        super(FLOAD_3, self).__init__(0x25)
# → value
# Load a float value from local variable 3

class FMUL(Opcode):
    def __init__(self):
        super(FMUL, self).__init__(0x6a)
# value1, value2 → result multiply two floats

class FNEG(Opcode):
    def __init__(self):
        super(FNEG, self).__init__(0x76)
# value → result  negate a float

class FREM(Opcode):
    def __init__(self):
        super(FREM, self).__init__(0x72)
# value1, value2 → result get the remainder from a division between two floats

class FRETURN(Opcode):
    def __init__(self):
        super(FRETURN, self).__init__(0xae)
# value → [empty] return a float

class FSTORE(Opcode):
    def __init__(self):
        super(FSTORE, self).__init__(0x38)
# 1: index
# value →
# Store a float value into a local variable #index

class FSTORE_0(Opcode):
    def __init__(self):
        super(FSTORE_0, self).__init__(0x43)
# value →
# Store a float value into local variable 0

class FSTORE_1(Opcode):
    def __init__(self):
        super(FSTORE_1, self).__init__(0x44)
# value →
# Store a float value into local variable 1

class FSTORE_2(Opcode):
    def __init__(self):
        super(FSTORE_2, self).__init__(0x45)
# value →
# Store a float value into local variable 2

class FSTORE_3(Opcode):
    def __init__(self):
        super(FSTORE_3, self).__init__(0x46)
# value →
# Store a float value into local variable 3

class FSUB(Opcode):
    def __init__(self):
        super(FSUB, self).__init__(0x66)
# value1, value2 → result subtract two floats

class GETFIELD(Opcode):
    def __init__(self):
        super(GETFIELD, self).__init__(0xb4)
# 2: index1, index2   objectref → value
# Get a field value of an object objectref, where the field is identified by
# field reference in the constant pool index (index1 << 8 + index2)


class GETSTATIC(Opcode):
    # Args(2): index1, index2   → value
    # Get a static field value of a class, where the field is identified by field
    # reference in the constant pool index (index1 << 8 + index2)
    def __init__(self, classname, fieldname, descriptor):
        super(GETSTATIC, self).__init__(0xb2)
        self.field = Fieldref(classname, fieldname, descriptor)

    def __len__(self):
        return 3

    def write_extra(self, writer):
        writer.write_u2(writer.constant_pool[self.field])

    def resolve(self, constant_pool):
        self.field.resolve(constant_pool)


class GOTO(Opcode):
    def __init__(self):
        super(GOTO, self).__init__(0xa7)
# 2: branchbyte1, branchbyte2
# [no change]
# Goes to another instruction at branchoffset (signed short constructed from
# unsigned bytes branchbyte1 << 8 + branchbyte2)

class GOTO_W(Opcode):
    def __init__(self):
        super(GOTO_W, self).__init__(0xc8)
# 4: branchbyte1, branchbyte2, branchbyte3, branchbyte4
# [no change]
# Goes to another instruction at branchoffset (signed int constructed from
# unsigned bytes branchbyte1 << 24 + branchbyte2 << 16 + branchbyte3 << 8 +
# branchbyte4)

class I2B(Opcode):
    def __init__(self):
        super(I2B, self).__init__(0x91)
# value → result
# Convert an int into a byte

class I2C(Opcode):
    def __init__(self):
        super(I2C, self).__init__(0x92)
# value → result
# Convert an int into a character

class I2D(Opcode):
    def __init__(self):
        super(I2D, self).__init__(0x87)
# value → result
# Convert an int into a double

class I2F(Opcode):
    def __init__(self):
        super(I2F, self).__init__(0x86)
# value → result
# Convert an int into a float

class I2L(Opcode):
    def __init__(self):
        super(I2L, self).__init__(0x85)
# value → result
# Convert an int into a long

class I2S(Opcode):
    def __init__(self):
        super(I2S, self).__init__(0x93)
# value → result
# Convert an int into a short

class IADD(Opcode):
    def __init__(self):
        super(IADD, self).__init__(0x60)
# value1, value2 → result add two ints

class IALOAD(Opcode):
    def __init__(self):
        super(IALOAD, self).__init__(0x2e)
# arrayref, index → value
# Load an int from an array

class IAND(Opcode):
    def __init__(self):
        super(IAND, self).__init__(0x7e)
# value1, value2 → result
# Perform a bitwise and on two integers

class IASTORE(Opcode):
    def __init__(self):
        super(IASTORE, self).__init__(0x4f)
# arrayref, index, value →
# Store an int into an array

class ICONST_M1(Opcode):
    def __init__(self):
        super(ICONST_M1, self).__init__(0x02)
# → -1
# Load the int value -1 onto the stack

class ICONST_0(Opcode):
    def __init__(self):
        super(ICONST_0, self).__init__(0x03)
# → 0
# Load the int value 0 onto the stack

class ICONST_1(Opcode):
    def __init__(self):
        super(ICONST_1, self).__init__(0x04)
# → 1
# Load the int value 1 onto the stack

class ICONST_2(Opcode):
    def __init__(self):
        super(ICONST_2, self).__init__(0x05)
# → 2
# Load the int value 2 onto the stack

class ICONST_3(Opcode):
    def __init__(self):
        super(ICONST_3, self).__init__(0x06)
# → 3
# Load the int value 3 onto the stack

class ICONST_4(Opcode):
    def __init__(self):
        super(ICONST_4, self).__init__(0x07)
# → 4
# Load the int value 4 onto the stack

class ICONST_5(Opcode):
    def __init__(self):
        super(ICONST_5, self).__init__(0x08)
# → 5
# Load the int value 5 onto the stack

class IDIV(Opcode):
    def __init__(self):
        super(IDIV, self).__init__(0x6c)
# value1, value2 → result
# Divide two integers

class IF_ACMPEQ(Opcode):
    def __init__(self):
        super(IF_ACMPEQ, self).__init__(0xa5)
# 2: branchbyte1, branchbyte2 value1, value2 →
# If references are equal, branch to instruction at branchoffset (signed short
# constructed from unsigned bytes branchbyte1 << 8 + branchbyte2)

class IF_ACMPNE(Opcode):
    def __init__(self):
        super(IF_ACMPNE, self).__init__(0xa6)
# 2: branchbyte1, branchbyte2 value1, value2 →
# If references are not equal, branch to instruction at branchoffset (signed
# short constructed from unsigned bytes branchbyte1 << 8 + branchbyte2)

class IF_ICMPEQ(Opcode):
    def __init__(self):
        super(IF_ICMPEQ, self).__init__(0x9f)
# 2: branchbyte1, branchbyte2 value1, value2 →
# If ints are equal, branch to instruction at branchoffset (signed short
# constructed from unsigned bytes branchbyte1 << 8 + branchbyte2)

class IF_ICMPGE(Opcode):
    def __init__(self):
        super(IF_ICMPGE, self).__init__(0xa2)
# 2: branchbyte1, branchbyte2 value1, value2 →
# If value1 is greater than or equal to value2, branch to instruction at
# Iranchoffset (signed short constructed from unsigned bytes branchbyte1 << 8 +
# branchbyte2)

class IF_ICMPGT(Opcode):
    def __init__(self):
        super(IF_ICMPGT, self).__init__(0xa3)
# 2: branchbyte1, branchbyte2 value1, value2 →
# If value1 is greater than value2, branch to instruction at branchoffset
# (signed short constructed from unsigned bytes branchbyte1 << 8 + branchbyte2)

class IF_ICMPLE(Opcode):
    def __init__(self):
        super(IF_ICMPLE, self).__init__(0xa4)
# 2: branchbyte1, branchbyte2 value1, value2 →
# If value1 is less than or equal to value2, branch to instruction at
# Iranchoffset (signed short constructed from unsigned bytes branchbyte1 << 8 +
# branchbyte2)

class IF_ICMPLT(Opcode):
    def __init__(self):
        super(IF_ICMPLT, self).__init__(0xa1)
# 2: branchbyte1, branchbyte2 value1, value2 →
# If value1 is less than value2, branch to instruction at branchoffset (signed
# short constructed from unsigned bytes branchbyte1 << 8 + branchbyte2)

class IF_ICMPNE(Opcode):
    def __init__(self):
        super(IF_ICMPNE, self).__init__(0xa0)
# 2: branchbyte1, branchbyte2 value1, value2 →
# If ints are not equal, branch to instruction at branchoffset (signed short
# constructed from unsigned bytes branchbyte1 << 8 + branchbyte2)

class IFEQ(Opcode):
    def __init__(self):
        super(IFEQ, self).__init__(0x99)
# 2: branchbyte1, branchbyte2 value →
# If value is 0, branch to instruction at branchoffset (signed short constructed
# from unsigned bytes branchbyte1 << 8 + branchbyte2)

class IFGE(Opcode):
    def __init__(self):
        super(IFGE, self).__init__(0x9c)
# 2: branchbyte1, branchbyte2 value →
# If value is greater than or equal to 0, branch to instruction at branchoffset
# (signed short constructed from unsigned bytes branchbyte1 << 8 + branchbyte2)

class IFGT(Opcode):
    def __init__(self):
        super(IFGT, self).__init__(0x9d)
# 2: branchbyte1, branchbyte2 value →
# If value is greater than 0, branch to instruction at branchoffset (signed
# short constructed from unsigned bytes branchbyte1 << 8 + branchbyte2)

class IFLE(Opcode):
    def __init__(self):
        super(IFLE, self).__init__(0x9e)
# 2: branchbyte1, branchbyte2 value →
# If value is less than or equal to 0, branch to instruction at branchoffset
# (signed short constructed from unsigned bytes branchbyte1 << 8 + branchbyte2)

class IFLT(Opcode):
    def __init__(self):
        super(IFLT, self).__init__(0x9b)
# 2: branchbyte1, branchbyte2 value →
# If value is less than 0, branch to instruction at branchoffset (signed short
# constructed from unsigned bytes branchbyte1 << 8 + branchbyte2)

class IFNE(Opcode):
    def __init__(self):
        super(IFNE, self).__init__(0x9a)
# 2: branchbyte1, branchbyte2 value →
# If value is not 0, branch to instruction at branchoffset (signed short
# constructed from unsigned bytes branchbyte1 << 8 + branchbyte2)

class IFNONNULL(Opcode):
    def __init__(self):
        super(IFNONNULL, self).__init__(0xc7)
# 2: branchbyte1, branchbyte2 value →
# If value is not null, branch to instruction at branchoffset (signed short
# constructed from unsigned bytes branchbyte1 << 8 + branchbyte2)

class IFNULL(Opcode):
    def __init__(self):
        super(IFNULL, self).__init__(0xc6)
# 2: branchbyte1, branchbyte2 value →
# If value is null, branch to instruction at branchoffset (signed short
# constructed from unsigned bytes branchbyte1 << 8 + branchbyte2)

class IINC(Opcode):
    def __init__(self):
        super(IINC, self).__init__(0x84)
# 2: index, const
# [No change]
# Increment local variable #index by signed byte const

class ILOAD(Opcode):
    def __init__(self):
        super(ILOAD, self).__init__(0x15)
# 1: index
# → value
# Load an int value from a local variable #index

class ILOAD_0(Opcode):
    def __init__(self):
        super(ILOAD_0, self).__init__(0x1a)
# → value
# Load an int value from local variable 0

class ILOAD_1(Opcode):
    def __init__(self):
        super(ILOAD_1, self).__init__(0x1b)
# → value
# Load an int value from local variable 1

class ILOAD_2(Opcode):
    def __init__(self):
        super(ILOAD_2, self).__init__(0x1c)
# → value
# Load an int value from local variable 2

class ILOAD_3(Opcode):
    def __init__(self):
        super(ILOAD_3, self).__init__(0x1d)
# → value
# Load an int value from local variable 3

class IMPDEP1(Opcode):
    def __init__(self):
        super(IMPDEP1, self).__init__(0xfe)
# Reserved for implementation-dependent operations within debuggers; should not
# appear in any class file

class IMPDEP2(Opcode):
    def __init__(self):
        super(IMPDEP2, self).__init__(0xff)
# Reserved for implementation-dependent operations within debuggers; should not
# appear in any class file

class IMUL(Opcode):
    def __init__(self):
        super(IMUL, self).__init__(0x68)
# value1, value2 → result
# Multiply two integers

class INEG(Opcode):
    def __init__(self):
        super(INEG, self).__init__(0x74)
# value → result
# Negate int

class INSTANCEOF(Opcode):
    def __init__(self):
        super(INSTANCEOF, self).__init__(0xc1)
# 2: indexbyte1, indexbyte2
# objectref → result
# Determines if an object objectref is of a given type, identified by class
# reference index in constant pool (indexbyte1 << 8 + indexbyte2)

class INVOKEDYNAMIC(Opcode):
    def __init__(self):
        super(INVOKEDYNAMIC, self).__init__(0xba)
# 4: indexbyte1, indexbyte2, 0, 0
# [arg1, [arg2 ...]] → result
# Invokes a dynamic method and puts the result on the stack (might be void); the
# method is identified by method reference index in constant pool (indexbyte1 <<
# 8 + indexbyte2)

class INVOKEINTERFACE(Opcode):
    def __init__(self):
        super(INVOKEINTERFACE, self).__init__(0xb9)
# 4: indexbyte1, indexbyte2, count, 0 objectref,
# [arg1, arg2, ...] → result
# Invokes an interface method on object objectref and puts the result on the
# stack (might be void); the interface method is identified by method reference
# index in constant pool (indexbyte1 << 8 + indexbyte2)


class INVOKESPECIAL(Opcode):
    # Args (2): indexbyte1, indexbyte2
    # Stack: objectref, [arg1, arg2, ...] → result
    # Invoke instance method on object objectref and puts the result on the stack
    # (might be void); the method is identified by method reference index in
    # constant pool (indexbyte1 << 8 + indexbyte2)
    def __init__(self, classname, methodname, descriptor):
        super(INVOKESPECIAL, self).__init__(0xb7)
        self.method = Methodref(classname, methodname, descriptor)

    def __len__(self):
        return 3

    def write_extra(self, writer):
        writer.write_u2(writer.constant_pool[self.method])

    def resolve(self, constant_pool):
        self.method.resolve(constant_pool)


class INVOKESTATIC(Opcode):
    def __init__(self):
        super(INVOKESTATIC, self).__init__(0xb8)
# 2: indexbyte1, indexbyte2
# [arg1, arg2, ...] → result
# Invoke a static method and puts the result on the stack (might be void); the
# method is identified by method reference index in constant pool (indexbyte1 <<
# 8 + indexbyte2)


class INVOKEVIRTUAL(Opcode):
    # Args(2): indexbyte1, indexbyte2
    # Stack: objectref, [arg1, arg2, ...] → result
    # Invoke virtual method on object objectref and puts the result on the stack
    # (might be void); the method is identified by method reference index in
    # constant pool (indexbyte1 << 8 + indexbyte2)
    def __init__(self, classname, methodname, descriptor):
        super(INVOKEVIRTUAL, self).__init__(0xb6)
        self.method = Methodref(classname, methodname, descriptor)

    def __len__(self):
        return 3

    def write_extra(self, writer):
        writer.write_u2(writer.constant_pool[self.method])

    def resolve(self, constant_pool):
        self.method.resolve(constant_pool)


class IOR(Opcode):
    def __init__(self):
        super(IOR, self).__init__(0x80)
# value1, value2 → result
# Bitwise int or

class IREM(Opcode):
    def __init__(self):
        super(IREM, self).__init__(0x70)
# value1, value2 → result
# Logical int remainder

class IRETURN(Opcode):
    def __init__(self):
        super(IRETURN, self).__init__(0xac)
# value → [empty]
# Return an integer from a method

class ISHL(Opcode):
    def __init__(self):
        super(ISHL, self).__init__(0x78)
# value1, value2 → result
# int shift left

class ISHR(Opcode):
    def __init__(self):
        super(ISHR, self).__init__(0x7a)
# value1, value2 → result
# int arithmetic shift right

class ISTORE(Opcode):
    def __init__(self):
        super(ISTORE, self).__init__(0x36)
# 1: index
# value →
# Store int value into variable #index

class ISTORE_0(Opcode):
    def __init__(self):
        super(ISTORE_0, self).__init__(0x3b)
# value →
# Store int value into variable 0

class ISTORE_1(Opcode):
    def __init__(self):
        super(ISTORE_1, self).__init__(0x3c)
# value →
# Store int value into variable 1

class ISTORE_2(Opcode):
    def __init__(self):
        super(ISTORE_2, self).__init__(0x3d)
# value →
# Store int value into variable 2

class ISTORE_3(Opcode):
    def __init__(self):
        super(ISTORE_3, self).__init__(0x3e)
# value →
# Store int value into variable 3

class ISUB(Opcode):
    def __init__(self):
        super(ISUB, self).__init__(0x64)
# value1, value2 → result int subtract

class IUSHR(Opcode):
    def __init__(self):
        super(IUSHR, self).__init__(0x7c)
# value1, value2 → result int logical shift right

class IXOR(Opcode):
    def __init__(self):
        super(IXOR, self).__init__(0x82)
# value1, value2 → result int xor

class JSR(Opcode):
    def __init__(self):
        super(JSR, self).__init__(0xa8)
# 2: branchbyte1, branchbyte2 → address
# Jump to subroutine at branchoffset (signed short constructed from unsigned
# bytes branchbyte1 << 8 + branchbyte2) and place the return address on the
# stack

class JSR_W(Opcode):
    def __init__(self):
        super(JSR_W, self).__init__(0xc9)
# 4: branchbyte1, branchbyte2, branchbyte3, branchbyte4   → address
# Jump to subroutine at branchoffset (signed int constructed from unsigned bytes
# branchbyte1 << 24 + branchbyte2 << 16 + branchbyte3 << 8 + branchbyte4) and
# place the return address on the stack

class L2D(Opcode):
    def __init__(self):
        super(L2D, self).__init__(0x8a)
# value → result
# Convert a long to a double

class L2F(Opcode):
    def __init__(self):
        super(L2F, self).__init__(0x89)
# value → result
# Convert a long to a float

class L2I(Opcode):
    def __init__(self):
        super(L2I, self).__init__(0x88)
# value → result
# Convert a long to a int

class LADD(Opcode):
    def __init__(self):
        super(LADD, self).__init__(0x61)
# value1, value2 → result add two longs

class LALOAD(Opcode):
    def __init__(self):
        super(LALOAD, self).__init__(0x2f)
# arrayref, index → value
# Load a long from an array

class LAND(Opcode):
    def __init__(self):
        super(LAND, self).__init__(0x7f)
# value1, value2 → result bitwise and of two longs

class LASTORE(Opcode):
    def __init__(self):
        super(LASTORE, self).__init__(0x50)
# arrayref, index, value →
# Store a long to an array

class LCMP(Opcode):
    def __init__(self):
        super(LCMP, self).__init__(0x94)
# value1, value2 → result
# Compare two longs values

class LCONST_0(Opcode):
    def __init__(self):
        super(LCONST_0, self).__init__(0x09)
# → 0L
# Push the long 0 onto the stack

class LCONST_1(Opcode):
    def __init__(self):
        super(LCONST_1, self).__init__(0x0a)
# → 1L
# Push the long 1 onto the stack


class LDC(Opcode):
    # Args(1): index → value
    # Push a constant #index from a constant pool (String, int or float) onto the
    # stack
    def __init__(self, const):
        super(LDC, self).__init__(0x12)
        if isinstance(const, str):
            self.const = String(const)
        elif isinstance(const, int):
            self.const = Integer(const)
        elif isinstance(const, long):
            self.const = Long(const)
        else:
            raise TypeError('Invalid type for LDC: %s' % type(const))

    def __len__(self):
        return 2

    def write_extra(self, writer):
        writer.write_u1(writer.constant_pool[self.const])

    def resolve(self, constant_pool):
        self.const.resolve(constant_pool)


class LDC_W(Opcode):
    def __init__(self):
        super(LDC_W, self).__init__(0x13)
# 2: indexbyte1, indexbyte2   → value
# push a constant #index from a constant pool (String, int or float) onto the
# stack (wide index is constructed as indexbyte1 << 8 + indexbyte2)

class LDC2_W(Opcode):
    def __init__(self):
        super(LDC2_W, self).__init__(0x14)
# 2: indexbyte1, indexbyte2   → value
# push a constant #index from a constant pool (double or long) onto the stack
# (wide index is constructed as indexbyte1 << 8 + indexbyte2)

class LDIV(Opcode):
    def __init__(self):
        super(LDIV, self).__init__(0x6d)
# value1, value2 → result
# Divide two longs

class LLOAD(Opcode):
    def __init__(self):
        super(LLOAD, self).__init__(0x16)
# 1: index
# → value
# Load a long value from a local variable #index

class LLOAD_0(Opcode):
    def __init__(self):
        super(LLOAD_0, self).__init__(0x1e)
# → value
# Load a long value from a local variable 0

class LLOAD_1(Opcode):
    def __init__(self):
        super(LLOAD_1, self).__init__(0x1f)
# → value
# Load a long value from a local variable 1

class LLOAD_2(Opcode):
    def __init__(self):
        super(LLOAD_2, self).__init__(0x20)
# → value
# Load a long value from a local variable 2

class LLOAD_3(Opcode):
    def __init__(self):
        super(LLOAD_3, self).__init__(0x21)
# → value
# Load a long value from a local variable 3

class LMUL(Opcode):
    def __init__(self):
        super(LMUL, self).__init__(0x69)
# value1, value2 → result multiply two longs

class LNEG(Opcode):
    def __init__(self):
        super(LNEG, self).__init__(0x75)
# value → result  negate a long

class LOOKUPSWITCH(Opcode):
    def __init__(self):
        super(LOOKUPSWITCH, self).__init__(0xab)
# 4+: <0-3 bytes padding>, defaultbyte1, defaultbyte2, defaultbyte3, defaultbyte4, npairs1, npairs2, npairs3, npairs4, match-offset pairs...
# key →
# A target address is looked up from a table using a key and execution continues
# from the instruction at that address

class LOR(Opcode):
    def __init__(self):
        super(LOR, self).__init__(0x81)
# value1, value2 → result
# Bitwise or of two longs

class LREM(Opcode):
    def __init__(self):
        super(LREM, self).__init__(0x71)
# value1, value2 → result
# Remainder of division of two longs

class LRETURN(Opcode):
    def __init__(self):
        super(LRETURN, self).__init__(0xad)
# value → [empty] return a long value

class LSHL(Opcode):
    def __init__(self):
        super(LSHL, self).__init__(0x79)
# value1, value2 → result
# Bitwise shift left of a long value1 by int value2 positions

class LSHR(Opcode):
    def __init__(self):
        super(LSHR, self).__init__(0x7b)
# value1, value2 → result
# Bitwise shift right of a long value1 by int value2 positions

class LSTORE(Opcode):
    def __init__(self):
        super(LSTORE, self).__init__(0x37)
# 1: index
# value →
# Store a long value in a local variable #index

class LSTORE_0(Opcode):
    def __init__(self):
        super(LSTORE_0, self).__init__(0x3f)
# value →
# Store a long value in a local variable 0

class LSTORE_1(Opcode):
    def __init__(self):
        super(LSTORE_1, self).__init__(0x40)
# value →
# Store a long value in a local variable 1

class LSTORE_2(Opcode):
    def __init__(self):
        super(LSTORE_2, self).__init__(0x41)
# value →
# Store a long value in a local variable 2

class LSTORE_3(Opcode):
    def __init__(self):
        super(LSTORE_3, self).__init__(0x42)
# value →
# Store a long value in a local variable 3

class LSUB(Opcode):
    def __init__(self):
        super(LSUB, self).__init__(0x65)
# value1, value2 → result subtract two longs

class LUSHR(Opcode):
    def __init__(self):
        super(LUSHR, self).__init__(0x7d)
# value1, value2 → result
# Bitwise shift right of a long value1 by int value2 positions, unsigned

class LXOR(Opcode):
    def __init__(self):
        super(LXOR, self).__init__(0x83)
# value1, value2 → result
# Bitwise exclusive or of two longs

class MONITORENTER(Opcode):
    def __init__(self):
        super(MONITORENTER, self).__init__(0xc2)
# objectref →
# Enter monitor for object ("grab the lock" - start of synchronized() section)

class MONITOREXIT(Opcode):
    def __init__(self):
        super(MONITOREXIT, self).__init__(0xc3)
# objectref →
# Exit monitor for object ("release the lock" - end of synchronized() section)

class MULTIANEWARRAY(Opcode):
    def __init__(self):
        super(MULTIANEWARRAY, self).__init__(0xc5)
# 3: indexbyte1, indexbyte2, dimensions
# count1, [count2,...] → arrayref
# Create a new array of dimensions dimensions with elements of type identified
# by class reference in constant pool index (indexbyte1 << 8 + indexbyte2); the
# sizes of each dimension is identified by count1, [count2, etc.]

class NEW(Opcode):
    def __init__(self):
        super(NEW, self).__init__(0xbb)
# 2: indexbyte1, indexbyte2   → objectref
# Create new object of type identified by class reference in constant pool index
# (indexbyte1 << 8 + indexbyte2)

class NEWARRAY(Opcode):
    def __init__(self):
        super(NEWARRAY, self).__init__(0xbc)
# 1: atype
# count → arrayref
# Create new array with count elements of primitive type identified by atype

class NOP(Opcode):
    def __init__(self):
        super(NOP, self).__init__(0x00)
# [No change]
# Perform no operation

class POP(Opcode):
    def __init__(self):
        super(POP, self).__init__(0x57)
# value →
# Discard the top value on the stack

class POP2(Opcode):
    def __init__(self):
        super(POP2, self).__init__(0x58)
# {value2, value1} →
# Discard the top two values on the stack (or one value, if it is a double or long)

class PUTFIELD(Opcode):
    def __init__(self):
        super(PUTFIELD, self).__init__(0xb5)
# 2: indexbyte1, indexbyte2
# objectref, value →
# Set field to value in an object objectref, where the field is identified by a
# field reference index in constant pool (indexbyte1 << 8 + indexbyte2)

class PUTSTATIC(Opcode):
    def __init__(self):
        super(PUTSTATIC, self).__init__(0xb3)
# 2: indexbyte1, indexbyte2
# value →
# Set static field to value in a class, where the field is identified by a field
# reference index in constant pool (indexbyte1 << 8 + indexbyte2)

class RET(Opcode):
    def __init__(self):
        super(RET, self).__init__(0xa9)
# 1: index
# [No change]
# Continue execution from address taken from a local variable #index (the
# asymmetry with jsr is intentional)


class RETURN(Opcode):
    # Return void from method
    # Stack:→ [empty]
    def __init__(self):
        super(RETURN, self).__init__(0xb1)


class SALOAD(Opcode):
    def __init__(self):
        super(SALOAD, self).__init__(0x35)
# arrayref, index → value
# Load short from array

class SASTORE(Opcode):
    def __init__(self):
        super(SASTORE, self).__init__(0x56)
# arrayref, index, value →
# Store short to array

class SIPUSH(Opcode):
    def __init__(self):
        super(SIPUSH, self).__init__(0x11)
# 2: byte1, byte2
# → value push a short onto the stack

class SWAP(Opcode):
    def __init__(self):
        super(SWAP, self).__init__(0x5f)
# value2, value1 → value1, value2
# Swaps two top words on the stack (note that value1 and value2 must not be
# double or long)

class TABLESWITCH(Opcode):
    def __init__(self):
        super(TABLESWITCH, self).__init__(0xaa)
# 4+: [0-3 bytes padding], defaultbyte1, defaultbyte2, defaultbyte3, defaultbyte4, lowbyte1, lowbyte2, lowbyte3, lowbyte4, highbyte1, highbyte2, highbyte3, highbyte4, jump offsets...
# index →
# continue execution from an address in the table at offset index

class WIDE(Opcode):
    def __init__(self):
        super(WIDE, self).__init__(0xc4)
# 3/5: Opcode, indexbyte1, indexbyte2
# or
# iinc, indexbyte1, indexbyte2, countbyte1, countbyte2
# Execute Opcode, where Opcode is either iload, fload, aload, lload, dload,
# istore, fstore, astore, lstore, dstore, or ret, but assume the index is 16
# bit; or execute iinc, where the index is 16 bits and the constant to
# increment by is a signed 16 bit short
