from selenium import webdriver
from selenium.webdriver.common.by import By
import time

""" Avoid Download Popup window to download file """
firefoxProfile = webdriver.FirefoxProfile()
#  to disable download popup window
firefoxProfile.set_preference('browser.helperApps.neverAsk.saveToDisk','text/plain,application/pdf') # Mine Type
firefoxProfile.set_preference('browser.download.manager.showWhenStarting',False)

# Location on where to download these files
firefoxProfile.set_preference('browser.download.dir','C:\\Users\\rohit\\PycharmProjects\\Selenium_Automation\\Files&Folder\\Firefox_Download')
firefoxProfile.set_preference('browser.download.folderList',2)
firefoxProfile.set_preference('pdfjs.disabled',True)

""" Change download file path in Firefox and other attributes """
driver = webdriver.Firefox(executable_path="../Driver/geckodriver.exe",firefox_profile=firefoxProfile)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://demo.automationtesting.in/FileDownload.html")

# Add some text to generate file
""" This Downloads File in default location """
# 1) Download text File
driver.find_element(By.ID,'textbox').send_keys("Downloading Text File With FireFox Browser")
time.sleep(1)
driver.find_element(By.ID,'createTxt').click()
time.sleep(1)
driver.find_element(By.ID,'link-to-download').click()

time.sleep(2)

# 2) Download Pdf File
driver.find_element(By.ID,'pdfbox').send_keys("Downloading PDF file with FireFox Browser")
time.sleep(1)
driver.find_element(By.ID,'createPdf').click()
time.sleep(1)
driver.find_element(By.ID,'pdf-link-to-download').click()


time.sleep(4)
driver.close()
driver.quit()