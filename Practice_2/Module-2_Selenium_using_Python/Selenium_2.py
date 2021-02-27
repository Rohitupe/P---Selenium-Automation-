from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="../../Driver/chromedriver.exe")

URL = "https://www.rahulshettyacademy.com/AutomationPractice/"
driver.get(URL)

if driver.current_url == URL:
    print(driver.title)

driver.get("https://www.google.com")

driver.back()
time.sleep(3)
driver.refresh()

time.sleep(5)
driver.close()
driver.quit()
