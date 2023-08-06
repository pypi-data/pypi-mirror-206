"""
 * FFT Multiplication
 *
 * @author      Moin Khan
 * @copyright   Moin Khan
 *
 * @link https://mo.inkhan.dev
 *
 */
 """

import unittest
from fft_multiplication import multiply, direct_multiply


class TestDivideByThree(unittest.TestCase):

    def test_multiply_case_1(self):
        self.assertEqual(multiply([1, 1], [1]), [1.0, 1.0])

    def test_multiply_case_2(self):
        self.assertEqual(multiply([1, 1.5], [1, 0]), [1.0, 1.5, 0.0, 0.0])

    def test_multiply_case_3(self):
        self.assertEqual(multiply([1, 1.5], [1, 0, 1, 1]), [
                         1.0, 1.5, 1.0, 2.5, 1.5, 0.0, 0.0, 0.0])

    def test_multiply_case_4(self):
        self.assertEqual(direct_multiply([1, 1], [1]), [1.0, 1.0])

    def test_multiply_case_5(self):
        self.assertEqual(direct_multiply(
            [1, 1.5], [1, 0]), [1.0, 1.5, 0.0, 0.0])

    def test_multiply_case_6(self):
        self.assertEqual(direct_multiply([1, 1.5], [1, 0, 1, 1]), [
                         1.0, 1.5, 1.0, 2.5, 1.5, 0.0, 0.0, 0.0])


unittest.main()
