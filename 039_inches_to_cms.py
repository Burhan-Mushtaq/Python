def inch_to_cms(inch):
    return inch * 2.54

inch = int(input("Enter value in Inches: "))
cms = inch_to_cms(inch)

print(f"{inch} Inches is equal to {cms} Centimeters")