"""
File: common_elements.py
------------------------
File to implement a function that is passed two lists and returns a new list
containing those elements that appear in both of the lists passed in.
"""


def common(list1, list2):
    result_list = []
    for elem in list2:
        if elem not in result_list and elem in list1:
            result_list.append(elem)

    """
    This function is passed two lists and returns a new list containing
    those elements that appear in both of the lists passed in.
    >>> common(['a'], ['a'])
    ['a']
    >>> common(['a', 'b', 'c'], ['x', 'a', 'z', 'c'])
    ['a', 'c']
    >>> common(['a', 'b', 'c'], ['x', 'y', 'z'])
    []
    >>> common(['a', 'a', 'b'], ['a', 'a', 'x'])
    ['a']
    """
    return result_list


def main():
    # Same tests as the doctests above, but can be run from the terminal:
    # python3 common_elements.py
    print(common(['a'], ['a']))  # should print ['a']
    print(common(['a', 'b', 'c'], ['x', 'a', 'z', 'c']))  # should print ['a', 'c']
    print(common(['a', 'b', 'c'], ['x', 'y', 'z']))  # should print []
    print(common(['a', 'a', 'b'], ['a', 'a', 'x']))  # should print ['a']


if __name__ == '__main__':
    main()
