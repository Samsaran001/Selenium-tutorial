from selenium import webdriver
driver=webdriver.Firefox()
driver.maximize_window()
driver.get('https://blog.qasource.com/software-development-and-qa-tips/how-do-you-handle-a-broken-image-in-selenium')
driver.switch_to.new_window()
driver.get('https://dangal.io/login')
print(f'total windows count{len(driver.window_handles)}')
windows_handle=driver.window_handles
print(windows_handle)
current_handle=driver.current_window_handle
print(current_handle)