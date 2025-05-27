import todolistmanager
from unittest import TestCase

class TestTodolistmanager (TestCase): 
        def test_that_get_menu_function_exist(self)
                todolistmanager.get_menu()
                
        def test_that_get_menu_function_return_properly(self):
                actual = todolistmanager.get_menu("go to work")
                expected = " "
                self.assertEqual(actual, expected)

        def test_that