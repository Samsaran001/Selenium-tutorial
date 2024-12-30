from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
url="https://the-internet.herokuapp.com/drag_and_drop"
driver.get(url)

actions=ActionChains(driver)

source_element = driver.find_element(By.ID,'column-a')
desigation_element = driver.find_element(By.ID,"column-b")

actions.drag_and_drop(source_element,desigation_element).perform()
print("the drag and Drop process is complete")
time.sleep(5)
print("Drag and drop code process is complete")