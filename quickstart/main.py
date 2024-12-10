"""
Quickstart examples
"""


def main():
    """
    TextLogCheck simple usage
    :return:
    """
    from text_log_check import exists, tail, clear, is_modifiable  # pylint: disable=import-outside-toplevel

    if exists('/var/log/auth.log'):
        print(tail('var/log/auth.log', 5))
        if is_modifiable('var/log/auth.log'):
            clear('var/log/auth.log')
