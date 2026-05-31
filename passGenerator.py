from random import choice
def generate_password():
    print("Welcome to the password generator!")
    print("Please select the type of password you want to generate:")
    print("1. Numeric password (numbers only)")
    print("2. Alphabetic password (letters only)")
    print("3. Alphanumeric password (letters and numbers)")
    print("4. Alphanumeric password with special characters (letters, numbers, and symbols)")
    print("5. Exit")
    userChoice = int(input("Enter your choice (1-5): "))
    print("Enter the length of the password 4/8?:")
    passLength = int(input())
    if passLength not in (4, 8):
        print("Invalid password length. Please enter a  4 or 8.")
        return
    numeric = "0123456789"
    alphabetic = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphanumeric = alphabetic + numeric
    special_characters = "!@#$%^&*()-+"
    if userChoice == 1:
        password = ''
        for _ in range(passLength):
                password += choice(numeric)
                
        print("Generated password:", password)
    elif userChoice == 2:
        password = ''
        for _ in range(passLength):
                password += choice(alphabetic)
                
        print("Generated password:", password)  
    elif userChoice == 3:
        password = ''
        for _ in range(passLength):
                password += choice(alphanumeric)
                
        print("Generated password:", password)
    elif userChoice == 4:
        password = ''
        for _ in range(passLength):
                password += choice(alphanumeric + special_characters)
        print("Generated password:", password)
    elif userChoice == 5:
        print("Exiting the password generator. Goodbye!")
        return
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
        return
    print ('Do you want to generate another password? (yes/no)')
    user_input = input().lower()
    if user_input == 'yes':
        generate_password()
    else:
        print("Exiting the password generator. Goodbye!")
        
generate_password()