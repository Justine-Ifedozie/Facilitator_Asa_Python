import arithmetic
from unittest import TestCase

class TestArithmeticFunction(TestCase):

        def test_that_arithmetic_function_exist(self): 
                arithmetic.get_arithmetic(2, 3, 4)

        def test_that_arithmetic_function_returns_addition_correctly(self):
                actual = arithmetic.get_arithmetic(2, 3, 4)
                expected = 9
                self.assertEqual(actual, expected)
                
def test_that_arithmetic_function_returns_subtraction_correctly(self):
                actual = subtraction