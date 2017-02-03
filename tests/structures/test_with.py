from unittest import expectedFailure

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
