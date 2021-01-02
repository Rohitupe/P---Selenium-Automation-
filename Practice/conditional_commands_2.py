from selenium import  webdriver
import time

driver = webdriver.Edge(executable_path="../driver/msedgedriver.exe")

# driver.maximize_window()

driver.get("https://form.jotform.com/203142708911449")

#  to check the login button is loaded or not
"""
    is_displayed()
    is_enabled()
    is_seleted()
     
     `returns True / False`
"""

X_PATH = '//*[@id="input_5"]'

dropdown = driver.find_element_by_xpath(X_PATH).is_displayed()
checkbox = driver.find_element_by_xpath('//*[@id="input_6_0"]')

checkbox.click()
confirm = checkbox.is_selected()

print(dropdown,confirm)

time.sleep(5)
driver.close()