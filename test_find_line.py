import unittest
from fractions import Fraction
from find_line import try_get_slope


class Test_Find_Line(unittest.TestCase):
    def test_try_find_slope(self):
        self.assertEqual(1, try_get_slope(0, -1, 1, 0))

unittest.main()
