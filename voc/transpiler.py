import importlib
import marshal
import os
import py_compile

from .python.modules import Module


def transpile(sourcefile, namespace, outdir=None):
    print("Compiling %s ..." % sourcefile)
    py_compile.compile(sourcefile)

    transpiler = Transpiler(namespace)
    transpiler.transpile(sourcefile)
    transpiler.write(outdir)


class Transpiler:
    def __init__(self, namespace):
        self.namespace = namespace
        self.classfiles = []

    def write(self, outdir):
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

            print("Writing %s ..." % classfilename)
            with open(classfilename, 'wb') as out:
                javaclassfile.write(out)
        print("Done.")

    def transpile(self, sourcefile):
        with open(importlib.util.cache_from_source(sourcefile), 'rb') as compiled:
            # Read off the magic from the start of the PYC file.
            compiled.read(12)

            # Decompile the code object.
            code = marshal.load(compiled)

        module = Module(self.namespace, sourcefile)

        # Extract commands from the code block
        module.extract(code)

        # Transpile the module code, adding any classfiles generated
        # to the list to be exported.
        self.classfiles.extend(module.transpile())
