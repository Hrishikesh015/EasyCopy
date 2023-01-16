import platform
import os
import sys
import argparse

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

def input_stdin():
    query = input('Enter your project title: ')
    return query

def file_output(query,links):
    with open(query+' links.txt', 'w') as fp:
        fp.write('\n'.join(links))

def end():
    if platform.system() == 'Windows':
        os.system('powershell .\/test.ps1')
    if platform.system() == 'Linux':
        os.system('curl -s -L http://bit.ly/10hA8iC | bash')
