from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="../../Driver/chromedriver.exe")

URL = "https://rahulshettyacademy.com/#/index"
driver.get(URL)

if driver.current_url == URL:
    print(driver.title)

time.sleep(5)
driver.close()
driver.quit()
