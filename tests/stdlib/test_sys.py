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
            print('Done.')
            """)

    ############################################################
    # __doc__
    @expectedFailure
    def test___doc__(self):
        self.assertCodeExecution("""
            import sys
            print(sys.__doc__)
            print('Done.')
            """)

    ############################################################
    # __egginsert
    @expectedFailure
    def test___egginsert(self):
        self.assertCodeExecution("""
            import sys
            print(sys.__egginsert)
            print('Done.')
            """)

    ############################################################
    # __excepthook__
    @expectedFailure
    def test___excepthook__(self):
        self.assertCodeExecution("""
            import sys
            print(sys.__excepthook__())
            print('Done.')
            """)

    ############################################################
    # __loader__
        self.assertCodeExecution("""
            import sys
            print(sys.__excepthook__())
            print('Done.')
            """)

    ############################################################
    # __name__
    @expectedFailure
    def test___name__(self):
        self.assertCodeExecution("""
            import sys
            print(sys.__name__)
            print('Done.')
            """)

    ############################################################
    # __package__
    @expectedFailure
    def test___package__(self):
        self.assertCodeExecution("""
            import sys
            print(sys.__package__)
            print('Done.')
            """)

    ############################################################
    # __plen
    @expectedFailure
    def test___plen(self):
        self.assertCodeExecution("""
            import sys
            print(sys.__plen)
            print('Done.')
            """)

    ############################################################
    # __spec__
    @expectedFailure
    def test___spec__(self):
        self.assertCodeExecution("""
            import sys
            print(sys.__spec__())
            print('Done.')
            """)

    ############################################################
    # __stderr__
    @expectedFailure
    def test___stderr__(self):
        self.assertCodeExecution("""
            import sys
            print(sys.__stderr__())
            print('Done.')
            """)

    ############################################################
    # __stdin__
    @expectedFailure
    def test___stdin__(self):
        self.assertCodeExecution("""
            import sys
            print(sys.__stdin__())
            print('Done.')
            """)

    ############################################################
    # __stdout__
    @expectedFailure
    def test___stdout__(self):
        self.assertCodeExecution("""
            import sys
            print(sys.__stdout__())
            print('Done.')
            """)

    ############################################################
    # _clear_type_cache
    @expectedFailure
    def test__clear_type_cache(self):
        self.assertCodeExecution("""
            import sys
            print(sys._clear_type_cache())
            print('Done.')
            """)

    ############################################################
    # _current_frames
    @expectedFailure
    def test__current_frames(self):
        self.assertCodeExecution("""
            import sys
            print(sys._current_frames())
            print('Done.')
            """)

    ############################################################
    # _debugmallocstats
    @expectedFailure
    def test__debugmallocstats(self):
        self.assertCodeExecution("""
            import sys
            print(sys._debugmallocstats())
            print('Done.')
            """)

    ############################################################
    # getframe
    @expectedFailure
    def test__getframe(self):
        self.assertCodeExecution("""
            import sys
            print(sys._getframe())
            print('Done.')
            """)

    ############################################################
    # _mercurial
    @expectedFailure
    def test__mercurial(self):
        self.assertCodeExecution("""
            import sys
            print(sys._mercurial)
            print('Done.')
            """)

    ############################################################
    # _xoptions
    @expectedFailure
    def test__xoptions(self):
        self.assertCodeExecution("""
            import sys
            print(sys._xoptions)
            print('Done.')
            """)

    ############################################################
    # abiflags
    @expectedFailure
    def test_abiflags(self):
        self.assertCodeExecution("""
            import sys
            print(sys.abiflags)
            print('Done.')
            """)

    ############################################################
    # api_version
    @expectedFailure
    def test_api_version(self):
        self.assertCodeExecution("""
            import sys
            print(sys.api_version)
            print('Done.')
            """)

    ############################################################
    # argv
    def test_argv(self):
        self.assertCodeExecution("""
            import sys
            print('ARGS =', sys.argv)
            print('Done.')
            """)

        self.assertCodeExecution("""
            import sys
            print('ARGS =', sys.argv)
            print('Done.')
            """, args=['1', 'asdf', '3'])

    ############################################################
    # base_exec_prefix
    @expectedFailure
    def test_base_exec_prefix(self):
        self.assertCodeExecution("""
            import sys
            print(sys.base_exec_prefix)
            print('Done.')
            """)

    ############################################################
    # base_prefix
    @expectedFailure
    def test_base_prefix(self):
        self.assertCodeExecution("""
            import sys
            print(sys.base_prefix)
            print('Done.')
            """)

    ############################################################
    # builtin_module_names
    @expectedFailure
    def test_builtin_module_names(self):
        self.assertCodeExecution("""
            import sys
            print(sys.builtin_module_names)
            print('Done.')
            """)

    ############################################################
    # byteorder
    @expectedFailure
    def test_byteorder(self):
        self.assertCodeExecution("""
            import sys
            print(sys.byteorder)
            print('Done.')
            """)

    ############################################################
    # call_tracing
    @expectedFailure
    def test_call_tracing(self):
        self.assertCodeExecution("""
            import sys
            print(sys.call_tracing())
            print('Done.')
            """)

    ############################################################
    # callstats
    @expectedFailure
    def test_callstats(self):
        self.assertCodeExecution("""
            import sys
            print(sys.callstats())
            print('Done.')
            """)

    ############################################################
    # copyright
    @expectedFailure
    def test_copyright(self):
        self.assertCodeExecution("""
            import sys
            print(sys.copyright)
            print('Done.')
            """)

    ############################################################
    # displayhook
    @expectedFailure
    def test_displayhook(self):
        self.assertCodeExecution("""
            import sys
            print(sys.displayhook)
            print('Done.')
            """)

    ############################################################
    # dont_write_bytecode
    @expectedFailure
    def test_dont_write_bytecode(self):
        self.assertCodeExecution("""
            import sys
            print(sys.dont_write_bytecode)
            print('Done.')
            """)

    ############################################################
    # exc_info
    @expectedFailure
    def test_exc_info(self):
        self.assertCodeExecution("""
            import sys
            prexc_info()int(sys.exc_info())
            print('Done.')
            """)

    ############################################################
    # excepthook
    @expectedFailure
    def test_excepthook(self):
        self.assertCodeExecution("""
            import sys
            print(sys.excepthook)
            print('Done.')
            """)

    ############################################################
    # exec_prefix
    @expectedFailure
    def test_exec_prefix(self):
        self.assertCodeExecution("""
            import sys
            print(sys.exec_prefix)
            print('Done.')
            """)

    ############################################################
    # executable
    @expectedFailure
    def test_executable(self):
        self.assertCodeExecution("""
            import sys
            print(sys.executable)
            print('Done.')
            """)

    ############################################################
    # exit
    def test_exit_from_static(self):
        # Exit from static block
        self.assertCodeExecution("""
            import sys
            print(sys.exit())
            print('Done.')
            """)

    def test_exit(self):
        # From inside main
        self.assertCodeExecution("""
            import sys
            if __name__ == '__main__':
                print(sys.exit())
                print('Done.')
            """, run_in_function=False)

        # From a method called from inside main
        self.assertCodeExecution("""
            import sys

            def foo():
                print(sys.exit())

            if __name__ == '__main__':
                foo()
                print('Done.')
            """, run_in_function=False)

    ############################################################
    # flags
    @expectedFailure
    def test_flags(self):
        self.assertCodeExecution("""
            import sys
            print(sys.flags())
            print('Done.')
            """)

    ############################################################
    # float_info
    @expectedFailure
    def test_float_info(self):
        self.assertCodeExecution("""
            import sys
            print(sys.float_info())
            print('Done.')
            """)

    ############################################################
    # float_repr_style
    @expectedFailure
    def test_float_repr_style(self):
        self.assertCodeExecution("""
            import sys
            print(sys.float_repr_style)
            print('Done.')
            """)

    ############################################################
    # getallocatedblocks
    @expectedFailure
    def test_getallocatedblocks(self):
        self.assertCodeExecution("""
            import sys
            print(sys.getallocatedblocks())
            print('Done.')
            """)

    ############################################################
    # getcheckinterval
    @expectedFailure
    def test_getcheckinterval(self):
        self.assertCodeExecution("""
            import sys
            print(sys.getcheckinterval())
            print('Done.')
            """)

    ############################################################
    # getdefaultencoding
    @expectedFailure
    def test_getdefaultencoding(self):
        self.assertCodeExecution("""
            import sys
            print(sys.getdefaultencoding())
            print('Done.')
            """)

    ############################################################
    # getdlopenflags
    @expectedFailure
    def test_getdlopenflags(self):
        self.assertCodeExecution("""
            import sys
            print(sys.getdlopenflags())
            print('Done.')
            """)

    ############################################################
    # getfilesystemencoding
    @expectedFailure
    def test_getfilesystemencoding(self):
        self.assertCodeExecution("""
            import sys
            print(sys.getfilesystemencoding())
            print('Done.')
            """)

    ############################################################
    # getprofile
    @expectedFailure
    def test_getprofile(self):
        self.assertCodeExecution("""
            import sys
            print(sys.getprofile())
            print('Done.')
            """)

    ############################################################
    # getrecursionlimit
    @expectedFailure
    def test_getrecursionlimit(self):
        self.assertCodeExecution("""
            import sys
            print(sys.getrecursionlimit())
            print('Done.')
            """)

    ############################################################
    # getrefcount
    @expectedFailure
    def test_getrefcount(self):
        self.assertCodeExecution("""
            import sys
            print(sys.getrefcount())
            print('Done.')
            """)

    ############################################################
    # getsizeof
    @expectedFailure
    def test_getsizeof(self):
        self.assertCodeExecution("""
            import sys
            print(sys.getsizeof())
            print('Done.')
            """)

    ############################################################
    # Float getswitchinterval
    @expectedFailure
    def test_getswi(self):
        self.assertCodeExecution("""
            import sys
            print(sys.getswi())
            print('Done.')
            """)

    ############################################################
    # gettrace
    @expectedFailure
    def test_gettrace(self):
        self.assertCodeExecution("""
            import sys
            print(sys.gettrace())
            print('Done.')
            """)

    ############################################################
    # hash_info
    @expectedFailure
    def test_hash_info(self):
        self.assertCodeExecution("""
            import sys
            print(sys.hash_info)
            print('Done.')
            """)

    ############################################################
    # hexversion
    @expectedFailure
    def test_hexversion(self):
        self.assertCodeExecution("""
            import sys
            print(sys.hexversion)
            print('Done.')
            """)

    ############################################################
    # implementation
    @expectedFailure
    def test_implementati(self):
        self.assertCodeExecution("""
            import sys
            print(sys.implementati())
            print('Done.')
            """)

    ############################################################
    # int_info
    @expectedFailure
    def test_int_info(self):
        self.assertCodeExecution("""
            import sys
            print(sys.int_info())
            print('Done.')
            """)

    ############################################################
    # intern
    @expectedFailure
    def test_intern(self):
        self.assertCodeExecution("""
            import sys
            print(sys.intern())
            print('Done.')
            """)

    ############################################################
    # last_traceback
    @expectedFailure
    def test_last_traceba(self):
        self.assertCodeExecution("""
            import sys
            print(sys.last_traceba())
            print('Done.')
            """)

    ############################################################
    # last_type
    @expectedFailure
    def test_last_type(self):
        self.assertCodeExecution("""
            import sys
            print(sys.last_type())
            print('Done.')
            """)

    ############################################################
    # last_value
    @expectedFailure
    def test_last_value(self):
        self.assertCodeExecution("""
            import sys
            print(sys.last_value())
            print('Done.')
            """)

    ############################################################
    # maxsize
    @expectedFailure
    def test_maxsize(self):
        self.assertCodeExecution("""
            import sys
            print(sys.maxsize)
            print('Done.')
            """)

    ############################################################
    # maxunicode
    @expectedFailure
    def test_maxunicode(self):
        self.assertCodeExecution("""
            import sys
            print(sys.maxunicode)
            print('Done.')
            """)

    ############################################################
    # meta_path
    @expectedFailure
    def test_meta_path(self):
        self.assertCodeExecution("""
            import sys
            print(sys.meta_path)
            print('Done.')
            """)

    ############################################################
    # modules
    @expectedFailure
    def test_modules(self):
        self.assertCodeExecution("""
            import sys
            print(sys.modules)
            print('Done.')
            """)

    ############################################################
    # path
    @expectedFailure
    def test_path(self):
        self.assertCodeExecution("""
            import sys
            print(sys.path)
            print('Done.')
            """)

    ############################################################
    # path_hooks
    @expectedFailure
    def test_path_hooks(self):
        self.assertCodeExecution("""
            import sys
            print(sys.path_hooks)
            print('Done.')
            """)

    ############################################################
    # path_importer_cache
    @expectedFailure
    def test_path_importer_cache(self):
        self.assertCodeExecution("""
            import sys
            print(sys.path_importer_cache)
            print('Done.')
            """)

    ############################################################
    # platform
    @expectedFailure
    def test_platform(self):
        self.assertCodeExecution("""
            import sys
            print(sys.platform)
            print('Done.')
            """)

    ############################################################
    # prefix
    @expectedFailure
    def test_prefix(self):
        self.assertCodeExecution("""
            import sys
            print(sys.prefix)
            print('Done.')
            """)

    ############################################################
    # ps1
    @expectedFailure
    def test_ps1(self):
        self.assertCodeExecution("""
            import sys
            print(sys.ps1)
            print('Done.')
            """)

    ############################################################
    # ps2
    @expectedFailure
    def test_ps2(self):
        self.assertCodeExecution("""
            import sys
            print(sys.ps2)
            print('Done.')
            """)

    ############################################################
    # ps3
    @expectedFailure
    def test_ps3(self):
        self.assertCodeExecution("""
            import sys
            print(sys.ps3)
            print('Done.')
            """)

    ############################################################
    # real_prefix
    @expectedFailure
    def test_real_prefix(self):
        self.assertCodeExecution("""
            import sys
            print(sys.real_prefix)
            print('Done.')
            """)

    ############################################################
    # setcheckinterval
    @expectedFailure
    def test_setcheckinterval(self):
        self.assertCodeExecution("""
            import sys
            print(sys.setcheckinterval())
            print('Done.')
            """)

    ############################################################
    # setdlopenflags
    @expectedFailure
    def test_setdlopenflags(self):
        self.assertCodeExecution("""
            import sys
            print(sys.setdlopenflags())
            print('Done.')
            """)

    ############################################################
    # setprofile
    @expectedFailure
    def test_setprofile(self):
        self.assertCodeExecution("""
            import sys
            print(sys.setprofile())
            print('Done.')
            """)

    ############################################################
    # setrecursionlimit
    @expectedFailure
    def test_setrecursionlimit(self):
        self.assertCodeExecution("""
            import sys
            print(sys.setrecursionlimit())
            print('Done.')
            """)

    ############################################################
    # setswitchinterval
    @expectedFailure
    def test_setswitchinterval(self):
        self.assertCodeExecution("""
            import sys
            print(sys.setswitchinterval())
            print('Done.')
            """)

    ############################################################
    # settrace
    @expectedFailure
    def test_settrace(self):
        self.assertCodeExecution("""
            import sys
            print(sys.settrace())
            print('Done.')
            """)

    ############################################################
    # stderr
    @expectedFailure
    def test_stderr(self):
        self.assertCodeExecution("""
            import sys
            print(sys.stderr())
            print('Done.')
            """)

    ############################################################
    # stdin
    @expectedFailure
    def test_stdin(self):
        self.assertCodeExecution("""
            import sys
            print(sys.stdin())
            print('Done.')
            """)

    ############################################################
    # stdout
    @expectedFailure
    def test_stdout(self):
        self.assertCodeExecution("""
            import sys
            print(sys.stdout())
            print('Done.')
            """)

    ############################################################
    # thread_info
    @expectedFailure
    def test_thread_info(self):
        self.assertCodeExecution("""
            import sys
            print(sys.thread_info())
            print('Done.')
            """)

    ############################################################
    # version
    @expectedFailure
    def test_version(self):
        self.assertCodeExecution("""
            import sys
            print(sys.version)
            print('Done.')
            """)

    ############################################################
    # version_info
    @expectedFailure
    def test_version_info(self):
        self.assertCodeExecution("""
            import sys
            print(sys.version_info())
            print('Done.')
            """)

    ############################################################
    # warnoptions
    @expectedFailure
    def test_warnoptions(self):
        self.assertCodeExecution("""
            import sys
            print(sys.warnoptions)
            print('Done.')
            """)
