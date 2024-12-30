from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
url="https://demo.automationtesting.in/Resizable.html"
driver.get(url)
actions=ActionChains(driver)

resizeable = driver.find_element(By.XPATH,"//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
standard = driver.find_element(By.XPATH,"//div[@id='resizable']")

resize_size = resizeable.size
print(resize_size)

actions.click_and_hold(resizeable).move_by_offset(100,100).release().perform()
changed_size=standard.size
print(changed_size)
print('The box size is changed and code is complete')
driver.quit()
