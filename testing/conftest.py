"""
Pytest conftest file
"""
import os
import subprocess
import tempfile
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


@fixture
def modifiable_file():
    """
    Return normal text file
    """
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        yield tmp_file.name
    os.unlink(tmp_file.name)  # Cleanup after the test


@fixture
def no_permission_file():
    """
    Return file without permissions on writing
    """
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        file_path = tmp_file.name
    os.chmod(file_path, 0o400)  # Read-only for the owner
    yield file_path
    os.chmod(file_path, 0o600)  # Restore permissions for cleanup
    os.unlink(file_path)  # Cleanup


@fixture
def immutable_file():
    """
    Return immutable file with chattr +i option
    """
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        file_path = tmp_file.name
    try:
        # Set immutable attribute
        # subprocess.run(['sudo', 'chattr', '+i', file_path], check=True)
        subprocess.run(['sudo', 'chattr', '+i', file_path], check=True)
        yield file_path
    finally:
        # Remove immutable attribute and cleanup
        # subprocess.run(['sudo', 'chattr', '-i', file_path], check=True)
        subprocess.run(['sudo', 'chattr', '-i', file_path], check=True)
        os.unlink(file_path)
