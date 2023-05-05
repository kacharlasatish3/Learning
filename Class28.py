# Navigation commands
# Conditional commands
# input boxes
# Radio buttons & check boxes
# drop-downs
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
# driver.back()
# time.sleep(5)
# driver.forward()
# time.sleep(5)
# driver.refresh()

# drop downs
dropdown = Select(driver.find_element(By.CSS_SELECTOR,".product_sort_container"))
print(dropdown.options)
dropdown.select_by_index(1)
time.sleep(5)
dropdown = Select(driver.find_element(By.CSS_SELECTOR,".product_sort_container"))
dropdown.select_by_value("lohi")
time.sleep(5)
dropdown = Select(driver.find_element(By.CSS_SELECTOR,".product_sort_container"))
dropdown.select_by_visible_text("Price (high to low)")

time.sleep(20)
driver.close()




# dropdowns