print("Welcome to this program that determine's a customer's credit worthiness")
print("Enter the Customer's Details".center(45,'-'))
fname = input("First Owner Name: ") #First Owner Name
sname = input("Second Owner Name: ") #Second Owner Name
fullnames = fname + " & " + sname #Aggregate full names
phone = input("Phone Number: ") #Enter Phone Number
email = input("Email Address: ") #Enter Email Address
mail = input("Physical Address: ") #Enter Physical Address
city = input("City: ") #Enter City
zipcode = input("Zipcode: ") #Enter Zipcode
price = float(input("Price of New House: ")) #Enter New House Price
creditscore = int(input("Credit Score: ")) #Enter Credit Score

#Set variables
message = "Poor Credit Score"
downpayment = float(price)

#Check credit score and determine downpayment
if 780 <= creditscore <= 850:
    message = "Extend Credit\nZero Down Payment"
    downpayment = 0.0 * price
elif 740 <= creditscore <= 779:
    message = "Very Good"
    downpayment = 0.02 * price
elif 720 <= creditscore <= 739:
    message = "Above Average"
    downpayment = 0.03 * price
elif 680 <= creditscore <= 719:
    message = "Average"
    downpayment = 0.06 * price
elif 620 <= creditscore <= 679:
    message = "Below Average"
    downpayment = 0.18 * price
elif 580 <= creditscore <= 619:
    message = "Poor Credit Score"
    downpayment = 0.20 * price
elif 520 <= creditscore <= 579:
    message = "Poor Credit Score"
    downpayment = 0.22 * price
elif creditscore < 520:
    message = "Poor Credit Score"
    downpayment = 0.25 * price
else:
    message = "Review the Credit Score it should be a number between 300 and 850"
    downpayment = price

#Output the report on screen
print('='.center(80,'='))
print('Credit Worthiness Report'.center(80,'-')) #center heading for 40 pixel width and fill with -
print(f"Full Names: {fullnames}")
print('Phone: {0}-{1}-{2} Email: {3}'.format(phone[:4],phone[4:7],phone[7:],email))
print(f"Physical Address:{mail} City:{city} Zipcode:{zipcode}")
print()
print(f"New House Price: {price:,.2f}")
print(f"Down Payment: {downpayment:,.2f}")
print(f"Credit Score: {creditscore}")
print(f"Credit Status: {message}")
print()
print(f"CONGRATULATIONS - YOU NOW OWN YOUR DREAM HOME - {fullnames}")
print('='.center(80,'='))