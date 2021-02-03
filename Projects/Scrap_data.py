from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

MAX_PAGE = 5

driver = webdriver.Edge(executable_path="../Driver/msedgedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

# go to Url
driver.get("https://www.freelancer.in/jobs/")

driver.find_element(By.ID,'keyword-input').send_keys("web devepment")
driver.find_element(By.ID,'search-submit').click()

time.sleep(3)

# Select Number of Results
dropdown = Select(driver.find_element(By.ID,'table-row-count-select'))
dropdown.select_by_value('100')

time.sleep(3)

# Scrap data
tag_name = "Python"
elements = driver.find_elements(By.CLASS_NAME, 'JobSearchCard-primary-tagsLink')
count=0
# print(len(elements))

for _ in range(1, MAX_PAGE+1):
    for tag in driver.find_elements(By.CLASS_NAME, 'JobSearchCard-primary-tagsLink'):
        try:
            if tag.text == tag_name:
                print("-"+tag.text+"-")
                count+=1
        except:
            continue
    driver.find_element_by_xpath('/html/body/div[2]/main/section/div[3]/div/div[2]/div[1]/div[1]/div[4]/ul/li[6]').click()
    time.sleep(1)

print(count)

# time.sleep(3)

# driver.close()
# driver.quit()