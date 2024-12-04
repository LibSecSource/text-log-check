import os
from pytest import fixture


@fixture
def support_folder_path():
    return os.path.join(os.path.dirname(__file__), 'support')

@fixture
def auth_log_path(support_folder_path):
    log_path = os.path.join(support_folder_path, 'auth.example.log')
    return log_path
