import importlib
import marshal
import os
import py_compile

from .python.modules import Module


def transpile(filename, srcdir='.', outdir=None):
    print("Compiling %s ..." % filename)
    py_compile.compile(filename, doraise=True)

    transpiler = Transpiler()
    transpiler.transpile(filename, srcdir)
    transpiler.write(outdir)


class Transpiler:
    def __init__(self, namespace="python"):
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
            classfilename = os.path.join(dirname, '%s.class' % class_name)

            try:
                os.makedirs(os.path.dirname(classfilename))
            except FileExistsError:
                pass

            if verbosity:
                print("Writing %s ..." % classfilename)

            with open(classfilename, 'wb') as out:
                javaclassfile.write(out)
        if verbosity:
            print("Done.")

    def transpile(self, filename, srcdir):
        "Transpile a Python source file into class files"
        with open(importlib.util.cache_from_source(filename), 'rb') as compiled:
            # Read off the magic from the start of the PYC file.
            compiled.read(12)

            # Decompile the code object.
            code = marshal.load(compiled)

            # Determine what portion of the filename is part of the
            # common source directory, and which is namespace.
            common = os.path.commonprefix([
                os.path.abspath(srcdir),
                os.path.abspath(filename)
            ])

            self.transpile_code(os.path.abspath(filename)[len(common):], code)

    def transpile_string(self, filename, code_string):
        "Transpile a string containing Python code into class files"
        code = compile(code_string, filename, "exec")

        self.transpile_code(filename, code)

    def transpile_code(self, filename, code):
        "Transpile a code object into class files"
        module = Module(self.namespace, filename)

        # Extract commands from the code block
        module.extract(code)

        # Materialize the code structures
        module.materialize()

        # Transpile the module code, adding any classfiles generated
        # to the list to be exported.
        self.classfiles.extend(module.transpile())
