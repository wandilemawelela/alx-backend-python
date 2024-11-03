#!/usr/bin/env python3
"""
Tests for access_nested_map function
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import get_json


class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        # Create a mock response object with a json method
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the function with the test URL
        result = get_json(test_url)

        # Check that the mock get method was called once with the test URL
        mock_get.assert_called_once_with(test_url)

        # Check that the result is equal to the test payload
        self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()
