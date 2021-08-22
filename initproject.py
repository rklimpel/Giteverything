#!/usr/bin/python3

import os
import sys
import time
from selenium import webdriver

default_path = "/asdf/asdf/asdf"
github_username = "asdf"
github_password = "asdf"
project_name = str(sys.argv[1])

print("Create new project '" + project_name + "' at '" + default_path + "'.")

def create_remote_repository():
    browser = webdriver.Chrome("./chromedriver")

    #Github Login
    print("Login to github.com...")
    browser.get("https://github.com/login")
    field_user_name = browser.find_elements_by_xpath("//*[@id='login_field']")[0]
    field_user_name.send_keys('rklimpel')
    field_user_pw = browser.find_elements_by_xpath("//*[@id='password']")[0]
    field_user_pw.send_keys(github_pw)
    btn_login = browser.find_elements_by_xpath("//*[@name='commit']")[0]
    btn_login.click()

    #Create Repo
    print("Creating repo on github.com...")
    browser.get("https://github.com/new")
    field_repo_name = browser.find_elements_by_xpath("//*[@name='repository[name]']")[0]
    field_repo_name.send_keys(project_name)
    toggle_private = browser.find_elements_by_xpath("//*[@id='repository_visibility_private']")[0]
    toggle_private.click()
    toggle_readme = browser.find_elements_by_xpath("//*[@id='repository_auto_init']")[0]
    toggle_readme.click()
    btn_create_repo = browser.find_element_by_xpath("//button[contains(text(),'Create repository')]")
    btn_create_repo.submit()

    browser.quit()

def clone_repo():
    print("Cloning repo to local machine...")
    os.chdir(default_path)
    os.system("git clone git@github.com:" + github_username + "/" + project_name + ".git")

if __name__ == "__main__":
    create_remote_repository()
    clone_repo()