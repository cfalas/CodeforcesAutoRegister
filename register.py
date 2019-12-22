#!/usr/bin/python
################### Constants ####################
username = "USERNAME"
password = "PASSWORD"
chromedriver_path = "/path/to/chromedriver"
##################################################
from selenium import webdriver

browser = webdriver.Chrome(chromedriver_path)

# Find the id of the next contest by looking on the table on the consest page
browser.get('http://codeforces.com/contests')
src = browser.page_source
index = src.find("data-contestid")
contestid = (src[index+16:index+20])

# Redirect browser to registration page
browser.get("http://codeforces.com/contestRegistration/" + contestid)

# In case that the user is not logged in, log in
try:
    browser.find_element_by_xpath("/html/body/div[5]/div[4]/div/div/div/form/table/tbody/tr[1]/td[2]/input").send_keys(username)
    browser.find_element_by_xpath("/html/body/div[5]/div[4]/div/div/div/form/table/tbody/tr[2]/td[2]/input").send_keys(password)
    browser.find_element_by_xpath("/html/body/div[5]/div[4]/div/div/div/form/table/tbody/tr[4]/td/div[1]/input").click()
except NoSuchElementException:
    print("Already logged in, skipping login")

# Wait until page loads before clicking register button
browser.implicitly_wait(3)

# Click register button
browser.find_element_by_xpath("/html/body/div[5]/div[4]/div[2]/form/table/tbody/tr[3]/td/div/input").click()
