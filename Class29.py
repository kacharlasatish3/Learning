import time
# Navigation commands =>
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://demo.guru99.com/test/radio.html")
driver.maximize_window()
time.sleep(5)
rd_button = driver.find_element(By.ID,"vfb-7-1")

# conditional commands
print(rd_button.is_enabled())
rd_button.click()
time.sleep(5)
print(rd_button.is_selected())
print(rd_button.is_displayed())

driver.find_element(By.ID,"vfb-6-0").click()
driver.find_element(By.ID,"vfb-6-1").click()

time.sleep(10)