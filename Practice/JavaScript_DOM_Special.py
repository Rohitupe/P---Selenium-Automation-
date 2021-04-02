# DOM can access any element on webpage just like selenium does
# Selenium have a method to execute javascript code in it

from selenium import webdriver
import time

driver = webdriver.Edge(executable_path="../Driver/msedgedriver.exe")
driver.implicitly_wait(10)

# Automate This Page
driver.get("https://rahulshettyacademy.com/angularpractice/")

# by Selenium
inputNAme = driver.find_element_by_xpath("//div[@class='form-group']/input[@name='name']")
inputNAme.send_keys("Hello Rohit")
time.sleep(3)
print(inputNAme.text)  # --> Not Working -> Here We can Use DOM
