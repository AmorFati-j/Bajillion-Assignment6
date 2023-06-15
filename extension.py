"""
File: extension.py
------------------
This is a file for creating an optional extension program, if
you'd like to do so. For the server extension, write your code in
extension_server.py
"""


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    pass


def custom_sort_key(string):
    lower_string = str.lower(string)

    if lower_string.startswith("'"):
        return ord(lower_string[1]), lower_string[1:]
    else:
        return ord(lower_string[0]), lower_string

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
