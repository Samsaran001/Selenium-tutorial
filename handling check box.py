from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://app.endtest.io/guides/docs/how-to-test-checkboxes/')
#driver.execute_script("windows.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
#driver.find_element(By.ID,'pet1').click()
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")

check_count=0
for checkbox in  checkboxes:
    if checkbox.is_selected():
           check_count+=1
print(check_count)
total_checkbox=3
if check_count==total_checkbox:
    print('check box is verified')
else:
    print('check box is not defined')

time.sleep(3)
driver.close()
