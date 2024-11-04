#!/usr/bin/env python3
"""Test case for access_nested_map function"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap is a test case class for access_nested_map function.

    Methods:
        test_access_nested_map(nested_map, path, expected):
            Tests the access_nested_map function with various inputs using
            parameterized test cases.
        Args:
            nested_map (dict): The nested dictionary to access.
            path (tuple): The sequence of keys to access the nested value.
            expected: The expected value to be returned by access_nested_map.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map with various inputs"""
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    unittest.main()
