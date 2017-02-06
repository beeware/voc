from ..utils import TranspileTestCase


class WithLoopTests(TranspileTestCase):
    def test_with(self):
        self.assertCodeExecution("""
            class CtxMgr:
                def __enter__(self):
                    print('entering CtxMgr')
                    return 42
                def __exit__(self, *args):
                    print('exiting CtxMgr', args)

            with CtxMgr() as val:
                print('val', val)

            print('val outside block', val)

            val = 16
            with CtxMgr():
                print('in another ctx, val now is', val)
            """)

    def test_with_body_fails(self):
        # TODO: add support for exc_type and traceback information
        self.assertCodeExecution("""
            class CtxMgr:
                def __enter__(self):
                    print('entering CtxMgr')
                def __exit__(self, exc_type, exc_value, traceback):
                    print('exiting CtxMgr')
                    # print('exc_type', exc_type)
                    print('exc_value', exc_value)
                    # print('traceback', traceback)

            with CtxMgr():
                raise KeyError('ola')
            """, exits_early=True)

    def test_with_noexit(self):
        self.assertCodeExecution("""
            class CtxMgrMissingExit:
                def __enter__(self):
                    print('entering CtxMgrMissingExit')
            with CtxMgrMissingExit():
                print('inside')
        """, exits_early=True)

    def test_with_noenter(self):
        self.assertCodeExecution("""
            class CtxMgrMissingEnter:
                def __exit__(self, *args):
                    print('exiting CtxMgrMissingEnter')
            with CtxMgrMissingEnter():
                print('inside')
        """, exits_early=True)

    def test_with_nested(self):
        self.assertCodeExecution("""
            class CtxMgr:
                def __enter__(self):
                    print('entering CtxMgr')
                    return 42
                def __exit__(self, *args):
                    print('exiting CtxMgr')

            class CtxMgr2:
                def __enter__(self):
                    print('entering CtxMgr2')
                    return 24
                def __exit__(self, *args):
                    print('exiting CtxMgr2')

            with CtxMgr() as val, CtxMgr2() as val2:
                print('val', val)
                print('val2', val2)
            """)
