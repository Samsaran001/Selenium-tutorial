from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

username="standard_user"
password="secret_sauce"

driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID,"user-name").send_keys(username)
driver.find_element(By.ID,"password").send_keys(password)
driver.find_element(By.ID,"login-button").click()
driver.find_element(By.ID,"react-burger-menu-btn").click()
element=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//input[@id='login-button']")))
#driver.find_element(By.ID,"logout_sidebar_link").click()
print("The logout process is complete")    