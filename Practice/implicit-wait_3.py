from selenium import webdriver
import time
driver = webdriver.Edge(executable_path="../driver/msedgedriver.exe")

driver.implicitly_wait(10)  # will wait for complete page to load
driver.get("https://www.amazon.in")

time.sleep(10)
driver.quit()