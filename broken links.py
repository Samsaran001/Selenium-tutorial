from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
driver=webdriver.Chrome() 
driver.get('https://dangal.io/dashboard')
user_name='stl0335'
password='Mahi@123'
user_field=driver.find_element(By.ID,'username')
password_field=driver.find_element(By.ID,'password')
user_field.send_keys(user_name)
password_field.send_keys(password)
driver.find_element(By.ID,'login_btn').click()

#driver.switch_to.new_window()
#driver.get('https://dangal.io/dashboard')
time.sleep(5)

all_link=driver.find_elements(By.TAG_NAME,'a')
print(f"total count of links{len(all_link)}")

for link in all_link:
    href = link.get_attribute('href')
    response = requests.get(href)
    if response.status_code >=400:
        print(f"the request{href} status code is {response.status_code}")
    else:
        print('the server also good')    

time.sleep(3)
driver.quit()
