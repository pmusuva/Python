# Introduction to Python 2021 Training
# Assignment 10 - Employee .csv file ingested into MySQL Employee Database Table
# Written by Paula Musuva
# Date: 20 May 2021

import os
import csv
import pandas as pd #!pip install pandas
from faker import Faker #!pip install Faker
import mysql.connector #!pip install mysql-connector-python
from getpass import getpass
from mysql.connector import connect, Error
 
# Create and initialize a Faker generator
fake = Faker()

# Specify how many records to generate
record_count = 100 

# Set filename
filename = 'Employee_Records.csv'

# Check if filename exists and records had been created before
if not (os.path.exists(filename)):
    # Generate 100 records with fake data and store them in Employee_Records.csv file
    with open(filename, 'w', newline= '') as csvfile:
        fieldnames = ['firstname', 'lastname', 'ssn', 'email', 'phone', 'address', 'city', 'state', 'zipcode', 'country']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for i in range(record_count):
            writer.writerow({
            'firstname': fake.first_name(),
            'lastname': fake.last_name(),
            'ssn': fake.ssn(),
            'email': fake.email(),
            'phone': fake.phone_number(),
            'address': fake.street_address(),
            'city': fake.city(),
            'state': fake.state(),
            'zipcode': fake.zipcode(),
            'country': fake.country()
    })
# End generation of records and storing in file

# Read generated records into pandas data frame to prepare import to database
empdata = pd.read_csv(filename, index_col=False, delimiter = ',')
print(empdata.head())

# Define various SQL statements for execution
create_db = "CREATE DATABASE IF NOT EXISTS assign10"
create_employees_table = """
    CREATE TABLE IF NOT EXISTS assign10.employee_records(
    id INT AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    ssn VARCHAR(20),
    email VARCHAR(100),
    phone VARCHAR(50),
    address VARCHAR(100),
    city VARCHAR(20),
    state VARCHAR(20),
    zipcode VARCHAR(10),
    country VARCHAR(50)
    )
"""
employees_table_schema = "DESCRIBE assign10.employee_records"

all_employee_records = "SELECT * FROM assign10.employee_records"

update_employee_record = """
    UPDATE assign10.employee_records 
    SET phone = "+1-165-650-7700766" 
    WHERE firstname = "Alejandro" AND lastname = "Hess"
"""

delete_employee_record = """
    DELETE FROM assign10.employee_records 
    WHERE firstname = "Crystal" AND lastname = "Salazar"
"""
# End SQL statement definitions

# Connect to Database using credentials provided by the user. We should never hard-code login credentials
print("Initializing MySQL database. Please key in the following")
try: #If successfull we get a MySQL connection object
    with connect(
        host = "localhost",
        user = input("username: "),
        password = getpass("password: "),
    ) as connection:
        #print(connection)
        with connection.cursor() as cursor:
            # Create assign10 database
            cursor.execute(create_db)
            print("Database has been created successfully")

            # Create employees table
            cursor.execute(create_employees_table)
            connection.commit() # Connection is not auto committed we must commit to save our changes
            print("Employees table has been created successfully with the following schema:")
            # Display schema
            cursor.execute(employees_table_schema)
            # Fetch rows from last executed query showing employees table schema
            result = cursor.fetchall()
            for row in result:
                print(row)
            
            # Import data from Employee_Records.csv into database
            print("Importing data from Employee_Records.csv into Employees table...")
            for i,row in empdata.iterrows():
                #%s means string values
                insert_record = "INSERT INTO assign10.employee_records(firstname,lastname,ssn,email,phone,address,city,state,zipcode,country) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" 
                cursor.execute(insert_record, tuple(row))
                connection.commit() # Commit to save our changes
            print("Records imported successfully")

            # Update specific record
            cursor.execute(update_employee_record)
            connection.commit() # Commit to save our changes
            print("Record updated successfully")

            # Delete specific records
            cursor.execute(delete_employee_record)
            connection.commit() # Commit to save our changes
            print("Record deleted successfully")

            # View all Employee records 
            cursor.execute(all_employee_records)
            result = cursor.fetchall()
            for row in result:
                print(row)
except Error as e:
    print("Error while connecting to MySQL", e)
# End database operations 