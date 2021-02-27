from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="../../Driver/chromedriver.exe")

URL = "https://rahulshettyacademy.com/angularpractice"
driver.get(URL)

# select gender dropdown
dropdown = Select(driver.find_element_by_id('exampleFormControlSelect1'))
print(dropdown.select_by_visible_text('Female'))

time.sleep(3)
driver.close()
driver.quit()
