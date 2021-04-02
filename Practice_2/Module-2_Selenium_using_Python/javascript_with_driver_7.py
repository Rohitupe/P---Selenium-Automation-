from selenium import webdriver
import time

driver = webdriver.Edge(executable_path="../../Driver/msedgedriver.exe")

driver.get("https://www.rahulshettyacademy.com/angularpractice/")

driver.find_element_by_xpath("/html/body/app-root/form-comp/div/form/div[1]/input").send_keys("Hello")

# Executing javascript in selenium
js_script = driver.execute_script("return document.getElementsByName('name')[0].value")
print(js_script)

# clicking on a button or link with the help of javascript
shop_button = driver.find_element_by_css_selector("a[href*='shop']")
js_script_click = driver.execute_script("arguments[0].click();", shop_button)

# scrolling pages with javascript
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(4)
driver.close()
driver.quit()