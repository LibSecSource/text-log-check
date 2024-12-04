"""
Quickstart examples
"""


def main():
    """
    TextLogCheck simple usage
    :return:
    """
    from text_log_check import exists  # pylint: disable=import-outside-toplevel

    print(exists('/var/log/auth.log'))
