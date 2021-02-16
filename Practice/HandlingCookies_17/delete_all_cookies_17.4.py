from selenium import webdriver
import time

driver = webdriver.Edge(executable_path="../../Driver/msedgedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.amazon.in")

# get cookie length
allCookies = driver.get_cookies()
print(len(allCookies))

# delete all cookies from browser
driver.delete_all_cookies()

# ge cookies length
allCookies = driver.get_cookies()
print(len(allCookies))
print(allCookies)

time.sleep(3)
driver.close()
driver.quit()