from .constants import Utf8, Classref, NameAndType
from .opcodes import Opcode
from .signatures import method_descriptor

# From: http://docs.oracle.com/javase/specs/jvms/se7/html/jvms-4.html

##########################################################################
# 4.7. Attributes
##########################################################################

# Attributes are used in the ClassFile, field_info, method_info, and
# Code_attribute structures (§4.1, §4.5, §4.6, §4.7.3) of the class file format.


class Attribute:
    # u2 attribute_name_index;
    # u4 attribute_length;
    # u1 info[attribute_length];

    def __init__(self):
        self.name = Utf8(self.__class__.__name__)

    def __repr__(self):
        return '<%s>' % self.__class__.__name__

    @staticmethod
    def read(reader, dump=None):
        name = reader.constant_pool[reader.read_u2()].bytes.decode('utf8')
        size = reader.read_u4()
        if dump is not None:
            reader.debug("    " * dump, '%s (%s bytes)' % (name, size))

        try:
            return globals()[name].read_info(reader, dump + 1 if dump is not None else dump)
        except KeyError:
            # Unknown attribute - just read the bytes and ignore them.
            if dump is not None:
                reader.debug("    " * (dump + 1), 'Reading and ignoring %s bytes' % size)

            reader.read_bytes(size)

    def write(self, writer):
        writer.write_u2(writer.constant_pool.index(self.name))
        writer.write_u4(len(self))
        self.write_info(writer)

    def write_info(self, writer):
        pass

    def resolve(self, constant_pool):
        constant_pool.add(self.name)
        self.resolve_info(constant_pool)

    def resolve_info(self, constant_pool):
        pass

# For all attributes, the attribute_name_index must be a valid unsigned 16-bit
# index into the constant pool of the class. The constant_pool entry at
# attribute_name_index must be a CONSTANT_Utf8_info structure (§4.4.7)
# representing the name of the attribute. The value of the attribute_length item
# indicates the length of the subsequent information in bytes. The length does
# not include the initial six bytes that contain the attribute_name_index and
# attribute_length items.

# Certain attributes are predefined as part of the class file specification.
# They are listed in Table 4.6, accompanied by the version of the Java SE
# platform and the version of the class file format in which each first
# appeared. Within the context of their use in this specification, that is, in
# the attributes tables of the class file structures in which they appear, the
# names of these predefined attributes are reserved. Of the predefined
# attributes:

# The ConstantValue, Code and Exceptions attributes must be recognized and
# correctly read by a class file reader for correct interpretation of the class
# file by a Java Virtual Machine implementation.

# The InnerClasses, EnclosingMethod and Synthetic attributes must be recognized
# and correctly read by a class file reader in order to properly implement the
# Java SE platform class libraries (§2.12).

# The RuntimeVisibleAnnotations, RuntimeInvisibleAnnotations,
# RuntimeVisibleParameterAnnotations, RuntimeInvisibleParameterAnnotations and
# AnnotationDefault attributes must be recognized and correctly read by a class
# file reader in order to properly implement the Java SE platform class
# libraries (§2.12), if the class file's version number is 49.0 or above and the
# Java Virtual Machine implementation recognizes class files whose version
# number is 49.0 or above.

# The Signature attribute must be recognized and correctly read by a class file
# reader if the class file's version number is 49.0 or above and the Java
# Virtual Machine implementation recognizes class files whose version number is
# 49.0 or above.

# The StackMapTable attribute must be recognized and correctly read by a class
# file reader if the class file's version number is 50.0 or above and the Java
# Virtual Machine implementation recognizes class files whose version number is
# 50.0 or above.

# The BootstrapMethods attribute must be recognized and correctly read by a
# class file reader if the class file's version number is 51.0 or above and the
# Java Virtual Machine implementation recognizes class files whose version
# number is 51.0 or above.

# Use of the remaining predefined attributes is optional; a class file reader
# may use the information they contain, or otherwise must silently ignore those
# attributes.

# Table 4.6. Predefined class file attributes

# Attribute   Section Java SE class file
# ConstantValue   §4.7.2  1.0.2   45.3
# Code    §4.7.3  1.0.2   45.3
# StackMapTable   §4.7.4  6   50.0
# Exceptions  §4.7.5  1.0.2   45.3
# InnerClasses    §4.7.6  1.1 45.3
# EnclosingMethod §4.7.7  5.0 49.0
# Synthetic   §4.7.8  1.1 45.3
# Signature   §4.7.9  5.0 49.0
# SourceFile  §4.7.10 1.0.2   45.3
# SourceDebugExtension    §4.7.11 5.0 49.0
# LineNumberTable §4.7.12 1.0.2   45.3
# LocalVariableTable  §4.7.13 1.0.2   45.3
# LocalVariableTypeTable  §4.7.14 5.0 49.0
# Deprecated  §4.7.15 1.1 45.3
# RuntimeVisibleAnnotations   §4.7.16 5.0 49.0
# RuntimeInvisibleAnnotations §4.7.17 5.0 49.0
# RuntimeVisibleParameterAnnotations  §4.7.18 5.0 49.0
# RuntimeInvisibleParameterAnnotations    §4.7.19 5.0 49.0
# AnnotationDefault   §4.7.20 5.0 49.0
# BootstrapMethods    §4.7.21 7   51.0

# ------------------------------------------------------------------------
# 4.7.1. Defining and Naming New Attributes
# ------------------------------------------------------------------------

# Compilers are permitted to define and emit class files containing new
# attributes in the attributes tables of class file structures. Java Virtual
# Machine implementations are permitted to recognize and use new attributes
# found in the attributes tables of class file structures. However, any
# attribute not defined as part of this Java Virtual Machine specification must
# not affect the semantics of class or interface types. Java Virtual Machine
# implementations are required to silently ignore attributes they do not
# recognize.

# For instance, defining a new attribute to support vendor-specific debugging is
# permitted. Because Java Virtual Machine implementations are required to ignore
# attributes they do not recognize, class files intended for that particular
# Java Virtual Machine implementation will be usable by other implementations
# even if those implementations cannot make use of the additional debugging
# information that the class files contain.

# Java Virtual Machine implementations are specifically prohibited from throwing
# an exception or otherwise refusing to use class files simply because of the
# presence of some new attribute. Of course, tools operating on class files may
# not run correctly if given class files that do not contain all the attributes
# they require.

# Two attributes that are intended to be distinct, but that happen to use the
# same attribute name and are of the same length, will conflict on
# implementations that recognize either attribute. Attributes defined other than
# in this specification must have names chosen according to the package naming
# convention described in The Java Language Specification, Java SE 7 Edition
# (JLS §6.1).

# Future versions of this specification may define additional attributes.

# ------------------------------------------------------------------------
# 4.7.2. The ConstantValue Attribute
# ------------------------------------------------------------------------

# The ConstantValue attribute is a fixed-length attribute in the attributes table of a field_info structure (§4.5). A ConstantValue attribute represents the value of a constant field. There can be no more than one ConstantValue attribute in the attributes table of a given field_info structure. If the field is static (that is, the ACC_STATIC flag (Table 4.4) in the access_flags item of the field_info structure is set) then the constant field represented by the field_info structure is assigned the value referenced by its ConstantValue attribute as part of the initialization of the class or interface declaring the constant field (§5.5). This occurs prior to the invocation of the class or interface initialization method (§2.9) of that class or interface.

# If a field_info structure representing a non-static field has a ConstantValue attribute, then that attribute must silently be ignored. Every Java Virtual Machine implementation must recognize ConstantValue attributes.

# The ConstantValue attribute has the following format:

# ConstantValue_attribute {
#     u2 attribute_name_index;
#     u4 attribute_length;
#     u2 constantvalue_index;
# }
# The items of the ConstantValue_attribute structure are as follows:

# attribute_name_index
# The value of the attribute_name_index item must be a valid index into the constant_pool table. The constant_pool entry at that index must be a CONSTANT_Utf8_info (§4.4.7) structure representing the string "ConstantValue".

# attribute_length
# The value of the attribute_length item of a ConstantValue_attribute structure must be 2.

# constantvalue_index
# The value of the constantvalue_index item must be a valid index into the constant_pool table. The constant_pool entry at that index gives the constant value represented by this attribute. The constant_pool entry must be of a type appropriate to the field, as shown by Table 4.7.

# Table 4.7. Constant value attribute types

# Field Type  Entry Type
# long    CONSTANT_Long
# float   CONSTANT_Float
# double  CONSTANT_Double
# int, short, char, byte, boolean CONSTANT_Integer
# String  CONSTANT_String

# ------------------------------------------------------------------------
# 4.7.3. The Code Attribute
# ------------------------------------------------------------------------

# The Code attribute is a variable-length attribute in the attributes table of a
# method_info (§4.6) structure. A Code attribute contains the Java Virtual
# Machine instructions and auxiliary information for a single method, instance
# initialization method (§2.9), or class or interface initialization method
# (§2.9). Every Java Virtual Machine implementation must recognize Code
# attributes. If the method is either native or abstract, its method_info
# structure must not have a Code attribute. Otherwise, its method_info structure
# must have exactly one Code attribute.


class ExceptionInfo:
    def __init__(self, start_pc, end_pc, handler_pc, catch_type):
        # The values of the two items start_pc and end_pc indicate the ranges in
        # the code array at which the exception handler is active. The value of
        # start_pc must be a valid index into the code array of the opcode of an
        # instruction. The value of end_pc either must be a valid index into the
        # code array of the opcode of an instruction or must be equal to
        # code_length, the length of the code array. The value of start_pc must
        # be less than the value of end_pc.

        # The start_pc is inclusive and end_pc is exclusive; that is, the
        # exception handler must be active while the program counter is within
        # the interval [start_pc, end_pc).

        # The fact that end_pc is exclusive is a historical mistake in the
        # design of the Java Virtual Machine: if the Java Virtual Machine code
        # for a method is exactly 65535 bytes long and ends with an instruction
        # that is 1 byte long, then that instruction cannot be protected by an
        # exception handler. A compiler writer can work around this bug by
        # limiting the maximum size of the generated Java Virtual Machine code
        # for any method, instance initialization method, or static initializer
        # (the size of any code array) to 65534 bytes.
        self.start_pc = start_pc
        self.end_pc = end_pc

        # The value of the handler_pc item indicates the start of the exception
        # handler. The value of the item must be a valid index into the code
        # array and must be the index of the opcode of an instruction.
        self.handler_pc = handler_pc

        # If the value of the catch_type item is nonzero, it must be a valid
        # index into the constant_pool table. The constant_pool entry at that
        # index must be a CONSTANT_Class_info structure (§4.4.1) representing a
        # class of exceptions that this exception handler is designated to
        # catch. The exception handler will be called only if the thrown
        # exception is an instance of the given class or one of its subclasses.

        # If the value of the catch_type item is zero, this exception handler is
        # called for all exceptions. This is used to implement finally (§3.13).
        if catch_type is None:
            self.catch_type = None
        else:
            self.catch_type = Classref(catch_type)

    @staticmethod
    def read(reader, dump=None):
        start_pc = reader.read_u2()
        end_pc = reader.read_u2()
        handler_pc = reader.read_u2()
        item = reader.read_u2()
        if item != 0:
            catch_type = reader.constant_pool[item].name.bytes.decode('utf8')
        else:
            catch_type = None

        if dump is not None:
            reader.debug("    " * dump, '%s: %s-%s [%s]' % (
                catch_type if catch_type else 'finally', start_pc, end_pc, handler_pc,
            ))

        return ExceptionInfo(start_pc, end_pc, handler_pc, catch_type)

    def write(self, writer):
        writer.write_u2(self.start_pc)
        writer.write_u2(self.end_pc)
        writer.write_u2(self.handler_pc)
        if self.catch_type is None:
            writer.write_u2(0)
        else:
            writer.write_u2(writer.constant_pool.index(self.catch_type))

    def resolve(self, constant_pool):
        if self.catch_type:
            self.catch_type.resolve(constant_pool)

    def __len__(self):
        return 2 + 2 + 2 + 2


class Code(Attribute):
    # u2 attribute_name_index;
    # u4 attribute_length;
    # u2 max_stack;
    # u2 max_locals;
    # u4 code_length;
    # u1 code[code_length];
    # u2 exception_table_length;
    # {   u2 start_pc;
    #     u2 end_pc;
    #     u2 handler_pc;
    #     u2 catch_type;
    # } exception_table[exception_table_length];
    # u2 attributes_count;
    # attribute_info attributes[attributes_count];

    def __init__(self, max_stack, max_locals, code, exceptions=None, attributes=None):
        super(Code, self).__init__()
        # The value of the max_stack item gives the maximum depth of the operand
        # stack of this method (§2.6.2) at any point during execution of the
        # method.
        self.max_stack = max_stack

        # The value of the max_locals item gives the number of local variables
        # in the local variable array allocated upon invocation of this method
        # (§2.6.1), including the local variables used to pass parameters to the
        # method on its invocation.

        # The greatest local variable index for a value of type long or double
        # is max_locals - 2. The greatest local variable index for a value of
        # any other type is max_locals - 1.
        self.max_locals = max_locals

        # The code array gives the actual bytes of Java Virtual Machine code
        # that implement the method.

        # When the code array is read into memory on a byte-addressable machine,
        # if the first byte of the array is aligned on a 4-byte boundary, the
        # tableswitch and lookupswitch 32-bit offsets will be 4-byte aligned.
        # (Refer to the descriptions of those instructions for more information
        # on the consequences of code array alignment.)

        # The detailed constraints on the contents of the code array are
        # extensive and are given in a separate section (§4.9).
        self.code = code

        # Each entry in the exception_table array describes one exception
        # handler in the code array. The order of the handlers in the
        # exception_table array is significant (§2.10).
        self.exception_table = exceptions if exceptions else []

        # Each value of the attributes table must be an attribute structure
        # (§4.7). A Code attribute can have any number of optional attributes
        # associated with it.

        # The only attributes defined by this specification as appearing in the
        # attributes table of a Code attribute are the LineNumberTable
        # (§4.7.12), LocalVariableTable (§4.7.13), LocalVariableTypeTable
        # (§4.7.14), and StackMapTable (§4.7.4) attributes.

        # If a Java Virtual Machine implementation recognizes class files whose
        # version number is 50.0 or above, it must recognize and correctly read
        # StackMapTable (§4.7.4) attributes found in the attributes table of a
        # Code attribute of a class file whose version number is 50.0 or above.

        # A Java Virtual Machine implementation is required to silently ignore
        # any or all attributes in the attributes table of a Code attribute that
        # it does not recognize. Attributes not defined in this specification
        # are not allowed to affect the semantics of the class file, but only to
        # provide additional descriptive information (§4.7.1).
        self.attributes = attributes if attributes else []

    def __len__(self):
        return (
            2 +  # max_stack
            2 +  # max_locals
            4 +  # code_length
            self.code_length +  # code
            2 +  # exception_table_length
            sum(len(e) for e in self.exception_table) +  # exception table
            2 +  # attributes_count
            sum(6 + len(a) for a in self.attributes)  # attributes
        )

    def __repr__(self):
        return '<Code (%d opcodes)>' % len(self.code)

    @staticmethod
    def read_info(reader, dump=None):
        max_stack = reader.read_u2()
        max_locals = reader.read_u2()

        if dump is not None:
            reader.debug("    " * dump, 'Max stack: %s' % max_stack)
            reader.debug("    " * dump, 'Max locals: %s' % max_locals)

        code_length = reader.read_u4()
        if dump is not None:
            reader.debug("    " * dump, 'Bytecode: (%d bytes)' % code_length)

        code = []
        i = 0
        reader.depth = 0
        while i < code_length:
            reader.offset = i
            opcode = Opcode.read(reader, dump=dump + 1 if dump is not None else dump)
            code.append(opcode)
            i += len(opcode)

        exception_table_length = reader.read_u2()
        if dump is not None:
            reader.debug("    " * dump, 'Exceptions: (%d)' % exception_table_length)

        exceptions = []
        for i in range(0, exception_table_length):
            exceptions.append(ExceptionInfo.read(reader, dump=dump + 1 if dump is not None else dump))

        attributes_count = reader.read_u2()
        if dump is not None:
            reader.debug("    " * dump, 'Attributes: (%s)' % attributes_count)

        attributes = []
        for i in range(0, attributes_count):
            attributes.append(Attribute.read(reader, dump=dump + 1 if dump is not None else dump))

        return Code(max_stack, max_locals, code, exceptions=exceptions, attributes=attributes)

    def write_info(self, writer):
        writer.write_u2(self.max_stack)
        writer.write_u2(self.max_locals)

        writer.write_u4(self.code_length)
        for opcode in self.code:
            opcode.write(writer)

        writer.write_u2(self.exception_table_length)
        for exception in self.exception_table:
            exception.write(writer)

        writer.write_u2(self.attributes_count)
        for attribute in self.attributes:
            attribute.write(writer)

    def resolve_info(self, constant_pool):
        for opcode in self.code:
            opcode.resolve(constant_pool)

        for attribute in self.attributes:
            attribute.resolve(constant_pool)

        for exception in self.exception_table:
            exception.resolve(constant_pool)

    @property
    def code_length(self):
        """The value of the code_length item gives the number of bytes in the
        code array for this method. The value of code_length must be greater
        than zero; the code array must not be empty.
        """
        return sum(len(opcode) for opcode in self.code)

    @property
    def exception_table_length(self):
        """The value of the exception_table_length item gives the number of
        entries in the exception_table table.
        """
        return len(self.exception_table)

    @property
    def attributes_count(self):
        """The value of the attributes_count item indicates the number of
        attributes of the Code attribute.
        """
        return len(self.attributes)

# ------------------------------------------------------------------------
# 4.7.4. The StackMapTable Attribute
# ------------------------------------------------------------------------

# The StackMapTable attribute is a variable-length attribute in the attributes
# table of a Code (§4.7.3) attribute. This attribute is used during the process
# of verification by type checking (§4.10.1). A method's Code attribute may have
# at most one StackMapTable attribute.

# A StackMapTable attribute consists of zero or more stack map frames. Each
# stack map frame specifies (either explicitly or implicitly) a bytecode offset,
# the verification types (§4.10.1.2) for the local variables, and the
# verification types for the operand stack.

# The type checker deals with and manipulates the expected types of a method's
# local variables and operand stack. Throughout this section, a location refers
# to either a single local variable or to a single operand stack entry.

# We will use the terms stack map frame and type state interchangeably to
# describe a mapping from locations in the operand stack and local variables of
# a method to verification types. We will usually use the term stack map frame
# when such a mapping is provided in the class file, and the term type state
# when the mapping is used by the type checker.

# In a class file whose version number is greater than or equal to 50.0, if a
# method's Code attribute does not have a StackMapTable attribute, it has an
# implicit stack map attribute. This implicit stack map attribute is equivalent
# to a StackMapTable attribute with number_of_entries equal to zero.


class StackMapTable(Attribute):
    # The StackMapTable attribute has the following format:

    # u2 attribute_name_index;
    # u4 attribute_length;
    # u2 number_of_entries;
    # stack_map_frame entries[number_of_entries];

    def __init__(self, entries=None):
        super(StackMapTable, self).__init__()

        # The entries array gives the method's stack_map_frame structures.

        # Each stack_map_frame structure specifies the type state at a
        # particular bytecode offset. Each frame type specifies (explicitly or
        # implicitly) a value, offset_delta, that is used to calculate the
        # actual bytecode offset at which a frame applies. The bytecode offset
        # at which a frame applies is calculated by adding offset_delta + 1 to
        # the bytecode offset of the previous frame, unless the previous frame
        # is the initial frame of the method, in which case the bytecode offset
        # is offset_delta.

        # By using an offset delta rather than the actual bytecode offset we
        # ensure, by definition, that stack map frames are in the correctly
        # sorted order. Furthermore, by consistently using the formula
        # offset_delta + 1 for all explicit frames, we guarantee the absence of
        # duplicates.

        # We say that an instruction in the bytecode has a corresponding stack
        # map frame if the instruction starts at offset i in the code array of a
        # Code attribute, and the Code attribute has a StackMapTable attribute
        # whose entries array has a stack_map_frame structure that applies at
        # bytecode offset i.

        # The stack_map_frame structure consists of a one-byte tag followed by
        # zero or more bytes, giving more information, depending upon the tag.
        self.entries = entries if entries is not None else []

    def __repr__(self):
        return '<StackMapTable (%d entries)>' % self.number_of_entries

    def __len__(self):
        return 2 + sum(len(entry) for entry in self.entries)

    @property
    def number_of_entries(self):
        """The value of the number_of_entries item gives the number of
        # stack_map_frame entries in the entries table.
        """
        return len(self.entries)

    @staticmethod
    def read_info(reader, dump=None):
        number_of_entries = reader.read_u2()
        if dump is not None:
            reader.debug("    " * dump, 'Entries: (%d entries)' % number_of_entries)

        entries = []
        for i in range(0, number_of_entries):
            entries.append(StackMapFrame.read(reader, dump=dump + 1 if dump is not None else dump))

        return StackMapTable(entries)

    def write_info(self, writer):
        writer.write_u2(self.number_of_entries)
        for entry in self.entries:
            entry.write(writer)

    def resolve_info(self, constant_pool):
        for entry in self.entries:
            entry.resolve(constant_pool)


# A stack map frame may belong to one of several frame types:

class StackMapFrame:
    def __init__(self, frame_type):
        self.frame_type = frame_type

    @staticmethod
    def read(reader, dump=None):
        frame_type = reader.read_u1()
        if 0 <= frame_type <= 63:
            frameClass = SameFrame
        elif 64 <= frame_type <= 127:
            frameClass = SameLocals1StackItemFrame
        elif frame_type == 247:
            frameClass = SameLocals1StackItemFrameExtended
        elif 248 <= frame_type <= 250:
            frameClass = ChopFrame
        elif frame_type == 251:
            frameClass = SameFrameExtended
        elif 252 <= frame_type <= 254:
            frameClass = AppendFrame
        elif frame_type == 255:
            frameClass = FullFrame
        else:
            raise Exception("Unknown frame class %s" % frame_type)

        stack_map_frame = frameClass.read_info(reader, frame_type)

        if dump is not None:
            reader.debug("    " * dump, str(stack_map_frame))

        return stack_map_frame

    def write(self, writer):
        writer.write_u1(self.frame_type)
        self.write_info(writer)

    def write_info(self, writer):
        pass

    def resolve(self, constant_pool):
        pass


# All frame types, even full_frame, rely on the previous frame for some of
# their semantics. This raises the question of what is the very first frame?
# The initial frame is implicit, and computed from the method descriptor. (See
# the Prolog predicate methodInitialStackFrame (§4.10.1.6).)


class SameFrame(StackMapFrame):
    # The frame type same_frame is represented by tags in the range [0-63]. If
    # the frame type is same_frame, it means the frame has exactly the same
    # locals as the previous stack map frame and that the number of stack
    # items is zero. The offset_delta value for the frame is the value of the
    # tag item, frame_type.

    # u1 frame_type = SAME; /* 0-63 */

    def __init__(self, offset_delta):
        super().__init__(offset_delta)

    def __repr__(self):
        return '<SameFrame %s>' % self.frame_type

    def __len__(self):
        return 1

    @property
    def offset_delta(self):
        return self.frame_type

    @staticmethod
    def read_info(reader, frame_type):
        return SameFrame(frame_type)


class SameLocals1StackItemFrame(StackMapFrame):
    # The frame type same_locals_1_stack_item_frame is represented by tags in
    # the range [64, 127]. If the frame_type is
    # same_locals_1_stack_item_frame, it means the frame has exactly the same
    # locals as the previous stack map frame and that the number of stack
    # items is 1. The offset_delta value for the frame is the value
    # (frame_type - 64). There is a verification_type_info following the
    # frame_type for the one stack item.

    # u1 frame_type = SAME_LOCALS_1_STACK_ITEM; /* 64-127 */
    # verification_type_info stack[1];

    def __init__(self, offset_delta, stack):
        super().__init__(offset_delta + 64)
        self.stack = stack

    def __repr__(self):
        return '<SameLocals1StackItemFrame %s %s>' % (self.offset_delta, self.stack)

    def __len__(self):
        return 1 + len(self.stack)

    @property
    def offset_delta(self):
        return self.frame_type - 64

    @staticmethod
    def read_info(reader, frame_type):
        stack = VerificationTypeInfo.read(reader)
        return SameLocals1StackItemFrame(frame_type - 64, stack)

    def write_info(self, writer):
        self.stack.write(writer)

    def resolve(self, constant_pool):
        self.stack.resolve(constant_pool)


# Tags in the range [128-246] are reserved for future use.


class SameLocals1StackItemFrameExtended(StackMapFrame):
    # The frame type same_locals_1_stack_item_frame_extended is represented by
    # the tag 247. The frame type same_locals_1_stack_item_frame_extended
    # indicates that the frame has exactly the same locals as the previous
    # stack map frame and that the number of stack items is 1. The
    # offset_delta value for the frame is given explicitly. There is a
    # verification_type_info following the frame_type for the one stack item.

    # u1 frame_type = SAME_LOCALS_1_STACK_ITEM_EXTENDED; /* 247 */
    # u2 offset_delta;
    # verification_type_info stack[1];

    def __init__(self, offset_delta, stack):
        super().__init__(247)
        self.offset_delta = offset_delta
        self.stack = stack

    def __repr__(self):
        return '<SameLocals1StackItemFrameExtended %s>' % self.offset_delta

    def __len__(self):
        return 3 + len(self.stack)

    @staticmethod
    def read_info(reader, frame_type):
        offset_delta = reader.read_u2()
        stack = VerificationTypeInfo.read(reader)
        return SameLocals1StackItemFrameExtended(offset_delta, stack)

    def write_info(self, writer):
        writer.write_u2(self.offset_delta)
        self.stack.write(writer)

    def resolve(self, constant_pool):
        self.stack.resolve(constant_pool)


class ChopFrame(StackMapFrame):
    # The frame type chop_frame is represented by tags in the range [248-250].
    # If the frame_type is chop_frame, it means that the operand stack is
    # empty and the current locals are the same as the locals in the previous
    # frame, except that the k last locals are absent. The value of k is given
    # by the formula 251 - frame_type.

    # u1 frame_type = CHOP; /* 248-250 */
    # u2 offset_delta;

    def __init__(self, k, offset_delta):
        super().__init__(251-k)
        self.offset_delta = offset_delta

    def __repr__(self):
        return '<ChopFrame %s, k=%s>' % (self.offset_delta, self.k)

    def __len__(self):
        return 3

    @property
    def k(self):
        return 251 - self.frame_type

    @staticmethod
    def read_info(reader, frame_type):
        offset_delta = reader.read_u2()
        return ChopFrame(251 - frame_type, offset_delta)

    def write_info(self, writer):
        writer.write_u2(self.offset_delta)


class SameFrameExtended(StackMapFrame):
    # The frame type same_frame_extended is represented by the tag value 251.
    # If the frame type is same_frame_extended, it means the frame has exactly
    # the same locals as the previous stack map frame and that the number of
    # stack items is zero.

    # u1 frame_type = SAME_FRAME_EXTENDED; /* 251 */
    # u2 offset_delta;

    def __init__(self, offset_delta):
        super().__init__(251)
        self.offset_delta = offset_delta

    def __repr__(self):
        return '<SameFrameExtended %s>' % self.offset_delta

    def __len__(self):
        return 3

    @property
    def k(self):
        return 251 - self.frame_type

    @staticmethod
    def read_info(reader, frame_type):
        offset_delta = reader.read_u2()
        return SameFrameExtended(offset_delta)

    def write_info(self, writer):
        writer.write_u2(self.offset_delta)


class AppendFrame(StackMapFrame):
    # The frame type append_frame is represented by tags in the range
    # [252-254]. If the frame_type is append_frame, it means that the operand
    # stack is empty and the current locals are the same as the locals in the
    # previous frame, except that k additional locals are defined. The value
    # of k is given by the formula frame_type - 251.

    # u1 frame_type = APPEND; /* 252-254 */
    # u2 offset_delta;
    # verification_type_info locals[frame_type - 251];

    # The 0th entry in locals represents the type of the first additional local
    # variable. If locals[M] represents local variable N, then locals[M+1]
    # represents local variable N+1 if locals[M] is one of:
    #
    # * Top_variable_info
    # * Integer_variable_info
    # * Float_variable_info
    # * Null_variable_info
    # * UninitializedThis_variable_info
    # * Object_variable_info
    # * Uninitialized_variable_info
    #
    # Otherwise locals[M+1] represents local variable N+2.
    #
    # It is an error if, for any index i, locals[i] represents a local
    # variable whose index is greater than the maximum number of local
    # variables for the method.

    def __init__(self, k, offset_delta, locals):
        super().__init__(k + 251)
        self.offset_delta = offset_delta
        self.locals = locals

    def __repr__(self):
        return '<AppendFrame %s, k=%s, locals=%s>' % (self.offset_delta, self.k, self.locals)

    def __len__(self):
        return 3 + sum(len(local) for local in locals)

    @property
    def k(self):
        return self.frame_type - 251

    @staticmethod
    def read_info(reader, frame_type):
        offset_delta = reader.read_u2()
        locals = []
        for i in range(0, frame_type - 251):
            locals.append(VerificationTypeInfo.read(reader))
        return AppendFrame(frame_type - 251, offset_delta, locals)

    def write_info(self, writer):
        writer.write_u2(self.offset_delta)
        for local in self.locals:
            local.write(writer)

    def resolve(self, constant_pool):
        for local in self.locals:
            local.resolve(constant_pool)


class FullFrame(StackMapFrame):
    # The frame type full_frame is represented by the tag value 255.

    # u1 frame_type = FULL_FRAME; /* 255 */
    # u2 offset_delta;
    # u2 number_of_locals;
    # verification_type_info locals[number_of_locals];
    # u2 number_of_stack_items;
    # verification_type_info stack[number_of_stack_items];

    # The 0th entry in locals represents the type of local variable 0. If
    # locals[M] represents local variable N, then locals[M+1] represents local
    # variable N+1 if locals[M] is one of:
    #
    # * Top_variable_info
    # * Integer_variable_info
    # * Float_variable_info
    # * Null_variable_info
    # * UninitializedThis_variable_info
    # * Object_variable_info
    # * Uninitialized_variable_info
    #
    # Otherwise locals[M+1] represents local variable N+2.
    #
    # It is an error if, for any index i, locals[i] represents a local
    # variable whose index is greater than the maximum number of local
    # variables for the method.
    #
    # The 0th entry in stack represents the type of the bottom of the stack,
    # and subsequent entries represent types of stack elements closer to the
    # top of the operand stack. We shall refer to the bottom element of the
    # stack as stack element 0, and to subsequent elements as stack element 1,
    # 2 etc. If stack[M] represents stack element N, then stack[M+1]
    # represents stack element N+1 if stack[M] is one of:
    #
    # * Top_variable_info
    # * Integer_variable_info
    # * Float_variable_info
    # * Null_variable_info
    # * UninitializedThis_variable_info
    # * Object_variable_info
    # * Uninitialized_variable_info
    #
    # Otherwise, stack[M+1] represents stack element N+2.
    #
    # It is an error if, for any index i, stack[i] represents a stack entry
    # whose index is greater than the maximum operand stack size for the
    # method.

    def __init__(self, offset_delta, locals, stack):
        super().__init__(255)
        self.offset_delta = offset_delta
        self.locals = locals
        self.stack = stack

    def __repr__(self):
        return '<FullFrame %s, locals=%s, stack=%s>' % (self.offset_delta, self.locals, self.stack)

    def __len__(self):
        return 7 + sum(len(local) for local in locals) + sum(len(frame) for frame in self.stack)

    @staticmethod
    def read_info(reader, frame_type):
        offset_delta = reader.read_u2()

        n_locals = reader.read_u2()
        locals = []
        for i in range(0, n_locals):
            locals.append(VerificationTypeInfo.read(reader))

        n_frames = reader.read_u2()
        stack = []
        for i in range(0, n_frames):
            stack.append(VerificationTypeInfo.read(reader))
        return FullFrame(offset_delta, locals, stack)

    def write_info(self, writer):
        writer.write_u2(self.offset_delta)
        for local in self.locals:
            local.write(writer)

    def resolve(self, constant_pool):
        for local in self.locals:
            local.resolve(constant_pool)


# The verification_type_info structure consists of a one-byte tag followed by
# zero or more bytes, giving more information about the tag. Each
# verification_type_info structure specifies the verification type of one or
# two locations.


class VerificationTypeInfo:
    ITEM_Top = 0
    ITEM_Integer = 1
    ITEM_Float = 2
    ITEM_Long = 4
    ITEM_Double = 3
    ITEM_Null = 5
    ITEM_UninitializedThis = 6
    ITEM_Object = 7
    ITEM_Uninitialized = 8

    def __init__(self, tag):
        self.tag = tag

    def __len__(self):
        return 1

    @staticmethod
    def read(reader):
        tag = reader.read_u1()

        if tag == VerificationTypeInfo.ITEM_Top:
            return TopVariableInfo()
        elif tag == VerificationTypeInfo.ITEM_Integer:
            return IntegerVariableInfo()
        elif tag == VerificationTypeInfo.ITEM_Float:
            return FloatVariableInfo()
        elif tag == VerificationTypeInfo.ITEM_Long:
            return LongVariableInfo()
        elif tag == VerificationTypeInfo.ITEM_Double:
            return DoubleVariableInfo()
        elif tag == VerificationTypeInfo.ITEM_Null:
            return NullVariableInfo()
        elif tag == VerificationTypeInfo.ITEM_UninitializedThis:
            return UninitializedThisVariableInfo()
        elif tag == VerificationTypeInfo.ITEM_Object:
            return ObjectVariableInfo.read_info(reader)
        elif tag == VerificationTypeInfo.ITEM_Uninitialized:
            return UninitializedVariableInfo.read_info(reader)
        else:
            raise Exception("Unknow verification tag type %s" % tag)

    def write(self, writer):
        writer.write_u1(self.tag)
        self.write_info(writer)

    def write_info(self, writer):
        pass

    def resolve(self, constant_pool):
        pass


class TopVariableInfo(VerificationTypeInfo):
    # The Top_variable_info type indicates that the local variable has the
    # verification type top.

    # u1 tag = ITEM_Top; /* 0 */
    def __init__(self):
        super().__init__(0)

    def __repr__(self):
        return "top"


class IntegerVariableInfo(VerificationTypeInfo):
    # The Integer_variable_info type indicates that the location contains the
    # verification type int.

    # u1 tag = ITEM_Integer; /* 1 */
    def __init__(self):
        super().__init__(1)

    def __repr__(self):
        return "Integer"


class FloatVariableInfo(VerificationTypeInfo):
    # The Float_variable_info type indicates that the location contains the
    # verification type float.

    # u1 tag = ITEM_Float; /* 2 */
    def __init__(self):
        super().__init__(2)

    def __repr__(self):
        return "Float"


class LongVariableInfo(VerificationTypeInfo):
    # The Long_variable_info type indicates that the location contains the
    # verification type long.

    # u1 tag = ITEM_Long; /* 4 */

    # This structure gives the contents of two locations in the operand stack
    # or in the local variable array.
    #
    # If the location is a local variable, then:
    # * It must not be the local variable with the highest index.
    # * The next higher numbered local variable contains the verification type
    #   top.
    #
    # If the location is an operand stack entry, then:
    # * The current location must not be the topmost location of the operand
    #   stack.
    # * The next location closer to the top of the operand stack contains the
    #   verification type top.
    def __init__(self):
        super().__init__(4)

    def __repr__(self):
        return "Long"


class DoubleVariableInfo(VerificationTypeInfo):
    # The Double_variable_info type indicates that the location contains the
    # verification type double.

    # u1 tag = ITEM_Double; /* 3 */

    # This structure gives the contents of two locations in the operand stack
    # or in the local variable array.
    #
    # If the location is a local variable, then:
    #
    # * It must not be the local variable with the highest index.
    # * The next higher numbered local variable contains the verification type
    #   top.
    #
    # If the location is an operand stack entry, then:
    #
    # * The current location must not be the topmost location of the operand
    #   stack.
    #
    # * The next location closer to the top of the operand stack contains the
    #   verification type top.
    def __init__(self):
        super().__init__(3)

    def __repr__(self):
        return "Double"


class NullVariableInfo(VerificationTypeInfo):
    # The Null_variable_info type indicates that location contains the verification type null.

    # u1 tag = ITEM_Null; /* 5 */
    def __init__(self):
        super().__init__(5)

    def __repr__(self):
        return "Null"


class UninitializedThisVariableInfo(VerificationTypeInfo):
    # The UninitializedThis_variable_info type indicates that the location
    # contains the verification type uninitializedThis.

    # u1 tag = ITEM_UninitializedThis; /* 6 */
    def __init__(self):
        super().__init__(6)

    def __repr__(self):
        return "Unitialized this"


class ObjectVariableInfo(VerificationTypeInfo):
    # The Object_variable_info type indicates that the location contains an
    # instance of the class represented by the CONSTANT_Class_info (§4.4.1)
    # structure found in the constant_pool table at the index given by
    # cpool_index.

    # u1 tag = ITEM_Object; /* 7 */
    # u2 cpool_index;
    def __init__(self, class_name):
        super().__init__(VerificationTypeInfo.ITEM_Object)
        self.class_name = class_name
        self.klass = Classref(class_name)

    def __repr__(self):
        return "Object %s" % self.klass

    def __len__(self):
        return 3

    @staticmethod
    def read_info(reader):
        val = reader.read_u2()
        klass = reader.constant_pool[val].name.bytes.decode('utf8')
        return ObjectVariableInfo(klass)

    def write_info(self, writer):
        writer.write_u2(writer.constant_pool.index(self.klass))

    def resolve(self, constant_pool):
        self.klass.resolve(constant_pool)


class UninitializedVariableInfo(VerificationTypeInfo):
    # The Uninitialized_variable_info type indicates that the location
    # contains the verification type uninitialized(offset). The offset item
    # indicates the offset, in the code array of the Code attribute (§4.7.3)
    # that contains this StackMapTable attribute, of the new instruction
    # (§new) that created the object being stored in the location.

    # u1 tag = ITEM_Uninitialized /* 8 */
    # u2 offset;
    def __init__(self, offset):
        super().__init__(VerificationTypeInfo.ITEM_Uninitialized)
        self.offset = offset

    def __repr__(self):
        return "Unitialized"

    @staticmethod
    def read_info(reader):
        offset = reader.read_u2()
        return ObjectVariableInfo(offset)

    def write_info(self, writer):
        writer.write_u2(self.offset)


# ------------------------------------------------------------------------
# 4.7.5. The Exceptions Attribute
# ------------------------------------------------------------------------

# The Exceptions attribute is a variable-length attribute in the attributes table of a method_info structure (§4.6). The Exceptions attribute indicates which checked exceptions a method may throw. There may be at most one Exceptions attribute in each method_info structure.

# The Exceptions attribute has the following format:

# Exceptions_attribute {
#     u2 attribute_name_index;
#     u4 attribute_length;
#     u2 number_of_exceptions;
#     u2 exception_index_table[number_of_exceptions];
# }
# The items of the Exceptions_attribute structure are as follows:

# attribute_name_index
# The value of the attribute_name_index item must be a valid index into the constant_pool table. The constant_pool entry at that index must be the CONSTANT_Utf8_info (§4.4.7) structure representing the string "Exceptions".

# attribute_length
# The value of the attribute_length item indicates the attribute length, excluding the initial six bytes.

# number_of_exceptions
# The value of the number_of_exceptions item indicates the number of entries in the exception_index_table.

# exception_index_table[]
# Each value in the exception_index_table array must be a valid index into the constant_pool table. The constant_pool entry referenced by each table item must be a CONSTANT_Class_info structure (§4.4.1) representing a class type that this method is declared to throw.

# A method should throw an exception only if at least one of the following three criteria is met:

# The exception is an instance of RuntimeException or one of its subclasses.

# The exception is an instance of Error or one of its subclasses.

# The exception is an instance of one of the exception classes specified in the exception_index_table just described, or one of their subclasses.

# These requirements are not enforced in the Java Virtual Machine; they are enforced only at compile-time.

# ------------------------------------------------------------------------
# 4.7.6. The InnerClasses Attribute
# ------------------------------------------------------------------------

# The InnerClasses attribute is a variable-length attribute in the attributes
# table of a ClassFile structure (§4.1). If the constant pool of a class or
# interface C contains a CONSTANT_Class_info entry which represents a class or
# interface that is not a member of a package, then C's ClassFile structure must
# have exactly one InnerClasses attribute in its attributes table.

class InnerClass:
    # Table 4.8. Nested class access and property flags

    ACC_PUBLIC = 0x0001  # Marked or implicitly public in source.
    ACC_PRIVATE = 0x0002  # Marked private in source.
    ACC_PROTECTED = 0x0004  # Marked protected in source.
    ACC_STATIC = 0x0008  # Marked or implicitly static in source.
    ACC_FINAL = 0x0010  # Marked final in source.
    ACC_INTERFACE = 0x0200  # Was an interface in source.
    ACC_ABSTRACT = 0x0400  # Marked or implicitly abstract in source.
    ACC_SYNTHETIC = 0x1000  # Declared synthetic; not present in the source code.
    ACC_ANNOTATION = 0x2000  # Declared as an annotation type.
    ACC_ENUM = 0x4000  # Declared as an enum type.

    def __init__(self, inner_class_name, outer_class_name, inner_name,
            public=True, private=False, protected=False, static=False,
            final=False, interface=False, abstract=False, synthetic=False,
            annotation=False, enum=False):

        self.public = public
        self.private = private
        self.protected = protected
        self.static = static
        self.final = final
        self.interface = interface
        self.abstract = abstract
        self.synthetic = synthetic
        self.annotation = annotation
        self.enum = enum
        # Each classes array entry contains the following four items:

        # The value of the inner_class_info_index item must be a valid index
        # into the constant_pool table. The constant_pool entry at that index
        # must be a CONSTANT_Class_info structure (§4.4.1) representing C. The
        # remaining items in the classes array entry give information about C.
        self.inner_class_name = inner_class_name
        self.inner_class = Classref(inner_class_name)

        # If C is not a member of a class or an interface (that is, if C is a
        # top-level class or interface (JLS §7.6) or a local class (JLS §14.3)
        # or an anonymous class (JLS §15.9.5)), the value of the
        # outer_class_info_index item must be zero.
        #
        # Otherwise, the value of the outer_class_info_index item must be a
        # valid index into the constant_pool table, and the entry at that index
        # must be a CONSTANT_Class_info (§4.4.1) structure representing the
        # class or interface of which C is a member.
        if outer_class_name is None:
            self.outer_class_name = None
            self.outer_class = None
        else:
            self.outer_class_name = outer_class_name
            self.outer_class = Classref(outer_class_name)

        # If C is anonymous (JLS §15.9.5), the value of the inner_name_index
        # item must be zero.
        #
        # Otherwise, the value of the inner_name_index item must be a valid
        # index into the constant_pool table, and the entry at that index must
        # be a CONSTANT_Utf8_info (§4.4.7) structure that represents the
        # original simple name of C, as given in the source code from which this
        # class file was compiled.
        if inner_name:
            self.inner_name = Utf8(inner_name)
        else:
            self.inner_name = None

    @property
    def inner_class_access_flags(self):
        # The value of the inner_class_access_flags item is a mask of flags used
        # to denote access permissions to and properties of class or interface C
        # as declared in the source code from which this class file was
        # compiled. It is used by a compiler to recover the original information
        # when source code is not available. The flags are shown in Table 4.8.
        #
        # All bits of the inner_class_access_flags item not assigned in Table
        # 4.8 are reserved for future use. They should be set to zero in
        # generated class files and should be ignored by Java Virtual Machine
        # implementations.
        return (
            (self.ACC_PUBLIC if self.public else 0) |
            (self.ACC_PRIVATE if self.private else 0) |
            (self.ACC_PROTECTED if self.protected else 0) |
            (self.ACC_STATIC if self.static else 0) |
            (self.ACC_FINAL if self.final else 0) |
            (self.ACC_INTERFACE if self.interface else 0) |
            (self.ACC_ABSTRACT if self.abstract else 0) |
            (self.ACC_SYNTHETIC if self.synthetic else 0) |
            (self.ACC_ANNOTATION if self.annotation else 0) |
            (self.ACC_ENUM if self.enum else 0)
        )


class InnerClasses(Attribute):
    # The InnerClasses attribute has the following format:

    # u2 attribute_name_index;
    # u4 attribute_length;
    # u2 number_of_classes;
    # {
    #     u2 inner_class_info_index;
    #     u2 outer_class_info_index;
    #     u2 inner_name_index;
    #     u2 inner_class_access_flags;
    # } classes[number_of_classes];

    def __init__(self, classes=None):
        super(InnerClasses, self).__init__()

        # The items of the InnerClasses_attribute structure are as follows:

        # Every CONSTANT_Class_info entry in the constant_pool table which
        # represents a class or interface C that is not a package member must
        # have exactly one corresponding entry in the classes array.

        # If a class has members that are classes or interfaces, its
        # constant_pool table (and hence its InnerClasses attribute) must refer
        # to each such member, even if that member is not otherwise mentioned by
        # the class. These rules imply that a nested class or interface member
        # will have InnerClasses information for each enclosing class and for
        # each immediate member.
        if classes:
            self.classes = classes
        else:
            self.classes = []

        # If a class file has a version number that is greater than or equal to
        # 51.0, and has an InnerClasses attribute in its attributes table, then
        # for all entries in the classes array of the InnerClasses attribute,
        # the value of the outer_class_info_index item must be zero if the value
        # of the inner_name_index item is zero.

        # Oracle's Java Virtual Machine implementation does not check the
        # consistency of an InnerClasses attribute against a class file
        # representing a class or interface referenced by the attribute.

    def __repr__(self):
        return '<EnclosingMethod %s.%s>' % (self.klass, self.method)

    def __len__(self):
        return 2 + (2 + 2 + 2 + 2) * self.number_of_classes

    @property
    def number_of_classes(self):
        # The value of the number_of_classes item indicates the number of
        # entries in the classes array.
        return len(self.classes)

    @staticmethod
    def read_info(reader, dump=None):
        n_classes = reader.read_u2()
        classes = []

        if dump is not None:
            reader.debug("    " * (dump + 1), 'Inner Classes: (%s)' % n_classes)

        for i in range(0, n_classes):
            c1 = reader.read_u2()
            inner_class = reader.constant_pool[c1].name.string
            if dump is not None:
                reader.debug("    " * (dump + 2), 'Inner Class: %s' % inner_class)

            c2 = reader.read_u2()
            if c2 == 0:
                outer_class = None
                if dump is not None:
                    reader.debug("    " * (dump + 3), 'Outer Class: (Anonymous)')
            else:
                outer_class = reader.constant_pool[c2].name.string
                if dump is not None:
                    reader.debug("    " * (dump + 3), 'Outer Class: %s' % outer_class)

            c3 = reader.read_u2()
            if c3 == 0:
                inner_name = None
            else:
                inner_name = reader.constant_pool[c3].string
                if dump is not None:
                    reader.debug("    " * (dump + 3), 'Inner Name: %s' % inner_name)

            flags = reader.read_u2()

            if dump is not None:
                access_description = ', '.join(f for f in [
                        flag if flags & mask else None
                        for flag, mask in [
                            ('public', InnerClass.ACC_PUBLIC),
                            ('private', InnerClass.ACC_PRIVATE),
                            ('protected', InnerClass.ACC_PROTECTED),
                            ('static', InnerClass.ACC_STATIC),
                            ('final', InnerClass.ACC_FINAL),
                            ('interface', InnerClass.ACC_INTERFACE),
                            ('abstract', InnerClass.ACC_ABSTRACT),
                            ('synthetic', InnerClass.ACC_SYNTHETIC),
                            ('annotation', InnerClass.ACC_ANNOTATION),
                            ('enum', InnerClass.ACC_ENUM),
                        ]
                    ] if f)
                reader.debug("    " * (dump + 3), 'Flags: 0x%04x%s' % (flags, ' (%s)') % (access_description if access_description else ''))

            classes.append(
                InnerClass(
                    inner_class,
                    outer_class,
                    inner_name,
                    public=bool(flags & InnerClass.ACC_PUBLIC),
                    private=bool(flags & InnerClass.ACC_PRIVATE),
                    protected=bool(flags & InnerClass.ACC_PROTECTED),
                    static=bool(flags & InnerClass.ACC_STATIC),
                    final=bool(flags & InnerClass.ACC_FINAL),
                    abstract=bool(flags & InnerClass.ACC_ABSTRACT),
                    synthetic=bool(flags & InnerClass.ACC_SYNTHETIC),
                    annotation=bool(flags & InnerClass.ACC_ANNOTATION),
                    enum=bool(flags & InnerClass.ACC_ENUM),
                )
            )

        return InnerClasses(classes)

    def write_info(self, writer):
        writer.write_u2(writer.constant_pool.index(self.inner_class))

        if self.outer_class:
            writer.write_u2(writer.constant_pool.index(self.outer_class))
        else:
            writer.write_u2(0)

        if self.inner_name:
            writer.write_u2(writer.constant_pool.index(self.inner_name))
        else:
            writer.write_u2(0)

    def resolve_info(self, constant_pool):
        self.inner_class.resolve(constant_pool)
        if self.outer_class:
            self.outer_class.resolve(constant_pool)
        if self.inner_name:
            self.inner_name.resolve(constant_pool)

# ------------------------------------------------------------------------
# 4.7.7. The EnclosingMethod Attribute
# ------------------------------------------------------------------------

# The EnclosingMethod attribute is an optional fixed-length attribute in the
# attributes table of a ClassFile structure (§4.1). A class must have an
# EnclosingMethod attribute if and only if it is a local class or an anonymous
# class. A class may have no more than one EnclosingMethod attribute.


class EnclosingMethod(Attribute):
    # The EnclosingMethod attribute has the following format:

    # u2 attribute_name_index;
    # u4 attribute_length;
    # u2 class_index;
    # u2 method_index;

    def __init__(self, class_name, method_name, descriptor):
        super(EnclosingMethod, self).__init__()

        # The items of the EnclosingMethod_attribute structure are as follows:

        # The value of the class_index item must be a valid index into the
        # constant_pool table. The constant_pool entry at that index must be a
        # CONSTANT_Class_info (§4.4.1) structure representing the innermost
        # class that encloses the declaration of the current class.
        self.class_name = class_name
        self.klass = Classref(class_name)

        # If the current class is not immediately enclosed by a method or
        # constructor, then the value of the method_index item must be zero.
        #
        # Otherwise, the value of the method_index item must be a valid index
        # into the constant_pool table. The constant_pool entry at that index
        # must be a CONSTANT_NameAndType_info structure (§4.4.6) representing
        # the name and type of a method in the class referenced by the
        # class_index attribute above.
        #
        # It is the responsibility of a Java compiler to ensure that the method
        # identified via the method_index is indeed the closest lexically
        # enclosing method of the class that contains this EnclosingMethod
        # attribute.
        self.method_name = method_name
        self.descriptor = method_descriptor(descriptor)

        self.method = NameAndType(method_name, descriptor)

    def __repr__(self):
        return '<EnclosingMethod %s.%s>' % (self.klass, self.method)

    def __len__(self):
        return 2 + 2

    @staticmethod
    def read_info(reader, dump=None):
        klass = reader.read_u2()
        name_and_type = reader.read_u2()

        if dump is not None:
            reader.debug("    " * dump, '%s.%s %s' % (
                reader.constant_pool[klass].name,
                reader.constant_pool[name_and_type].name,
                reader.constant_pool[name_and_type].descriptor
            ))

        return EnclosingMethod(
            reader.constant_pool[klass].name.bytes.decode('utf8'),
            reader.constant_pool[name_and_type].name.bytes.decode('utf8'),
            reader.constant_pool[name_and_type].descriptor.bytes.decode('utf8'),
        )

    def write_info(self, writer):
        writer.write_u2(writer.constant_pool.index(self.klass))
        writer.write_u2(writer.constant_pool.index(self.name_and_type))

    def resolve_info(self, constant_pool):
        self.klass.resolve(constant_pool)
        self.name_and_type.resolve(constant_pool)


# ------------------------------------------------------------------------
# 4.7.8. The Synthetic Attribute
# ------------------------------------------------------------------------

# The Synthetic attribute is a fixed-length attribute in the attributes table of
# a ClassFile, field_info, or method_info structure (§4.1, §4.5, §4.6). A class
# member that does not appear in the source code must be marked using a
# Synthetic attribute, or else it must have its ACC_SYNTHETIC flag set. The only
# exceptions to this requirement are compiler-generated methods which are not
# considered implementation artifacts, namely the instance initialization method
# representing a default constructor of the Java programming language (§2.9),
# the class initialization method (§2.9), and the Enum.values() and
# Enum.valueOf() methods.

# The Synthetic attribute was introduced in JDK release 1.1 to support nested
# classes and interfaces.

class Synthetic(Attribute):
    # The Synthetic attribute has the following format:

    # u2 attribute_name_index;
    # u4 attribute_length;
    # u2 signature_index;

    def __repr__(self):
        return '<Synthetic>'

    def __len__(self):
        return 0

    @staticmethod
    def read_info(reader, dump=None):
        return Synthetic()

    def write_info(self, writer):
        pass

    def resolve_info(self, constant_pool):
        pass

# ------------------------------------------------------------------------
# 4.7.9. The Signature Attribute
# ------------------------------------------------------------------------

# The Signature attribute is an optional fixed-length attribute in the
# attributes table of a ClassFile, field_info, or method_info structure (§4.1,
# §4.5, §4.6). The Signature attribute records generic signature information for
# any class, interface, constructor or member whose generic signature in the
# Java programming language would include references to type variables or
# parameterized types.

# The Signature attribute has the following format:


class Signature(Attribute):
    # u2 attribute_name_index;
    # u4 attribute_length;
    # u2 signature_index;

    def __init__(self, signature):
        super(Signature, self).__init__()

        # The value of the signature_index item must be a valid index into the
        # constant_pool table. The constant pool entry at that index must be a
        # CONSTANT_Utf8_info (§4.4.7) structure representing a class signature
        # (§4.3.4) if this Signature attribute is an attribute of a ClassFile
        # structure; a method signature if this Signature attribute is an
        # attribute of a method_info structure; or a field type signature
        # otherwise.
        self.signature = Utf8(signature)

    def __repr__(self):
        return '<SourceFile: %s>' % self.signature

    def __len__(self):
        return 2

    @staticmethod
    def read_info(reader, dump=None):
        signature = reader.constant_pool[reader.read_u2()].bytes.decode('utf8')

        if dump is not None:
            reader.debug("    " * dump, 'Signature: %s' % signature)

        return Signature(signature)

    def write_info(self, writer):
        writer.write_u2(writer.constant_pool.index(self.signature))

    def resolve_info(self, constant_pool):
        constant_pool.add(self.signature)

# ------------------------------------------------------------------------
# 4.7.10. The SourceFile Attribute
# ------------------------------------------------------------------------

# The SourceFile attribute is an optional fixed-length attribute in the
# attributes table of a ClassFile structure (§4.1). There can be no more than
# one SourceFile attribute in the attributes table of a given ClassFile
# structure.


class SourceFile(Attribute):
    # u2 attribute_name_index;
    # u4 attribute_length;
    # u2 sourcefile_index;

    def __init__(self, sourcefile_name):
        super(SourceFile, self).__init__()

        # The value of the sourcefile_index item must be a valid index into the
        # constant_pool table. The constant pool entry at that index must be a
        # CONSTANT_Utf8_info (§4.4.7) structure representing a string.

        # The string referenced by the sourcefile_index item will be
        # interpreted as indicating the name of the source file from which
        # this class file was compiled. It will not be interpreted as
        # indicating the name of a directory containing the file or an
        # absolute path name for the file; such platform-specific additional
        # information must be supplied by the run-time interpreter or
        # development tool at the time the file name is actually used.
        self.sourcefile_name = Utf8(sourcefile_name)

    def __repr__(self):
        return '<SourceFile: %s>' % self.sourcefile_name

    def __len__(self):
        return 2

    @staticmethod
    def read_info(reader, dump=None):
        sourcefile_name = reader.constant_pool[reader.read_u2()].bytes.decode('utf8')

        if dump is not None:
            reader.debug("    " * dump, 'Source file: %s' % sourcefile_name)

        return SourceFile(sourcefile_name)

    def write_info(self, writer):
        writer.write_u2(writer.constant_pool.index(self.sourcefile_name))

    def resolve_info(self, constant_pool):
        constant_pool.add(self.sourcefile_name)

# ------------------------------------------------------------------------
# 4.7.11. The SourceDebugExtension Attribute
# ------------------------------------------------------------------------

# The SourceDebugExtension attribute is an optional attribute in the attributes table of a ClassFile structure (§4.1). There can be no more than one SourceDebugExtension attribute in the attributes table of a given ClassFile structure.

# The SourceDebugExtension attribute has the following format:

# SourceDebugExtension_attribute {
#     u2 attribute_name_index;
#     u4 attribute_length;
#     u1 debug_extension[attribute_length];
# }
# The items of the SourceDebugExtension_attribute structure are as follows:

# attribute_name_index
# The value of the attribute_name_index item must be a valid index into the constant_pool table. The constant_pool entry at that index must be a CONSTANT_Utf8_info (§4.4.7) structure representing the string "SourceDebugExtension".

# attribute_length
# The value of the attribute_length item indicates the length of the attribute, excluding the initial six bytes.

# The value of the attribute_length item is thus the number of bytes in the debug_extension[] item.

# debug_extension[]
# The debug_extension array holds extended debugging information which has no semantic effect on the Java Virtual Machine. The information is represented using a modified UTF-8 string (§4.4.7) with no terminating zero byte.

# Note that the debug_extension array may denote a string longer than that which can be represented with an instance of class String.

# ------------------------------------------------------------------------
# 4.7.12. The LineNumberTable Attribute
# ------------------------------------------------------------------------

# The LineNumberTable attribute is an optional variable-length attribute in the
# attributes table of a Code (§4.7.3) attribute. It may be used by debuggers to
# determine which part of the Java Virtual Machine code array corresponds to a
# given line number in the original source file.
#
# If LineNumberTable attributes are present in the attributes table of a given
# Code attribute, then they may appear in any order. Furthermore, multiple
# LineNumberTable attributes may together represent a given line of a source
# file; that is, LineNumberTable attributes need not be one-to-one with source
# lines.


class LineNumberTable(Attribute):
    # u2 attribute_name_index;
    # u4 attribute_length;
    # u2 line_number_table_length;
    # {   u2 start_pc;
    #     u2 line_number;
    # } line_number_table[line_number_table_length];

    def __init__(self, line_numbers):
        super(LineNumberTable, self).__init__()

        # Each entry in the line_number_table array indicates that the line
        # number in the original source file changes at a given point in the
        # code array. Each line_number_table entry must contain the following
        # two items:
        #
        # * start_pc
        #     The value of the start_pc item must indicate the index into the code
        #     array at which the code for a new line in the original source file
        #     begins.
        #
        # * line_number
        #     The value of start_pc must be less than the value of the code_length
        #     item of the Code attribute of which this LineNumberTable is an
        #     attribute.
        #
        #     The value of the line_number item must give the corresponding line
        #     number in the original source file.
        self.line_number_table = line_numbers

    def __len__(self):
        return 2 + (2 + 2) * self.line_number_table_length

    @property
    def line_number_table_length(self):
        """The value of the line_number_table_length item indicates the number of
        entries in the line_number_table array.
        """
        return len(self.line_number_table)

    @staticmethod
    def read_info(reader, dump=None):
        line_number_table_length = reader.read_u2()

        if dump is not None:
            reader.debug("    " * dump, 'Line numbers (%s total):' % line_number_table_length)

        line_numbers = []
        for i in range(0, line_number_table_length):
            start_pc = reader.read_u2()
            line_number = reader.read_u2()
            if dump is not None:
                reader.debug("    " * (dump + 1), '%s: %s' % (start_pc, line_number))
            line_numbers.append((start_pc, line_number))

        return LineNumberTable(line_numbers)

    def write_info(self, writer):
        writer.write_u2(self.line_number_table_length)
        for start_pc, line_number in self.line_number_table:
            writer.write_u2(start_pc)
            writer.write_u2(line_number)

# ------------------------------------------------------------------------
# 4.7.13. The LocalVariableTable Attribute
# ------------------------------------------------------------------------

# The LocalVariableTable attribute is an optional variable-length attribute in the attributes table of a Code (§4.7.3) attribute. It may be used by debuggers to determine the value of a given local variable during the execution of a method.

# If LocalVariableTable attributes are present in the attributes table of a given Code attribute, then they may appear in any order. There may be no more than one LocalVariableTable attribute per local variable in the Code attribute.

# The LocalVariableTable attribute has the following format:

# LocalVariableTable_attribute {
#     u2 attribute_name_index;
#     u4 attribute_length;
#     u2 local_variable_table_length;
#     {   u2 start_pc;
#         u2 length;
#         u2 name_index;
#         u2 descriptor_index;
#         u2 index;
#     } local_variable_table[local_variable_table_length];
# }
# The items of the LocalVariableTable_attribute structure are as follows:

# attribute_name_index
# The value of the attribute_name_index item must be a valid index into the constant_pool table. The constant_pool entry at that index must be a CONSTANT_Utf8_info (§4.4.7) structure representing the string "LocalVariableTable".

# attribute_length
# The value of the attribute_length item indicates the length of the attribute, excluding the initial six bytes.

# local_variable_table_length
# The value of the local_variable_table_length item indicates the number of entries in the local_variable_table array.

# local_variable_table[]
# Each entry in the local_variable_table array indicates a range of code array offsets within which a local variable has a value. It also indicates the index into the local variable array of the current frame at which that local variable can be found. Each entry must contain the following five items:

# start_pc, length
# The given local variable must have a value at indices into the code array in the interval [start_pc, start_pc + length), that is, between start_pc inclusive and start_pc + length exclusive.

# The value of start_pc must be a valid index into the code array of this Code attribute and must be the index of the opcode of an instruction.

# The value of start_pc + length must either be a valid index into the code array of this Code attribute and be the index of the opcode of an instruction, or it must be the first index beyond the end of that code array.

# name_index
# The value of the name_index item must be a valid index into the constant_pool table. The constant_pool entry at that index must contain a CONSTANT_Utf8_info (§4.4.7) structure representing a valid unqualified name (§4.2.2) denoting a local variable.

# descriptor_index
# The value of the descriptor_index item must be a valid index into the constant_pool table. The constant_pool entry at that index must contain a CONSTANT_Utf8_info structure (§4.4.7) representing a field descriptor (§4.3.2) encoding the type of a local variable in the source program.

# index
# The given local variable must be at index in the local variable array of the current frame.

# If the local variable at index is of type double or long, it occupies both index and index + 1.

# ------------------------------------------------------------------------
# 4.7.14. The LocalVariableTypeTable Attribute
# ------------------------------------------------------------------------

# The LocalVariableTypeTable attribute is an optional variable-length attribute in the attributes table of a Code (§4.7.3) attribute. It may be used by debuggers to determine the value of a given local variable during the execution of a method.

# If LocalVariableTypeTable attributes are present in the attributes table of a given Code attribute, then they may appear in any order. There may be no more than one LocalVariableTypeTable attribute per local variable in the Code attribute.

# The LocalVariableTypeTable attribute differs from the LocalVariableTable attribute in that it provides signature information rather than descriptor information. This difference is only significant for variables whose type is a generic reference type. Such variables will appear in both tables, while variables of other types will appear only in LocalVariableTable.

# The LocalVariableTypeTable attribute has the following format:

# LocalVariableTypeTable_attribute {
#     u2 attribute_name_index;
#     u4 attribute_length;
#     u2 local_variable_type_table_length;
#     {   u2 start_pc;
#         u2 length;
#         u2 name_index;
#         u2 signature_index;
#         u2 index;
#     } local_variable_type_table[local_variable_type_table_length];
# }
# The items of the LocalVariableTypeTable_attribute structure are as follows:

# attribute_name_index
# The value of the attribute_name_index item must be a valid index into the constant_pool table. The constant_pool entry at that index must be a CONSTANT_Utf8_info (§4.4.7) structure representing the string "LocalVariableTypeTable".

# attribute_length
# The value of the attribute_length item indicates the length of the attribute, excluding the initial six bytes.

# local_variable_type_table_length
# The value of the local_variable_type_table_length item indicates the number of entries in the local_variable_type_table array.

# local_variable_type_table[]
# Each entry in the local_variable_type_table array indicates a range of code array offsets within which a local variable has a value. It also indicates the index into the local variable array of the current frame at which that local variable can be found. Each entry must contain the following five items:

# start_pc, length
# The given local variable must have a value at indices into the code array in the interval [start_pc, start_pc + length), that is, between start_pc inclusive and start_pc + length exclusive.

# The value of start_pc must be a valid index into the code array of this Code attribute and must be the index of the opcode of an instruction.

# The value of start_pc + length must either be a valid index into the code array of this Code attribute and be the index of the opcode of an instruction, or it must be the first index beyond the end of that code array.

# name_index
# The value of the name_index item must be a valid index into the constant_pool table. The constant_pool entry at that index must contain a CONSTANT_Utf8_info (§4.4.7) structure representing a valid unqualified name (§4.2.2) denoting a local variable.

# signature_index
# The value of the signature_index item must be a valid index into the constant_pool table. The constant_pool entry at that index must contain a CONSTANT_Utf8_info structure (§4.4.7) representing a field type signature (§4.3.4) encoding the type of a local variable in the source program.

# index
# The given local variable must be at index in the local variable array of the current frame.

# If the local variable at index is of type double or long, it occupies both index and index + 1.

# ------------------------------------------------------------------------
# 4.7.15. The Deprecated Attribute
# ------------------------------------------------------------------------

# The Deprecated attribute is an optional fixed-length attribute in the attributes table of a ClassFile, field_info, or method_info structure (§4.1, §4.5, §4.6). A class, interface, method, or field may be marked using a Deprecated attribute to indicate that the class, interface, method, or field has been superseded.

# A run-time interpreter or tool that reads the class file format, such as a compiler, can use this marking to advise the user that a superceded class, interface, method, or field is being referred to. The presence of a Deprecated attribute does not alter the semantics of a class or interface.

# The Deprecated attribute has the following format:

# Deprecated_attribute {
#     u2 attribute_name_index;
#     u4 attribute_length;
# }
# The items of the Deprecated_attribute structure are as follows:

# attribute_name_index
# The value of the attribute_name_index item must be a valid index into the constant_pool table. The constant_pool entry at that index must be a CONSTANT_Utf8_info (§4.4.7) structure representing the string "Deprecated".

# attribute_length
# The value of the attribute_length item is zero.

# ------------------------------------------------------------------------
# 4.7.16. The RuntimeVisibleAnnotations attribute
# ------------------------------------------------------------------------

# The RuntimeVisibleAnnotations attribute is a variable-length attribute in the attributes table of a ClassFile, field_info, or method_info structure (§4.1, §4.5, §4.6). The RuntimeVisibleAnnotations attribute records run-time-visible Java programming language annotations on the corresponding class, field, or method.

# Each ClassFile, field_info, and method_info structure may contain at most one RuntimeVisibleAnnotations attribute, which records all the run-time-visible Java programming language annotations on the corresponding program element. The Java Virtual Machine must make these annotations available so they can be returned by the appropriate reflective APIs.

# The RuntimeVisibleAnnotations attribute has the following format:

# RuntimeVisibleAnnotations_attribute {
#     u2         attribute_name_index;
#     u4         attribute_length;
#     u2         num_annotations;
#     annotation annotations[num_annotations];
# }
# The items of the RuntimeVisibleAnnotations_attribute structure are as follows:

# attribute_name_index
# The value of the attribute_name_index item must be a valid index into the constant_pool table. The constant_pool entry at that index must be a CONSTANT_Utf8_info (§4.4.7) structure representing the string "RuntimeVisibleAnnotations".

# attribute_length
# The value of the attribute_length item indicates the length of the attribute, excluding the initial six bytes.

# The value of the attribute_length item is thus dependent on the number of run-time-visible annotations represented by the structure, and their values.

# num_annotations
# The value of the num_annotations item gives the number of run-time-visible annotations represented by the structure.

# Note that a maximum of 65535 run-time-visible Java programming language annotations may be directly attached to a program element.

# annotations
# Each value of the annotations table represents a single run-time-visible annotation on a program element. The annotation structure has the following format:

# annotation {
#     u2 type_index;
#     u2 num_element_value_pairs;
#     {   u2            element_name_index;
#         element_value value;
#     } element_value_pairs[num_element_value_pairs];
# }

# The items of the annotation structure are as follows:

# type_index
# The value of the type_index item must be a valid index into the constant_pool table. The constant_pool entry at that index must be a CONSTANT_Utf8_info (§4.4.7) structure representing a field descriptor representing the annotation type corresponding to the annotation represented by this annotation structure.

# num_element_value_pairs
# The value of the num_element_value_pairs item gives the number of element-value pairs of the annotation represented by this annotation structure.

# Note that a maximum of 65535 element-value pairs may be contained in a single annotation.

# element_value_pairs
# Each value of the element_value_pairs table represents a single element-value pair in the annotation represented by this annotation structure. Each element_value_pairs entry contains the following two items:

# element_name_index
# The value of the element_name_index item must be a valid index into the constant_pool table. The constant_pool entry at that index must be a CONSTANT_Utf8_info structure (§4.4.7) representing a valid field descriptor (§4.3.2) that denotes the name of the annotation type element represented by this element_value_pairs entry.

# value
# The value of the value item represents the value of the element-value pair represented by this element_value_pairs entry.

# ------------------------------------------------------------------------
# 4.7.16.1. The element_value structure
# ------------------------------------------------------------------------

# The element_value structure is a discriminated union representing the value of an element-value pair. It is used to represent element values in all attributes that describe annotations (RuntimeVisibleAnnotations, RuntimeInvisibleAnnotations, RuntimeVisibleParameterAnnotations, and RuntimeInvisibleParameterAnnotations).

# The element_value structure has the following format:

# element_value {
#     u1 tag;
#     union {
#         u2 const_value_index;

#         {   u2 type_name_index;
#             u2 const_name_index;
#         } enum_const_value;

#         u2 class_info_index;

#         annotation annotation_value;

#         {   u2            num_values;
#             element_value values[num_values];
#         } array_value;
#     } value;
# }
# The items of the element_value structure are as follows:

# tag
# The tag item indicates the type of this annotation element-value pair.

# The letters B, C, D, F, I, J, S, and Z indicate a primitive type. These letters are interpreted as if they were field descriptors (§4.3.2).

# The other legal values for tag are listed with their interpretations in Table 4.9.

# Table 4.9. Interpretation of additional tag values

# tag Value   Element Type
# s   String
# e   enum constant
# c   class
# @   annotation type
# [   array
# value
# The value item represents the value of this annotation element. This item is a union. The tag item, above, determines which item of the union is to be used:

# const_value_index
# The const_value_index item is used if the tag item is one of B, C, D, F, I, J, S, Z, or s.

# The value of the const_value_index item must be a valid index into the constant_pool table. The constant_pool entry at that index must be of the correct entry type for the field type designated by the tag item, as specified in Table 4.9.

# enum_const_value
# The enum_const_value item is used if the tag item is e.

# The enum_const_value item consists of the following two items:

# type_name_index
# The value of the type_name_index item must be a valid index into the constant_pool table. The constant_pool entry at that index must be a CONSTANT_Utf8_info structure (§4.4.7) representing a valid field descriptor (§4.3.2) that denotes the internal form of the binary name (§4.2.1) of the type of the enum constant represented by this element_value structure.

# const_name_index
# The value of the const_name_index item must be a valid index into the constant_pool table. The constant_pool entry at that index must be a CONSTANT_Utf8_info structure (§4.4.7) representing the simple name of the enum constant represented by this element_value structure.

# class_info_index
# The class_info_index item is used if the tag item is c.

# The class_info_index item must be a valid index into the constant_pool table. The constant_pool entry at that index must be a CONSTANT_Utf8_info (§4.4.7) structure representing the return descriptor (§4.3.3) of the type that is reified by the class represented by this element_value structure.

# For example, V for Void.class, Ljava/lang/Object; for Object, etc.

# annotation_value
# The annotation_value item is used if the tag item is @.

# The element_value structure represents a "nested" annotation.

# array_value
# The array_value item is used if the tag item is [.

# The array_value item consists of the following two items:

# num_values
# The value of the num_values item gives the number of elements in the array-typed value represented by this element_value structure.

# Note that a maximum of 65535 elements are permitted in an array-typed element value.

# values
# Each value of the values table gives the value of an element of the array-typed value represented by this element_value structure.

# ------------------------------------------------------------------------
# 4.7.17. The RuntimeInvisibleAnnotations attribute
# ------------------------------------------------------------------------

# The RuntimeInvisibleAnnotations attribute is similar to the RuntimeVisibleAnnotations attribute, except that the annotations represented by a RuntimeInvisibleAnnotations attribute must not be made available for return by reflective APIs, unless the Java Virtual Machine has been instructed to retain these annotations via some implementation-specific mechanism such as a command line flag. In the absence of such instructions, the Java Virtual Machine ignores this attribute.

# The RuntimeInvisibleAnnotations attribute is a variable-length attribute in the attributes table of a ClassFile, field_info, or method_info structure (§4.1, §4.5, §4.6). The RuntimeInvisibleAnnotations attribute records run-time-invisible Java programming language annotations on the corresponding class, method, or field.

# Each ClassFile, field_info, and method_info structure may contain at most one RuntimeInvisibleAnnotations attribute, which records all the run-time-invisible Java programming language annotations on the corresponding program element.

# The RuntimeInvisibleAnnotations attribute has the following format:

# RuntimeInvisibleAnnotations_attribute {
#     u2         attribute_name_index;
#     u4         attribute_length;
#     u2         num_annotations;
#     annotation annotations[num_annotations];
# }
# The items of the RuntimeInvisibleAnnotations_attribute structure are as follows:

# attribute_name_index
# The value of the attribute_name_index item must be a valid index into the constant_pool table. The constant_pool entry at that index must be a CONSTANT_Utf8_info (§4.4.7) structure representing the string "RuntimeInvisibleAnnotations".

# attribute_length
# The value of the attribute_length item indicates the length of the attribute, excluding the initial six bytes.

# The value of the attribute_length item is thus dependent on the number of run-time-invisible annotations represented by the structure, and their values.

# num_annotations
# The value of the num_annotations item gives the number of run-time-invisible annotations represented by the structure.

# Note that a maximum of 65535 run-time-invisible Java programming language annotations may be directly attached to a program element.

# annotations
# Each value of the annotations table represents a single run-time-invisible annotation on a program element.

# ------------------------------------------------------------------------
# 4.7.18. The RuntimeVisibleParameterAnnotations attribute
# ------------------------------------------------------------------------

# The RuntimeVisibleParameterAnnotations attribute is a variable-length attribute in the attributes table of the method_info structure (§4.6). The RuntimeVisibleParameterAnnotations attribute records run-time-visible Java programming language annotations on the parameters of the corresponding method.

# Each method_info structure may contain at most one RuntimeVisibleParameterAnnotations attribute, which records all the run-time-visible Java programming language annotations on the parameters of the corresponding method. The Java Virtual Machine must make these annotations available so they can be returned by the appropriate reflective APIs.

# The RuntimeVisibleParameterAnnotations attribute has the following format:

# RuntimeVisibleParameterAnnotations_attribute {
#     u2 attribute_name_index;
#     u4 attribute_length;
#     u1 num_parameters;
#     {   u2         num_annotations;
#         annotation annotations[num_annotations];
#     } parameter_annotations[num_parameters];
# }
# The items of the RuntimeVisibleParameterAnnotations_attribute structure are as follows:

# attribute_name_index
# The value of the attribute_name_index item must be a valid index into the constant_pool table. The constant_pool entry at that index must be a CONSTANT_Utf8_info structure (§4.4.7) representing the string "RuntimeVisibleParameterAnnotations".

# attribute_length
# The value of the attribute_length item indicates the length of the attribute, excluding the initial six bytes.

# The value of the attribute_length item is thus dependent on the number of parameters, the number of run-time-visible annotations on each parameter, and their values.

# num_parameters
# The value of the num_parameters item gives the number of parameters of the method represented by the method_info structure on which the annotation occurs. (This duplicates information that could be extracted from the method descriptor (§4.3.3).)

# parameter_annotations
# Each value of the parameter_annotations table represents all of the run-time-visible annotations on a single parameter. The sequence of values in the table corresponds to the sequence of parameters in the method descriptor. Each parameter_annotations entry contains the following two items:

# num_annotations
# The value of the num_annotations item indicates the number of run-time-visible annotations on the parameter corresponding to the sequence number of this parameter_annotations element.

# annotations
# Each value of the annotations table represents a single run-time-visible annotation on the parameter corresponding to the sequence number of this parameter_annotations element.

# ------------------------------------------------------------------------
# 4.7.19. The RuntimeInvisibleParameterAnnotations attribute
# ------------------------------------------------------------------------

# The RuntimeInvisibleParameterAnnotations attribute is similar to the RuntimeVisibleParameterAnnotations attribute, except that the annotations represented by a RuntimeInvisibleParameterAnnotations attribute must not be made available for return by reflective APIs, unless the Java Virtual Machine has specifically been instructed to retain these annotations via some implementation-specific mechanism such as a command line flag. In the absence of such instructions, the Java Virtual Machine ignores this attribute.

# The RuntimeInvisibleParameterAnnotations attribute is a variable-length attribute in the attributes table of a method_info structure (§4.6). The RuntimeInvisibleParameterAnnotations attribute records run-time-invisible Java programming language annotations on the parameters of the corresponding method.

# Each method_info structure may contain at most one RuntimeInvisibleParameterAnnotations attribute, which records all the run-time-invisible Java programming language annotations on the parameters of the corresponding method.

# The RuntimeInvisibleParameterAnnotations attribute has the following format:

# RuntimeInvisibleParameterAnnotations_attribute {
#     u2 attribute_name_index;
#     u4 attribute_length;
#     u1 num_parameters;
#     {   u2         num_annotations;
#         annotation annotations[num_annotations];
#     } parameter_annotations[num_parameters];
# }
# The items of the RuntimeInvisibleParameterAnnotations_attribute structure are as follows:

# attribute_name_index
# The value of the attribute_name_index item must be a valid index into the constant_pool table. The constant_pool entry at that index must be a CONSTANT_Utf8_info structure (§4.4.7) representing the string "RuntimeInvisibleParameterAnnotations".

# attribute_length
# The value of the attribute_length item indicates the length of the attribute, excluding the initial six bytes.

# The value of the attribute_length item is thus dependent on the number of parameters, the number of run-time-invisible annotations on each parameter, and their values.

# num_parameters
# The value of the num_parameters item gives the number of parameters of the method represented by the method_info structure on which the annotation occurs. (This duplicates information that could be extracted from the method descriptor (§4.3.3).)

# parameter_annotations
# Each value of the parameter_annotations table represents all of the run-time-invisible annotations on a single parameter. The sequence of values in the table corresponds to the sequence of parameters in the method descriptor. Each parameter_annotations entry contains the following two items:

# num_annotations
# The value of the num_annotations item indicates the number of run-time-invisible annotations on the parameter corresponding to the sequence number of this parameter_annotations element.

# annotations
# Each value of the annotations table represents a single run-time-invisible annotation on the parameter corresponding to the sequence number of this parameter_annotations element.

# ------------------------------------------------------------------------
# 4.7.20. The AnnotationDefault attribute
# ------------------------------------------------------------------------

# The AnnotationDefault attribute is a variable-length attribute in the attributes table of certain method_info structures (§4.6), namely those representing elements of annotation types. The AnnotationDefault attribute records the default value for the element represented by the method_info structure.

# Each method_info structure representing an element of an annotation type may contain at most one AnnotationDefault attribute. The Java Virtual Machine must make this default value available so it can be applied by appropriate reflective APIs.

# The AnnotationDefault attribute has the following format:

# AnnotationDefault_attribute {
#     u2            attribute_name_index;
#     u4            attribute_length;
#     element_value default_value;
# }
# The items of the AnnotationDefault_attribute structure are as follows:

# attribute_name_index
# The value of the attribute_name_index item must be a valid index into the constant_pool table. The constant_pool entry at that index must be a CONSTANT_Utf8_info structure (§4.4.7) representing the string "AnnotationDefault".

# attribute_length
# The value of the attribute_length item indicates the length of the attribute, excluding the initial six bytes.

# The value of the attribute_length item is thus dependent on the default value.

# default_value
# The default_value item represents the default value of the annotation type element whose default value is represented by this AnnotationDefault attribute.

# ------------------------------------------------------------------------
# 4.7.21. The BootstrapMethods attribute
# ------------------------------------------------------------------------

# The BootstrapMethods attribute is a variable-length attribute in the attributes table of a ClassFile structure (§4.1). The BootstrapMethods attribute records bootstrap method specifiers referenced by invokedynamic instructions (§invokedynamic).

# There must be exactly one BootstrapMethods attribute in the attributes table of a given ClassFile structure if the constant_pool table of the ClassFile structure has at least one CONSTANT_InvokeDynamic_info entry (§4.4.10). There can be no more than one BootstrapMethods attribute in the attributes table of a given ClassFile structure.

# The BootstrapMethods attribute has the following format:

# BootstrapMethods_attribute {
#     u2 attribute_name_index;
#     u4 attribute_length;
#     u2 num_bootstrap_methods;
#     {   u2 bootstrap_method_ref;
#         u2 num_bootstrap_arguments;
#         u2 bootstrap_arguments[num_bootstrap_arguments];
#     } bootstrap_methods[num_bootstrap_methods];
# }
# The items of the BootstrapMethods_attribute structure are as follows:

# attribute_name_index
# The value of the attribute_name_index item must be a valid index into the constant_pool table. The constant_pool entry at that index must be a CONSTANT_Utf8_info structure (§4.4.7) representing the string "BootstrapMethods".

# attribute_length
# The value of the attribute_length item indicates the length of the attribute, excluding the initial six bytes.

# The value of the attribute_length item is thus dependent on the number of invokedynamic instructions in this ClassFile structure.

# num_bootstrap_methods
# The value of the num_bootstrap_methods item determines the number of bootstrap method specifiers in the bootstrap_methods array.

# bootstrap_methods[]
# Each entry in the bootstrap_methods array contains an index to a CONSTANT_MethodHandle_info structure (§4.4.8) which specifies a bootstrap method, and a sequence (perhaps empty) of indexes to static arguments for the bootstrap method.

# Each bootstrap_methods entry must contain the following three items:

# bootstrap_method_ref
# The value of the bootstrap_method_ref item must be a valid index into the constant_pool table. The constant_pool entry at that index must be a CONSTANT_MethodHandle_info structure (§4.4.8).

# The reference_kind item of the CONSTANT_MethodHandle_info structure should have the value 6 (REF_invokeStatic) or 8 (REF_newInvokeSpecial) (§5.4.3.5) or else invocation of the bootstrap method handle during call site specifier resolution for an invokedynamic instruction will complete abruptly.

# num_bootstrap_arguments
# The value of the num_bootstrap_arguments item gives the number of items in the bootstrap_arguments array.

# bootstrap_arguments
# Each entry in the bootstrap_arguments array must be a valid index into the constant_pool table. The constant_pool entry at that index must be a CONSTANT_String_info, CONSTANT_Class_info, CONSTANT_Integer_info, CONSTANT_Long_info, CONSTANT_Float_info, CONSTANT_Double_info, CONSTANT_MethodHandle_info, or CONSTANT_MethodType_info structure (§4.4.3, §4.4.1, §4.4.4, §4.4.5), §4.4.8, §4.4.9).
