from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

chrome_option=Options()
chrome_option.add_argument('--incognito')

driver=webdriver.Chrome(options=chrome_option)
driver.get('https://www.google.co.in/')
time.sleep(5)
driver.quit()

