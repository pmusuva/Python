print("Welcome this program that records a user's personal details")
print("Enter your personal details".center(45,'-'))
fname = input("First Name: ") #First Name
lname = input("Last Name: ") #Last Name
fullnames = fname + " " + lname #Aggregate full names
country = input("Country of Origin: ") #Enter Country
profession = input("Nature of Current Job: ") #Enter Job
email = input("Email Address: ") #Enter Email Address
phone = input("Phone Number: ") #Enter Phone Number
city = input("City of Residence: ") #Enter City
address = input("Mailing or Physical Address: ") #Enter Mailing 

#Output the report on screen
print()
print('Personal Details Report'.center(45,'-')) #center heading for 40 pixel width and fill with -
print(f"Name: {fullnames}")
print(f"Country: {country}")
print(f"Profession: {profession}")
print(f"Email: {email}" )
print(f"Phone: {phone}" )
print(f"City: {city}" )
print(f"Address: {address}" )

