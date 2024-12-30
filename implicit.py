from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
username="standard_user"
password="secret_sauce"
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID,"user-name").send_keys(username)
driver.find_element(By.ID,"password").send_keys(password)
driver.find_element(By.ID,"login-button").click()
driver.find_element(By.ID,"react-burger-menu-btn").click()
driver.find_element(By.ID,"logout_sidebar_link").click()
print("The logout process is complete")    