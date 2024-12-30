from  selenium import webdriver 
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

username='STL0002'
password='Mahi@123'
url='http://34.225.34.54/stldemo/login'
driver.get(url)
title=driver.title
print(title)
assert 'Dangal' in title
user_field=driver.find_element(By.ID,'username')
password_field=driver.find_element(By.ID,'password')

user_field.send_keys(username)
password_field.send_keys(password)

login_button=driver.find_element(By.ID,'login_btn')
assert not login_button.get_attribute('disabled')
login_button.click()
success_element=driver.find_element(By.TAG_NAME.h3,"card-title")
assert success_element.text == 'Tasks'