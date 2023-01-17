from actions.errorlog import *
from actions.output import *
from actions.basic import *
from actions.g_scraper import *
import os
import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format
import argparse

def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r')  # return an open file handle

def parse_args():
    parser = argparse.ArgumentParser(description="Efficient GitHub repo finder and error detector")
    parser.add_argument('-t', help='Title or Error name', type=str, default=None)
    parser.add_argument("-f", dest="filename", help="Input file with titles or error logs", metavar="FILE", type=lambda x: is_valid_file(parser, x))
    parser.add_argument('-gg', help='GitHub Support give 1 if you need else give 0', type=int, default=None)
    parser.add_argument('-st', help='StackOverflow support 1 if you need else give 0', type=str, default=None)
    parser.add_argument('-d', help='Debug Mode give 1 for debug else give 0', type=int, default=None)
    parser.add_argument('-b', help='Get the output in browser give 1 for yes else 0', type=int, default=None)
    parser.add_argument('-o', help='Get the output to a file give 1 for yes and 0 for no', type=int, default=None)
    if len(sys.argv) == 1:
        print(banner())
        parser.print_help()
        exit_gracefully()
    args = parser.parse_args()
    return args

def banner():
    cprint(figlet_format('Easy Copy', font='sblood'),
       'red',  attrs=['bold'])

# parsers

def file_input_parser(args):
    if args.f is not None:
        queries = file_input()
        for query in queries:
            links = scrape_google(query)
            return links
    else:
        print("Give filename as input")

def title_input_parser(args):
    if args.t is not None:
        query = args.t
        links = scrape_google(query)
        return links
    else:
        print("Enter title or error")

def github_support_parser(args):
    if args.gg is not None or args.gg == 1:
        if args.t is not None and args.f is None:
            links = title_input_parser(args)
        elif args.t is None and args.f is not None:
            links = file_input_parser(args)
        else:
            print("Provide title or error as input either through file or cli")
        print(links)
        github_browser_output(links)

def stackoverflow_support_parser(args):
    if args.st is not None or args.st == 1:
        if args.t is not None and args.f is None:
            links = title_input_parser(args)
        elif args.t is None and args.f is not None:
            links = file_input_parser(args)
        else:
            print("Provide title or error as input either through file or cli")
        print(links)
        stack_browser_output(links)

def file_output_parser(args):
    if args.o is not None and args.o == 1:
        if args.t is not None and args.f is None:
            query = args.t
            links = title_input_parser(args)
            file_output(query, links)
        elif args.t is None and args.f is not None:
            queries = file_input()
            for query in queries:
                links = file_input_parser(args)
                file_output(query, links)
        else:
            print("Provide title using cli or file")
    else:
        print("Invalid option")

def debug_support_parser(args):
    if args.d is not None and args.d == 1:
        debug_support()
    elif args.d is not None and args.d == 0:
        pass
    else:
        print("Invalid Option")

def browser_output_parser(args):
    if args.b is not None  and args.b == 1:
        if args.f is not None and args.t is None:
            links = file_input_parser(args)
            print(links)
            browser_output(links)
        elif args.f is None and args.t is not None:
            links = title_input_parser(args)
            print(links)
            browser_output(links)
        else:
            print("Provide title or error in cli or file input")
    elif args.b is not None and args.b == 0:
        pass
    else:
        print("Invalid option")    
        
def init():
    os.system('cls')
    args = parse_args()
    
    # parsing arguments
    if args.t is not None:
        title_input_parser(args)
    elif args.f is not None:
        file_input_parser(args)
    elif args.gg is not None:
        github_support_parser(args)
    elif args.st is not None:
        stackoverflow_support_parser(args)
    elif args.o is not None:
        file_output_parser(args)
    elif args.b is not None:
        browser_output_parser(args)
    elif args.d is not None:
        debug_support_parser(args)
    else:
        exit_gracefully()
    # # TODO argparser instead of sys.argv
    # try:
    #     if len(sys.argv) > 1:
    #         if sys.argv[1] == '-f':
    #             file_input()
    #             queries = file_input()
    #             for query in queries:
    #                 links = scrape_google(query)
    #                 file_output(query,links) # comment this if you need only browser output
    #                 browser_output(links) # comment this if u need only file output
    #                 input("Press Enter twice to continue....")
    #                 keyboard.wait('enter')
    # except KeyboardInterrupt:
    #     exit_gracefully()
    # else:
    #     try:
    #         query = input_stdin()
    #         links = scrape_google(query)
    #         file_output(query,links) # comment this if you need only browser output
    #         browser_output(links) # comment this if you need only file output
    #     except KeyboardInterrupt:
    #         exit_gracefully()
    # end()

if __name__ == '__main__':
    init()
