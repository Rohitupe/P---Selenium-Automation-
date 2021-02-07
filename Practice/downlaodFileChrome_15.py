from selenium import webdriver
from selenium.webdriver.common.by import By
import time

""" Download file in location we want """
from selenium.webdriver.chrome.options import Options
chromeOptions = Options()
chromeOptions.add_experimental_option('prefs',{'download.default_directory':'C:\\Users\\rohit\\PycharmProjects\\Selenium_Automation\\Files&Folder\\Chrome_Download'}) # change default download path


driver = webdriver.Chrome(executable_path="../Driver/chromedriver.exe",options=chromeOptions)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://demo.automationtesting.in/FileDownload.html")

# Add some text to generate file
""" This Downloads File in default location """
# 1) Download text File
driver.find_element(By.ID,'textbox').send_keys("Downloading Text File With Chrome Browser")
time.sleep(1)
driver.find_element(By.ID,'createTxt').click()
time.sleep(1)
driver.find_element(By.ID,'link-to-download').click()

time.sleep(2)

# 2) Download Pdf File
driver.find_element(By.ID,'pdfbox').send_keys("Downloading PDF file with Chrome Browser")
time.sleep(1)
driver.find_element(By.ID,'createPdf').click()
time.sleep(1)
driver.find_element(By.ID,'pdf-link-to-download').click()


time.sleep(4)
driver.close()
driver.quit()

