import function
from unittest import TestCase

class TestCategorizedNumbers(TestCase):
        def test_that_categorized_numbers_function_exist(self):
                function.get_categorized_numbers(10)
                
        def test_that_categorized_numbers_function_evaluate_each_input_and_return_them_as_result(self):
                actual = function.get_categorized_numbers(10, 15, 21, 30, divisor = 5)
                expected = 10, 15, 30
                self.assertEqual(actual, expected)