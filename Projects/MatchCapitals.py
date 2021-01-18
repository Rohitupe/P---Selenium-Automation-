# Match Capitals
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Edge(executable_path="../Driver/msedgedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

time.sleep(2)

# get all element
capitals_id = ["box1","box2","box3","box4","box5","box6","box7"]
country_id = ["box101","box102","box103","box104","box105","box106","box107"]

actions = ActionChains(driver)

# 1st Method
for run in range(len(country_id)):
    source = driver.find_element(By.ID, capitals_id[run])
    target = driver.find_element(By.ID,country_id[run])
    actions.drag_and_drop(source,target).perform()

# # 2nd Method
# for run in range(1,8):
#     source = driver.find_element(By.ID, f"box{run}")
#     target = driver.find_element(By.ID,f"box10{run}")
#     actions.drag_and_drop(source,target).perform()

driver.save_screenshot("../Screenshot/matchCapital.png")

time.sleep(3)
driver.close()
driver.quit()
