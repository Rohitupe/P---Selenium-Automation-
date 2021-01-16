from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge(executable_path="../Driver/msedgedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

"""
    Working with Browser Window
    - driver.current_window_handle
    - driver.window_handles
"""

driver.get("http://demo.automationtesting.in/Windows.html")
driver.find_element(By.XPATH,'//*[@id="Tabbed"]/a/button').click()

# To get value of single window or parent window which is open
print("Parent Window Value :- "+driver.current_window_handle)
# Parent Window handle value = CDwindow-835AA03BBA89425728AADC6F1340F946

# To get value of all open or running window
print("Driver Windows Values :- ",driver.window_handles)
# All Windows values - ['CDwindow-4FA08EC48E7D953D32295B8A1DCE57CD', 'CDwindow-5682371677D75E22D78F568C2E0E7DEA']

""" Perform Switching between different window with the help of values 2 ways to this """
windows = driver.window_handles
for win in windows:
    driver.switch_to.window(win)
    print(driver.title)
    time.sleep(3)
# OR
driver.switch_to.window(windows[1])

time.sleep(3)

driver.close()
driver.quit()