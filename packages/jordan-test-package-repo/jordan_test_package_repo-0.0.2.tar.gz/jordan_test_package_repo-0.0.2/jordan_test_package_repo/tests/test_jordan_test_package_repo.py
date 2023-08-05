"""
Unit and regression test for the jordan_test_package_repo package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import jordan_test_package_repo


def test_jordan_test_package_repo_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "jordan_test_package_repo" in sys.modules
