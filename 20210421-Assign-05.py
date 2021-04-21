import os

#Conversion Functions
def toFahrenheit():
    """This function converts input in Celsius to Fahrenheit"""
    celsius = float(input("Enter Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"Conversion: {fahrenheit} Fahrenheit")
    print('='.center(50,'='))
def toCelsius():
    """This function converts input in Fahrenheit to Celsius"""
    fahrenheit = float(input("Enter Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"Conversion: {celsius} Celsius")
    print('='.center(50,'='))
def toMiles():
    """This function converts input in Kilometers to Miles"""
    kilometers = float(input("Enter Kilometers: "))
    miles = kilometers / 1.6
    print(f"Conversion: {miles} Miles")
    print('='.center(50,'='))
def toKilometers():
    """This function converts input in Miles to Kilometers"""
    miles = float(input("Enter Miles: "))
    kilometers = miles * 1.6
    print(f"Conversion: {kilometers} Kilometers")
    print('='.center(50,'='))
def toInches():
    """This function converts input in Centimeters to Inches"""
    centimeters = float(input("Enter Centimeters: "))
    inches = centimeters / 2.54
    print(f"Conversion: {inches} Inches")
    print('='.center(50,'='))
def toCentimeters():
    """This function converts input in Inches to Centimeters"""
    inches = float(input("Enter Inches: "))
    centimeters = inches * 2.54
    print(f"Conversion: {centimeters} Centimeters")
    print('='.center(50,'='))
def clearscreen():
    """This function uses the OS library to clear the screen"""
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
    # for windows platfrom
        _ = os.system('cls')

#set program to loop
loop = True

while loop:
    #Start Program Interaction
    print('Welcome to this Metric and SI Unit Conversion program'.center(70,'='))
    print("Options:")
    print("[C] Convert from Celsius")
    print("[F] Convert from Fahrenheit")
    print("[M] Convert from Miles")
    print("[KM] Convert from Kilometers")
    print("[IN] Convert from Inches")
    print("[CM] Convert from Centimeters")
    print("[Q] Quit")
    option=input("Input Option: ")

    if option.lower() == 'c':
        toFahrenheit()
    elif option.lower() == 'f':
        toCelsius()
    elif option.lower() == 'm':
        toKilometers()
    elif option.lower() == 'km':
        toMiles()
    elif option.lower() == 'in':
        toCentimeters()
    elif option.lower() == 'cm':
        toInches()
    elif option.lower() == 'q':
        loop = False
        break
    else:
        print("Please select correct option")
    
    #ask if user would like to run program again
    runAgain = input("Would you like to run program again?[y/n]: ")
    if runAgain.lower()=='n':
        loop = False
    else:
        loop = True
        clearscreen()

print('Thank you for using the program'.center(60,'-'))
