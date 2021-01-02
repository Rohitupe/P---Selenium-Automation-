from selenium import webdriver
import time

driver = webdriver.Edge(executable_path="../driver/msedgedriver.exe")

driver.maximize_window()

driver.get("https://www.facebook.com")
print(driver.title)
time.sleep(5)

driver.get("https://www.instagram.com")
print(driver.title)
time.sleep(10)

driver.back()
time.sleep(5)
driver.forward()

time.sleep(5)
driver.quit()