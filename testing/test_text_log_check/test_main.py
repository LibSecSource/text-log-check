"""
Test main
"""
from pytest import raises
from text_log_check import exists, get_tail_of_log


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


def test_get_tail_of_log(auth_log_path):
    """
    Test get_tail_of_log
    success: get 2 end lines
    """
    tail_lines = get_tail_of_log(auth_log_path, 2)
    assert [
               'Dec  4 12:28:05 yourhostname systemd[1]: Stopping Session 6 of user user2.',
               'Dec  4 12:28:05 yourhostname systemd[1]: Stopped Session 6 of user user2.',
           ] == tail_lines


def test_get_tail_of_log_file_not_found():
    """
    Test get_tail_of_log
    error: file not found
    """
    with raises(FileNotFoundError):
        get_tail_of_log('/my/log/not/exists/some.log', 2)


def test_get_tail_of_log_file_big_n_lines(auth_log_path):
    """
    Test get_tail_of_log
    success: got full file then n_lines > len file
    """
    # open and read full file
    with open(auth_log_path, 'r', encoding='utf-8') as file:
        all_lines = file.readlines()
        all_lines = [line.strip() for line in all_lines]

    big_tail_size = len(all_lines) + 1
    # use tail function give big tail size
    log_tail = get_tail_of_log(auth_log_path, big_tail_size)
    assert all_lines == log_tail
