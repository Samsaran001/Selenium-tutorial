from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

json_file='testdata.json'

with open(json_file,'r') as file:
       test_data = json.load(file)            

for data in test_data["users"]:
       driver = webdriver.Chrome()
       driver.maximize_window()
       driver.get("https://www.saucedemo.com/")
       driver.find_element(By.ID,"user-name").send_keys(data['username'])
       driver.find_element(By.ID,"password").send_keys(data['password'])
       time.sleep(5)
       driver.find_element(By.ID,"login-button").click()
       time.sleep(5)