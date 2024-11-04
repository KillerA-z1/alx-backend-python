#!/usr/bin/env python3
"""Unit tests for GithubOrgClient"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        expected_result = {"login": org_name}
        mock_get_json.return_value = expected_result

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected_result)
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)

    def test_public_repos_url(self):
        """Test the _public_repos_url property returns the correct URL"""
        mock_payload = {
            "repos_url": "https://api.github.com/orgs/testorg/repos"
        }
        patch_target = 'client.GithubOrgClient.org'
        mock_org_patch = patch(patch_target, new_callable=PropertyMock)
        with mock_org_patch as mock_org:
            mock_org.return_value = mock_payload
            client = GithubOrgClient("testorg")
            self.assertEqual(
                client._public_repos_url,
                mock_payload["repos_url"]
            )


if __name__ == '__main__':
    unittest.main()
