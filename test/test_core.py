import unittest
import numpy as np
import shrew
import os


class TestReadEnrollFile(unittest.TestCase):

	def test_read_empty_file(self):
		c = shrew.read_enroll_file(os.path.join('test', 'enroll1.txt'), [3, 2, 3], 2)
		np.testing.assert_array_equal(c, np.zeros((3, 2, 3, 2)))

	def test_read_enroll_2x2x2_file(self):
		c = shrew.read_enroll_file(os.path.join('test', 'enroll2.txt'), [2, 2], 2)
		exp_mat = np.zeros((2, 2, 2))
		exp_mat[1, 0, 0] = 1
		exp_mat[0, 0, 1] = 2
		np.testing.assert_array_equal(c, exp_mat)
