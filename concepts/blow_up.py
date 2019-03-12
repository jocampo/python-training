"""A module for demonstrating exceptions"""


import sys


def convert(s):
    """Convert to an integer."""
    x = -1
    try:
        x = int(s)
    except (ValueError, TypeError) as e:  # tuples
        print("Yikes: {}".format(str(e)), file=sys.stderr)
        # pass = no op
        # raise = throw :)
        # raise ValueError()  # throw a new ValueError
    finally:
        print("Finished!")
    return x


if __name__ == "__main__":
    print(convert('9a'))
