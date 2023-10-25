import unittest
from isTriangle import Triangle 
class TriangleTest(unittest.TestCase):

    def test_triangle_precondition_negative(self):
        actual = Triangle.classify(-1, -1, -1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_triangle_precondition_zero(self):
        actual = Triangle.classify(0, 0, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_invalid_triangle_less_than(self):
        actual = Triangle.classify(1, 2, 4)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_invalid_triangle_equal(self):
        actual = Triangle.classify(1, 2, 3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_scalene_triangle(self):
        actual = Triangle.classify(2, 3, 4)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

    def test_equilateral_triangle(self):
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    def test_isosceles_triangle1(self):
        actual = Triangle.classify(2, 2, 3)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test_isosceles_triangle2(self):
        actual = Triangle.classify(3, 2, 2)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test_isosceles_triangle3(self):
        actual = Triangle.classify(2, 3, 2)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def test_invalid_return1(self):
        actual = Triangle.classify(3, 3, 7)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_invalid_return2(self):
        actual = Triangle.classify(3, 7, 3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def test_invalid_return3(self):
        actual = Triangle.classify(7, 3, 3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()