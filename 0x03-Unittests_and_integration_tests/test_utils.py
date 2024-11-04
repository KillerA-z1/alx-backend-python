#!/usr/bin/env python3
"""This code defines unit tests function ,verifying its correct behavior
and exception handling using the unittest framework and parameterized
test cases."""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map
from utils import get_json


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
        ({"a": 1}, ("a", "b"), 'b'),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_key):
        """Test that KeyError is raised for invalid paths"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(context.exception.args[0], expected_key)


class TestGetJson(unittest.TestCase):
    """Test case for utils.get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test that get_json returns the expected result"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
