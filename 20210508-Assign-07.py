import json
import os
import re
import csv
import pandas as pd

# Define Phonebook Column Headers
columns = [
    'First Name', 
    'Middle Name', 
    'Last Name',
    'Phone Number',
    'Email',
    'Mailing Address',
    'City',
    'Zip Code',
    'Country'
]

# Intialize Phonebook
def initPhonebook():
    if not (os.path.exists('phonebook.csv')):
        with open('phonebook.csv', 'w') as outcsv:
            writer = csv.DictWriter(outcsv, fieldnames = columns)
            writer.writeheader()
    else:
        pass
# End initPhonebook()
        
# Function to clear screen
def clearscreen():
    """This function uses the OS library to clear the screen"""
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
    # for windows platfrom
        _ = os.system('cls')
# End clearscreen()

# Function to display menu
def menu():
    """This function diplays menu options for user to choose"""
        #Get user input
    print('='.center(55,'='))
    print("Welcome to the Motorola Phonebook & Contacts Manager")
    print('='.center(55,'='))
    print(
        """
        What would you like to do?
        1. List all Contacts
        2. Add a Contact
        3. Remove a Contact
        4. Update a Contact 
        5. Lookup a Contact
        """
    )
    # Ask user to select option
    option = input("Type in a number (1-5): ")
    return option
# End menu()

# Function to List all Contacts in phonebook
def listContacts():
    """This function lists all contacts in the phonebook"""
    df=pd.read_csv('phonebook.csv',header=0)
    if df.empty:
        print("No Contacts in Phonebook")
    else:
        print(df)
# End listContacts()

# Function to add contact from user input
def addContact():
    """This function captures contact details and writes to file"""
    # Get user input for every key in the contact Dictionary 
    print("Please Enter Contact Details as follows:")
    fname = input("First Name: ") #First Name
    mname = input("Middle Name: ") #Middle Name
    lname = input("Last Name: ") #Second Name
    phone = input("Phone Number: ") #Enter Phone Number
    email = input("Email Address: ") #Enter Email Address
    mail = input("Physical Address: ") #Enter Physical Address
    city = input("City: ") #Enter City
    zipcode = input("Zipcode: ") #Enter Zipcode
    country = input("Country: ") #Enter Country
    userDetails = [[fname,mname,lname,phone,email,mail,city,zipcode,country]]

    with open('phonebook.csv','a', newline='') as outfile:
        writer = csv.writer(outfile) #Need to write the user input to the .csv file.
        writer.writerows(userDetails)
        print("Contact Added")
# End addContact()

# Function to add contact from user input
def deleteContact():
    """This function deletes a specified contact detail from phonebook file"""
    df=pd.read_csv('phonebook.csv',header=0)
    if df.empty:
        print("No Contacts in Phonebook")
    else:
        print("The following contacts exist")
        print(df)
        rowCount = len(df) #returns num of rows
        rowIndex = int(input("Which row number would you like to delete? "))
        if rowIndex <= rowCount:
            df = df.drop(df.index[rowIndex])
            print(df)
            df.to_csv('phonebook.csv',header=columns,index=False)
            print("Contact Deleted")
        else:
            pass
# End delContact()

# Function to add contact from user input
def updateContact():
    """This function updates a specified contact detail in phonebook file"""
    df = pd.read_csv('phonebook.csv',header=0)
    if df.empty:
        print("No Contacts in Phonebook")
    else:
        print("The following contacts exist")
        print(df)
        fname = input("Please input First Name of contact to update: ")
        newNumber = input("Key in the new phone number")
        df.loc[(df['First Name']== fname),'Phone Number' ] = newNumber
        print(df)
        df.to_csv('phonebook.csv',header=columns,index=False)
        print("Contact Updated")
# End updateContact()

# Function to Search for Contact from phonebook
def searchContact():
    """This function searches for a particular contact by first name"""
    fname = input("Please input First Name of contact to search: ") 
    df = pd.read_csv('phonebook.csv',header=0)
    if df.empty:
        print("No Contacts in Phonebook")
    else:
        print(df.loc[df['First Name'] == fname])
# End searchContact()

# START MAIN PROGRAM
# Initialize Phonebook
initPhonebook()
# Set program to loop
loop = True
while loop:
    # Display the menu and prompt user to select option
    option = menu()
    
    # 1. List Contacts
    if option == "1":
        listContacts()
    # 2. Add a Contact
    elif option == "2":
        addContact()
    # 3. Remove a Contact
    elif option == "3":
        deleteContact()
    # 4. Update a Contact 
    elif option == "4":
        updateContact()
    # 5. Lookup a Contact
    elif option == "5":
        searchContact()
    else:
        print("Please choose a correct value")
        continue
    
    # Ask if user would like to run program again
    runAgain = input("Would you like to run program again?[y/n]: ")
    if runAgain.lower()=='n':
        loop = False
    else:
        loop = True
        clearscreen()
# END MAIN PROGRAM