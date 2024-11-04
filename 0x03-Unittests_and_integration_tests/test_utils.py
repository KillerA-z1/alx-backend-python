#!/usr/bin/env python3
"""This code defines unit tests function ,verifying its correct behavior
and exception handling using the unittest framework and parameterized
test cases."""
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

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_key):
        """Test that KeyError is raised for invalid paths"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_key)


if __name__ == "__main__":
    unittest.main()
