from selenium import webdriver
import time

driver = webdriver.Edge(executable_path="../Driver/msedgedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.google.com")

""" There are two ways to capture screen in selenium """
filePath = r"C:\Users\rohit\PycharmProjects\Selenium_Automation\Screenshot"

# 1. first method
driver.save_screenshot(filePath+"\\takeScreenshot.png")

# 2. second method
driver.get_screenshot_as_file(filePath+"\\takeScreenshot.jpg")


time.sleep(3)
driver.close()
driver.quit()