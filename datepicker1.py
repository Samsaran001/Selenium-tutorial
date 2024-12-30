from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime,timedelta
from selenium.webdriver import Keys
driver=webdriver.Chrome()

url="https://www.globalsqa.com/demo-site/datepicker/"
driver.get(url)
driver.maximize_window()
print("windows maximize process is complete")

driver.find_element(By.XPATH,"//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//a[@class='close_img']").click
print("Red alert msg is cancelled")
time.sleep(3)

i_frame = driver.find_element(By.XPATH,"//iframe[@class='demo-frame lazyloaded']")
driver.switch_to.frame(i_frame)
print("iframe swiched process is complete")

date=driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
current_date=datetime.now()
next_date = current_date + timedelta(days=-1) #days -1 minimize to current date days +1 added the current date
format_date = next_date.strftime("%m/%d/%y")
final=driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys(format_date,Keys.TAB) 
print("date also selected")
time.sleep(4)
print("Code running is completed")