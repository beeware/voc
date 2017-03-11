from ...java import opcodes as JavaOpcodes


##########################################################################
# Local variables are stored in a dictionary, keyed by name,
# and with the value of the local variable register they are stored in.
#
# If an attempt is used to use a name that has been deleted, an exception
# is raised.
#
# Once a name has been deleted, the index will be recycled for re-use
# as a different name.
##########################################################################

class ALOAD_index:
    """Generate the opcode to load an object variable at the given index onto the stack.

    This uses the optimized register operations for the first 4 local variables.
    """
    def __init__(self, index):
        self.index = index

    def process(self, context):
        # if self.index is None:
        #     print("LOAD AVAR NAME", context, self.name)
        #     print("locals: ", context.local_vars, context.deleted_vars)
        if self.index is None:
            raise NameError(self.name)
        elif self.index == 0:
            context.add_opcodes(JavaOpcodes.ALOAD_0())
        elif self.index == 1:
            context.add_opcodes(JavaOpcodes.ALOAD_1())
        elif self.index == 2:
            context.add_opcodes(JavaOpcodes.ALOAD_2())
        elif self.index == 3:
            context.add_opcodes(JavaOpcodes.ALOAD_3())
        else:
            context.add_opcodes(JavaOpcodes.ALOAD(self.index))

        # This opcode isn't for the final output.
        return False


class ALOAD_name(ALOAD_index):
    """Generate the opcode to load an object variable with the given name onto the stack.

    This looks up the local variable dictionary to find which
    register is being used for that variable, using the optimized
    register operations for the first 4 local variables.
    """
    def __init__(self, name):
        self.name = name
        super().__init__(None)

    def process(self, context):
        # print("LOAD AVAR NAME", context, self.name)
        # print("locals: ", context.local_vars, context.deleted_vars)
        try:
            self.index = context.local_vars[self.name]
        except KeyError:
            pass

        return super().process(context)


class ASTORE_index:
    """Generate the opcode to store an object variable at the given index.

    This uses the optimized register operations for the first 4 local variables.
    """
    def __init__(self, index):
        self.index = index

    def process(self, context):
        if self.index is None:
            try:
                self.index = context.deleted_vars.pop()
                # print ("REUSE index", self.index)
            except KeyError:
                self.index = len(context.active_local_vars)
                # print ("GET NEW index", self.index)
            context.local_vars[self.name] = self.index

        # if self.index is None:
        #     print("STORE AVAR NAME", context, self.index, self.name)
        #     print("locals: ", context.local_vars, context.deleted_vars)

        if self.index == 0:
            context.add_opcodes(JavaOpcodes.ASTORE_0())
        elif self.index == 1:
            context.add_opcodes(JavaOpcodes.ASTORE_1())
        elif self.index == 2:
            context.add_opcodes(JavaOpcodes.ASTORE_2())
        elif self.index == 3:
            context.add_opcodes(JavaOpcodes.ASTORE_3())
        else:
            context.add_opcodes(JavaOpcodes.ASTORE(self.index))

        # This opcode isn't for the final output.
        return False


class ASTORE_name(ASTORE_index):
    """Generate the opcode to store an object variable with the given name.

    This looks up the local variable dictionary to find which
    register is being used for that variable, using the optimized
    register operations for the first 4 local variables.
    """
    def __init__(self, name):
        self.name = name
        super().__init__(None)

    def process(self, context):
        try:
            self.index = context.local_vars[self.name]
        except KeyError:
            self.index = None

        return super().process(context)


class ILOAD_name:
    """Generate the opcode to load an integer variable with the given name onto the stack.

    This looks up the local variable dictionary to find which
    register is being used for that variable, using the optimized
    register operations for the first 4 local variables.
    """
    def __init__(self, name):
        self.name = name

    def process(self, context):
        # print("LOAD IVAR NAME", context, self.name)
        # print("locals: ", context.local_vars)
        try:
            index = context.local_vars[self.name]
        except KeyError:
            index = None

        if index is None:
            raise NameError(self.name)
        elif index == 0:
            context.add_opcodes(JavaOpcodes.ILOAD_0())
        elif index == 1:
            context.add_opcodes(JavaOpcodes.ILOAD_1())
        elif index == 2:
            context.add_opcodes(JavaOpcodes.ILOAD_2())
        elif index == 3:
            context.add_opcodes(JavaOpcodes.ILOAD_3())
        else:
            context.add_opcodes(JavaOpcodes.ILOAD(index))

        # This opcode isn't for the final output.
        return False


class ISTORE_name:
    """Generate the opcode to store a variable with the given name.

    This looks up the local variable dictionary to find which
    register is being used for that variable, using the optimized
    register operations for the first 4 local variables.
    """
    def __init__(self, name):
        self.name = name

    def process(self, context):
        try:
            index = context.local_vars[self.name]
        except KeyError:
            index = None

        if index is None:
            try:
                index = context.deleted_vars.pop()
                # print ("REUSE index", index)
            except KeyError:
                index = len(context.active_local_vars)
                # print ("GET NEW index", index)
            context.local_vars[self.name] = index

        # print("STORE IVAR NAME", context, index, self.name)
        # print("locals: ", context.local_vars)

        if index == 0:
            context.add_opcodes(JavaOpcodes.ISTORE_0())
        elif index == 1:
            context.add_opcodes(JavaOpcodes.ISTORE_1())
        elif index == 2:
            context.add_opcodes(JavaOpcodes.ISTORE_2())
        elif index == 3:
            context.add_opcodes(JavaOpcodes.ISTORE_3())
        else:
            context.add_opcodes(JavaOpcodes.ISTORE(index))

        # This opcode isn't for the final output.
        return False


class IINC_name:
    """Generate the opcode to increment an integer variable with the given name
    by the provided value.

    This looks up the local variable dictionary to find which
    register is being used for that variable, using the optimized
    register operations for the first 4 local variables.
    """
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def process(self, context):
        # print("LOAD IVAR NAME", context, self.name)
        # print("locals: ", context.local_vars)
        try:
            index = context.local_vars[self.name]
        except KeyError:
            index = None

        if index is None:
            raise NameError(self.name)

        context.add_opcodes(
            JavaOpcodes.IINC(index, self.value)
        )

        # This opcode isn't for the final output.
        return False


class LLOAD_name:
    """Generate the opcode to load a long variable with the given name onto the stack.

    This looks up the local variable dictionary to find which
    register is being used for that variable, using the optimized
    register operations for the first 4 local variables.
    """
    def __init__(self, name):
        self.name = name

    def process(self, context):
        # print("LOAD LVAR NAME", context, self.name, index)
        # print("locals: ", context.local_vars)
        try:
            index = context.local_vars[self.name]
        except KeyError:
            index = None

        if index is None:
            raise NameError(self.name)
        elif index == 0:
            context.add_opcodes(JavaOpcodes.LLOAD_0())
        elif index == 1:
            context.add_opcodes(JavaOpcodes.LLOAD_1())
        elif index == 2:
            context.add_opcodes(JavaOpcodes.LLOAD_2())
        elif index == 3:
            context.add_opcodes(JavaOpcodes.LLOAD_3())
        else:
            context.add_opcodes(JavaOpcodes.LLOAD(index))

        # This opcode isn't for the final output.
        return False


class FLOAD_name:
    """Generate the opcode to load a float variable with the given name onto the stack.

    This looks up the local variable dictionary to find which
    register is being used for that variable, using the optimized
    register operations for the first 4 local variables.
    """
    def __init__(self, name):
        self.name = name

    def process(self, context):
        # print("LOAD FVAR NAME", context, self.name, index)
        # print("locals: ", context.local_vars)
        try:
            index = context.local_vars[self.name]
        except KeyError:
            index = None

        if index is None:
            raise NameError(self.name)
        elif index == 0:
            context.add_opcodes(JavaOpcodes.FLOAD_0())
        elif index == 1:
            context.add_opcodes(JavaOpcodes.FLOAD_1())
        elif index == 2:
            context.add_opcodes(JavaOpcodes.FLOAD_2())
        elif index == 3:
            context.add_opcodes(JavaOpcodes.FLOAD_3())
        else:
            context.add_opcodes(JavaOpcodes.FLOAD(index))

        # This opcode isn't for the final output.
        return False


class DLOAD_name:
    """Generate the opcode to load a double variable with the given name onto the stack.

    This looks up the local variable dictionary to find which
    register is being used for that variable, using the optimized
    register operations for the first 4 local variables.
    """
    def __init__(self, name):
        self.name = name

    def process(self, context):
        # print("LOAD LVAR NAME", context, self.name, index)
        # print("locals: ", context.local_vars)
        try:
            index = context.local_vars[self.name]
        except KeyError:
            index = None

        if index is None:
            raise NameError(self.name)
        elif index == 0:
            context.add_opcodes(JavaOpcodes.DLOAD_0())
        elif index == 1:
            context.add_opcodes(JavaOpcodes.DLOAD_1())
        elif index == 2:
            context.add_opcodes(JavaOpcodes.DLOAD_2())
        elif index == 3:
            context.add_opcodes(JavaOpcodes.DLOAD_3())
        else:
            context.add_opcodes(JavaOpcodes.DLOAD(index))

        # This opcode isn't for the final output.
        return False


class free_name:
    """Remove a name from the local variable pool

    By default the variable must exist. However, if you pass
    in must_exist, the non-existence of the variable will not
    be treated as an error. This is to allow for variables that
    are created as part of looping constructs, and may not be
    created in the case of an empty loop.
    """
    def __init__(self, name, must_exist=True):
        self.name = name
        self.must_exist = must_exist

    def process(self, context):
        try:
            index = context.local_vars[self.name]
        except KeyError:
            index = None

        if index is None and self.must_exist:
            raise NameError(self.name)

        context.deleted_vars.add(index)
        context.local_vars[self.name] = None

        # print("FREE", context, self.name, index)
        # print("locals: ", context.local_vars, context.deleted_vars)

        # This opcode isn't for the final output.
        return False


##########################################################################
# Handle constant values.
#
# There are multiple opcodes to load and retrieve constants. Use the
# best option available at any given time.
##########################################################################

def ICONST_val(value):
    """Write an integer constant onto the stack.

    There are a couple of opcodes that can be used to optimize the
    loading of small integers; use them if possible.
    """
    if isinstance(value, bool):
        if value:
            return JavaOpcodes.ICONST_1()
        else:
            return JavaOpcodes.ICONST_0()
    elif isinstance(value, int):
        if value == 0:
            return JavaOpcodes.ICONST_0()
        elif value == 1:
            return JavaOpcodes.ICONST_1()
        elif value == 2:
            return JavaOpcodes.ICONST_2()
        elif value == 3:
            return JavaOpcodes.ICONST_3()
        elif value == 4:
            return JavaOpcodes.ICONST_4()
        elif value == 5:
            return JavaOpcodes.ICONST_5()
        elif value == -1:
            return JavaOpcodes.ICONST_M1()
        elif -32768 <= value <= 32767:
            return JavaOpcodes.SIPUSH(value)
        elif -2147483648 <= value <= 2147483647:
            return JavaOpcodes.LDC(value)
        else:
            raise RuntimeError("%s is out of integer range" % value)
    else:
        raise RuntimeError("%s is not an integer constant" % value)


def LCONST_val(value):
    """Write an long integer constant onto the stack.

    There are a couple of opcodes that can be used to optimize the
    loading of small longs; use them if possible.
    """
    if isinstance(value, int):
        if value == 0:
            return JavaOpcodes.LCONST_0()
        elif value == 1:
            return JavaOpcodes.LCONST_1()
        else:
            return JavaOpcodes.LDC2_W(value)
    else:
        raise RuntimeError("%s is not a long integer constant" % value)


def FCONST_val(value):
    """Write a float constant onto the stack.

    There are a couple of opcodes that can be used to optimize the
    loading of some floats; use them if possible.
    """
    if isinstance(value, float):
        if value == 0.0:
            return JavaOpcodes.FCONST_0()
        elif value == 1.0:
            return JavaOpcodes.FCONST_1()
        elif value == 2.0:
            return JavaOpcodes.FCONST_2()
        else:
            return JavaOpcodes.LDC_W(value)
    else:
        raise RuntimeError("%s is not a float constant" % value)


def DCONST_val(value):
    """Write an double constant onto the stack.

    There are a couple of opcodes that can be used to optimize the
    loading of some doubles; use them if possible.
    """
    if isinstance(value, float):
        if value == 0.0:
            return JavaOpcodes.DCONST_0()
        elif value == 1.0:
            return JavaOpcodes.DCONST_1()
        else:
            return JavaOpcodes.LDC2_W(value)
    else:
        raise RuntimeError("%s is not a double constant" % value)
