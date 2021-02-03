from selenium import webdriver
from selenium.webdriver.common.by import By
import time

""" Download file in location you want by configuring default download path in - only works Chrome Browser """
# from selenium.webdriver.chrome.options import Options
#
# chromeOptions = Options()
# chromeOptions.add_experimental_option("prefs",{"download.default_directory":"c:\Desktop"})
#
# driver = webdriver.Chrome(executable_path="Chrome driver file path",chrome_options = chromeOptions)

# Driver code

driver = webdriver.Edge(executable_path="../Driver/msedgedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

# download file website
driver.get("http://demo.automationtesting.in/FileDownload.html")


""" Download TXT File """
driver.find_element(By.ID,'textbox').send_keys("Hello Rohit TEXT")
time.sleep(1)

driver.execute_script("window.scrollBy(0,250)")
time.sleep(1)

driver.find_element(By.ID,'createTxt').click()
time.sleep(2)

driver.find_element(By.ID,'link-to-download').click()


""" Download PDF File """
pdfTextBox = driver.find_element(By.ID,'pdfbox')
driver.find_element(By.ID,'pdfbox').send_keys("Hello Rohit PDF")
time.sleep(1)

driver.execute_script("arguments[0].scrollIntoView();",pdfTextBox)
time.sleep(1)

driver.find_element(By.ID,'createPdf').click()
time.sleep(2)

driver.find_element(By.ID,'pdf-link-to-download').click()

driver.close()
driver.quit()