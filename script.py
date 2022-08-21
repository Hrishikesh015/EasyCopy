import requests
import urllib
from requests_html import HTML
from requests_html import HTMLSession
from selenium import webdriver
import time
import os
import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format
import keyboard
from selenium.webdriver.chrome.options import Options



def banner():
    cprint(figlet_format('Easy Copy', font='sblood'),
       'red',  attrs=['bold'])


def get_source(url):
    """Return the source code for the provided URL. 

    Args: 
        url (string): URL of the page to scrape.

    Returns:
        response (object): HTTP response object from requests_html. 
    """

    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)


def scrape_google(query):

    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.co.uk/search?q=" + query + 'github')

    links = list(response.html.absolute_links)
    google_domains = ('https://www.google.', 
                      'https://google.', 
                      'https://webcache.googleusercontent.', 
                      'http://webcache.googleusercontent.', 
                      'https://policies.google.',
                      'https://support.google.',
                      'https://maps.google.')

    for url in links[:]:
        if url.startswith(google_domains):
            links.remove(url)

    return links

def browser_output(links):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(executable_path='C:\chromedriver.exe', options=chrome_options)
    for posts in range(len(links)):
        if 'https://github.com' in links[posts]:
            browser.get(links[posts])    
            if(posts!=len(links)-1):
                browser.execute_script("window.open('');")
                chwd = browser.window_handles
                browser.switch_to.window(chwd[-1])

def file_output(query,links):
    with open(query+' links.txt', 'w') as fp:
        fp.write('\n'.join(links))

def input_stdin():
    query = input('Enter your project title: ')
    return query

def file_input():
    queries = []
    with open(sys.argv[1], 'r') as fp:
        for line in fp:
            x = line[:-1]
            queries.append(x)
    return queries

def init():
    os.system('cls')
    banner()
    if len(sys.argv) > 1:
        file_input()
        queries = file_input()
        for query in queries:
            links = scrape_google(query)
            file_output(query,links) # comment this if you need only browser output
            browser_output(links) # comment this if u need only file output
            input("Press Enter twice to continue....")
            keyboard.wait('enter')
    else:
        query = input_stdin()
        links = scrape_google(query)
        file_output(query,links) # comment this if you need only browser output
        browser_output(links) # comment this if u need only file output

if __name__ == '__main__':
    init()