from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
login_url="https://www.saucedemo.com/"
driver.get(login_url)
#driver.minimize_window()
username="standard_user"
password="secret_sauce"

username_field=driver.find_element(By.ID,"user-name")
passowrd_field=driver.find_element(By.ID,"password")
time.sleep(2)
username_field.send_keys(username)
time.sleep(2)
passowrd_field.send_keys(password)

login_button=driver.find_element(By.ID,"login-button")
login_button.get_attribute('disabled')
login_button.click()
time.sleep(5)
success_page=driver.find_element(By.CSS_SELECTOR,".title")

assert success_page.text == "Products"

