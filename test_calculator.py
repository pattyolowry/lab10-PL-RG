# https://github.com/pattyolowry/lab10-PL-RG
# Partner 1: Patrick Lowry
# Partner 2: Ria Gupta
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1,2), 3)
        self.assertEqual(add(2, -2), 0)
        self.assertEqual(add(-1.3, -2.5), -3.8)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(23,6), 17)
        self.assertEqual(subtract(9, 9), 0)
        self.assertEqual(subtract(8.4, 9.9), -1.5)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(4, 0), 0)
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-3, 6), -18)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(5, 100), 20)
        self.assertEqual(div(3, 0), 0)
        self.assertEqual(div(2, -5), -2.5)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2,2), 1)
        self.assertEqual(logarithm(100, 10), 0.5)
        self.assertEqual(logarithm(10, 100), 2)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(10, 1)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(0, 6), 6)
        self.assertEqual(hypotenuse(-6, 8), 10)

    def test_sqrt(self): # 3 assertions
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(0), 0)
        with self.assertRaises(ValueError):
            square_root(-1)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()