from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.firefox.options import Options

Firefox_option=Options()
Firefox_option.add_argument('--private')

driver=webdriver.Firefox(options=Firefox_option)
driver.get('https://www.google.co.in/')
time.sleep(5)
driver.quit()

