from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Edge(executable_path="../Driver/msedgedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

"""
    Working with frames
    - switch_to.frame(name)
    - switch_to.frame(id)
"""

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

# 1. Frame 1 - Top Left Frame
driver.switch_to.frame("packageListFrame")
# click on "org.openqa.selenium.chrome" this link
driver.find_element(By.LINK_TEXT,"org.openqa.selenium.chrome").click()

time.sleep(3)

# 2. Go Back to main page
driver.switch_to.default_content()

time.sleep(3)

# 3. Frame 2 - Bottom Left Frame
driver.switch_to.frame('packageFrame')
# click on "AbstractFindByBuilder" this link
driver.find_element(By.LINK_TEXT,"ChromeDriver").click()

time.sleep(3)

# 4. Go Back TO main page
driver.switch_to.default_content()

time.sleep(3)

# 5. Frame 3 - Right side Frame
driver.switch_to.frame("classFrame")
# click on "org.openqa.selenium.cli" this link
driver.find_element(By.LINK_TEXT,"ChromiumDriver").click()

time.sleep(3)

driver.close()
driver.quit()