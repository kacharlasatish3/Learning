# API Testing
# Pytest Framework
# Requests , Json
# UI Testing => User interface
# Language => Python
# Frame work => Pytest , Selenium / Robot Framework/Playwright
# Selenium => Webdriver => it is an interface => Chromedriver,Firefox,IEedge,safari
# Page object model => Accessing DOM (Document object Model) as object with same object will perform all UI actions

# Locators =>
# ID
# Name
# Class Name
# Css Selector => cascading style sheet
# XPath => Absolute XPATH => this wil identify element from root to till last element
# this will use / (single slash) => /html/body/div[1]/div/div[2]/div[1]/div/div/form/div[1]/input
#   Relative /dynamic XPATH => this will identify the element based on from particular level
# and this will use // (double slash)
# //div[@class='featured-box cloumnsize1']/h4[1]
# LinkText
# Partial Link Text


import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(2)
# driver.find_element(By.ID,"user-name").send_keys("standard_user")
# driver.find_element(By.ID,"password").send_keys("secret_sauce")
# driver.find_element(By.NAME,"user-name").send_keys("standard_user")
# driver.find_element(By.NAME,"password").send_keys("secret_sauce")
# driver.find_element(By.ID,"user-name").send_keys("standard_user")
# driver.find_element(By.ID,"password").send_keys("secret_sauce")
# driver.find_element(By.CSS_SELECTOR,".form_group input#user-name").send_keys("standard_user")
# driver.find_element(By.CSS_SELECTOR,".form_group input#password").send_keys("secret_sauce")
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[1]/input").send_keys("standard_user")
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[2]/input").send_keys("secret_sauce")
time.sleep(2)
driver.find_element(By.ID,"login-button").click()

time.sleep(20)
driver.close()