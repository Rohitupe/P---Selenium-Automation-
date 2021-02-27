from selenium import webdriver
import time

driver = webdriver.Edge(executable_path="../../Driver/msedgedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

URL = "https://rahulshettyacademy.com/AutomationPractice/"
driver.get(URL)

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))
for check in checkboxes:
    check.click()

time.sleep(4)
driver.close()
driver.quit()
