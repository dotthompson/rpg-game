# import pickle

def welcome():
    userInput = int(input(f"""
Electronic Phone Book
=====================
1. Look up an entry
2. Add an entry
3. Delete an entry
4. List all entries
5. Quit
>>>>      """))
    return userInput

def phonebook():
    contact = {}

    while True:
        userInput = welcome()

        if userInput == 1:
            name = input("Enter the name of the contact >>>  ")
            if name in contact:
                print("The contact is", name, ":", contact[name])
            else:
                print("That contact does not exist. Return to main menu to enter a contact.")
        elif userInput == 2:
            phone_number = input("Please enter a 10 digit phone number >>>")
            contact_name = input('Enter the contact name >>> Ex: "FirstName LastName".:')
            if phone_number not in contact.items():
                contact.update({contact_name: phone_number})
                print("Contact saved")
                print("Your updated phonebook is shown below:  ")
                for k, v in contact.items():
                    print(k, "-->", v)
            else:
                print("That contact already exists")
        elif userInput == 3:
            name = input("enter the name of the contact you want to delete: >> ")
            if name in contact:
                print("The ocntact is", name, ":", contact[name])

            else:
                print("That contact does not exist. Return to the maine menu to delete contact.")
            confirm = input("Are you sure you wish to delete this contact? Yes/No:  ")
            if confirm.capitalize() == "Yes" :
                contact.pop(name,None)
                for k, v in contact.items():
                    print("Your updated phonebook is shown below: ")
                    print(k, "-->", v)
            else:
                print("Return to main menu.")
        elif userInput == 4:
            if bool(contact) != False:
                for k, v in contact.items():
                    print(k, "-->", v)
            else:
                print("You have an empty phonebook! Go back to the menu to add a new contact.")
        elif userInput == 5:
            print("Goodbye")
            break
        else:
            print("Incorrect Entry")


phonebook()

with open('contact.pickle', 'wb') as filehandler:
    pickle.dump(contact, filhandler)
    


