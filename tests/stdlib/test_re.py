import unittest

from ..utils import TranspileTestCase


class ReModuleTests(TranspileTestCase):
    def test_escape(self):
        self.assertCodeExecution("""
        import re
        print (re.escape('python.exe'))
        """)
