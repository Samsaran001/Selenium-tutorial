from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/iframe")

iframe = driver.find_element(By.ID,"mce_0_ifr")
driver.switch_to.frame(iframe)

driver.find_element(By.XPATH,"//*[name()='path' and contains(@d,'M17.3 8.2L')]").click()
time.sleep(2)
Text_Editor = driver.find_element(By.ID,"tinymce")
#Text_Editor.clear()
Text_Editor.send_keys(Keys.CONTROL + "a")  
Text_Editor.send_keys(Keys.DELETE) 
Text_Editor.send_keys("selenium using with python")
time.sleep(3)

driver.switch_to.default_content()
Navigate_Link = driver.find_element(By.XPATH,"//a[normalize-space()='Elemental Selenium']")
Navigate_Link.click()
time.sleep(3)