from selenium import webdriver

# using select classs for dropdown menu
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Edge(executable_path="../Driver/msedgedriver.exe")

driver.implicitly_wait(10)

driver.get('https://www.amazon.in/')

# select = driver.find_element_by_name('url')
dropdown = Select(driver.find_element_by_name('url'))
""" Multiple ways to select dropdown option """
dropdown.select_by_visible_text('Deals')
dropdown.select_by_value('search-alias=baby')

# length of options
print(len(dropdown.options))

# to get all options which are there in dropdown box
for i in dropdown.options:
    print(i.text)

time.sleep(5)
# print(select)
driver.close()
driver.quit()