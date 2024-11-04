#!/usr/bin/env python3
"""
Tests for GithubOrgClient class
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([
        ("google", {"login": "google", "id": 1, "url": "https://api.github.com/orgs/google"}),
        ("abc", {"login": "abc", "id": 2, "url": "https://api.github.com/orgs/abc"}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected_response, mock_get_json):
        # Configure the mock to return a specific response
        mock_get_json.return_value = expected_response

        # Create an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Call the org method and check the result
        result = client.org
        self.assertEqual(result, expected_response)

        # Ensure get_json was called once with the correct URL
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")


if __name__ == '__main__':
    unittest.main()
