import sys

from unittest import expectedFailure

from ..utils import TranspileTestCase


class SysModuleTests(TranspileTestCase):

    ############################################################
    # __displayhook__
    @expectedFailure
    def test___displayhook__(self):
        self.assertCodeExecution("""
            import sys
            print(sys.__displayhook__())
            """)

    ############################################################
    # __doc__
    def test___doc__(self):
        if sys.hexversion < 0x03040500:
            # A minor change in the docstring for 3.4.5
            substitutions = {
                'the value of the largest Unicode code point': [
                    'the value of the largest Unicode codepoint'
                ]
            }
        else:
            substitutions = None

        self.assertCodeExecution(
            """
            import sys
            print(sys.__doc__)
            """,
            substitutions=substitutions
        )

    ############################################################
    # __egginsert
    @expectedFailure
    def test___egginsert(self):
        self.assertCodeExecution("""
            import sys
            print(sys.__egginsert)
            """)

    ############################################################
    # __excepthook__
    @expectedFailure
    def test___excepthook__(self):
        self.assertCodeExecution("""
            import sys
            print(sys.__excepthook__())
            """)

    ############################################################
    # __loader__
        self.assertCodeExecution("""
            import sys
            print(sys.__excepthook__())
            """)

    ############################################################
    # __name__
    def test___name__(self):
        self.assertCodeExecution("""
            import sys
            print(sys.__name__)
            """)

    ############################################################
    # __package__
    def test___package__(self):
        self.assertCodeExecution("""
            import sys
            print(sys.__package__)
            """)

    ############################################################
    # __plen
    @expectedFailure
    def test___plen(self):
        self.assertCodeExecution("""
            import sys
            print(sys.__plen)
            """)

    ############################################################
    # __spec__
    @expectedFailure
    def test___spec__(self):
        self.assertCodeExecution("""
            import sys
            print(sys.__spec__())
            """)

    ############################################################
    # __stderr__
    @expectedFailure
    def test___stderr__(self):
        self.assertCodeExecution("""
            import sys
            print(sys.__stderr__())
            """)

    ############################################################
    # __stdin__
    @expectedFailure
    def test___stdin__(self):
        self.assertCodeExecution("""
            import sys
            print(sys.__stdin__())
            """)

    ############################################################
    # __stdout__
    @expectedFailure
    def test___stdout__(self):
        self.assertCodeExecution("""
            import sys
            print(sys.__stdout__())
            """)

    ############################################################
    # _clear_type_cache
    @expectedFailure
    def test__clear_type_cache(self):
        self.assertCodeExecution("""
            import sys
            print(sys._clear_type_cache())
            """)

    ############################################################
    # _current_frames
    @expectedFailure
    def test__current_frames(self):
        self.assertCodeExecution("""
            import sys
            print(sys._current_frames())
            """)

    ############################################################
    # _debugmallocstats
    @expectedFailure
    def test__debugmallocstats(self):
        self.assertCodeExecution("""
            import sys
            print(sys._debugmallocstats())
            """)

    ############################################################
    # getframe
    @expectedFailure
    def test__getframe(self):
        self.assertCodeExecution("""
            import sys
            print(sys._getframe())
            """)

    ############################################################
    # _mercurial
    @expectedFailure
    def test__mercurial(self):
        self.assertCodeExecution("""
            import sys
            print(sys._mercurial)
            """)

    ############################################################
    # _xoptions
    @expectedFailure
    def test__xoptions(self):
        self.assertCodeExecution("""
            import sys
            print(sys._xoptions)
            """)

    ############################################################
    # abiflags
    @expectedFailure
    def test_abiflags(self):
        self.assertCodeExecution("""
            import sys
            print(sys.abiflags)
            """)

    ############################################################
    # api_version
    @expectedFailure
    def test_api_version(self):
        self.assertCodeExecution("""
            import sys
            print(sys.api_version)
            """)

    ############################################################
    # argv
    def test_argv(self):
        self.assertCodeExecution("""
            import sys
            print('ARGS =', sys.argv)
            """)

        self.assertCodeExecution("""
            import sys
            print('ARGS =', sys.argv)
            """, args=['1', 'asdf', '3'])

    ############################################################
    # base_exec_prefix
    @expectedFailure
    def test_base_exec_prefix(self):
        self.assertCodeExecution("""
            import sys
            print(sys.base_exec_prefix)
            """)

    ############################################################
    # base_prefix
    @expectedFailure
    def test_base_prefix(self):
        self.assertCodeExecution("""
            import sys
            print(sys.base_prefix)
            """)

    ############################################################
    # builtin_module_names
    @expectedFailure
    def test_builtin_module_names(self):
        self.assertCodeExecution("""
            import sys
            print(sys.builtin_module_names)
            """)

    ############################################################
    # byteorder
    @expectedFailure
    def test_byteorder(self):
        self.assertCodeExecution("""
            import sys
            print(sys.byteorder)
            """)

    ############################################################
    # call_tracing
    @expectedFailure
    def test_call_tracing(self):
        self.assertCodeExecution("""
            import sys
            print(sys.call_tracing())
            """)

    ############################################################
    # callstats
    @expectedFailure
    def test_callstats(self):
        self.assertCodeExecution("""
            import sys
            print(sys.callstats())
            """)

    ############################################################
    # copyright
    @expectedFailure
    def test_copyright(self):
        self.assertCodeExecution("""
            import sys
            print(sys.copyright)
            """)

    ############################################################
    # displayhook
    @expectedFailure
    def test_displayhook(self):
        self.assertCodeExecution("""
            import sys
            print(sys.displayhook)
            """)

    ############################################################
    # dont_write_bytecode
    @expectedFailure
    def test_dont_write_bytecode(self):
        self.assertCodeExecution("""
            import sys
            print(sys.dont_write_bytecode)
            """)

    ############################################################
    # exc_info
    @expectedFailure
    def test_exc_info(self):
        self.assertCodeExecution("""
            import sys
            prexc_info()int(sys.exc_info())
            """)

    ############################################################
    # excepthook
    @expectedFailure
    def test_excepthook(self):
        self.assertCodeExecution("""
            import sys
            print(sys.excepthook)
            """)

    ############################################################
    # exec_prefix
    @expectedFailure
    def test_exec_prefix(self):
        self.assertCodeExecution("""
            import sys
            print(sys.exec_prefix)
            """)

    ############################################################
    # executable
    @expectedFailure
    def test_executable(self):
        self.assertCodeExecution("""
            import sys
            print(sys.executable)
            """)

    ############################################################
    # exit
    def test_exit_from_static(self):
        # Exit from static block
        self.assertCodeExecution("""
            import sys
            print(sys.exit())
            """, exits_early=True)

    def test_exit(self):
        # From inside main
        self.assertCodeExecution("""
            import sys
            if __name__ == '__main__':
                print(sys.exit())
            """, run_in_function=False, exits_early=True)

        # From a method called from inside main
        self.assertCodeExecution("""
            import sys

            def foo():
                print(sys.exit())

            if __name__ == '__main__':
                foo()
            """, run_in_function=False, exits_early=True)

    ############################################################
    # flags
    @expectedFailure
    def test_flags(self):
        self.assertCodeExecution("""
            import sys
            print(sys.flags())
            """)

    ############################################################
    # float_info
    @expectedFailure
    def test_float_info(self):
        self.assertCodeExecution("""
            import sys
            print(sys.float_info())
            """)

    ############################################################
    # float_repr_style
    @expectedFailure
    def test_float_repr_style(self):
        self.assertCodeExecution("""
            import sys
            print(sys.float_repr_style)
            """)

    ############################################################
    # getallocatedblocks
    @expectedFailure
    def test_getallocatedblocks(self):
        self.assertCodeExecution("""
            import sys
            print(sys.getallocatedblocks())
            """)

    ############################################################
    # getcheckinterval
    @expectedFailure
    def test_getcheckinterval(self):
        self.assertCodeExecution("""
            import sys
            print(sys.getcheckinterval())
            """)

    ############################################################
    # getdefaultencoding
    @expectedFailure
    def test_getdefaultencoding(self):
        self.assertCodeExecution("""
            import sys
            print(sys.getdefaultencoding())
            """)

    ############################################################
    # getdlopenflags
    @expectedFailure
    def test_getdlopenflags(self):
        self.assertCodeExecution("""
            import sys
            print(sys.getdlopenflags())
            """)

    ############################################################
    # getfilesystemencoding
    @expectedFailure
    def test_getfilesystemencoding(self):
        self.assertCodeExecution("""
            import sys
            print(sys.getfilesystemencoding())
            """)

    ############################################################
    # getprofile
    @expectedFailure
    def test_getprofile(self):
        self.assertCodeExecution("""
            import sys
            print(sys.getprofile())
            """)

    ############################################################
    # getrecursionlimit
    @expectedFailure
    def test_getrecursionlimit(self):
        self.assertCodeExecution("""
            import sys
            print(sys.getrecursionlimit())
            """)

    ############################################################
    # getrefcount
    @expectedFailure
    def test_getrefcount(self):
        self.assertCodeExecution("""
            import sys
            print(sys.getrefcount())
            """)

    ############################################################
    # getsizeof
    @expectedFailure
    def test_getsizeof(self):
        self.assertCodeExecution("""
            import sys
            print(sys.getsizeof())
            """)

    ############################################################
    # Float getswitchinterval
    @expectedFailure
    def test_getswi(self):
        self.assertCodeExecution("""
            import sys
            print(sys.getswi())
            """)

    ############################################################
    # gettrace
    @expectedFailure
    def test_gettrace(self):
        self.assertCodeExecution("""
            import sys
            print(sys.gettrace())
            """)

    ############################################################
    # hash_info
    @expectedFailure
    def test_hash_info(self):
        self.assertCodeExecution("""
            import sys
            print(sys.hash_info)
            """)

    ############################################################
    # hexversion
    def test_hexversion(self):
        self.assertCodeExecution("""
            import sys
            print(sys.hexversion)
            """)

    ############################################################
    # implementation
    @expectedFailure
    def test_implementati(self):
        self.assertCodeExecution("""
            import sys
            print(sys.implementati())
            """)

    ############################################################
    # int_info
    @expectedFailure
    def test_int_info(self):
        self.assertCodeExecution("""
            import sys
            print(sys.int_info())
            """)

    ############################################################
    # intern
    @expectedFailure
    def test_intern(self):
        self.assertCodeExecution("""
            import sys
            print(sys.intern())
            """)

    ############################################################
    # last_traceback
    @expectedFailure
    def test_last_traceba(self):
        self.assertCodeExecution("""
            import sys
            print(sys.last_traceba())
            """)

    ############################################################
    # last_type
    @expectedFailure
    def test_last_type(self):
        self.assertCodeExecution("""
            import sys
            print(sys.last_type())
            """)

    ############################################################
    # last_value
    @expectedFailure
    def test_last_value(self):
        self.assertCodeExecution("""
            import sys
            print(sys.last_value())
            """)

    ############################################################
    # maxsize
    @expectedFailure
    def test_maxsize(self):
        self.assertCodeExecution("""
            import sys
            print(sys.maxsize)
            """)

    ############################################################
    # maxunicode
    @expectedFailure
    def test_maxunicode(self):
        self.assertCodeExecution("""
            import sys
            print(sys.maxunicode)
            """)

    ############################################################
    # meta_path
    @expectedFailure
    def test_meta_path(self):
        self.assertCodeExecution("""
            import sys
            print(sys.meta_path)
            """)

    ############################################################
    # modules
    @expectedFailure
    def test_modules(self):
        self.assertCodeExecution("""
            import sys
            print(sys.modules)
            """)

    ############################################################
    # path
    @expectedFailure
    def test_path(self):
        self.assertCodeExecution("""
            import sys
            print(sys.path)
            """)

    ############################################################
    # path_hooks
    @expectedFailure
    def test_path_hooks(self):
        self.assertCodeExecution("""
            import sys
            print(sys.path_hooks)
            """)

    ############################################################
    # path_importer_cache
    @expectedFailure
    def test_path_importer_cache(self):
        self.assertCodeExecution("""
            import sys
            print(sys.path_importer_cache)
            """)

    ############################################################
    # platform
    def test_platform(self):
        self.assertCodeExecution("""
            import sys
            print(sys.platform)
            """)

    ############################################################
    # prefix
    @expectedFailure
    def test_prefix(self):
        self.assertCodeExecution("""
            import sys
            print(sys.prefix)
            """)

    ############################################################
    # ps1
    @expectedFailure
    def test_ps1(self):
        self.assertCodeExecution("""
            import sys
            print(sys.ps1)
            """)

    ############################################################
    # ps2
    @expectedFailure
    def test_ps2(self):
        self.assertCodeExecution("""
            import sys
            print(sys.ps2)
            """)

    ############################################################
    # ps3
    @expectedFailure
    def test_ps3(self):
        self.assertCodeExecution("""
            import sys
            print(sys.ps3)
            """)

    ############################################################
    # real_prefix
    @expectedFailure
    def test_real_prefix(self):
        self.assertCodeExecution("""
            import sys
            print(sys.real_prefix)
            """)

    ############################################################
    # setcheckinterval
    @expectedFailure
    def test_setcheckinterval(self):
        self.assertCodeExecution("""
            import sys
            print(sys.setcheckinterval())
            """)

    ############################################################
    # setdlopenflags
    @expectedFailure
    def test_setdlopenflags(self):
        self.assertCodeExecution("""
            import sys
            print(sys.setdlopenflags())
            """)

    ############################################################
    # setprofile
    @expectedFailure
    def test_setprofile(self):
        self.assertCodeExecution("""
            import sys
            print(sys.setprofile())
            """)

    ############################################################
    # setrecursionlimit
    @expectedFailure
    def test_setrecursionlimit(self):
        self.assertCodeExecution("""
            import sys
            print(sys.setrecursionlimit())
            """)

    ############################################################
    # setswitchinterval
    @expectedFailure
    def test_setswitchinterval(self):
        self.assertCodeExecution("""
            import sys
            print(sys.setswitchinterval())
            """)

    ############################################################
    # settrace
    @expectedFailure
    def test_settrace(self):
        self.assertCodeExecution("""
            import sys
            print(sys.settrace())
            """)

    ############################################################
    # stderr
    @expectedFailure
    def test_stderr(self):
        self.assertCodeExecution("""
            import sys
            print(sys.stderr())
            """)

    ############################################################
    # stdin
    @expectedFailure
    def test_stdin(self):
        self.assertCodeExecution("""
            import sys
            print(sys.stdin())
            """)

    ############################################################
    # stdout
    @expectedFailure
    def test_stdout(self):
        self.assertCodeExecution("""
            import sys
            print(sys.stdout())
            """)

    ############################################################
    # thread_info
    @expectedFailure
    def test_thread_info(self):
        self.assertCodeExecution("""
            import sys
            print(sys.thread_info())
            """)

    ############################################################
    # version
    @expectedFailure
    def test_version(self):
        self.assertCodeExecution("""
            import sys
            lines = sys.version.split('\n')
            print("There are %d lines" % len(lines))
            print(lines[0].split(' ')[0])
            """)

    ############################################################
    # version_info
    def test_version_info(self):
        self.assertCodeExecution("""
            import sys
            print(sys.version_info)
            """)

    ############################################################
    # warnoptions
    @expectedFailure
    def test_warnoptions(self):
        self.assertCodeExecution("""
            import sys
            print(sys.warnoptions)
            """)
