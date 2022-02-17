"""
This program, to automate login proccess using username and password
"""

from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.phptravels.net/login')
messageField = driver.find_element_by_xpath('//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[1]/div/input')
messageField.send_keys('user@phptravels.com')
passField = driver.find_element_by_xpath('//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[2]/div[1]/input')
passField.send_keys('demouser')

loginButton = driver.find_element_by_xpath('//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[3]/button/span[1]')
loginButton.click()
