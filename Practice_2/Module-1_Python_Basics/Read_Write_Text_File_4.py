# read and write text files with python

file_path = r"C:\Users\rohit\PycharmProjects\Selenium_Automation\Practice_2\Udemy_Selenium_Python_Course.txt"

# reading File
with open(file_path, 'r') as r:
    reading = r.read()
    print(reading)

# Writing File - will overwrite this
with open(file_path, 'w') as w:
    w.write("** Learn Python Programming & Selenium Python Automation from Basics to Advanced level + 5 LIVE Project")

# append data in file - will not going to overwrite this
with open(file_path, 'a') as a:
    a.write("Hello World")
