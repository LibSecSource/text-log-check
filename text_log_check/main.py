"""
Main module
"""
import os


def exists(path):
    """
    Log file exists
    param: path - filepath
    return: bool
    """
    print('EX', path)
    return os.path.exists(path)