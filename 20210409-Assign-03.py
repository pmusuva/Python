#........ and shoot for the Sky in you getting a big promotion & opportunity

print("Welcome this program that determine's a customer's credit worthiness")
print("Enter the Customer's Details".center(45,'-'))
fname = input("First Name: ") #First Name
lname = input("Last Name: ") #Last Name
fullnames = fname + " " + lname #Aggregate full names
phone = input("Phone Number: ") #Enter Phone Number
email = input("Email Address: ") #Enter Email Address

#Set price of a used car
price = 10000

#Check credit and determine downpayment
has_good_credit = True
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

#Output the report on screen
print()
print('Credit Worthiness Report'.center(45,'-')) #center heading for 40 pixel width and fill with -
print(f"Full Names: {fullnames}")
print('Phone: {}-{}-{}'.format(phone[:3],phone[3:6],phone[6:]))
print(f"Email: {email}" )
print(f"Down Payment: {down_payment:.2f}")