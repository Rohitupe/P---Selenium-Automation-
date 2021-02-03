from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge(executable_path="../Driver/msedgedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

# Upload File
driver.get("https://cgi-lib.berkeley.edu/ex/fup.html")

time.sleep(3)

# upload file button - no need to click just specify file path
driver.find_element(By.NAME,"upfile").send_keys("C://Users//rohit//PycharmProjects//Selenium_Automation//Files&Folder//File.txt")