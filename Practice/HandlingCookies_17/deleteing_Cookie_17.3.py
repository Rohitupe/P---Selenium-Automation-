from selenium import webdriver
import time

driver = webdriver.Edge(executable_path="../../Driver/msedgedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.amazon.in")

# get cookie length
allCookies = driver.get_cookies()
print(len(allCookies))

# 2. Adding new cookie to the browser
cookie = {
    'name': 'My Cookie',
    'value': '1234567890'
}  # for each cookie we should specify name and value
driver.add_cookie(cookie)  # adding cookie to browser

# get cookie length
allCookies = driver.get_cookies()
print(len(allCookies))

# Deleting cookie from browser
driver.delete_cookie(name='My Cookie')  # to delete cookie we need to know it's name

# get cookie length
allCookies = driver.get_cookies()
print(len(allCookies))

time.sleep(3)
driver.close()
driver.quit()
