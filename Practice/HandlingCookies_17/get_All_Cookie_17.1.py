from selenium import webdriver
import time

driver = webdriver.Edge(executable_path="../../Driver/msedgedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.amazon.in")

# 1. Capture all cookies related to browser
all_cookies = driver.get_cookies()

print(len(all_cookies)) # print number of cookies created
print(all_cookies) # actual cookies information

time.sleep(3)
driver.close()
driver.quit()

