from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument('start-maximized')
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

def browser_output(links):
    # TODO check for debug option here
    # parser = argparse.ArgumentParser()
    for posts in range(links):
        browser.get(links[posts])
        if(posts!=len(links)-1):
                browser.execute_script("window.open('');")
                chwd = browser.window_handles
                browser.switch_to.window(chwd[-1])


def stack_browser_output(links):
    for posts in range(len(links)):
        if 'https://stackoverflow.com' in links[posts]:
            browser.get(links[posts])    
            if(posts!=len(links)-1):
                browser.execute_script("window.open('');")
                chwd = browser.window_handles
                browser.switch_to.window(chwd[-1])


def github_browser_output(links):
    for posts in range(len(links)):
        if 'https://github.com' in links[posts]:
            browser.get(links[posts])    
            if(posts!=len(links)-1):
                browser.execute_script("window.open('');")
                chwd = browser.window_handles
                browser.switch_to.window(chwd[-1])