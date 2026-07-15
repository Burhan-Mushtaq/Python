value = float(input("Enter the value in Celsius to get its Fahrenheit value: "))

def celsius(Celsius):    
    Fahrenheit = (Celsius * 1.8) + 32
    print(f"{Celsius}°C is equal to {Fahrenheit}°F")

celsius(value)