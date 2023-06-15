"""
File: searchengine.py
---------------------
You fill in this comment
"""


import os
import sys
import string
from common_elements import common
# FILENAMES = ['test1.txt', 'test2.txt']

PATTERN = str.maketrans('', '', string.punctuation)

def create_index(filenames, index, file_titles):
    """
    This function is passed:
        filenames:      a list of file names (strings)

        index:          a dictionary mapping from terms to file names (i.e., inverted index)
                        (term -> list of file names that contain that term)

        file_titles:    a dictionary mapping from a file names to the title of the article
                        in a given file
                        (file name -> title of article in that file)

    The function will update the index passed in to include the terms in the files
    in the list filenames.  Also, the file_titles dictionary will be updated to
    include files in the list of filenames.
    """
    # filenames = FILENAMES
    for filename in filenames:
        with open(filename, 'r', encoding='UTF-8') as f:
            first_line = f.readline().rstrip()      # .translate(pattern)
            file_titles[filename] = [first_line]
            f.seek(0)
            for line in iter(f.readline, ''):
                # removes (\n) from the start and end of the line
                words = [word for word in line.lower().translate(PATTERN).split()]
                if words:
                    for elem in words:
                        # if elem == 'nice':
                        if elem not in index:
                            index[elem] = [filename]           # [os.path.basename(filename)]
                        else:
                            if filename not in index[elem]:
                                index[elem].append(filename)        # (os.path.basename(filename))


def search(index, query):
    """
    This function is passed:
        index:      a dictionary mapping from terms to file names (inverted index)
                    (term -> list of file names that contain that term)

        query  :    a query (string), where any letters will be lowercase

    The function returns a list of the names of all the files that contain *all* of the
    terms in the query (using the index passed in).
    """
    index_list = {}
    common_list = []
    query_list = query.lower().translate(PATTERN).split()

    for elem in query_list:
        if elem not in index:
            break
        index_list[elem] = index[elem]
        if len(common_list) == 0:
            common_list = index_list[elem]
        else:
            common_list = common(common_list, index_list[elem])
            if len(common_list) == 0:
                break
    return common_list





##### YOU SHOULD NOT NEED TO MODIFY ANY CODE BELOW THIS LINE (UNLESS YOU'RE ADDING EXTENSIONS) #####


def do_searches(index, file_titles):
    """
    This function is given an inverted index and a dictionary mapping from
    file names to the titles of articles in those files.  It allows the user
    to run searches against the data in that index.
    """
    while True:
        query = input("Query (empty query to stop): ")
        query = query.lower()                   # convert query to lowercase
        if query == '':
            break
        results = search(index, query)

        # display query results
        print("Results for query '" + query + "':")
        if results:                             # check for non-empty results list
            for i in range(len(results)):
                title = file_titles[results[i]]
                print(str(i + 1) + ".  Title: ", title, ",  File: ", results[i])
        else:
            print("No results match that query.")


def textfiles_in_dir(directory):
    """
    DO NOT MODIFY
    Given the name of a valid directory, returns a list of the .txt
    file names within it.

    Input:
        directory (string): name of directory
    Returns:
        list of (string) names of .txt files in directory
    """
    filenames = []

    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filenames.append(os.path.join(directory, filename))

    return filenames


def main():
    """
    Usage: searchengine.py <file directory> -s
    The first argument specified should be the directory of text files that
    will be indexed/searched.  If the parameter -s is provided, then the
    user can interactively search (using the index).  Otherwise (if -s is
    not included), the index and the dictionary mapping file names to article
    titles are just printed on the console.
    """
    # Get command line arguments
    args = sys.argv[1:]

    num_args = len(args)


    if num_args < 1 or num_args > 2:
        print('Please specify directory of files to index as first argument.')
        print('Add -s to also search (otherwise, index and file titles will just be printed).')
    else:
        # args[0] should be the folder containing all the files to index/search.
        directory = args[0]
        if os.path.exists(directory):
            # Build index from files in the given directory
            files = textfiles_in_dir(directory)
            index = {}          # index is empty to start
            file_titles = {}    # mapping of file names to article titles is empty to start
            create_index(files, index, file_titles)

            # Either allow the user to search using the index, or just print the index
            if num_args == 2 and args[1] == '-s':
                do_searches(index, file_titles)
            else:
                print('')
                # print(index)
                # print('File names -> document titles:')
                # print(file_titles)
        else:
            print('Directory "' + directory + '" does not exist.')


if __name__ == '__main__':
    main()
