#!/usr/bin/python3
"""This is the rectangle.py unittest module."""
import unittest
import pep8
import inspect
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestCodingStandards(unittest.TestCase):
    """Tests to check the documentation and style of Base class"""
    @classmethod
    def setUp(cls):
        """Set up for the doc tests"""
        cls.base_funcs = inspect.getmembers(Square, inspect.isfunction)

    def test_pep8_rectangle(self):
        """Test that models/base.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_test_rectangle(self):
        """Test that tests/test_models/test_rectangle.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestSquare(unittest.TestCase):
    """Test cases for Rectangle initialization."""
    def setUp(self):
        """Test setup"""
        Base._Base__nb_objects = 0
        self.s1 = Square(2)
        self.s2 = Square(2, 10)
        self.s3 = Square(8, 4, 6)
        self.s4 = Square(2, 15, 6, 8)
        self.tests = [self.s1, self.s2, self.s3, self.s4]

    def test_id(self):
        """Test for id"""
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)
        self.assertEqual(self.s3.id, 3)
        self.assertEqual(self.s4.id, 8)

    def test_size(self):
        """Test for size"""
        self.assertEqual(self.s1.size, 2)
        self.assertEqual(self.s2.size, 2)
        self.assertEqual(self.s3.size, 8)
        self.assertEqual(self.s4.size, 2)

    def test_x(self):
        """Test for x"""
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s2.x, 10)
        self.assertEqual(self.s3.x, 4)
        self.assertEqual(self.s4.x, 15)

    def test_y(self):
        """Test for y"""
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.y, 0)
        self.assertEqual(self.s3.y, 6)
        self.assertEqual(self.s4.y, 6)

    def test_input_errors(self):
        """Input errors"""
        with self.assertRaises(TypeError):
            Square()
        with self.assertRaises(Exception):
            Square(1, 2, 3, 4, 5, 6)

    def test_size_TypeError(self):
        """Size TypeError"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("Hello world!")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1])

    def test_x_TypeError(self):
        """x TypeError"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "Hello world!")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, True)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [3])

    def test_y_TypeError(self):
        """y TypeError"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "Hello world!")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, True)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, [4])

    def test_width_ValueError(self):
        """Size ValueError"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_x_ValueError(self):
        """x ValeuError"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -1)

    def test_y_ValueError(self):
        """y ValueError"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -1)

    def test_area_method(self):
        """Test area method"""
        for rct in self.tests:
            self.assertEqual(rct.area(), rct.size * rct.size)

    def test_area_with_args(self):
        """Test area method errors"""
        with self.assertRaises(Exception):
            self.s1.area(1)

    def test_display_with_args(self):
        """Test display method errors"""
        with self.assertRaises(Exception):
            self.s1.display(1)

    def test__str__(self):
        """Test for __str__ method"""
        for rct in self.tests:
            expected = "[Square] ({}) {}/{} \
- {}\n".format(rct.id, rct.x, rct.y, rct.size, rct)
            with patch('sys.stdout', new=StringIO()) as fake_out:
                print(rct)
                self.assertEqual(fake_out.getvalue(), expected)

    def test_display_with_xy(self):
        """Test for display method v2"""
        for rct in self.tests:
            e = '\n' * rct.y
            e += ((' ' * rct.x) + ('#' * rct.size + '\n')) * rct.size
            with patch('sys.stdout', new=StringIO()) as fake_out:
                rct.display()
                self.assertEqual(fake_out.getvalue(), e)

    def test_update_args(self):
        """Test for update method with args"""
        s1 = Square(10, 10, 10, 1)
        e = "[Square] (1) 10/10 - 10\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), e)
        s1.update(89)
        e = "[Square] (89) 10/10 - 10\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), e)
        s1.update(89, 2)
        e = "[Square] (89) 10/10 - 2\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), e)
        s1.update(89, 2, 3)
        e = "[Square] (89) 3/10 - 2\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), e)
        s1.update(89, 2, 3, 4)
        e = "[Square] (89) 3/4 - 2\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), e)
        s1.update(89, 2, 3, 4, 5)
        e = "[Square] (89) 3/4 - 2\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), e)
        s1.update(6, 5, 4, 3, 2, 1, 0)
        e = "[Square] (6) 4/3 - 5\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), e)
        s1.update()
        e = "[Square] (6) 4/3 - 5\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), e)

    def test_update_method_kwargs(self):
        r1 = Square(10, 10, 10, 1)
        e = "[Square] (1) 10/10 - 10\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), e)
        r1.update(size=1)
        e = "[Square] (1) 10/10 - 1\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), e)
        r1.update(size=1, x=2)
        e = "[Square] (1) 2/10 - 1\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), e)
        r1.update(y=1, size=2, x=3, id=89)
        e = "[Square] (89) 3/1 - 2\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), e)
        r1.update(x=1, size=2, y=3)
        e = "[Square] (89) 1/3 - 2\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), e)

    def test_update_module_args_kwargs(self):
        r1 = Square(10, 10, 10, 1)
        e = "[Square] (1) 10/10 - 10\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), e)
        r1.update(89, 1, 2, 3, size=4, x=1)
        e = "[Square] (89) 2/3 - 1\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), e)

    def test_update_errors(self):
        r1 = Square(10, 10, 10, 1)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r1.update(10, "2")
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r1.update(10, True)
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            r1.update(10, 2, -4)
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            r1.update(10, 3, 4, False)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r1.update(size=0)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r1.update(size=-4)
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            r1.update(x=True)
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            r1.update(y=-10)
