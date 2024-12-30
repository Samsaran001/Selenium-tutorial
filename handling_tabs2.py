from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.selenium.dev/')
driver.switch_to.new_window()
driver.get('https://www.google.co.in/')
print(f'the number of windows count {len(driver.window_handles)}')
print(f'The windows tabs {driver.window_handles}')
current_tab=driver.current_window_handle
print(f'current tab{driver.current_window_handle}')

driver.find_element(By.CSS_SELECTOR,"div[class='FPdoLc lJ9FBc'] input[name='btnK']").click()
first_tab = driver.window_handles[0]
if current_tab != first_tab:
        driver.switch_to.window(first_tab)