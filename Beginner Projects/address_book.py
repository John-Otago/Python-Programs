###################################################################################################
# This is a Python program for a simple command-line Address Book                                 #
#                                                                                                 #
# Version 1.0                                                                                     #
# Last update: 19 April 2022                                                                      #
# Python version = 3.9.7 | Also tested: Python 3.10.4                                             #
#                                                                                                 #
# Functions:                                                                                      #
# - Create an Address Book                                                                        #
# - Add contacts (name, email, phone) to the Address Book                                         #
# - Browse contacts                                                                               #
# - Search for a contact                                                                          #
# - Modify a contact                                                                              #
# - Delete a contact                                                                              #
#                                                                                                 #
# Limits & Possible Future Updates:                                                               #
# - No check for whether the email or the phone number is valid (function: add_contact)           #
# - Browse function will return all the contacts, rather than browsing one by one                 #
# - Some functions (search, modify, delete) only work when the Full Name of a contact is entered  #
# - Can only search by name, not by email or phone number                                         #
# - Code can be better (this program was written by a beginner)                                   #
# - DocStrings may need to be added                                                               #
###################################################################################################

###################################################################################################
# Note: this is a challenge set at the end of A Byte of Python, an excellent introductory book to #
# Python programming: https://github.com/swaroopch/byte-of-python (edition: 05 Jan 2022)          #
#                                                                                                 #
# Challenge:                                                                                      #
# Create your own command-line address-book program using which you can browse, add, modify,      #
# delete or search for your contacts such as friends, family and colleagues and their information #
# such as email address and/or phone number. Details must be stored for later retrieval.          #
#                                                                                                 #
# Hint:                                                                                           #
# Create a class to represent the person's information. Use a dictionary to store person objects  #
# with their name as the key. Use the pickle module to store the objects persistently on your     #
# hard disk. Use the dictionary built-in methods to add, delete and modify the persons.           #
#                                                                                                 #
# A possible solution to this challenge using Python2 can be found here:                          #
# https://github.com/akshar-raaj/Python-Programs/blob/master/address-book.py                      #
#                                                                                                 #
# You can find my solution below                                                                  #
###################################################################################################


import pickle

class Contacts:
    def __init__(self, n, e, p):
        self.n = n
        self.e = e
        self.p = p


# Add contact to Address Book
def add_contact():

    while True:
        addressbook = {}

        name = input("To add a new contact, please enter name, or enter 'c' to cancel: ")
        if name == "c":
            print("Canceled.")
            break
        else:
            pass

        email = input("Please enter email, or enter 'c' to cancel: ")
        if email == "c":
            print("Canceled.")
            break
        else:
            pass

        phone = input("Please enter phone number, or enter 'c' to cancel: ")
        if phone == "c":
            print("Canceled.")
            break
        else:
            pass

        new_contact = Contacts(name, email, phone)
        addressbook[new_contact.n] = {"email": new_contact.e, "phone": new_contact.p}

        with open("addressbook.data", "ab") as f:
            pickle.dump(addressbook, f)
            print("Contact added successfully")


# Browse the entries or print out by line
def browse_contact():

    with open("addressbook.data", "rb") as f:
        while True:
            command = input("Enter b to browse all contacts, or enter 'c' to cancel: ")
            if command == "b":
                while True:
                    try:
                        print(pickle.load(f))
                    except EOFError:
                        print("You have reached the end of the list!")
                        break
                continue
            elif command == "c":
                print("Canceled.")
                break
            else:
                print("Sorry, please enter the right command.")
                continue


# Search for an entry
def search_contact():

    with open("addressbook.data", "rb") as f:
        loaded_contacts = {}

        while True:
            try:
                loaded_contacts.update(pickle.load(f))
            except EOFError:
                break

    while True:
        search_name = input("Please enter a name, or enter 'c' to cancel: ")
        if search_name in loaded_contacts:
            print(search_name, loaded_contacts[search_name])
            continue
        elif search_name == "c":
            print("Canceled.")
            break
        else:
            print("Sorry, contact not found, or you may have entered the wrong command.")
            continue


# Delete a contact
def delete_contact():

    with open("addressbook.data", "rb") as f:
        loaded_contacts = {}

        while True:
            try:
                loaded_contacts.update(pickle.load(f))
            except EOFError:
                break

    while True:
        name = input("Enter the name of the contact that you want to delete, "
                     "or enter 'c' to cancel: ")
        if name in loaded_contacts:
            confirm = input("Enter y to confirm, or enter any other key to cancel: ")
            if confirm == "y":
                loaded_contacts.pop(name)
                print("Contact deleted successfully.")
                with open("addressbook.data", "wb") as f:
                    pickle.dump(loaded_contacts, f)
                    print("Address Book updated successfully")
            else:
                continue
        elif name == "c":
            print("Canceled.")
            break
        else:
            print("Sorry, contact not found, or you may have entered the wrong command.")
            continue


# Modify a contact
def modify_contact():

    with open("addressbook.data", "rb") as f:
        loaded_contacts = {}

        while True:
            try:
                loaded_contacts.update(pickle.load(f))
            except EOFError:
                break

    while True:
        name = input("Enter the name of the contact that you'd like to modify, "
                     "or enter 'c' to cancel: ")
        if name in loaded_contacts:
            command = input("Enter 'e' to enter a new email, "
                            "enter 'p' to enter a new phone number, "
                            "or enter 'c' to cancel: ")
            if command == "e":
                new_email = input("Enter a new email address: ")
                loaded_contacts[name] = {"email": new_email, "phone": loaded_contacts[name]["phone"]}
                print("Email updated successfully.")
                with open("addressbook.data", "wb") as f:
                    pickle.dump(loaded_contacts, f)
                    print("Address Book updated successfully")
            elif command == "p":
                new_phone = input("Enter a new phone number: ")
                loaded_contacts[name] = {"email": loaded_contacts[name]["email"], "phone": new_phone}
                print("Phone updated successfully.")
                with open("addressbook.data", "wb") as f:
                    pickle.dump(loaded_contacts, f)
                    print("Address Book updated successfully")
            elif command == "c":
                print("Canceled.")
                continue
            else:
                print("Sorry, please enter the right command.")
                continue
        elif name == "c":
            print("Canceled")
            break
        else:
            print("Sorry, contact not found, or you may have entered the wrong command.")
            continue


print("Enter 'a' to add a contact, "
      "'b' to browse contacts, "
      "'s' to search for contact, "
      "'d' to delete a contact, "
      "'m' to modify a contact, "
      "and 'q' to quit.")
while True:
    user_input = input("Enter your choice: ")
    if user_input == "q":
        print("Thank you for using Address Book.")
        break
    elif (user_input == "a"):
        add_contact()
    elif (user_input == "b"):
        browse_contact()
    elif (user_input == "s"):
        search_contact()
    elif (user_input == "d"):
        delete_contact()
    elif (user_input == "m"):
        modify_contact()
    else:
        print("Incorrect selection. Try again.")
