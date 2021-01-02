from selenium import webdriver
import time

driver = webdriver.Edge(executable_path="../driver/msedgedriver.exe")

driver.maximize_window()

driver.get("https://form.jotform.com/203142708911449")


X_PATH = '//*[@id="input_5"]'

check = driver.find_element_by_xpath(X_PATH).text
newcheck = check.split("\n")

newList = []

for i in newcheck:
    if i.strip():
        newList.append(i.strip())
    else:
        newcheck.remove(i)

print((newList))
time.sleep(5)
driver.close()