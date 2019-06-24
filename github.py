#!usr/bin/python

import os
import sys
import time
from selenium import webdriver

default_path = "/Users/rico/code/"
project_name = str(sys.argv[1])
github_pw = str(sys.argv[2])

def create_local_path():
    print("Creating local folder ",project_name," in ",default_path,".")
    #os.makedirs(default_path + project_name)

def create_remote_repository():
    browser = webdriver.Chrome("/usr/local/bin/chromedriver")

    #Github Login
    browser.get("https://github.com/login")
    field_user_name = browser.find_elements_by_xpath("//*[@id='login_field']")[0]
    field_user_name.send_keys('rklimpel')
    field_user_pw = browser.find_elements_by_xpath("//*[@id='password']")[0]
    field_user_pw.send_keys(github_pw)
    btn_login = browser.find_elements_by_xpath("//*[@name='commit']")[0]
    btn_login.click()
    time.sleep(3)
    browser.get("https://github.com/new")
    field_repo_name = browser.find_elements_by_xpath("//*[@name='repository[name]']")[0]
    field_repo_name.send_keys(project_name)
    toggle_private = browser.find_elements_by_xpath("//*[@id='repository_visibility_private']")[0]
    toggle_private.click()
    toggle_readme = browser.find_elements_by_xpath("//*[@id='repository_auto_init']")[0]
    toggle_readme.click()
    btn_create_repo = browser.find_element_by_css_selector("button.first-in-line")
    btn_create_repo.submit()
    time.sleep(3)

if __name__ == "__main__":
    print("Creating new project ",project_name,"...")
    create_local_path()
    create_remote_repository()