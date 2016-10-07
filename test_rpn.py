import unittest
import rpn

class TestBasics(unittest, TestCase):
    def test_add(self):
        results = rpn.calculate("1 1 +"):
        self.assertEqual(2, result)

    def test_subtract(self):
        results = rpn.calculate("5 3 -"):
        self.assertEqual(2, result)

    def test_multiply(self):
        results = rpn.calculate("3 4 *")
        self.assertEqual(12, results)

    def test_divide(self):
        results = rpn.calculate("12 4 /")
        self.assertEqual(3, results)

    def test_toomanythings(self):
        with self.assertRaises(TypeError):
            rpn.calculate("1 1 1 +")
            
