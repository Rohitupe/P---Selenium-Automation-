from selenium import webdriver
import time
from selenium.webdriver.common.by import By # another way to select an element
from selenium.webdriver.support.ui import WebDriverWait

# webdriver wait is used to wait for a specifi element to load
# but for this we need t use an condition so we import one more module

from  selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Edge(executable_path="../driver/msedgedriver.exe")

driver.get("https://www.amazon.in")

driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]').send_keys("Iphones")
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="nav-search-submit-text"]/input').click()

# Implementing the explicit wait
wait = WebDriverWait(driver,10)

# This is the normal way will wait for 10 second to load element
# driver.find_element(By.XPATH,'//*[@id="p_90/6741118031"]/span/a/div/label/i').click()

#  This is advance way wil respond as soon as the element available
element = wait.until(ec.element_to_be_clickable((By.XPATH,'//*[@id="p_90/6741118031"]/span/a/div/label/i')))
element.click()