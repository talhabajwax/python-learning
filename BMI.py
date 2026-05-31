def bmi (weight, height):
    print("Do you want to calculate your BMI? (yes/no)")
    answer = input()
    if answer.lower() == "yes":
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))
        bmi_value = weight / (height ** 2)
        print("Your BMI is: ", bmi_value)
        if bmi_value < 18.5:
            print("You are underweight.")
        elif 18.5 <= bmi_value < 24.9:
            print("You have a normal weight.")
        elif 25 <= bmi_value < 29.9:
            print("You are overweight.")
        else:
            print("You are obese.")
    else:       
        print("Okay, maybe next time!")
bmi()