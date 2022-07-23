from ast import arg
from playwright.sync_api import sync_playwright
import configparser
import sys


configParser = configparser.RawConfigParser()   
configFilePath = r'D:\Login_screen\Config.txt'
configParser.read(configFilePath)
url_details = dict(configParser.items('URL'))
cred_details = dict(configParser.items('Credentials'))
args1= (sys.argv)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=50)
    page=browser.new_page()
    page.goto(url_details[args1[1]])
    new_selector = page.is_visible('a[class="logo"]')
    if new_selector == True: 
        page.type('input[name="login[username]"]', cred_details['username'])  
        page.type('input[class="input-text required-entry validate-latin-only validate-password"]', cred_details['password'])
        page.click('button[title=Login]')
        dashboard_selector = page.is_visible('input[class="dashboard"]')
        if dashboard_selector == True:
            pass
        else:
            print("Access Denied for automation and the dashboard is not loaded")
    else:
        print("Login Page not loaded")
   