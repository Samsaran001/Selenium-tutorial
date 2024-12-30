from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver=webdriver.Firefox()
driver.get('https://blog.qasource.com/software-development-and-qa-tips/how-do-you-handle-a-broken-image-in-selenium')
driver.maximize_window()
images=driver.find_elements(By.TAG_NAME,'img')
print(f'total images count{len(images)}')
broken_images=[]
for demo in images:
      src = demo.get_attribute('src')
      resonse = requests.get(src)
      if resonse.status_code >=200:
        broken_images.append(src)
        print('images append process complete')
      else:
        print('not available in broken images')  
if broken_images:
    print('list of images')
    for broken_image in  broken_images:
        print(f'broken images{broken_image}')        