from .signatures import method_descriptor

##########################################################################
# Some utility methods to help compare and hash constants
##########################################################################


def multieq(obj1, obj2, *attrs):
    "Compare two objects using the provided attributes"
    return type(obj1) == type(obj2) and all(getattr(obj1, attr) == getattr(obj2, attr) for attr in attrs)


def multihash(obj, *attrs):
    """Generate a hash of the object using the provided attributes.

    31 is a "magic number"; it's the same magic number used by Java
    when hashing multiple objects.
    """
    result = 1
    for attr in attrs:
        result = 31 * result + hash(getattr(obj, attr))
    return result


##########################################################################
# Some utility methods to help reconstruct a constant pool.
# These allow us to read the entire constant pool, and then resolve it.
##########################################################################

def resolve(entry, pool):
    klass, args = entry

    resolved_args = []
    for arg in args:
        if hasattr(arg, '__call__'):
            resolved_args.append(arg(pool))
        else:
            resolved_args.append(arg)
    return klass(*resolved_args)


def read_ref_attr(index, attr):
    def resolver(pool):
        entry = pool[index - 1]
        if isinstance(entry, tuple):
            value = resolve(entry, pool)
            pool[index - 1] = value
        else:
            value = entry
        return getattr(value, attr).bytes.decode('utf8')
    return resolver


def read_utf8(index):
    def resolver(pool):
        entry = pool[index - 1]
        if isinstance(entry, tuple):
            value = resolve(entry, pool)
            pool[index - 1] = value
        else:
            value = entry
        return value.bytes.decode('utf8')
    return resolver

# From: http://docs.oracle.com/javase/specs/jvms/se7/html/jvms-4.html

##########################################################################
# 4.4. The Constant Pool
##########################################################################

# Java Virtual Machine instructions do not rely on the run-time layout of
# classes, interfaces, class instances, or arrays. Instead, instructions refer
# to symbolic information in the constant_pool table.


class ConstantPool:
    def __init__(self):
        self._constants = {}
        # The constant_pool is a table of structures (§4.4) representing various string
        # constants, class and interface names, field names, and other constants that
        # are referred to within the ClassFile structure and its substructures. The
        # format of each constant_pool table entry is indicated by its first "tag" byte.

        # The constant_pool table is indexed from 1 to constant_pool_count-1.
        self._constant_pool = []

    @property
    def count(self):
        """The value of the constant_pool_count item is equal to the number of entries in
        the constant_pool table plus one. A constant_pool index is considered valid if
        it is greater than zero and less than constant_pool_count, with the exception
        for constants of type long and double noted in §4.4.5.
        """
        return len(self._constant_pool) + 1

    def add(self, obj, allow_duplicates=False):
        if allow_duplicates or obj not in self._constants:
            self._constant_pool.append(obj)
            self._constants[obj] = len(self)
            if obj.__class__ in (Double, Long):
                self._constant_pool.append(None)

    def __len__(self):
        return len(self._constant_pool)

    def __getitem__(self, i):
        return self._constant_pool[i - 1]

    def index(self, obj):
        return self._constants[obj]

    def read(self, reader, dump=None):
        count = reader.read_u2()
        if dump is not None:
            reader.debug("    " * dump, 'Constant pool: (%s constants)' % (count - 1))

        raw_pool = []
        i = 1
        while i < count:
            constant = Constant.read(reader)
            raw_pool.append(constant)
            if constant[0] in (Double, Long):
                raw_pool.append(None)
                i += 2
            else:
                i += 1

        i = 0
        while i < count - 1:
            entry = raw_pool[i]
            if isinstance(entry, tuple):
                const = resolve(entry, raw_pool)
            else:
                const = entry
            self.add(const, allow_duplicates=True)
            if dump is not None:
                reader.debug("    " * (dump + 1), '%s: %s' % ((i + 1), repr(const)))
            if const.__class__ in (Double, Long):
                i += 2
            else:
                i += 1

    def write(self, writer):
        writer.write_u2(self.count)
        for i, constant in enumerate(self._constant_pool):
            if constant:
                constant.write(writer)


# All constant_pool table entries have the following general format:

class Constant:
    # u1 tag;
    # u1 info[];

    # Each item in the constant_pool table must begin with a 1-byte tag indicating
    # the kind of cp_info entry. The contents of the info array vary with the value
    # of tag. The valid tags and their values are listed in Table 4.3. Each tag byte
    # must be followed by two or more bytes giving information about the specific
    # constant. The format of the additional information varies with the tag value.

    # Table 4.3. Constant pool tags

    CONSTANT_Class = 7
    CONSTANT_Fieldref = 9
    CONSTANT_Methodref = 10
    CONSTANT_InterfaceMethodref = 11
    CONSTANT_String = 8
    CONSTANT_Integer = 3
    CONSTANT_Float = 4
    CONSTANT_Long = 5
    CONSTANT_Double = 6
    CONSTANT_NameAndType = 12
    CONSTANT_Utf8 = 1
    CONSTANT_MethodHandle = 15
    CONSTANT_MethodType = 16
    CONSTANT_InvokeDynamic = 18

    def __init__(self, tag):
        self.tag = tag

    @staticmethod
    def read(reader):
        tag = reader.read_u1()
        klass = {
            0: None,
            Constant.CONSTANT_Class: Classref,
            Constant.CONSTANT_Fieldref: Fieldref,
            Constant.CONSTANT_Methodref: Methodref,
            Constant.CONSTANT_InterfaceMethodref: InterfaceMethodref,
            Constant.CONSTANT_String: String,
            Constant.CONSTANT_Integer: Integer,
            Constant.CONSTANT_Float: Float,
            Constant.CONSTANT_Long: Long,
            Constant.CONSTANT_Double: Double,
            Constant.CONSTANT_NameAndType: NameAndType,
            Constant.CONSTANT_Utf8: Utf8,
            # Constant.CONSTANT_MethodHandle: MethodHandle
            # Constant.CONSTANT_MethodType: MethodType
            # Constant.CONSTANT_InvokeDynamic: InvokeDynamic
        }[tag]
        if klass:
            return klass.read_info(reader)

    def write(self, writer):
        writer.write_u1(self.tag)
        self.write_info(writer)

    def resolve(self, constant_pool):
        constant_pool.add(self)
        self.resolve_info(constant_pool)

    def resolve_info(self, constant_pool):
        pass

# ------------------------------------------------------------------------
# 4.4.1. The CONSTANT_Class_info Structure
# ------------------------------------------------------------------------

# The CONSTANT_Class_info structure is used to represent a class or an interface:


class Classref(Constant):
    # u1 tag;
    # u2 name_index;

    def __init__(self, name):
        # The tag item has the value CONSTANT_Class (7).
        super().__init__(Constant.CONSTANT_Class)

        # The value of the name item must be a valid index into the
        # constant_pool table. The constant_pool entry at that index must be a
        # CONSTANT_Utf8_info (§4.4.7) structure representing a valid binary
        # class or interface name encoded in internal form (§4.2.1).

        # Because arrays are objects, the opcodes anewarray and multianewarray
        # can reference array "classes" via CONSTANT_Class_info structures in
        # the constant_pool table. For such array classes, the name of the class
        # is the descriptor of the array type.

        # For example, the class name representing a two-dimensional int array
        # type:
        #
        #     int[][]
        #
        # is:
        #
        #     [[I
        #
        # The class name representing the type array of class Thread:
        #
        #     Thread[]
        # is
        #
        #     [Ljava/lang/Thread;
        #
        # An array type descriptor is valid only if it represents 255 or fewer
        # dimensions.
        self.class_name = name
        self.name = Utf8(name)

    def __repr__(self):
        return '<Class %s>' % self.name

    def __eq__(self, other):
        return multieq(self, other, 'tag', 'name')

    def __hash__(self):
        return multihash(self, 'tag', 'name')

    @staticmethod
    def read_info(reader):
        name = reader.read_u2()
        return Classref, (read_utf8(name),)

    def write_info(self, writer):
        writer.write_u2(writer.constant_pool.index(self.name))

    def resolve_info(self, constant_pool):
        self.name.resolve(constant_pool)


# ------------------------------------------------------------------------
# 4.4.2. The CONSTANT_Fieldref_info, CONSTANT_Methodref_info, and CONSTANT_InterfaceMethodref_info Structures
# ------------------------------------------------------------------------

# Fields, methods, and interface methods are represented by similar structures:

class Fieldref(Constant):
    # u1 tag;
    # u2 class_index;
    # u2 name_and_type_index;

    def __init__(self, class_name, name, descriptor):

        # The tag item of a CONSTANT_Fieldref_info structure has the value
        # CONSTANT_Fieldref (9).
        super().__init__(Constant.CONSTANT_Fieldref)

        # The value of the class item must be a valid index into the
        # constant_pool table. The constant_pool entry at that index must be a
        # CONSTANT_Class_info (§4.4.1) structure representing a class or
        # interface type that has the field or method as a member.

        # The class_index item of a CONSTANT_Fieldref_info structure may be
        # either a class type or an interface type.
        self.class_name = class_name
        self.klass = Classref(class_name)

        # The value of the name_and_type item must be a valid index into
        # the constant_pool table. The constant_pool entry at that index must be
        # a CONSTANT_NameAndType_info (§4.4.6) structure. This constant_pool
        # entry indicates the name and descriptor of the field or method.

        # The indicated descriptor must be a field descriptor (§4.3.2).
        self.name = name
        self.descriptor = descriptor
        self.name_and_type = NameAndType(name, descriptor)

    def __repr__(self):
        return '<Fieldref %s.%s (%s)>' % (self.class_name, self.name, self.descriptor)

    def __eq__(self, other):
        return multieq(self, other, 'tag', 'klass', 'name_and_type')

    def __hash__(self):
        return multihash(self, 'tag', 'klass', 'name_and_type')

    def __info_eq__(self, other):
        return

    def __info_hash__(self):
        return 31 * hash(self.klass) + 31

    @staticmethod
    def read_info(reader):
        klass = reader.read_u2()
        name_and_type = reader.read_u2()
        return Fieldref, (
            read_ref_attr(klass, 'name'),
            read_ref_attr(name_and_type, 'name'),
            read_ref_attr(name_and_type, 'descriptor'),
        )

    def write_info(self, writer):
        writer.write_u2(writer.constant_pool.index(self.klass))
        writer.write_u2(writer.constant_pool.index(self.name_and_type))

    def resolve_info(self, constant_pool):
        self.klass.resolve(constant_pool)
        self.name_and_type.resolve(constant_pool)


class Methodref(Constant):
    # u1 tag;
    # u2 class_index;
    # u2 name_and_type_index;

    def __init__(self, class_name, name, descriptor):

        # The tag item of a CONSTANT_Methodref_info structure has the value
        # CONSTANT_Methodref (10).
        super().__init__(Constant.CONSTANT_Methodref)

        # The value of the class item must be a valid index into the
        # constant_pool table. The constant_pool entry at that index must be a
        # CONSTANT_Class_info (§4.4.1) structure representing a class or
        # interface type that has the field or method as a member.

        # The class item of a CONSTANT_Methodref_info structure must be a
        # class type, not an interface type.
        self.class_name = class_name
        self.klass = Classref(class_name)

        # The value of the name_and_type item must be a valid index into
        # the constant_pool table. The constant_pool entry at that index must be
        # a CONSTANT_NameAndType_info (§4.4.6) structure. This constant_pool
        # entry indicates the name and descriptor of the field or method.

        # The indicated descriptor must be a method descriptor (§4.3.3).

        # If the name of the method of a CONSTANT_Methodref_info structure
        # begins with a '<' ('\u003c'), then the name must be the special name
        # <init>, representing an instance initialization method (§2.9). The
        # return type of such a method must be void.
        self.name_and_type = NameAndType(name, descriptor)

        # For convenience, store a parsed version of the descriptor.
        self.name = name
        self.descriptor = method_descriptor(descriptor)

    def __repr__(self):
        return '<Methodref %s.%s %s>' % (self.class_name, self.name, self.name_and_type.descriptor)

    def __eq__(self, other):
        return multieq(self, other, 'tag', 'klass', 'name_and_type')

    def __hash__(self):
        return multihash(self, 'tag', 'klass', 'name_and_type')

    @staticmethod
    def read_info(reader):
        klass = reader.read_u2()
        name_and_type = reader.read_u2()
        return Methodref, (
            read_ref_attr(klass, 'name'),
            read_ref_attr(name_and_type, 'name'),
            read_ref_attr(name_and_type, 'descriptor'),
        )

    def write_info(self, writer):
        writer.write_u2(writer.constant_pool.index(self.klass))
        writer.write_u2(writer.constant_pool.index(self.name_and_type))

    def resolve_info(self, constant_pool):
        self.klass.resolve(constant_pool)
        self.name_and_type.resolve(constant_pool)


class InterfaceMethodref(Constant):
    # u1 tag;
    # u2 class_index;
    # u2 name_and_type_index;

    def __init__(self, class_name, name, descriptor):

        # The tag item of a CONSTANT_InterfaceMethodref_info structure has the value
        # CONSTANT_InterfaceMethodref (11).
        super().__init__(Constant.CONSTANT_InterfaceMethodref)

        # The value of the class item must be a valid index into the
        # constant_pool table. The constant_pool entry at that index must be a
        # CONSTANT_Class_info (§4.4.1) structure representing a class or
        # interface type that has the field or method as a member.

        # The class item of a CONSTANT_InterfaceMethodref_info structure
        # must be an interface type.
        self.class_name = class_name
        self.klass = Classref(class_name)

        # The value of the name_and_type item must be a valid index into
        # the constant_pool table. The constant_pool entry at that index must be
        # a CONSTANT_NameAndType_info (§4.4.6) structure. This constant_pool
        # entry indicates the name and descriptor of the field or method.

        # The indicated descriptor must be a method descriptor (§4.3.3).
        self.name_and_type = NameAndType(name, descriptor)

        # For convenience, store a parsed version of the descriptor.
        self.name = name
        self.descriptor = method_descriptor(descriptor)

    def __repr__(self):
        return '<InterfaceMethodref %s.%s %s>' % (self.class_name, self.name, self.name_and_type.descriptor)

    def __eq__(self, other):
        return multieq(self, other, 'tag', 'klass', 'name_and_type')

    def __hash__(self):
        return multihash(self, 'tag', 'klass', 'name_and_type')

    @staticmethod
    def read_info(reader):
        klass = reader.read_u2()
        name_and_type = reader.read_u2()
        return InterfaceMethodref, (
            read_ref_attr(klass, 'name'),
            read_ref_attr(name_and_type, 'name'),
            read_ref_attr(name_and_type, 'descriptor'),
        )

    def write_info(self, writer):
        writer.write_u2(writer.constant_pool.index(self.klass))
        writer.write_u2(writer.constant_pool.index(self.name_and_type))

    def resolve_info(self, constant_pool):
        self.klass.resolve(constant_pool)
        self.name_and_type.resolve(constant_pool)


# ------------------------------------------------------------------------
# 4.4.3. The CONSTANT_String_info Structure
# ------------------------------------------------------------------------

# The CONSTANT_String_info structure is used to represent constant objects of
# the type String:

class String(Constant):
    # u1 tag;
    # u2 string_index;

    def __init__(self, value):
        # The tag item of the CONSTANT_String_info structure has the value
        # CONSTANT_String (8).
        super().__init__(Constant.CONSTANT_String)

        # The value of the string item must be a valid index into the
        # constant_pool table. The constant_pool entry at that index must be a
        # CONSTANT_Utf8_info (§4.4.7) structure representing the sequence of
        # Unicode code points to which the String object is to be initialized.
        self.value = Utf8(value)

    def __repr__(self):
        return "<String '%s'>" % self.value

    def __eq__(self, other):
        return multieq(self, other, 'tag', 'value')

    def __hash__(self):
        return multihash(self, 'tag', 'value')

    @staticmethod
    def read_info(reader):
        value = reader.read_u2()
        return String, (
            read_utf8(value),
        )

    def write_info(self, writer):
        writer.write_u2(writer.constant_pool.index(self.value))

    def resolve_info(self, constant_pool):
        self.value.resolve(constant_pool)


# ------------------------------------------------------------------------
# 4.4.4. The CONSTANT_Integer_info and CONSTANT_Float_info Structures
# ------------------------------------------------------------------------

# The CONSTANT_Integer_info and CONSTANT_Float_info structures represent 4-byte
# numeric (int and float) constants.
#
# The items of these structures are as follows:

class Integer(Constant):
    # u1 tag;
    # u4 bytes;

    def __init__(self, value):
        # The tag item of the CONSTANT_Integer_info structure has the value
        # CONSTANT_Integer (3).
        super().__init__(Constant.CONSTANT_Integer)

        # The bytes item of the CONSTANT_Integer_info structure represents the
        # value of the int constant. The bytes of the value are stored in big-
        # endian (high byte first) order.

        self.value = value

    def __repr__(self):
        return '<Integer %s>' % self.value

    def __eq__(self, other):
        return multieq(self, other, 'tag', 'value')

    def __hash__(self):
        return multihash(self, 'tag', 'value')

    @staticmethod
    def read_info(reader):
        value = reader.read_u4()
        return Integer, (value,)

    def write_info(self, writer):
        writer.write_u4(self.value)


class Float(Constant):
    # u1 tag;
    # u4 bytes;

    def __init__(self, value):
        # The tag item of the CONSTANT_Float_info structure has the value
        # CONSTANT_Float (4).
        super().__init__(Constant.CONSTANT_Float)

        # The bytes item of the CONSTANT_Float_info structure represents the
        # value of the float constant in IEEE 754 floating-point single format
        # (§2.3.2). The bytes of the single format representation are stored in
        # big-endian (high byte first) order.
        #
        # The value represented by the CONSTANT_Float_info structure is
        # determined as follows. The bytes of the value are first converted into
        # an int constant bits. Then:
        #
        #  * If bits is 0x7f800000, the float value will be positive infinity.
        #
        #  * If bits is 0xff800000, the float value will be negative infinity.
        #
        #  * If bits is in the range 0x7f800001 through 0x7fffffff or in the range
        #    0xff800001 through 0xffffffff, the float value will be NaN.
        #
        # In all other cases, let s, e, and m be three values that might be
        # computed from bits:
        #
        #     int s = ((bits >> 31) == 0) ? 1 : -1;
        #     int e = ((bits >> 23) & 0xff);
        #     int m = (e == 0) ?
        #               (bits & 0x7fffff) << 1 :
        #               (bits & 0x7fffff) | 0x800000;
        #
        # Then the float value equals the result of the mathematical expression
        # s · m · 2e-150.

        self.value = value

    def __repr__(self):
        return '<Float %s>' % self.value

    def __eq__(self, other):
        return multieq(self, other, 'tag', 'value')

    def __hash__(self):
        return multihash(self, 'tag', 'value')

    @staticmethod
    def read_info(reader):
        value = reader.read_f()
        return Integer, (value,)

    def write_info(self, writer):
        writer.write_f(self.value)


# ------------------------------------------------------------------------
# 4.4.5. The CONSTANT_Long_info and CONSTANT_Double_info Structures
# ------------------------------------------------------------------------

# The CONSTANT_Long_info and CONSTANT_Double_info represent 8-byte numeric (long
# and double) constants.

# All 8-byte constants take up two entries in the constant_pool table of the
# class file. If a CONSTANT_Long_info or CONSTANT_Double_info structure is the
# item in the constant_pool table at index n, then the next usable item in the
# pool is located at index n+2. The constant_pool index n+1 must be valid but is
# considered unusable.

# In retrospect, making 8-byte constants take two constant pool entries was a
# poor choice.

# The items of these structures are as follows:

class Long(Constant):
    # u1 tag;
    # u4 high_bytes;
    # u4 low_bytes;

    # The unsigned high_bytes and low_bytes items of the CONSTANT_Long_info
    # structure together represent the value of the long constant:
    #
    #     ((long) high_bytes << 32) + low_bytes
    #
    # where the bytes of each of high_bytes and low_bytes are stored in big-
    # endian (high byte first) order.

    def __init__(self, value):
        # The tag item of the CONSTANT_LONG_info structure has the value
        # CONSTANT_LONG (3).
        super().__init__(Constant.CONSTANT_LONG)

        self.value = value

    def __repr__(self):
        return '<Long %s>' % self.value

    def __eq__(self, other):
        return multieq(self, other, 'tag', 'value')

    def __hash__(self):
        return multihash(self, 'tag', 'value')

    @staticmethod
    def read_info(reader):
        value = reader.read_u8()
        return Long, (value,)

    def write_info(self, writer):
        writer.write_u8(self.value)


class Double(Constant):
    # u1 tag;
    # u4 high_bytes;
    # u4 low_bytes;

    # The high_bytes and low_bytes items of the CONSTANT_Double_info structure
    # together represent the double value in IEEE 754 floating-point double
    # format (§2.3.2). The bytes of each item are stored in big-endian (high
    # byte first) order.
    #
    # The value represented by the CONSTANT_Double_info structure is determined
    # as follows. The high_bytes and low_bytes items are converted into the long
    # constant bits, which is equal to
    #
    # ((long) high_bytes << 32) + low_bytes
    #
    # Then:
    #
    #  * If bits is 0x7ff0000000000000L, the double value will be positive infinity.
    #
    #  * If bits is 0xfff0000000000000L, the double value will be negative infinity.
    #
    #  * If bits is in the range 0x7ff0000000000001L through 0x7fffffffffffffffL or
    #    in the range 0xfff0000000000001L through 0xffffffffffffffffL, the double
    #    value will be NaN.
    #
    # In all other cases, let s, e, and m be three values that might be computed
    # from bits:
    #
    #     int s = ((bits >> 63) == 0) ? 1 : -1;
    #     int e = (int)((bits >> 52) & 0x7ffL);
    #     long m = (e == 0) ?
    #                (bits & 0xfffffffffffffL) << 1 :
    #                (bits & 0xfffffffffffffL) | 0x10000000000000L;
    #
    # Then the floating-point value equals the double value of the mathematical
    # expression s · m · 2e-1075.

    def __init__(self, value):
        # The tag item of the CONSTANT_Double_info structure has the value
        # CONSTANT_Double (6).
        super().__init__(Constant.CONSTANT_Double)

        self.value = value

    def __repr__(self):
        return '<Double %s>' % self.value

    def __eq__(self, other):
        return multieq(self, other, 'tag', 'value')

    def __hash__(self):
        return multihash(self, 'tag', 'value')

    @staticmethod
    def read_info(reader):
        value = reader.read_d()
        return Double, (value,)

    def write_info(self, writer):
        writer.write_d(self.value)


# ------------------------------------------------------------------------
# 4.4.6. The CONSTANT_NameAndType_info Structure
# ------------------------------------------------------------------------

# The CONSTANT_NameAndType_info structure is used to represent a field or
# method, without indicating which class or interface type it belongs to:

class NameAndType(Constant):
    # u1 tag;
    # u2 name_index;
    # u2 descriptor_index;

    def __init__(self, name, descriptor):

        # The tag item of the CONSTANT_NameAndType_info structure has the value
        # CONSTANT_NameAndType (12).
        super().__init__(Constant.CONSTANT_NameAndType)

        # The value of the name item must be a valid index into the
        # constant_pool table. The constant_pool entry at that index must be a
        # CONSTANT_Utf8_info (§4.4.7) structure representing either the special
        # method name <init> (§2.9) or a valid unqualified name (§4.2.2)
        # denoting a field or method.

        self.name = Utf8(name)

        # The value of the descriptor item must be a valid index into the
        # constant_pool table. The constant_pool entry at that index must be a
        # CONSTANT_Utf8_info (§4.4.7) structure representing a valid field
        # descriptor (§4.3.2) or method descriptor (§4.3.3).

        self.descriptor = Utf8(descriptor)

    def __repr__(self):
        return '<NameAndType: name:%s descriptor:%s>' % (self.name, self.descriptor)

    def __eq__(self, other):
        return multieq(self, other, 'tag', 'name', 'descriptor')

    def __hash__(self):
        return multihash(self, 'tag', 'name', 'descriptor')

    @staticmethod
    def read_info(reader):
        name = reader.read_u2()
        descriptor = reader.read_u2()
        return NameAndType, (
            read_utf8(name),
            read_utf8(descriptor)
        )

    def write_info(self, writer):
        writer.write_u2(writer.constant_pool.index(self.name))
        writer.write_u2(writer.constant_pool.index(self.descriptor))

    def resolve_info(self, constant_pool):
        self.name.resolve(constant_pool)
        self.descriptor.resolve(constant_pool)


# ------------------------------------------------------------------------
# 4.4.7. The CONSTANT_Utf8_info Structure
# ------------------------------------------------------------------------

# The CONSTANT_Utf8_info structure is used to represent constant string values:

class Utf8(Constant):
    # u1 tag;
    # u2 length;
    # u1 bytes[length];

    def __init__(self, string):

        # The tag item of the CONSTANT_Utf8_info structure has the value
        # CONSTANT_Utf8 (1).
        super().__init__(Constant.CONSTANT_Utf8)

        # The value of the length item gives the number of bytes in the bytes
        # array (not the length of the resulting string). The strings in the
        # CONSTANT_Utf8_info structure are not null-terminated.

        # The bytes array contains the bytes of the string. No byte may have the
        # value (byte)0 or lie in the range (byte)0xf0 - (byte)0xff.

        # String content is encoded in modified UTF-8. Modified UTF-8 strings
        # are encoded so that code point sequences that contain only non-null
        # ASCII characters can be represented using only 1 byte per code point,
        # but all code points in the Unicode codespace can be represented.

        # * Code points in the range '\u0001' to '\u007F' are represented by a
        #   single byte:
        #
        #     Table 4.4.
        #
        #         0   bits 6-0
        #
        #     The 7 bits of data in the byte give the value of the code point represented.
        #
        # * The null code point ('\u0000') and code points in the range '\u0080'
        #   to '\u07FF' are represented by a pair of bytes x and y :
        #
        #     Table 4.5.
        #
        #     x:
        #     Table 4.6.
        #
        #         1   1   0   bits 10-6
        #
        #     y:
        #     Table 4.7.
        #
        #         1   0   bits 5-0
        #
        #     The bytes represent the code point with the value:
        #
        #         ((x & 0x1f) << 6) + (y & 0x3f)
        #
        # * Code points in the range '\u0800' to '\uFFFF' are represented by 3
        #   bytes x, y, and z :
        #
        #     Table 4.8.
        #
        #         x:
        #         Table 4.9.
        #
        #             1   1   1   0   bits 15-12
        #
        #         y:
        #             Table 4.10.
        #
        #             1   0   bits 11-6
        #
        #         z:
        #             Table 4.11.
        #
        #             1   0   bits 5-0
        #
        #     The three bytes represent the code point with the value:
        #
        #         ((x & 0xf) << 12) + ((y & 0x3f) << 6) + (z & 0x3f)
        #
        # * Characters with code points above U+FFFF (so-called supplementary
        #   characters) are represented by separately encoding the two surrogate
        #   code units of their UTF-16 representation. Each of the surrogate
        #   code units is represented by three bytes. This means supplementary
        #   characters are represented by six bytes, u, v, w, x, y, and z :
        #
        #     Table 4.12.
        #
        #         u:
        #             Table 4.13.
        #
        #             1   1   1   0   1   1   0   1
        #
        #         v:
        #             Table 4.14.
        #
        #             1   0   1   0   (bits 20-16)-1
        #
        #         w:
        #             Table 4.15.
        #
        #             1   0   bits 15-10
        #
        #         x:
        #             Table 4.16.
        #
        #             1   1   1   0   1   1   0   1
        #
        #         y:
        #             Table 4.17.
        #
        #             1   0   1   1   bits 9-6
        #
        #         z:
        #             Table 4.18.
        #
        #             1   0   bits 5-0
        #
        #     The six bytes represent the code point with the value:
        #
        #     0x10000 + ((v & 0x0f) << 16) + ((w & 0x3f) << 10) +
        #     ((y & 0x0f) << 6) + (z & 0x3f)
        #
        # The bytes of multibyte characters are stored in the class file in big-
        # endian (high byte first) order.
        #
        # There are two differences between this format and the "standard" UTF-8
        # format. First, the null character (char)0 is encoded using the 2-byte
        # format rather than the 1-byte format, so that modified UTF-8 strings
        # never have embedded nulls. Second, only the 1-byte, 2-byte, and 3-byte
        # formats of standard UTF-8 are used. The Java Virtual Machine does not
        # recognize the four-byte format of standard UTF-8; it uses its own two-
        # times-three-byte format instead.
        #
        # For more information regarding the standard UTF-8 format, see Section
        # 3.9 Unicode Encoding Forms of The Unicode Standard, Version 6.0.0.
        self.string = string
        self._bytes = string.encode('utf8')

    def __repr__(self):
        return "b'%s'" % self._bytes.decode('utf8')

    def __str__(self):
        return self._bytes.decode('utf8')

    @staticmethod
    def read_info(reader):
        length = reader.read_u2()
        string = reader.read_bytes(length).decode('utf8')
        return Utf8, (string,)

    def write_info(self, writer):
        writer.write_u2(self.length)
        writer.write_bytes(self.bytes)

    def __eq__(self, other):
        return multieq(self, other, 'tag', '_bytes')

    def __hash__(self):
        return multihash(self, 'tag', '_bytes')

    @property
    def length(self):
        return len(self._bytes)

    @property
    def bytes(self):
        return self._bytes


# ------------------------------------------------------------------------
# 4.4.8. The CONSTANT_MethodHandle_info Structure
# ------------------------------------------------------------------------

# The CONSTANT_MethodHandle_info structure is used to represent a method handle:

# CONSTANT_MethodHandle_info {
#     u1 tag;
#     u1 reference_kind;
#     u2 reference_index;
# }
# The items of the CONSTANT_MethodHandle_info structure are the following:

# tag
# The tag item of the CONSTANT_MethodHandle_info structure has the value CONSTANT_MethodHandle (15).

# reference_kind
# The value of the reference_kind item must be in the range 1 to 9. The value denotes the kind of this method handle, which characterizes its bytecode behavior (§5.4.3.5).

# reference_index
# The value of the reference_index item must be a valid index into the constant_pool table.

# If the value of the reference_kind item is 1 (REF_getField), 2 (REF_getStatic), 3 (REF_putField), or 4 (REF_putStatic), then the constant_pool entry at that index must be a CONSTANT_Fieldref_info (§4.4.2) structure representing a field for which a method handle is to be created.

# If the value of the reference_kind item is 5 (REF_invokeVirtual), 6 (REF_invokeStatic), 7 (REF_invokeSpecial), or 8 (REF_newInvokeSpecial), then the constant_pool entry at that index must be a CONSTANT_Methodref_info structure (§4.4.2) representing a class's method or constructor (§2.9) for which a method handle is to be created.

# If the value of the reference_kind item is 9 (REF_invokeInterface), then the constant_pool entry at that index must be a CONSTANT_InterfaceMethodref_info (§4.4.2) structure representing an interface's method for which a method handle is to be created.

# If the value of the reference_kind item is 5 (REF_invokeVirtual), 6 (REF_invokeStatic), 7 (REF_invokeSpecial), or 9 (REF_invokeInterface), the name of the method represented by a CONSTANT_Methodref_info structure must not be <init> or <clinit>.

# If the value is 8 (REF_newInvokeSpecial), the name of the method represented by a CONSTANT_Methodref_info structure must be <init>.

# ------------------------------------------------------------------------
# 4.4.9. The CONSTANT_MethodType_info Structure
# ------------------------------------------------------------------------

# The CONSTANT_MethodType_info structure is used to represent a method type:

# CONSTANT_MethodType_info {
#     u1 tag;
#     u2 descriptor_index;
# }
# The items of the CONSTANT_MethodType_info structure are as follows:

# tag
# The tag item of the CONSTANT_MethodType_info structure has the value CONSTANT_MethodType (16).

# descriptor_index
# The value of the descriptor_index item must be a valid index into the constant_pool table. The constant_pool entry at that index must be a CONSTANT_Utf8_info (§4.4.7) structure representing a method descriptor (§4.3.3).

# ------------------------------------------------------------------------
# 4.4.10. The CONSTANT_InvokeDynamic_info Structure
# ------------------------------------------------------------------------

# The CONSTANT_InvokeDynamic_info structure is used by an invokedynamic instruction (§invokedynamic) to specify a bootstrap method, the dynamic invocation name, the argument and return types of the call, and optionally, a sequence of additional constants called static arguments to the bootstrap method.

# CONSTANT_InvokeDynamic_info {
#     u1 tag;
#     u2 bootstrap_method_attr_index;
#     u2 name_and_type_index;
# }
# The items of the CONSTANT_InvokeDynamic_info structure are as follows:

# tag
# The tag item of the CONSTANT_InvokeDynamic_info structure has the value CONSTANT_InvokeDynamic (18).

# bootstrap_method_attr_index
# The value of the bootstrap_method_attr_index item must be a valid index into the bootstrap_methods array of the bootstrap method table (§4.7.21) of this class file.

# name_and_type_index
# The value of the name_and_type_index item must be a valid index into the constant_pool table. The constant_pool entry at that index must be a CONSTANT_NameAndType_info (§4.4.6) structure representing a method name and method descriptor (§4.3.3).
