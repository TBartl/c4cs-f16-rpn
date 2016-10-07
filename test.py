import unittest
import rpn

class TestBasics(unittest, TestCase):
    def test_add(self):
        results = rpn.calculate("1 1 +"):
        self.assertEqual(2, result)

    def test_subtract(self):
        results = rpn.calculate("5 3 -"):
        self.assertEqual(2, result)
