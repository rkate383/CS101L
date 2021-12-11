import unittest
import Grades
import math

class Grade_Test(unittest.TestCase):
    def test_total_returns_total_of_list(self):
        result = Grades.total([1,10,22])
        self.assertEqual(result, 33, 'The total function should return 33')

    def test_total_returns_0(self):
        result = Grades.total([])
        self.assertEqual(result, 0, 'The total function should return 0')

    def test_average_one(self):
        result = Grades.average([2,5,9])
        self.assertAlmostEqual(result, 5.33333, 5)

    def test_average_two(self):
        result = Grades.average([2,15,22,9])
        self.assertAlmostEqual(result,12.0000,4)

    def test_average_return_nan(self):
        result = Grades.average([])
        self.assertIs(result, math.nan)

    def test_median_return_odd(self):
        result = Grades.median([2,5,1])
        self.assertEqual(result, 2)

    def test_median_return_even(self):
        result = Grades.median([5,2,1,3])
        self.assertEqual(result, 2.5)

    def test_median_empty(self):
        with self.assertRaises(ValueError):
            result = Grades.median([])
        
unittest.main()
