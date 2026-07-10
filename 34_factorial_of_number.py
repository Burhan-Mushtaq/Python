num = int(input("Enter the number to get it's factorial: "))

product = 1
for i in range (1,num+1):
    product = product * i 

print(product)