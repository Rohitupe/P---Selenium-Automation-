from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver  = webdriver.Edge(executable_path="../driver/msedgedriver.exe")

userSearch = input("Enter What you want to Search on Amazon?\n")

driver.get("https://www.amazon.in")

driver.implicitly_wait(10)

driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]').send_keys(userSearch)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="nav-search-submit-text"]/input').click()

# Explicit Condition

wait = WebDriverWait(driver,10)
element = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="p_90/6741118031"]/span/a/div/label/i')))
element.click()

time.sleep(4)
driver.quit()
