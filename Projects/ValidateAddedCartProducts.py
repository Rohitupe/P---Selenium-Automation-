from selenium import webdriver
import time

# Explicit wait Code
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Edge(executable_path="../Driver/msedgedriver.exe")
driver.implicitly_wait(4)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

# search for product starts with "ber"
driver.find_element_by_css_selector("input[type='search']").send_keys("ber")

# get all div elements
allProducts = driver.find_elements_by_xpath("//div[@class='product']")

allProductsName = []  # storing products name in list

# same for loop for getting product name and clicking add to cart button
for product in allProducts:
    productsName = product.find_element_by_tag_name("h4").text
    allProductsName.append(productsName)
    product.find_element_by_xpath("div[@class='product-action']/button").click()

# go to cart page
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[contains(text(),'PROCEED TO CHECKOUT')]").click()

time.sleep(2)

cartPageURL = driver.current_url
print(cartPageURL)

# get name of the product from table
productsNameTable = driver.find_elements_by_xpath("//td/p[@class='product-name']")

for product in productsNameTable:
    if product.text in allProductsName:
        print("Product is present")
    else:
        print("Not Present")

# apply promocode
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()

# promoCode = driver.find_element_by_class_name("promoInfo").text

EC_wait = WebDriverWait(driver, 10)

element = EC_wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
print(element.text)

# check for applied discount
def apply_Discount():
    totalAmount = driver.find_element_by_class_name("totAmt").text
    discountPrice = driver.find_element_by_class_name("discountAmt").text

    calculateDiscount = int(totalAmount) - (int(totalAmount)/10)
    assert float(discountPrice) == float(calculateDiscount)


if "Code applied ..!" in element.text:
    apply_Discount()
    print("DisCount Applied Successfully")
else:
    print("Error")

time.sleep(3)
driver.close()
driver.quit()




