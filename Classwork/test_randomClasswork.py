from randomClasswork import *
import unittest


class MyTestCase(unittest.TestCase):
    def test_for_the_length_of_list(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(get_length_of_list(list1), 10)

    def test_for_even_length_of_list(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(sum_of_elements_in_even_position(list1), 25)

    def test_for_odd_length_of_list(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(sum_of_elements_in_odd_position(list1), 30)

    def test_for_multiples_of_list_wrong(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertNotEqual(multiply_all_elements_in_third_positions(list1), 22)

    def test_for_multiples_of_list_is_correct(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(multiply_all_elements_in_third_positions(list1), 162)

    def test_for_multiples_index_at_index_nine_contain_zero_element(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 0, 10]
        self.assertEqual(multiply_all_elements_in_third_positions(list1), 0)

    def test_for_multiples_index_nine_does_not_contain_zero_element(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertNotEqual(multiply_all_elements_in_third_positions(list1), 1)



if __name__ == '__main__':
    unittest.main()
