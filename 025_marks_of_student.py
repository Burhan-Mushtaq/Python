English = int(input("Enter the marks of English: "))
Urdu = int(input("Enter the marks of Urdu: "))
Math = int(input("Enter the marks of Math: "))

percentage = (English + Urdu + Math) / 300 * 100

if(percentage >= 40 ):
    print("You are Passed" , int(percentage),"%")
else:
    print("You are Failed", int(percentage),"%")


