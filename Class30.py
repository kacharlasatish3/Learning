import time
# Navigation commands =>
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://demo.guru99.com/test/delete_customer.php")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@name='submit']").click()
time.sleep(3)
driver.switch_to.alert.accept() # ok
driver.switch_to.alert.dismiss() # cancel

time.sleep(10)

driver.switch_to.default_content()
driver.switch_to.frame("sample")

# how to switch between windows or tabs in browser
current_window = driver.current_window_handle
windows = driver.window_handles
driver.switch_to.window(windows[2])
for i in windows:
    driver.switch_to.window(i)

driver.switch_to.window(current_window)
