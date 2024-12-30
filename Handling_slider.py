from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
url="https://the-internet.herokuapp.com/horizontal_slider"
driver.get(url)
actions=ActionChains(driver)
range = driver.find_element(By.XPATH,"//input[@value='0']")

actions.click_and_hold(range).move_by_offset(50,0).release().perform()
print("the range process is complete")
time.sleep(5)

