from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge(executable_path="../Driver/msedgedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

"""
    Scrolling
    3 Ways to scroll page in selenium
    
    1. Scroll down page by pixel
    - driver.execute_script("window.scrollBy(0,500)","")
    
    2. Scroll down page till element found
    -  driver.execute_script("arguments[0].scrollIntoView();",Element)
    
    3. Scroll to end of the page
    - driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
"""

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
time.sleep(3)
# 1st scroll
driver.execute_script("window.scrollBy(0,1000)")

# 2nd scroll
element_India = driver.find_element(By.XPATH,'//*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img')
driver.execute_script("arguments[0].scrollIntoView();",element_India)

# 3rd scroll
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

time.sleep(3)
driver.close()
driver.quit()