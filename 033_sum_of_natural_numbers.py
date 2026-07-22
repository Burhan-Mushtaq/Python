n = int(input("Enter the limit upto you have to calculate sum of natural numbers: "))

sum = 0
for i in range(1,n+1):
    sum = sum + i

print(sum)