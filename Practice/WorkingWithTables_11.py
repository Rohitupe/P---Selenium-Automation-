from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge(executable_path="../Driver/msedgedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

"""
    Working With Web Tables
"""

driver.get('https://www.lambdatest.com/pricing')

# Get Table len(rows) and len(columns)
"""Rows"""
# rows_head = driver.find_elements(By.XPATH,'//*[@id="FullCompare"]/table/thead/tr')
rows_body = driver.find_elements(By.XPATH,'//*[@id="FullCompare"]/table/tbody/tr')
# print(len(rows_head))
print(len(rows_body))

# total_rows = rows_head + rows_body
"""Columns"""
columns_head = driver.find_elements(By.XPATH,'//*[@id="FullCompare"]/table/thead/tr/th')
# columns_body = driver.find_elements(By.XPATH,'//*[@id="FullCompare"]/table/tbody/tr/td')
print(len(columns_head))

# get complete table values

print("FEATURES"+'\t'+"FEATURES"+'\t'+"LIVE"+'\t'+"WEB AUTOMATION"+'\t'+"MOBILE + WEB AUTOMATION")
for r in range(1,len(rows_body)+1):
    for c in range(1,len(columns_head)+1):
        value = driver.find_element(By.XPATH,f'//*[@id="FullCompare"]/table/tbody/tr[{r}]/td[{c}]').text
        print(value,end="\t")
    print()
driver.close()
driver.quit()