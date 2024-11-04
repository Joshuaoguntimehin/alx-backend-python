#!/usr/bin/env python3
"""Unit tests for access_nested_map"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map
from utils import access_nested_map, get_json


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


class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test that get_json returns the expected result."""
        # Create a mock response object
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        
        # Set the return value of requests.get to our mock response
        mock_get.return_value = mock_response

        # Call the get_json function
        result = get_json(test_url)

        # Assert that the result matches the test payload
        self.assertEqual(result, test_payload)

        # Assert that requests.get was called exactly once with the correct URL
        mock_get.assert_called_once_with(test_url)



class TestMemoize(unittest.TestCase):
    def test_memoize(self):
        """Test that the memoize decorator works correctly."""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # Create an instance of TestClass
        instance = TestClass()

        # Patch a_method
        with patch.object(instance, 'a_method', return_value=42) as mock_method:
            # Call a_property twice
            result1 = instance.a_property()
            result2 = instance.a_property()

            # Assert that the result is correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Assert that a_method is called only once
            mock_method.assert_called_once()



if __name__ == "__main__":
    unittest.main()
