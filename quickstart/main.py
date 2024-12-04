"""
Quickstart examples
"""


def main():
    """
    TextLogCheck simple usage
    :return:
    """
    from text_log_check import exists, get_tail_of_log  # pylint: disable=import-outside-toplevel

    print(exists('/var/log/auth.log'))
    print(get_tail_of_log('var/log/auth.log', 5))
