from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import select as something
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://formstone.it/components/dropdown/demo/')
dropdown_list=driver.find_element(By.ID,'demo_basic-dropdown-selected')
#selected = Select(dropdown_list)
#selected.select_by_visible_text('Two')
#selected.select_by_index('2')
#selected.select_by_value('3')
Select = something.select(dropdown_list)
target_value='Two'
for option in Select.options:
       if option.text==target_value:
           print(f"dropdown list is verified{target_value}")
       else:
            print(f"values{target_value}is incorrect")   
'''
normal_count=len(selected.options)
expected_count=10
if normal_count==expected_count:
    print('test case is correct')
else:
    print('test case is incorrect') '''    
time.sleep(5)