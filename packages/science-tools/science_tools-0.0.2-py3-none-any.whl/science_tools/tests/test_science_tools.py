"""
Unit and regression test for the science_tools package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import science_tools


def test_science_tools_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "science_tools" in sys.modules
