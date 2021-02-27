from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="../../Driver/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

URL = "https://rahulshettyacademy.com/dropdownsPractise/"
driver.get(URL)

input_box = driver.find_element_by_id("autosuggest").send_keys("Ind")
time.sleep(3)

countriesName = driver.find_elements_by_css_selector("a[class='ui-corner-all']")

for country in countriesName:
    if country.text == "India":
        country.click()
        break

# to check whether our code works as expected or not
assert driver.find_element_by_id("autosuggest").get_property('value') == "India"

time.sleep(5)
driver.close()
driver.quit()
