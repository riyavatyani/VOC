def convert_temperature():
    try:
        temp = float(input("Enter the temperature value: "))
        unit = input("Enter the unit (F for Fahrenheit, C for Celsius): ").strip().upper()
        
        if unit == 'F':
            
            celsius = (temp - 32) * 5/9
            print(f"{temp}°F is {round(celsius, 2)}°C")
        elif unit == 'C':
            
            fahrenheit = (temp * 9/5) + 32
            print(f"{temp}°C is {round(fahrenheit, 2)}°F")
        else:
            print("Invalid unit. Use 'F' for Fahrenheit or 'C' for Celsius.")
    except ValueError:
        print("Invalid temperature value. Please enter a numeric value.")


convert_temperature()
