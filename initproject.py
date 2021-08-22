#!/usr/bin/env python3

import os
import sys
import time
from selenium import webdriver
import configparser

default_path = ""
github_username = ""
github_password = ""
project_name = str(sys.argv[1])

def read_config_file():
    global github_username, github_password, default_path
    config = configparser.ConfigParser()
    config.read('giteverything.ini')
    github_username = config["DEFAULT"]["GithubUsername"]
    github_password = config["DEFAULT"]["GithubPassword"]
    default_path = config["DEFAULT"]["ProjectDirectory"]
    print("Use Username " + github_username)
    print("Use password " + github_password)

def login_to_github():
    global github_username, github_password, default_path
    print("Login to github.com...")
    browser.get("https://github.com/login")
    field_user_name = browser.find_elements_by_xpath("//*[@id='login_field']")[0]
    field_user_name.send_keys(github_username)
    field_user_pw = browser.find_elements_by_xpath("//*[@id='password']")[0]
    field_user_pw.send_keys(github_password)
    btn_login = browser.find_elements_by_xpath("//*[@name='commit']")[0]
    btn_login.click()

def create_remote_repository():
    global github_username, github_password, default_path
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

def clone_repo():
    global github_username, github_password, default_path
    print("Cloning repo to local machine...")
    os.chdir(default_path)
    os.system("git clone git@github.com:" + github_username + "/" + project_name + ".git")

if __name__ == "__main__":
    print("Create new project '" + project_name + "' at '" + default_path + "'.")
    read_config_file()
    browser = webdriver.Chrome("./chromedriver")
    try:
        login_to_github()
        create_remote_repository()
    except:
        print("Something failed")
    browser.quit()
    clone_repo()