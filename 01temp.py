choice = int(input("Enter 0 to convert from Celsius to farenheit or 1 to convert from farenheit to celsius: "))
if choice == 0:
    celsius = float(input("Enter a temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F")
elif choice == 1:
    fahrenheit = float(input("Enter a temperature in Kelvin: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F")
else:
    print("Invalid choice. Please enter 0 or 1.")