import maxmin
from unittest import TestCase

class Testmaxmin(TestCase):
        
        def test_get_maxmin_function_exists(self):
                maxmin.get_maxmin(2)
                
        def test_that_maxmin_function_returns_result_correctly(self):
                actual = maxmin.get_maxmin(2, 3, 15, 9, 12)
                expected = 12
                self.assertEqual(actual, expected)