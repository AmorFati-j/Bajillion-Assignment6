"""
File: extension_server.py
---------------------
This starts a server! Go to http://localhost:8000 to enjoy it. Currently
the server only serves up the HTML. It does not search. Implement code in
the "TODO" parts of this file to make it work.
"""

# This imports the SimpleServer library
import SimpleServer

# This imports the functions you defined in searchengine.py
from searchengine import create_index, search, textfiles_in_dir
from extension import custom_sort_key
# To get the json.dumps function.
import json
from operator import itemgetter

# the directory of files to search over
DIRECTORY = 'bbcnews'
# perhaps you want to limit to only 10 responses per search.
MAX_RESPONSES_PER_REQUEST = 10


class SearchServer:
    index = {}  # index is empty to start
    file_titles = {}  # mapping of file names to article titles is empty to start

    def __init__(self):
        """
        load the data that we need to run the search engine. This happens
        once when the server is first created.
        """
        self.html = open('extension_client.html').read()

        # TODO: Your code here. Change this code to load any data you want to use!
        files = textfiles_in_dir(DIRECTORY)

        create_index(files, self.index, self.file_titles)

    # this is the server request callback function. You can't change its name or params!!!
    def handle_request(self, request):
        """
        This function gets called every time someone makes a request to our
        server. To handle a search, look for the query parameter with key "query"
        """
        # it is helpful to print out each request you receive!
        print(request)
        # if the command is empty, return the html for the search page
        if request.command == '':
            return self.html

        # if the command is search, the client wants you to perform a search!
        if request.command == 'search':
            # right now we respond to a search request with an empty string.
            # TODO: Your code here. change this code to return the string version 
            # of a list of dicts. Use json.dumps(collection) to turn a list into a string
            collection = []
            common_list = []
            query_words = request.get_params()['query']
            if query_words != '':
                common_list = search(self.index, query_words)

                if common_list:  # check for non-empty results list
                    for i in range(len(common_list)):
                        title = {'title': self.file_titles[common_list[i]]}
                        collection.append(title)

            collection.sort(key=lambda x: custom_sort_key(x['title'][0]))

            return json.dumps(collection, indent=2)


def main():
    # Make an instance of your Server
    handler = SearchServer()

    # Start the server to handle internet requests at http://localhost:8000
    SimpleServer.run_server(handler, 8000)


if __name__ == '__main__':
    main()
