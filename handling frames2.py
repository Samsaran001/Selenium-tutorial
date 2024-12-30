from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/iframe")

# Switch to the iframe
iframe = driver.find_element(By.ID, "mce_0_ifr")
driver.switch_to.frame(iframe)

# Locate the text editor
Text_Editor = driver.find_element(By.ID, "tinymce")

# Clear the text editor using Keys
Text_Editor.send_keys(Keys.CONTROL + "a")  # Select all text
Text_Editor.send_keys(Keys.DELETE)         # Delete selected text

# Enter new text
Text_Editor.send_keys("selenium using with python")
time.sleep(3)

# Switch back to the main content
driver.switch_to.default_content()

# Click on the link
Navigate_Link = driver.find_element(By.XPATH, "//a[normalize-space()='Elemental Selenium']")
Navigate_Link.click()
time.sleep(3)

driver.quit()
