# from selenium import webdriver
# import time
#
# driver = webdriver.Edge(executable_path="driver/msedgedriver.exe")
#
# driver.get("https://www.google.com")
# time.sleep(10)
# driver.quit()

# list1 = [1,2,3,4]
# list2 = [4,6,21,1]
list1 = input().split(' ')

list2 = input().split(' ')
mainlist = list1+list2

mainlist.sort()
print(mainlist)