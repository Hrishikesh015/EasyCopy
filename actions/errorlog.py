import subprocess
from output import stack_browser_output
from g_scraper import scrape_google

def get_error_log(command):
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        output = e.output
    return output.decode()

def debug_support():
    cmd = input("Enter command here: ")
    error_log = get_error_log(cmd)
    stack_browser_output(scrape_google(error_log)) 
    # TODO add browser arguement in stack_browser_output