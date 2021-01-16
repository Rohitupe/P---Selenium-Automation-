from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge(executable_path="../Driver/msedgedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

"""
    Working with alerts
    - switch_to_alert().accept()
    - switch_to_alert().dismiss()
"""

driver.get("http://testautomationpractice.blogspot.com/")

#  click on click me button
driver.find_element(By.XPATH,'//*[@id="HTML9"]/div[1]/button').click()

time.sleep(5)

# driver.switch_to_alert().accept() # click on ok button on alert window message

driver.switch_to.alert.dismiss() # click on cancel button on alert window message

driver.close()
driver.quit()