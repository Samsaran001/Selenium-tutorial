from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('https://dangal.io/')
driver.maximize_window()
title = driver.title
print(title)
assert 'Dangal' in title
driver.find_element(By.XPATH('#APjFqb'))
