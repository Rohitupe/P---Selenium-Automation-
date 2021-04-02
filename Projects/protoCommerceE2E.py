from selenium import webdriver
import time
from selenium.webdriver.common.by import By # another way to select an element
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Edge(executable_path="../Driver/msedgedriver.exe")

driver.get("https://www.rahulshettyacademy.com/angularpractice/")

driver.find_element_by_css_selector("a[href*='shop']").click()

all_cards = driver.find_elements_by_xpath("//div[@class='card h-100']")

# //div[@class='card h-100']/div/h4/a
for card in all_cards:
    product_name = card.find_element_by_xpath("div[1]/h4/a").text
    if product_name == "Blackberry":
        card.find_element_by_xpath("div[2]/button").click()

    else:
        assert "No product Found"

# click on checkout
driver.find_element_by_xpath("//div[@id='navbarResponsive']/ul/li/a").click()
driver.find_element_by_css_selector("button[class='btn btn-success']").click()

# enter city
driver.find_element_by_css_selector("input[id='country']").send_keys("in")

# explicit wait
wait = WebDriverWait(driver,10)

element = wait.until(ec.visibility_of_element_located((By.LINK_TEXT, 'India')))
element.click()

# click on purchase
driver.find_element_by_css_selector("input[type='submit']").click()

print(driver.find_element_by_class_name("alert-success").text)

time.sleep(4)
driver.close()
driver.quit()