import pytest

# "test" text must be the starting or ending text in pytest
def testOne():
    print("This is First Test")

def testTwo():
    print("This is Second Test")

"""
To run these text - in terminal Type => pytest -v -s --> -v(verbose), -s(will print print statements) 
        --> this command will run files in project folder to run specific test file 
        mention the name of that test file like ==> pytest -v- s test_demo.py 
"""