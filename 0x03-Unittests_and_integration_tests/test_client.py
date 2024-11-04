#!/usr/bin/env python3
"""
Tests for GithubOrgClient class
"""

import unittest
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock) as mock_org:
            # Set the return value of the mocked org property
            mock_org.return_value = {"repos_url": "https://api.github.com/orgs/google/repos"}

            # Create an instance of GithubOrgClient
            client = GithubOrgClient("google")

            # Call the _public_repos_url method and check the result
            result = client._public_repos_url
            self.assertEqual(result, "https://api.github.com/orgs/google/repos")


if __name__ == '__main__':
    unittest.main()
