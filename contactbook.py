
print('Welcome to Contact Book')
print('what would you want to do?')
print('1. Add contact')
print('2. View contact')
print('3. Delete contact')
print('4. Exit')

contacts = []
number = 0
while True:
    option = int(input('Enter your option: '))
    if option == 1:
        number += 1
        name = input('Enter name: ')
        phone = input('Enter phone number: ')
        contact = {
            'number': number,
            'name': name,
            'phone': phone
        }
        contacts.append(contact)
        print('Contact added successfully!')
    elif option == 2:
        print('Your contacts are:')
        for contact in contacts:
            print(contact)
    elif option == 3:
        numberToDelete = input('Enter the contact number to delete: ')
        for contact in contacts:
            if contact['number'] == int(numberToDelete):
                contacts.remove(contact)
                print('Contact deleted successfully!')
                break
        else:
            print('Contact not found!')
    elif option == 4:
        print('Exiting the program. Goodbye!')
        break
    else:
        print('Invalid option! Please try again.')
        
