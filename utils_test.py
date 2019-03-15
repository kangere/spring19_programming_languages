import unittest

from lang.utils import *


class UtilsTest(unittest.TestCase):
	def test_utils(self):
		t = UtilsMixIn()
		self.assertTrue(t.is_a(UtilsMixIn))