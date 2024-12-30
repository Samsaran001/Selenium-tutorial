from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
url="https://the-internet.herokuapp.com/javascript_alerts"
driver.get(url)

first_alert=driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']")
first_alert.click()
time.sleep(5)
alert=driver.switch_to.alert
alert_text=alert.text
print(f'this alert msg name is',{alert_text})
alert.accept()
time.sleep(3)
second_alert = driver.find_element(By.XPATH,"//button[@onclick='jsConfirm()']")
second_alert.click()
time.sleep(5)
alert = driver.switch_to.alert
alert_text2 = alert.text
print(f'second alert name is',{alert_text2})
alert.dismiss()
time.sleep(3)
third_alert=driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']")
third_alert.click()
time.sleep(5)
alert=driver.switch_to.alert
alert_text3=alert.text
print(f'the third alert msg is',{alert_text3})
alert.send_keys('this is selenium automation testing')
alert.accept()
time.sleep(4)
driver.close()
print('This program sucessfully runned')