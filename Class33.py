# Mouse Actions
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://saucedemo.com")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.ID,"user-name").send_keys("standard_user")

driver.find_element(By.ID,"password").send_keys("secret_sauce")


wait = WebDriverWait(driver,10)
element = wait.until(EC.element_to_be_clickable(driver.find_element(By.ID,"login-button")))
element.click()

# driver.find_element(By.ID,"login-button").click()
time.sleep(5)
actions = ActionChains(driver)
actions.move_to_element(driver.find_element(By.ID,"react-burger-menu-btn")).click().perform()
time.sleep(5)
actions.move_to_element(driver.find_element(By.ID,"about_sidebar_link")).click().perform()

time.sleep(5)
# Right click => to perform right click on particular element we need to use context_click
actions.context_click(driver.find_element(By.XPATH,"//*[@id='__next']/div[2]/div[1]/div/div[1]/div[1]/div/div[4]/div[1]/a/button")).perform()

time.sleep(20)

#drag and drop => provide source element from where we need to drag
# targetelement => where we need to drop
sourceelement = driver.find_element(By.XPATH,"//*[@id='fourth']/a")
targetelement = driver.find_element(By.XPATH,"//*[@id='loan']/li")
actions.drag_and_drop(sourceelement,targetelement)

# why we need time.sleep , is there any other alternative
# In selenium it will not wait for any element to load , it will continue execution
# Wait concepts => Implicit wait,explicit wait
# Implicit wait  => this we will give at top of the code or page level
# driver.Implicit_wait(10)=> if elements are loaded with in 8 secs it will save other 2 secs
# Explicit wait => we will provide wait on particular element and based on condition


# JIRA
# GIT hub
# SDLC => WATERFALL ,AGILE
# AGILE => Ceremonies
# 1) Sprint Planing  => Sprint duration =>we will plan work for 2 weeks
# ,in 2 weeks first day will be Sprint planing =>they will plan the work which we need work /which task we need to work
# they will define sprint goal => what we have to achieve end of the sprint
# Product owner , Scrum master
# Product owner => who will provide the requirement/acceptance criteria
# Scrum master => he will conduct daily scrum meeting, and he will co-ordinate with team members and
# dependencies and will arrange required things to team
# 2) daily scrum => we will have daily 15 mins meeting =>
# what I worked yesterday and what is the status of that , what I am working today
# is there any blockers for you
# 3) Sprint Review meeting => End of the sprint ,last day of the sprint or immediate next day of end of sprint
# we will show case/give demo regarding the work which we have done in last two weeks
# we will get suggestions from client/stack holders , product owners , we can get the requirement changes also
# and work in future sprint
# 4) Sprint Retro => how the last sprint was , this will be conduct next day of end of sprint
# Liked => what is the gud thing happend ,example : if every one completed task in on time
# Learnt => like we learnt about new apis/new functionality or we learnt any new technology
# Lacked => we are not able to achieve goals , we are not able to deliver results , you have some dependencies
# from developer you didnt received build in on time
# action => what to do to solve the issues which we have seen in last sprint

# 5) backlog refinement => it will be conducted by product owner, and he will plan the work future work
# he will explain about stories , what are the dependencies for each story and how much time it will take
# how time it will take from testing => he will create tasks under stories



# JIRA
# GIT hub => version control
# central repository => server where we can place our source code so every one will get access
# SVN , TFS(Team foundation server) ,Git hub , Bit Bucket ,Azure devops
# Git hub => open source version control
