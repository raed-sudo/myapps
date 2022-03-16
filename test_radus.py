from calendar import c
import unittest
from math import pi
from radus import circle_area, circle_perimetre

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # Test Area when radius >= 0
        self.assertEqual(circle_area(1),pi)
        self.assertRaises(ValueError,circle_area, -2)
    
    def test_CirclePerimetre(self):
        # Test Perimetre when radius >= 0
        self.assertEqual(circle_perimetre(1),pi*2)
        self.assertRaises(ValueError,circle_perimetre, -22)