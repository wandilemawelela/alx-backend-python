#!/usr/bin/env python3
"""
Tests for get_json function
"""

import unittest
from unittest.mock import patch, Mock
from utils import get_json
from parameterized import parameterized


class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        # Create a mock response object with the json method
        # returning the test_payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call get_json and check the returned value
        result = get_json(test_url)
        self.assertEqual(result, test_payload)

        # Ensure the mocked get method was called exactly once with test_url
        mock_get.assert_called_once_with(test_url)


if __name__ == '__main__':
    unittest.main()
