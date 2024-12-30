from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
url="https://testrigor.com/samples/table1/"
driver.get(url)
#driver.switch_to.frame("frame_name_or_id")  # If within an iframe
#driver.switch_to.window(driver.window_handles[0])  # If switching windows
driver.execute_script("window.scrollBy(0,400);")
#driver.execute_script("return window.location.href;")  # Correct
#driver.execute_script("return windows.location.href;")  # Incorrect

#time.sleep(5)

table = driver.find_element(By.CSS_SELECTOR,"tbody tr:nth-child(1) th:nth-child(1)")
rows = table.find_elements(By.TAG_NAME,'tr')
count_row = len(rows)
print(count_row)
target_value = "york1"
found = False
for row in rows:
    cells = row.find_elements(By.TAG_NAME,"td")
    for cell in cells:
          if target_value in cell:
               print(f'found value is {target_value}')
               break
          if found in True:
               break
if not found:
     print(f'{target_value} is not found')          
                
driver.quit()