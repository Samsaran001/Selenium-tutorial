from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime,timedelta
#from selenium.webdriver import Select
from selenium.webdriver.support.ui import Select


driver=webdriver.Chrome()
url="https://demo.automationtesting.in/Datepicker.html"
driver.get(url)

Tab_click = driver.find_element(By.XPATH,"//input[@id='datepicker2']").click()
time.sleep(3)

current_date = datetime.now()
current_month = datetime.now().month
current_year=current_date.year

next_date=current_date + timedelta(days=1)

print(f'current date is {current_date}')
print(f'current_month is {current_month}')
print(f'current_year is {current_year}')
print(f'the next day date is{next_date}')

The_day=(str(current_date.day))

print(The_day)

next_month=(current_month % 12)+1

month_format= f'{next_month}/{current_year}'

Month_dropdown = driver.find_element(By.CSS_SELECTOR,"select[title='Change the month']")

select = Select(Month_dropdown)
select.select_by_value(month_format)
time.sleep(5)

year_dropdown=driver.find_element(By.XPATH,"//select[@title='Change the year']")
select=Select(year_dropdown)
select=select.select_by_visible_text('2024')
time.sleep(3)

date_selector = driver.find_element(By.LINK_TEXT,'18').click()
time.sleep(5)





