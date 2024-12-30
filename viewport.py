from selenium import webdriver
import time
driver = webdriver.Chrome()

viewport=[(768,1024),(480,320),(726,1408)]
driver.get('https://www.google.co.in/')

try:
    for width,height in viewport:
            driver.set_window_size(width,height)
            time.sleep(3)

finally:
      driver.close()
