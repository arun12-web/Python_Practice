#factorial of a num 
num =int(input("eneter the no:"))
factorial = 1
while(num >0):
  factorial = factorial*num
  num = num-1
print("factorial is: ",factorial)

#mutliplication
i = int(input("enter the no:"))
for num in range(1,11):
  product = i*num
  print(i,"x",num, "=",product)