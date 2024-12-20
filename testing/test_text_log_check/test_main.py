"""
Test main
"""
from pytest import raises
from text_log_check import exists, tail, clear, is_modifiable


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
    Test tail
    success: get 2 end lines
    """
    tail_lines = tail(auth_log_path, 2)
    assert [
               'Dec  4 12:28:05 yourhostname systemd[1]: Stopping Session 6 of user user2.',
               'Dec  4 12:28:05 yourhostname systemd[1]: Stopped Session 6 of user user2.',
           ] == tail_lines


def test_get_tail_of_log_file_not_found():
    """
    Test tail
    error: file not found
    """
    with raises(FileNotFoundError):
        tail('/my/log/not/exists/some.log', 2)


def test_get_tail_of_log_file_big_n_lines(auth_log_path):
    """
    Test tail
    success: got full file then n_lines > len file
    """
    # open and read full file
    with open(auth_log_path, 'r', encoding='utf-8') as file:
        all_lines = file.readlines()
        all_lines = [line.strip() for line in all_lines]

    big_tail_size = len(all_lines) + 1
    # use tail function give big tail size
    log_tail = tail(auth_log_path, big_tail_size)
    assert all_lines == log_tail


def test_get_tail_of_log_default_n_lines(auth_log_path):
    """
    Test tail
    success: work without n_log param
    """
    tail(auth_log_path)
    assert True


def test_clear_log(log_to_clear_path):
    """
    Test clear log
    success: empty log
    """
    with open(log_to_clear_path, 'r', encoding='utf-8') as f:
        assert 'Clear me' == f.read()

    clear(log_to_clear_path)

    with open(log_to_clear_path, 'r', encoding='utf-8') as f:
        assert '' == f.read()


def test_is_modifiable(modifiable_file):
    """
    Test is modifiable
    Success: can modify, return True
    """
    assert is_modifiable(modifiable_file)


def test_is_modifiable_not_permissions(no_permission_file):
    """
    Test is_modifiable
    Success: can't modify file without permissions, return False
    """
    assert not is_modifiable(no_permission_file)


def test_is_modifiable_immutable(immutable_file):
    """
    Test is_modifiable
    Success: can't modify file with chattr +i attribute
    """
    print('CHECK')
    assert not is_modifiable(immutable_file)
