import unittest
from sesiunea8.app.func import is_div_3_5, only_ints, NotIntigerNumberException
from parameterized import parameterized


class TestFnc(unittest.TestCase):
    def test_is_div_3_5_35(self):
        self.assertEqual(is_div_3_5(45), 35)

    def test_is_div_3_5_3(self):
        self.assertEqual(is_div_3_5(9), 3)

    def test_is_div_3_5_5(self):
        self.assertEqual(is_div_3_5(10), 5)

    def test_is_div_3_5_not_div(self):
        self.assertEqual(is_div_3_5(19), None)

    @parameterized.expand([
        (45, 35),
        (9, 3),
        (10, 5),
        (19, None)
    ])

    def test_is_div_3_5(self, n, expected):
        self.assertEqual(is_div_3_5(n), expected)

    @parameterized.expand([
        [[1, 3, 8, 1.54, 9, 13]],
        [['545456454']],
        [[1 + 2j, 7]]
    ])
    def test_only_ints(self, numbers):
        self.assertRaises(NotIntigerNumberException, only_ints, numbers)
