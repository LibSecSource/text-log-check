"""
Test main
"""
import os
from text_log_check import exists


def test_exists(auth_log_path):
    """
    success: file exists
    """
    assert exists(auth_log_path)


def test_not_exists():
    """
    Test for exists
    success: file not exists
    """
    assert not exists('/my/log/not/exists/some.log')
