#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_at_end(self):
        """Test when the max integer is at the end of the list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_in_middle(self):
        """Test when the max integer is in the middle of the list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_one_element(self):
        """Test when the list has only one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test when the list is empty"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test with negative numbers in the list"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test with both positive and negative numbers"""
        self.assertEqual(max_integer([-1, 2, 3, -4]), 3)

    def test_floats(self):
        """Test with floats in the list"""
        self.assertEqual(max_integer([1.5, 2.8, 3.3, 2.2]), 3.3)

    def test_duplicates(self):
        """Test with duplicates in the list"""
        self.assertEqual(max_integer([1, 2, 2, 4, 4]), 4)

    def test_all_same(self):
        """Test when all elements in the list are the same"""
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_max_at_end(self):
        """Test max value when it's at the end of the list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test max value when it's at the beginning of the list"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test max value when it's in the middle of the list"""
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_one_negative_number(self):
        """Test list with one negative number"""
        self.assertEqual(max_integer([-1]), -1)

    def test_only_negative_numbers(self):
        """Test list with only negative numbers"""
        self.assertEqual(max_integer([-3, -1, -2]), -1)

    def test_one_element(self):
        """Test list with one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test empty list"""
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
