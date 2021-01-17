from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# For mouse action use package
from selenium.webdriver import ActionChains

driver = webdriver.Edge(executable_path="../Driver/msedgedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

"""
    - actions = ActionChains(driver)

    mouse Actions
    1. Mouse Hover
    - actions.move_to_element(admin).move_to_element(userManagement).move_to_element(user).click().perform()
    
    2. Double Click
    - actions.double_click(btn_dblClick).perform()
    
    3. Right Click
    - actions.context_click(right_click_btn).perform()
    
    4. Drag and Drop
    - actions.drag_and_drop(source_oslo,target_norway).perform()
"""

driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

user = "Admin"
password = "admin123"

# log in
driver.find_element(By.ID,'txtUsername').send_keys(user)
driver.find_element(By.ID,'txtPassword').send_keys(password)
time.sleep(3)
driver.find_element(By.ID,'btnLogin').click()

time.sleep(3)

# Perform Mouse Action
admin = driver.find_element(By.ID,'menu_admin_viewAdminModule')
userManagement = driver.find_element(By.ID,'menu_admin_UserManagement')
user = driver.find_element(By.ID,'menu_admin_viewSystemUsers')

""" Actions To Perform with Mouse """
actions = ActionChains(driver)

""" 1. Mouse Hover"""
# Hover and Click -perform() is necessary to perform click action
actions.move_to_element(admin).move_to_element(userManagement).move_to_element(user).click().perform()

time.sleep(3)

# logout
driver.find_element(By.ID,'welcome').click()
driver.find_element(By.XPATH,'//*[@id="welcome-menu"]/ul/li[2]/a').click()

""" 2. Double Click """
driver.get("http://testautomationpractice.blogspot.com/")
btn_dblClick = driver.find_element(By.XPATH,'//*[@id="HTML10"]/div[1]/button')

actions = ActionChains(driver)
actions.double_click(btn_dblClick).perform()

""" 3. Right Click """
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
right_click_btn = driver.find_element(By.XPATH,'/html/body/div/section/div/div/div/p/span')

actions = ActionChains(driver)
actions.context_click(right_click_btn).perform()

""" 4. Drag And Drop """
driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

source_oslo = driver.find_element(By.ID,'box1')
target_norway = driver.find_element(By.ID,'box101')

actions = ActionChains(driver)
actions.drag_and_drop(source_oslo,target_norway).perform()

time.sleep(3)
driver.close()
driver.quit()