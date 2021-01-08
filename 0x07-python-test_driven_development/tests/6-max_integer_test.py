#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
import sys
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_normal_list_0(self):
        """Test number 0"""
        a = max_integer([1, 2, 3, 4])
        e = 4
        self.assertEqual(a, e)

    def test_normal_list(self):
        """Test number 0"""
        a = max_integer([4, 1, 2, 3])
        e = 4
        self.assertEqual(a, e)

    def test_normal_list(self):
        """Test number 0"""
        a = max_integer([1, 2, 4, 3])
        e = 4
        self.assertEqual(a, e)

    def test_empty_list_0(self):
        """Test number 0"""
        actual = max_integer([])
        expected = None
        self.assertEqual(actual, expected)

    def test_empty_list_1(self):
        """Test number 0"""
        actual = max_integer()
        expected = None
        self.assertEqual(actual, expected)

    def test_same_nb_0(self):
        """Test number 0"""
        a = max_integer([0, 0, 0, 0])
        e = 0
        self.assertEqual(a, e)

    def test_same_nb_1(self):
        """Test number 0"""
        a = max_integer([-10, -10, -10])
        e = -10
        self.assertEqual(a, e)

    def test_hedge_case_0(self):
        """Test number 0"""
        a = max_integer([sys.maxsize, 1, 2])
        e = sys.maxsize
        self.assertEqual(a, e)

    def test_errors_0(self):
        """Test number 0"""
        with self.assertRaises(Exception):
            max_integer(None)

    def test_error_1(self):
        """Test number 0"""
        thisdict = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964
        }
        with self.assertRaises(Exception):
            max_integer(thisdict)

    def test_error_2(self):
        """Test number 0"""
        with self.assertRaises(Exception):
            max_integer([1, 2, 3, 4, 5], [6, 7, 8, 9])

    def test_error_3(self):
        """Test number 0"""
        tuple4 = ("abc", 34, True, 40, "male")
        with self.assertRaises(Exception):
            max_integer(tuple4)

    def test_matrix_0(self):
        """Test number 0"""
        a = max_integer([[1], [2]])
        e = [2]
        self.assertEqual(a, e)

    def test_strings_0(self):
        """Test number 0"""
        a = max_integer("Hello world!")
        e = 'w'
        self.assertEqual(a, e)

    def test_strings_1(self):
        """Test number 0"""
        a = max_integer("123456789")
        e = '9'
        self.assertEqual(a, e)

    def test_chars_0(self):
        """Test number 0"""
        a = max_integer(['a', 'x', 'z'])
        e = 'z'
        self.assertEqual(a, e)

    def test_tuple_0(self):
        """Test number 0"""
        tuple1 = ("apple", "banana", "cherry")
        a = max_integer(tuple1)
        e = 'cherry'
        self.assertEqual(a, e)

    def test_tuple_1(self):
        """Test number 0"""
        tuple2 = (1, 5, 7, 9, 3)
        a = max_integer(tuple2)
        e = 9
        self.assertEqual(a, e)

    def test_tuple_2(self):
        """Test number 0"""
        tuple3 = (True, False, False)
        a = max_integer(tuple3)
        e = True
        self.assertEqual(a, e)
