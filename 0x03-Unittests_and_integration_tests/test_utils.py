#!/usr/bin/env python3
"""Unit tests for access_nested_map"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that access_nested_map returns the expected result."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'")
    ])
    def test_access_nested_map_key_error(self, nested_map, path, expected_message):
        """Test that access_nested_map raises KeyError with the correct message."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        # Ensure the exception message matches the expected value
        self.assertEqual(str(context.exception), expected_message)


if __name__ == "__main__":
    unittest.main()
