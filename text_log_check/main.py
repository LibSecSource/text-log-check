"""
Main module
"""
import os
from collections import deque


def exists(path):
    """
    Log file exists
    param: path - filepath
    return: bool
    """
    return os.path.exists(path)


def tail(file_path, n_lines=10):
    """Return the last `n_lines` of a log file as a list of lines."""

    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in deque(file, maxlen=n_lines)]


def clear(file_path):
    """
    Clear log file
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('')


def is_modifiable(file_path):
    """
    Is modifiable file
    """
    # Check if the current user has write access to the file
    result = os.access(file_path, os.W_OK)
    return result
