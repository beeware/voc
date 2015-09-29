import importlib
import marshal
import os
import py_compile

from .python.modules import Module


def transpile(filename, namespace, outdir=None):
    print("Compiling %s ..." % filename)
    py_compile.compile(filename)

    transpiler = Transpiler(namespace)
    transpiler.transpile(filename)
    transpiler.write(outdir)


class Transpiler:
    def __init__(self, namespace):
        self.namespace = namespace
        self.classfiles = []

    def write(self, outdir, verbosity=1):
        # Create directory tree to store classfile
        if outdir:
            basedir = [outdir]
        else:
            basedir = []

        for namespace, class_name, javaclassfile in self.classfiles:
            dirname = os.path.join(*(basedir + namespace.split('.')))
            try:
                os.makedirs(dirname)
            except FileExistsError:
                pass

            classfilename = os.path.join(dirname, '%s.class' % class_name)

            if verbosity:
                print("Writing %s ..." % classfilename)
            with open(classfilename, 'wb') as out:
                javaclassfile.write(out)
        if verbosity:
            print("Done.")

    def transpile(self, filename):
        "Transpile a Python source file into class files"
        with open(importlib.util.cache_from_source(filename), 'rb') as compiled:
            # Read off the magic from the start of the PYC file.
            compiled.read(12)

            # Decompile the code object.
            code = marshal.load(compiled)

            self.transpile_code(filename, code)

    def transpile_string(self, filename, code_string):
        "Transpile a string containing Python code into class files"
        code = compile(code_string, filename, "exec")

        self.transpile_code(filename, code)

    def transpile_code(self, filename, code):
        "Transpile a code object into class files"
        module = Module(self.namespace, filename)

        # Extract commands from the code block
        module.extract(code)

        # Transpile the module code, adding any classfiles generated
        # to the list to be exported.
        self.classfiles.extend(module.transpile())
