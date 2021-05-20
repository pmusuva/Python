# Introduction to Python 2021 Training
# Assignment 9 - Kenya Power and Lighting Company (KPLC) Billing
# Written by Paula Musuva
# Date: 20 May 2021

import json
import os
import re
import csv
import pandas as pd
import mysql.connector #!pip install mysql-connector-python
from getpass import getpass
from mysql.connector import connect, Error

# Define Billing Column Headers
columns = [
    'First Name', 
    'Last Name',
    'Phone Number',
    'Email',
    'Billing Type',
    'Billing Address',
    'City',
    'Zip Code',
    'Country',
    'Consumption',
    'Total Bill'
]

billing_file = 'billing.txt'

# Intialize Billing File
def initBillingFile():
    if not (os.path.exists(billing_file)):
        with open(billing_file, 'w') as outcsv:
            writer = csv.DictWriter(outcsv, fieldnames = columns)
            writer.writeheader()
    else:
        pass
# End initBillingFile()

# Define various SQL statements for execution
create_db = "CREATE DATABASE IF NOT EXISTS assign9"
create_customers_table = """
    CREATE TABLE IF NOT EXISTS assign9.customers(
    id INT AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    phone VARCHAR(50),
    email VARCHAR(100),
    area VARCHAR(2),
    type VARCHAR(2),
    address VARCHAR(100),
    city VARCHAR(20),
    zipcode VARCHAR(10),
    country VARCHAR(50),
    consumption INT,
    bill FLOAT
    )
"""
all_customer_records = "SELECT * FROM assign9.customers"

# Intialize Billing Database and Customertble 
def initBillingDatabase():
    print("Initializing MySQL database. Please key in the following")
    try: #If successfull we get a MySQL connection object
        with connect(
            host = "localhost",
            user = input("username: "),
            password = getpass("password: "),
        ) as connection:
            #print(connection)
            with connection.cursor() as cursor:
                # Create assign9 database
                cursor.execute(create_db)
                print("Database has been created successfully")

                # Create customers table
                cursor.execute(create_customers_table)
                connection.commit() # Connection is not auto committed we must commit to save our changes
                print("Customers table has been created successfully")
    except Error as e:
        print("Error while connecting to MySQL", e)
# End initBillingDatabase()

def calculateBill(units, billingArea, billingType):
    """This function calculates customer bill based on specified parameters"""
    bill = -1 #Default bill if returned we have an error
    flatrate = 30 #Default billing rate
    discount = 1.00 #Default discount is no discount
    citytax = 1.04
    rural_residential = 10.00
    urban_residential = 15.00
    rural_light_industrial = 20.00
    urban_light_industrial = 23.00
    rural_heavy_industrial = 27.00
    urban_heavy_industrial = 30.00
    vat_industrial_urban = 1.18
    vat_industrial_rural = 1.15
    vat_residential = 1.10

    if (billingArea.upper() == 'R'): #Rural
        if (200 <= units <= 450):
            discount = 0.97
            if (billingType.upper() == 'R'): #Residential
                bill = units * rural_residential * vat_residential * citytax * discount
            elif (billingType.upper() == 'L'): #Light Industrial
                bill = units * rural_light_industrial * vat_industrial_rural * citytax * discount
            elif (billingType.upper() == 'H'): #Heavy Industrial
                bill = units * rural_heavy_industrial * vat_industrial_rural * citytax * discount
        elif (451 <= units <= 500):
            discount = 0.95
            if (billingType.upper() == 'R'): #Residential
                bill = units * rural_residential * vat_residential * citytax * discount
            elif (billingType.upper() == 'L'): #Light Industrial
                bill = units * rural_light_industrial * vat_industrial_rural * citytax * discount
            elif (billingType.upper() == 'H'): #Heavy Industrial
                bill = units * rural_heavy_industrial * vat_industrial_rural * citytax * discount
        elif (501 <= units <= 601):
            discount = 0.93
            if (billingType.upper() == 'R'): #Residential
                bill = units * rural_residential * vat_residential * citytax * discount
            elif (billingType.upper() == 'L'): #Light Industrial
                bill = units * rural_light_industrial * vat_industrial_rural * citytax * discount
            elif (billingType.upper() == 'H'): #Heavy Industrial
                bill = units * rural_heavy_industrial * vat_industrial_rural * citytax * discount
        elif (602 <= units <= 701):
            discount = 0.91
            if (billingType.upper() == 'R'): #Residential
                bill = units * rural_residential * vat_residential * citytax * discount
            elif (billingType.upper() == 'L'): #Light Industrial
                bill = units * rural_light_industrial * vat_industrial_rural * citytax * discount
            elif (billingType.upper() == 'H'): #Heavy Industrial
                bill = units * rural_heavy_industrial * vat_industrial_rural * citytax * discount
        elif (702 <= units <= 801):
            discount = 0.89
            if (billingType.upper() == 'R'): #Residential
                bill = units * rural_residential * vat_residential * citytax * discount
            elif (billingType.upper() == 'L'): #Light Industrial
                bill = units * rural_light_industrial * vat_industrial_rural * citytax * discount
            elif (billingType.upper() == 'H'): #Heavy Industrial
                bill = units * rural_heavy_industrial * vat_industrial_rural * citytax * discount
        elif (units >= 802):
            discount = 0.88
            if (billingType.upper() == 'R'): #Residential
                bill = units * rural_residential * vat_residential * citytax * discount
            elif (billingType.upper() == 'L'): #Light Industrial
                bill = units * rural_light_industrial * vat_industrial_rural * citytax * discount
            elif (billingType.upper() == 'H'): #Heavy Industrial
                bill = units * rural_heavy_industrial * vat_industrial_rural * citytax * discount
    elif (billingArea.toupper() == 'U'): #Urban
        if (200 <= units <= 450):
            discount = 0.97
            if (billingType.upper() == 'R'): #Residential
                bill = units * urban_residential * vat_residential * citytax * discount
            elif (billingType.upper() == 'L'): #Light Industrial
                bill = units * urban_light_industrial * vat_industrial_urban * citytax * discount
            elif (billingType.upper() == 'H'): #Heavy Industrial
                bill = units * urban_heavy_industrial * vat_industrial_urban * citytax * discount
            else:
                bill = units * flatrate * vat_residential * citytax * discount
        elif (451 <= units <= 500):
            discount = 0.95
            if (billingType.upper() == 'R'): #Residential
                bill = units * urban_residential * vat_residential * citytax * discount
            elif (billingType.upper() == 'L'): #Light Industrial
                bill = units * urban_light_industrial * vat_industrial_urban * citytax * discount
            elif (billingType.upper() == 'H'): #Heavy Industrial
                bill = units * urban_heavy_industrial * vat_industrial_urban * citytax * discount
            else:
                bill = units * flatrate * vat_residential * citytax * discount
        elif (501 <= units <= 601):
            discount = 0.93
            if (billingType.upper() == 'R'): #Residential
                bill = units * urban_residential * vat_residential * citytax * discount
            elif (billingType.upper() == 'L'): #Light Industrial
                bill = units * urban_light_industrial * vat_industrial_urban * citytax * discount
            elif (billingType.upper() == 'H'): #Heavy Industrial
                bill = units * urban_heavy_industrial * vat_industrial_urban * citytax * discount
        elif (602 <= units <= 701):
            discount = 0.91
            if (billingType.upper() == 'R'): #Residential
                bill = units * urban_residential * vat_residential * citytax * discount
            elif (billingType.upper() == 'L'): #Light Industrial
                bill = units * urban_light_industrial * vat_industrial_urban * citytax * discount
            elif (billingType.upper() == 'H'): #Heavy Industrial
                bill = units * urban_heavy_industrial * vat_industrial_urban * citytax * discount
        elif (702 <= units <= 801):
            discount = 0.89
            if (billingType.upper() == 'R'): #Residential
                bill = units * urban_residential * vat_residential * citytax * discount
            elif (billingType.upper() == 'L'): #Light Industrial
                bill = units * urban_light_industrial * vat_industrial_urban * citytax * discount
            elif (billingType.upper() == 'H'): #Heavy Industrial
                bill = units * urban_heavy_industrial * vat_industrial_urban * citytax * discount
        elif (units >= 802):
            discount = 0.88
            if (billingType.upper() == 'R'): #Residential
                bill = units * urban_residential * vat_residential * citytax * discount
            elif (billingType.upper() == 'L'): #Light Industrial
                bill = units * urban_light_industrial * vat_industrial_urban * citytax * discount
            elif (billingType.upper() == 'H'): #Heavy Industrial
                bill = units * urban_heavy_industrial * vat_industrial_urban * citytax * discount
    else: # Default bill calculation
        bill = units * flatrate * vat_industrial_urban * citytax * discount

    print(f"The total bill = {bill}")
    return bill
# End calculateBill()
        
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
    print("Welcome to the KPLC Billing App")
    print('='.center(55,'='))
    print(
        """
        What would you like to do?
        1. Add a Customer
        2. Generate a Customer Bill 
        3. Delete a Customer
        """
    )
    # Ask user to select option
    option = input("Type in a number (1-4): ")
    return option
# End menu()

# Function to add Customer from user input
def addCustomer():
    """This function captures contact details and writes to file"""
    # Get user input for every key in the contact Dictionary 
    print("Please Enter Customer Details as follows:")
    fname = input("First Name: ") #First Name
    lname = input("Last Name: ") #Last Name
    phone = input("Phone Number: ") #Enter Phone Number
    email = input("Email: ") #Enter Email Address
    billingArea = input("Input R for Rural or U for Urban (R|U): ") #Enter Billing Area
    billingType = input("Input R for Residential, L for Light Industrial or H for Heavy Industrial (R|L|H): ") #Enter Billing Type
    address = input("Billing Address: ") #Enter Billing Address
    city = input("City: ") #Enter City
    zipcode = input("Zipcode: ") #Enter Zipcode
    country = input("Country: ") #Enter Country
    consumption = float(input("Kilowatts Consumed: ")) #Enter Kilowatts Consumed
    bill = calculateBill(consumption, billingArea, billingType)
    userDetails = [[fname,lname,phone,email,billingArea,billingType,address,city,zipcode,country,consumption,bill]]

    # Write to file
    with open(billing_file,'a', newline='') as outfile:
        writer = csv.writer(outfile) #Need to write the user input to the billing file.
        writer.writerows(userDetails)
        print("Customer Added Successfully to Billing File")

    # Write to database
    print("Initializing MySQL database. Please key in the following")
    try: #If successfull we get a MySQL connection object
        with connect(
            host = "localhost",
            user = input("username: "),
            password = getpass("password: "),
        ) as connection:
            with connection.cursor() as cursor:
                # Insert Customer Record
                #insert_record = "INSERT INTO assign9.customers(firstname,lastname,phone,area,type,address,city,zipcode,country,consumption,bill) VALUES ({},{},{},{},{},{},{},{},{},{},{})".format(fname,lname,phone,billingArea,billingType,address,city,zipcode,country,consumption,bill)
                #cursor.execute(insert_record)
                #connection.commit() # Commit to save our changes
                print("Customer Added Successfully to Billing Database Table")
    except Error as e:
        print("Error while connecting to MySQL", e)
# End addContact()

def generateBill():
    """This function prints a specified customer's bill"""
    print("=================")
    print("Electricity Bill")
    print("=================")
    df = pd.read_csv(billing_file,header=0)
    if df.empty:
        print("No Customer Records")
    else:
        print("The following customers exist")
        print(df)
        rowCount = len(df) #returns num of rows
        rowIndex = int(input("Which row number would you like to generate bill for? "))
        if rowIndex <= rowCount:
            print(f"Full Names: {df.loc[rowIndex]['First Name']}") 

        else:
            print("Unable to Generate Bill")
# End getCustomerID()


# Function to delete Customer from user input
def deleteCustomer():
    """This function deletes a specified customer details from billing file"""
    df = pd.read_csv(billing_file,header=0)
    if df.empty:
        print("No Customer Records")
    else:
        print("The following customers exist")
        print(df)
        rowCount = len(df) #returns num of rows
        rowIndex = int(input("Which row number would you like to delete? "))
        if rowIndex <= rowCount:
            df = df.drop(df.index[rowIndex])
            print(df)
            df.to_csv(billing_file,header=columns,index=False)
            print("Customer Deleted")
        else:
            pass
# End deleteCustomer()


# START MAIN PROGRAM
# Initialize 
initBillingFile()
initBillingDatabase()
# Set program to loop
loop = True
while loop:
    # Display the menu and prompt user to select option
    option = menu()
    # 1. Add Customer
    if option == "1":
        addCustomer()
    # 2. Generate Bill
    elif option == "2":
        generateBill()
    # 3. Remove a Customer
    elif option == "3":
        deleteCustomer()
    else:
        print("Please choose a correct value")
        continue
    
    # Ask if user would like to run program again
    runAgain = input("Would you like to run program again?[y/n]: ")
    if (runAgain.lower()=='n'):
        loop = False
    else:
        loop = True
        clearscreen()
# END MAIN PROGRAM