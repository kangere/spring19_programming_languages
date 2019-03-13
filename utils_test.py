import unittest

from lang.utils import *


class UtilsTest(unittest.TestCase):
	def test_utils(self):
		t = TypeCheckerMixIn()
		self.assertTrue(t.is_a(TypeCheckerMixIn))