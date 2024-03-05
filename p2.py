#4 swap two variables
x = input("enter the no:")
y = input("enter the no:")
temp = x
x = y
y = temp
print("x after swapping:{}".format(x))
print("y after swapping:{}".format(y))
 
# ----------
a = 12
b = 14
a = a + b # a = 26
b = a - b # b = 26-14 = 12
a = a - b # a = 26-12 = 14
print(a)
print(b)

# -----------
n1 = 5
n2 = 7
n1,n2 = n2,n1 #here the swapping is made
print("n1=",n1)
print("n2=",n2)