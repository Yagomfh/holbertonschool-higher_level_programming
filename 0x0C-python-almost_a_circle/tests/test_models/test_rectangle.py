#!/usr/bin/python3
"""This is the rectangle.py unittest module."""
import unittest
import pep8
import inspect
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestCodingStandards(unittest.TestCase):
    """Tests to check the documentation and style of Base class"""
    @classmethod
    def setUp(cls):
        """Set up for the doc tests"""
        cls.base_funcs = inspect.getmembers(Rectangle, inspect.isfunction)

    def test_pep8_rectangle(self):
        """Test that models/base.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_test_rectangle(self):
        """Test that tests/test_models/test_rectangle.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle initialization."""
    def setUp(self):
        """Test setup"""
        Base._Base__nb_objects = 0
        self.r1 = Rectangle(2, 4)
        self.r2 = Rectangle(2, 10, 6)
        self.r3 = Rectangle(8, 4, 6, 8)
        self.r4 = Rectangle(2, 15, 6, 8, 10)
        self.tests = [self.r1, self.r2, self.r3, self.r4]

    def test_id(self):
        """Test for id"""
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 3)
        self.assertEqual(self.r4.id, 10)

    def test_width(self):
        """Test for width"""
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r3.width, 8)
        self.assertEqual(self.r4.width, 2)

    def test_height(self):
        """Test for height"""
        self.assertEqual(self.r1.height, 4)
        self.assertEqual(self.r2.height, 10)
        self.assertEqual(self.r3.height, 4)
        self.assertEqual(self.r4.height, 15)

    def test_x(self):
        """Test for x"""
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 6)
        self.assertEqual(self.r3.x, 6)
        self.assertEqual(self.r4.x, 6)

    def test_y(self):
        """Test for y"""
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r3.y, 8)
        self.assertEqual(self.r4.y, 8)

    def test_input_errors(self):
        """Input errors"""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)
        with self.assertRaises(Exception):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_TypeError(self):
        """Width TypeError"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("Hello world!", 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1], 1)

    def test_height_TypeError(self):
        """Height TypeError"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "Hello world!")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, True)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [2])

    def test_x_TypeError(self):
        """x TypeError"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "Hello world!")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, True)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [3])

    def test_y_TypeError(self):
        """y TypeError"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "Hello world!")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, True)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, [4])

    def test_width_ValueError(self):
        """Width ValueError"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 1)

    def test_height_ValueError(self):
        """Height ValueError"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)

    def test_x_ValueError(self):
        """x ValeuError"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -1)

    def test_y_ValueError(self):
        """y ValueError"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -1)

    def test_area_method(self):
        """Test area method"""
        for rct in self.tests:
            self.assertEqual(rct.area(), rct.width * rct.height)

    def test_area_with_args(self):
        """Test area method errors"""
        with self.assertRaises(Exception):
            self.r1.area(1)

    def test_display_with_args(self):
        """Test display method errors"""
        with self.assertRaises(Exception):
            self.r1.display(1)

    def test__str__(self):
        """Test for __str__ method"""
        for rct in self.tests:
            expected = "[Rectangle] ({}) {}/{} \
- {}/{}\n".format(rct.id, rct.x, rct.y, rct.width, rct.height)
            with patch('sys.stdout', new=StringIO()) as fake_out:
                print(rct)
                self.assertEqual(fake_out.getvalue(), expected)

    def test_display_with_xy(self):
        """Test for display method v2"""
        for rct in self.tests:
            e = '\n' * rct.y
            e += ((' ' * rct.x) + ('#' * rct.width + '\n')) * rct.height
            with patch('sys.stdout', new=StringIO()) as fake_out:
                rct.display()
                self.assertEqual(fake_out.getvalue(), e)
