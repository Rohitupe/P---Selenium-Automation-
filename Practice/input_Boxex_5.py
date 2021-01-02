from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge(executable_path="../driver/msedgedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

# Open Url
driver.get("https://form.jotform.com/203332326958457")

# Get Total number of input boxes on a page
total_input_boxes = driver.find_elements_by_class_name('form-textbox')
# total_input_boxes = driver.find_elements_by_tag_name("input")
print(len(total_input_boxes))

# to send values use = send_keys("Hello") at the end

# Get the status of an input box - text box is displayed or not / text box is enabled or not
element_status = driver.find_element(By.ID,'cardinalOrderNumber').is_displayed()
print("Input Box Which hidden on a webpage:- Status : ",element_status)

message_status = driver.find_element(By.ID,'sublabel_9_last').is_enabled()
print("Last name message just below the input box:- Status : ",message_status)

time.sleep(5)
driver.quit()