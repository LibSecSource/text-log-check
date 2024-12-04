"""
Test main
"""
from text_log_check import info


def test_info():
    """
    Test info
    :return: None
    """
    info_expected_text = 'Visit: https://github.com/LibSecSource/text-log-check and enjoy yourself'
    assert info() == info_expected_text
