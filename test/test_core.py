import unittest
import shrew


class TestTester(unittest.TestCase):

	def test_add(self):
		t = shrew.add(2, 3)
		self.assertEqual(t, 5)
