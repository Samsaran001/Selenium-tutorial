from selenium import webdriver
import time

driver=webdriver.Chrome()
username="admin"
password='admin'

url="https://admin:admin@the-internet.herokuapp.com/basic_auth"
driver.get(url)
time.sleep(5)
print('The code running process is complete')


