from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
url="https://demo.automationtesting.in/Datepicker.html"
driver.get(url)

actions = ActionChains(driver)
mouse_tougher=driver.find_element(By.XPATH,"//a[normalize-space()='SwitchTo']")
print("mouse tougher is sucessful")
time.sleep(5)

actions.move_to_element(mouse_tougher).perform()
driver.find_element(By.XPATH,"//a[normalize-space()='Frames']").click()
time.sleep(5)
print('handling mouse hover code running is complete')