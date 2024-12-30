from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
url="http://34.225.34.54/stldemo/login"
driver.get(url)
driver.maximize_window()
driver.find_element(By.XPATH,"//a[@class='text-muted']").click()

Find_page = driver.find_element(By.CSS_SELECTOR,"h5.text-primary")
assert Find_page.text == "Forgot Password"
print('The Proper page is navigate')
time.sleep(2)
driver.back()
time.sleep(2)

driver.find_element(By.XPATH,"//input[@id='username']").send_keys("stl0002")
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Mahi@123")
time.sleep(2)
driver.find_element(By.XPATH,"//i[@id='password-icon']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[@id='login_btn']").click()
time.sleep(2)
'''
driver.find_element(By.XPATH,"//a[@data-bs-toggle='slide']//span[contains(text(),'Task Assignment')]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[normalize-space()='Assign Tasks']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[@type='button']//span//span[contains(text(),'Task Assignment')]").click()
time.sleep(2)

side_menu = driver.find_element(By.CLASS_NAME,'main-sidemenu')
# Find the side menu element (you may need to adjust the selector)
#side_menu = driver.find_element(By.CSS_SELECTOR, '.side-menu')  # Adjust the selector to your side menu

# Scroll the side menu using JavaScript
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", side_menu)
#driver.execute_script("window.scrollBy(0,500);")

task_assignment = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "//span[@class='side-menu__label' and contains(text(),'Task Assignment')]"
    )))

task_assignment.click()

# Wait for the Assign Tasks link to be clickabl
assign_tasks = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Assign Tasks']"))
)
assign_tasks.click()
find_page = driver.find_element(By.CSS_SELECTOR,"h4.card-header")
assert find_page.text == "TASK ASSIGNMENT"
print('The page naivation process is complete')
'''

driver.switch_to.new_window("http://34.225.34.54/stldemo/new-task-request")
time.sleep(5)
note="The selenium sample test"
driver.find_element(By.XPATH,"//input[@name='task_description']").send_keys(note)
time.sleep(2)
driver.find_element(By.XPATH,"//input[@name='task_description']").send_keys(Keys.CONTROL + 'a')
time.sleep(2)
driver.find_element(By.XPATH,"//input[@name='task_description']").send_keys(Keys.DELETE)
time.sleep(2)
print('The process is complete')
