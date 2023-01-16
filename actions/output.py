from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def browser_output(links):
    chrome_options = Options()
    chrome_options.add_argument('start-maximized')
    chrome_options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
    # TODO check for debug option here
    # parser = argparse.ArgumentParser()
    stack_browser_output(browser,links)
    github_browser_output(browser,links)


def stack_browser_output(browser,links):
    for posts in range(len(links)):
        if 'https://stackoverflow.com' in links[posts]:
            browser.get(links[posts])    
            if(posts!=len(links)-1):
                browser.execute_script("window.open('');")
                chwd = browser.window_handles
                browser.switch_to.window(chwd[-1])


def github_browser_output(browser,links):
    for posts in range(len(links)):
        if 'https://github.com' in links[posts]:
            browser.get(links[posts])    
            if(posts!=len(links)-1):
                browser.execute_script("window.open('');")
                chwd = browser.window_handles
                browser.switch_to.window(chwd[-1])