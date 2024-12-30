from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()

url="https://the-internet.herokuapp.com/nested_frames"
driver.get("https://the-internet.herokuapp.com/nested_frames")

#Left nested frame
Left=driver.switch_to.frame("frame-top")
#middle frame
driver.switch_to.frame("frame-middle")
middle = driver.find_element(By.ID,"content").text
print("middle frame name is",middle)
#default frame
driver.switch_to.default_content()

driver.switch_to.frame("frame-bottom")
bottom = driver.find_element(By.TAG_NAME,"body").text
print("default frame name is",bottom)
time.sleep(3)






