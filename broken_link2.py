from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

driver = webdriver.Chrome()
driver.get('http://34.225.34.54/stldemo/login')

user_name = 'stl0002'
password = 'Mahi@123'


user_field = driver.find_element(By.ID, 'username')
password_field = driver.find_element(By.ID, 'password')

user_field.send_keys(user_name)
password_field.send_keys(password)

driver.find_element(By.ID, 'login_btn').click()

time.sleep(5)

all_links = driver.find_elements(By.TAG_NAME, 'a')
print(f"Total count of links: {len(all_links)}")

for link in all_links:
    href = link.get_attribute('href')
    # Check if the href is valid
    if href and href.startswith(('http://', 'https://')):
        try:
            response = requests.get(href)
            if response.status_code >= 400:
                print(f"The request to {href} returned status code {response.status_code}")
            else:
                print(f"The server is working fine for {href}")
        except requests.exceptions.RequestException as e:
            print(f"Error while requesting {href}: {e}")
    else:
        print(f"Skipping invalid href: {href}")

time.sleep(3)
driver.quit()
