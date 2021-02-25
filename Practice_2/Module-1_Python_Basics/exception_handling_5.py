# different ways to raise exception in python (Raise, assert(), try except finally)

# raise and assert
ItemsCart = 2
if ItemsCart != 2:
    raise Exception("Carts Count is not matching")
else:
    assert (ItemsCart == 2, "Carts Count matching")

# try except finally block
try:
    with open("log.txt", 'r') as r:
        print(r.read())
except Exception as e:
    print("File Not Found", e)
finally:
    print("try another way")
