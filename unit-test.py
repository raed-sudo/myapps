import unittest
import Calculator

class TestCalc(unittest.TestCase):
    def test_add(self):
        result = Calculator.add(10,5)
        self.assertEqual(result,15)
