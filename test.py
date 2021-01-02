from selenium import webdriver
import time

driver = webdriver.Edge(executable_path="driver/msedgedriver.exe")

driver.get("https://www.google.com")
time.sleep(10)
driver.quit()