from actions import *
import os
import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format
import keyboard

def help():
    print('Usage: python script.py -f [filename]\nGive filename if you want to load your titles from a file\nOr you can use cli to give your titles\nPlease exit the program to give filename\nPress Ctrl+c to exit')
    print("Specify language using -l\nUsage: python script.py -l [language]\nOr python script.py -f [filename] -l [language]")

def banner():
    cprint(figlet_format('Easy Copy', font='sblood'),
       'red',  attrs=['bold'])

def init():
    os.system('cls')
    banner()
    help()
    # TODO argparser instead of sys.argv
    try:
        if len(sys.argv) > 1:
            if sys.argv[1] == '-f':
                file_input()
                queries = file_input()
                for query in queries:
                    links = scrape_google(query)
                    file_output(query,links) # comment this if you need only browser output
                    browser_output(links) # comment this if u need only file output
                    input("Press Enter twice to continue....")
                    keyboard.wait('enter')
    except KeyboardInterrupt:
        exit_gracefully()
    else:
        try:
            query = input_stdin()
            links = scrape_google(query)
            file_output(query,links) # comment this if you need only browser output
            browser_output(links) # comment this if you need only file output
        except KeyboardInterrupt:
            exit_gracefully()
    end()

if __name__ == '__main__':
    init()
