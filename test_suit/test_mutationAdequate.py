import unittest
from isTriangle import Triangle

class TestTriangleMutationAdequate(unittest.TestCase):

    def test_equilateral(self):
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    def test_invalid_a(self):
        actual = Triangle.classify(-1, 10, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_invalid_b(self):
        actual = Triangle.classify(10, -1, 10)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_invalid_c(self):
        actual = Triangle.classify(10, 10, -1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_a_equal_b(self):
        actual = Triangle.classify(10, 10, 19)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test_a_equal_c(self):
        actual = Triangle.classify(10, 19, 10)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test_b_equal_c(self):
        actual = Triangle.classify(19, 10, 10)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test_trian_equal_0_case_1_a(self):
        actual = Triangle.classify(1, 2, 3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_trian_equal_0_case_1_b(self):
        actual = Triangle.classify(2, 3, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_trian_equal_0_case_1_c(self):
        actual = Triangle.classify(3, 2, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_trian_equal_0_case_2(self):
        actual = Triangle.classify(2, 6, 5)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

    def test_trian_gt_3(self):
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    def test_isosceles_1(self):
        actual = Triangle.classify(2, 2, 3)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test_isosceles_2(self):
        actual = Triangle.classify(3, 2, 2)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test_isosceles_3(self):
        actual = Triangle.classify(2, 3, 2)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
        
    def test_isosceles_4(self):
        actual = Triangle.classify(3, 3, 6)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
    def test_invalid_return_1(self):
        actual = Triangle.classify(3, 3, 7)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_invalid_return_2(self):
        actual = Triangle.classify(3, 7, 3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_invalid_return_3(self):
        actual = Triangle.classify(7, 3, 3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_invalid_zero(self):
        actual = Triangle.classify(0, 0, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
    def test_invalid_neg(self):
        actual = Triangle.classify(0, -1, -1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    def test_invalid_neg_1(self):
        actual = Triangle.classify(-1, -1, -1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
    def test_invalid_neg_2(self):
        actual = Triangle.classify(-1, 0, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        
if __name__ == '__main__':
    unittest.main()
