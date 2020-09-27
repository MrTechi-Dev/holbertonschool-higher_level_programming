#!/usr/bin/python3
#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    This is the class unittest for the max integer function
    """
    def test_sorted(self):
        sorted_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(sorted_list), 4)

    def test_list_float(self):
        f_l = [1.11, 2.22, 3.33, 4.44]
        self.assertEqual(max_integer(f_l), 4.44)

    def test_num_string(self):
        self.assertEqual(max_integer("1234567890"), "9")

    def test_strng(self):
        self.assertEqual(max_integer("abcdefg"), "g")

    def test_empty_list(self):
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_list(self):
        only_one = [1]
        self.assertEqual(max_integer(only_one), 1)

    def test_max_int(self):
        max_first = [4, 1, 2, 3]
        self.assertEqual(max_integer(max_first), 4)


if __name__ == '__main__':
    unittest.main()