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


@fixture
def log_to_clear_path(support_folder_path):
    """
    Return path to log to lear. Delete file after tests
    """
    file_path = os.path.join(support_folder_path, 'to_clear.example.log')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('Clear me')

    yield file_path

    # Cleanup after the test
    if os.path.exists(file_path):
        os.remove(file_path)
