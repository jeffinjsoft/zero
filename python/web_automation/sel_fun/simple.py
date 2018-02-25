from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://github.com/login")

if 'GitHub' in driver.title:
    print 'found login page'
else:
    print 'please check url'

elem = driver.find_element_by_id("login_field")
elem.send_keys('jeffin.jsoft@gmail.com')
elem = driver.find_element_by_id("password")
elem.send_keys('123')
login_attempt = driver.find_element_by_xpath("//*[@type='submit']")
login_attempt.click()



c=raw_input("Enter to exit")

driver.close()
