from ..utils import TranspileTestCase


class WithLoopTests(TranspileTestCase):
    def test_with(self):
        self.assertCodeExecution("""
            class CtxMgr:
                def __enter__(self):
                    print('entering CtxMgr')
                    return 42
                def __exit__(self, *args):
                    print('exiting CtxMgr')

            with CtxMgr() as val:
                print('val', val)

            val = 16
            with CtxMgr():
                print('in another ctx, val now is', val)
            """)

    # TODO: make this test pass
    # def test_with_body_fails(self):
    #     self.assertCodeExecution("""
    #         class CtxMgr:
    #             def __enter__(self):
    #                 print('entering CtxMgr')
    #             def __exit__(self, *args):
    #                 print('exiting CtxMgr')
    #
    #         with CtxMgr():
    #             raise ValueError
    #         """)

    def test_with_noexit(self):
        self.assertCodeExecution("""
            class CtxMgrMissingExit:
                def __enter__(self):
                    print('entering CtxMgrMissingExit')
            with CtxMgrMissingExit():
                print('inside')
        """)

    def test_with_noenter(self):
        self.assertCodeExecution("""
            class CtxMgrMissingEnter:
                def __exit__(self, *args):
                    print('exiting CtxMgrMissingEnter')
            with CtxMgrMissingEnter():
                print('inside')
        """)
