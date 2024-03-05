#ask user name and print back user name in reverse order 

name = input("your name:")
print(f"reverse ur name is {name[::-1]}")

name2 = input("your name:")
reverse = name2[-1::-1]
print("your reversal name is {}".format(reverse))