from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="../../Driver/chromedriver.exe")

URL = "https://rahulshettyacademy.com/angularpractice"
driver.get(URL)

# if driver.current_url == URL:
#     print(driver.title)
# else:
#     driver.close()

# Xpath and Css Selectors --> study more on selectors

# """
#     Customized CSS syntax
#         - tagname[attribute = 'value'] --> Tagname Optional
#         Red Ex:- [attribute* = 'value']
# """

# """
#     Customized Xpath Syntax
#         - //tagname[@attribute = value] --> Tagname Optional
#         Reg Ex:- //*[contains(@attribute, 'value')]
# """

driver.find_element_by_link_text("Shop").click()

time.sleep(5)
driver.close()
driver.quit()
