from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import XLUtils_16 # all excel code is present

driver = webdriver.Edge(executable_path="../../../Driver/msedgedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://practice.automationtesting.in/my-account/")

# get login data from excel file
ExcelPath = r"C:\Users\rohit\PycharmProjects\Selenium_Automation\Practice\DataDrivenTesting-Excel_16\DataDrivenTest_16.3\DataDrivenTest_16.3.xlsx"

rows = XLUtils_16.getRowCount(ExcelPath,"Sheet1")
columns = XLUtils_16.getColumnCount(ExcelPath,"Sheet1")

print(rows,columns)

for r in range(2,rows+1):
        userName = XLUtils_16.readData(ExcelPath,"Sheet1",r,1)
        passWord = XLUtils_16.readData(ExcelPath,"Sheet1",r,2)
        print(f"{userName}=={passWord}")

        driver.find_element(By.ID,'username').send_keys(userName)
        driver.find_element(By.ID,'password').send_keys(passWord)
        driver.find_element(By.NAME,'login').click()

        try:
            loginDashboard = driver.find_element(By.XPATH,'//*[@id="page-36"]/div/div[1]/nav/ul/li[1]/a').is_displayed()
            if loginDashboard:
                print("Login Successful")
                XLUtils_16.writeData(ExcelPath,"Sheet1",r,3,"Test Passed")
                time.sleep(1)
                driver.find_element(By.XPATH,'//*[@id="page-36"]/div/div[1]/div/p[1]/a').click()
                time.sleep(1)
        except:
            print("Except : Login Failed")
            driver.find_element(By.ID, 'username').clear()
            XLUtils_16.writeData(ExcelPath, "Sheet1", r, 3, "Test Failed")

time.sleep(3)
driver.close()
driver.quit()