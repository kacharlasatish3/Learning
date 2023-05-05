import time
# Navigation commands =>
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://saucedemo.com")
driver.maximize_window()

driver.find_element(By.ID,"user-name").send_keys("standard_user")

driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
time.sleep(5)
# driver.execute_script("window.scrollBy(0,500)","")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# Element  = driver.find_element_by_xpath(“xpath”)
# Driver.execute_script(“arguments[0].scrollIntoView();”,Element)
driver.save_screenshot("sample.jpg")
driver.get_screenshot_as_file("sample1.jpg")
time.sleep(20)

