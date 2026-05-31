def temperatureConvertor():
    print("Welcome to the Temperature Convertor!")
    print("Please select the conversion you would like to perform:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Kelvin to Celsius")
    print("4. Celsius to Kelvin")
    print("5. Kelvin to Fahrenheit")
    print("6. Fahrenheit to Kelvin")
    print("7. Exit")

    while True:
        choice = input("Enter your choice (1 or 2 or 3 or 4 or 5 or 6 or 7): ")

        if choice == '1':
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C is equal to {fahrenheit}°F")

        elif choice == '2':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit}°F is equal to {celsius}°C")

        elif choice == '3':
            kelvin = float(input("Enter temperature in Kelvin: "))
            celsius = kelvin - 273.15
            print(f"{kelvin}K is equal to {celsius}°C")

        elif choice == '4':
            celsius = float(input("Enter temperature in Celsius: "))
            kelvin = celsius + 273.15
            print(f"{celsius}°C is equal to {kelvin}K")

        elif choice == '5':
            kelvin = float(input("Enter temperature in Kelvin: "))
            fahrenheit = (kelvin - 273.15) * 9/5 + 32
            print(f"{kelvin}K is equal to {fahrenheit}°F")

        elif choice == '6':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            kelvin = (fahrenheit - 32) * 5/9 + 273.15
            print(f"{fahrenheit}°F is equal to {kelvin}K")

        elif choice == '7':
            print("Thank you for using the Temperature Convertor!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
            continue

temperatureConvertor()