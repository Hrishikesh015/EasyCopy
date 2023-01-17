import platform
import os
import sys

def file_input():
    queries = []
    # TODO add arparse instead of argv
    with open(sys.argv[1], 'r') as fp:
        for line in fp:
            x = line[:-1]
            queries.append(x)
    return queries

def exit_gracefully():
    print('\nExiting...')
    exit(0)

def file_output(query,links):
    with open(query+' links.txt', 'w') as fp:
        fp.write('\n'.join(links))
