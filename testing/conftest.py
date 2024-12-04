"""
Pytest conftest file
"""
import os
from pytest import fixture


@fixture
def support_folder_path():
    """
    Path to support test folder
    """
    return os.path.join(os.path.dirname(__file__), 'support')

@fixture
def auth_log_path(support_folder_path):
    """
    Path to log example
    """
    log_path = os.path.join(support_folder_path, 'auth.example.log')
    return log_path
