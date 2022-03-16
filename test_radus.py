import unittest
from math import pi
from radus import circle_area

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # Test Area when radius >= 0
        self.assertEqual(circle_area(1),pi)
        self.assertRaises(ValueError,circle_area, -2)
    

unittest.main()