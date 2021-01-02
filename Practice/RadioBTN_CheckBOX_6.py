from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge(executable_path="../driver/msedgedriver.exe")
# driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://form.jotform.com/203334210042435")

text = driver.find_element_by_id("input_8_0")
print(text.text)
# text.click()

time.sleep(5)
print("Driver is going to Close")
# driver.quit()