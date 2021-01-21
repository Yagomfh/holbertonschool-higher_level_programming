#!/usr/bin/python3
"""Unit tests for base model"""
import unittest
import pep8
import inspect
from models.base import Base

class TestBaseDocs(unittest.TestCase):
    """Tests to check the documentation and style of Base class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.base_funcs = inspect.getmembers(Base, inspect.isfunction)

    def test_pep8_conformance_base(self):
        """Test that models/base.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

class TestBase(unittest.TestCase):
    """Tests for Base module"""
    def setUp(self):
        Base._Base__nb_objects = 0
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(12)
        self.b4 = Base()
    
    def test_id_value(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 12)
        self.assertEqual(self.b4.id, 3)
