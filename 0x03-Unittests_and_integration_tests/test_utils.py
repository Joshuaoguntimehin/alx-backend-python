#!/usr/bin/env python3
"""import statement"""
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
        """Test access_nested_map returns expected result"""
        self.assertEqual(access_nested_map(nested_map, path))

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])


    def test_access_nested_map_key_error(self, nested_map, path, expected_message):
        with self.assertRaise(KeyError, expected_message) as context:
            access_nested_map(nested_map, path)

        # Ensure the exception message matches the expected value
        self.assertEqual(str(context.exception), expected_message)


if __name__ == "__main__":
    unittest.main()
