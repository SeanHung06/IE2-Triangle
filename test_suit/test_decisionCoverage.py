import unittest
from isTriangle import Triangle

class TestTriangleDecisionCoverage(unittest.TestCase):

    def test_invalid_all_zero(self):
        self.assertEqual(Triangle.classify(0, 0, 0), Triangle.Type.INVALID)

    def test_invalid_all_neg(self):
        self.assertEqual(Triangle.classify(-1, -1, -1), Triangle.Type.INVALID)

    def test_invalid_a_neg(self):
        self.assertEqual(Triangle.classify(-1, 10, 10), Triangle.Type.INVALID)

    def test_invalid_a_zero(self):
        self.assertEqual(Triangle.classify(0, 10, 10), Triangle.Type.INVALID)

    def test_invalid_a_pos(self):
        self.assertEqual(Triangle.classify(1, 10, 10), Triangle.Type.ISOSCELES)

    def test_invalid_b_neg(self):
        self.assertEqual(Triangle.classify(10, -1, 10), Triangle.Type.INVALID)

    def test_invalid_b_zero(self):
        self.assertEqual(Triangle.classify(10, 0, 10), Triangle.Type.INVALID)

    def test_invalid_b_pos(self):
        self.assertEqual(Triangle.classify(10, 1, 10), Triangle.Type.ISOSCELES)

    def test_invalid_c_neg(self):
        self.assertEqual(Triangle.classify(10, 10, -1), Triangle.Type.INVALID)

    def test_invalid_c_zero(self):
        self.assertEqual(Triangle.classify(10, 10, 0), Triangle.Type.INVALID)

    def test_invalid_c_pos(self):
        self.assertEqual(Triangle.classify(10, 10, 1), Triangle.Type.ISOSCELES)

    def test_a_equal_b(self):
        self.assertEqual(Triangle.classify(10, 10, 19), Triangle.Type.ISOSCELES)

    def test_a_equal_c(self):
        self.assertEqual(Triangle.classify(10, 19, 10), Triangle.Type.ISOSCELES)

    def test_b_equal_c(self):
        self.assertEqual(Triangle.classify(19, 10, 10), Triangle.Type.ISOSCELES)

    def test_trian_equal_0_case_1a(self):
        self.assertEqual(Triangle.classify(4, 2, 6), Triangle.Type.INVALID)

    def test_trian_equal_0_case_1b(self):
        self.assertEqual(Triangle.classify(4, 6, 2), Triangle.Type.INVALID)

    def test_trian_equal_0_case_1c(self):
        self.assertEqual(Triangle.classify(6, 2, 4), Triangle.Type.INVALID)

    def test_trian_equal_0_case_2(self):
        self.assertEqual(Triangle.classify(2, 6, 5), Triangle.Type.SCALENE)

    def test_trian_gt_3(self):
        self.assertEqual(Triangle.classify(10, 10, 10), Triangle.Type.EQUILATERAL)

    def test_isosceles_1(self):
        self.assertEqual(Triangle.classify(2, 2, 3), Triangle.Type.ISOSCELES)

    def test_isosceles_2(self):
        self.assertEqual(Triangle.classify(3, 2, 2), Triangle.Type.ISOSCELES)

    def test_isosceles_3(self):
        self.assertEqual(Triangle.classify(2, 3, 2), Triangle.Type.ISOSCELES)

    def test_invalid_isosceles_1(self):
        self.assertEqual(Triangle.classify(2, 2, 4), Triangle.Type.INVALID)

    def test_invalid_isosceles_2(self):
        self.assertEqual(Triangle.classify(4, 2, 2), Triangle.Type.INVALID)

    def test_invalid_isosceles_3(self):
        self.assertEqual(Triangle.classify(2, 4, 2), Triangle.Type.INVALID)

    def test_invalid_return_1(self):
        self.assertEqual(Triangle.classify(3, 3, 7), Triangle.Type.INVALID)

    def test_invalid_return_2(self):
        self.assertEqual(Triangle.classify(3, 7, 3), Triangle.Type.INVALID)

    def test_invalid_return_3(self):
        self.assertEqual(Triangle.classify(7, 3, 3), Triangle.Type.INVALID)

    def test_mutant_85(self):
        self.assertEqual(Triangle.classify(5, 2, 1), Triangle.Type.INVALID)

    def test_mutant_74(self):
        self.assertEqual(Triangle.classify(2, 5, 1), Triangle.Type.INVALID)

    def test_mutant_67(self):
        self.assertEqual(Triangle.classify(2, 1, 5), Triangle.Type.INVALID)

if __name__ == "__main__":
    unittest.main()
