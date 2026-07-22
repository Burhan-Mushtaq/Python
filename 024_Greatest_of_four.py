a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))
d = int(input("Enter 4th number : "))

if(a>b and a>c and a>d):
    print(f"{a} is greatest")
elif(b>a and b>c and b>d):
    print(f"{b} is greatest")
elif(c>a and c>b and c>d):
    print(f"{c} is greatest")
else:
    print(f"{d} is greatest")
    

    