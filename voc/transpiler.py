import importlib
import marshal
import os
import py_compile
import sys

from .python.modules import Module


def transpile(input, prefix='.', outdir=None, namespace='python', verbosity=0):
    transpiler = Transpiler(namespace=namespace, verbosity=verbosity)

    for source_file in input:
        if os.path.isfile(source_file):
            if verbosity:
                print("Compiling %s ..." % source_file)
            py_compile.compile(source_file, doraise=True)
            transpiler.transpile(source_file, prefix)
        elif os.path.isdir(source_file):
            for root, dirs, files in os.walk(source_file, followlinks=True):
                for filename in files:
                    if os.path.splitext(filename)[1] == '.py':
                        source = os.path.join(root, filename)
                        if verbosity:
                            print("Compiling %s ..." % source)
                        py_compile.compile(source, doraise=True)
                        transpiler.transpile(source, prefix)
        else:
            print("Unknown source file type: ", source_file, file=sys.stderr)

    transpiler.write(outdir)


class Transpiler:
    def __init__(self, namespace="python", verbosity=0):
        self.namespace = namespace
        self.classfiles = []
        self.verbosity = verbosity

    def write(self, outdir):
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

            if self.verbosity:
                print("Writing %s ..." % classfilename)

            with open(classfilename, 'wb') as out:
                javaclassfile.write(out)

    def transpile(self, filename, prefix):
        "Transpile a Python source file into class files"
        with open(importlib.util.cache_from_source(filename), 'rb') as compiled:
            # Read off the magic from the start of the PYC file.
            compiled.read(12)

            # Decompile the code object.
            code = marshal.load(compiled)

            # Determine what portion of the filename is part of the
            # common source directory, and which is namespace.
            common = os.path.commonprefix([
                os.path.abspath(prefix),
                os.path.abspath(filename)
            ])

            self.transpile_code(os.path.abspath(filename)[len(common):], code)

    def transpile_string(self, filename, code_string):
        "Transpile a string containing Python code into class files"
        code = compile(code_string, filename, "exec")

        self.transpile_code(filename, code)

    def transpile_code(self, filename, code):
        "Transpile a code object into class files"
        module = Module(self.namespace, filename, verbosity=self.verbosity)

        # Extract commands from the code block
        module.extract(code)

        # Materialize the code structures
        module.materialize()

        # Transpile the module code, adding any classfiles generated
        # to the list to be exported.
        self.classfiles.extend(module.transpile())
