from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge(executable_path="../Driver/msedgedriver.exe")

driver.implicitly_wait(10)

driver.get("https://www.amazon.in/")
driver.maximize_window()
# fnd all element by tag <a></a>
links = driver.find_elements(By.TAG_NAME,"a")

# print length of a element
print(len(links))

# print all links text
for i in links:
    print(i.text)

"""Click on Link with the help of Text"""
# click on the link
driver.find_element(By.LINK_TEXT,"Today's Deals").click()

# Customer Service - passing only partial text
driver.find_element(By.PARTIAL_LINK_TEXT,"Customer").click()

time.sleep(4)
driver.close()
driver.quit()
