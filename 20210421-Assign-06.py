import os

# Function to get average of a list
def listAverage(lst):
    """This function returns the average of a list"""
    return sum(lst) / len(lst)

# Function to award Scholarship
def awardScholarship(isAfrica=False,gender='m',grade='0'):
    """This function checks eligibility for scholarship and returns boolean whether to award scholarship"""
    # Default no scholarship
    isScholarship = False

    # Only award to those from Africa. Females with 76% or higher. Males with 80% or higher 
    if isAfrica:
        if gender == 'f' and grade >= 0.76:
            isScholarship = True
        elif (gender == 'm') and grade >= 0.80:
            isScholarship = True
    
    #print(f"Award scholarship function isScholarship:{isScholarship}")
    #return decision
    return isScholarship
#end awardScholarship

# Function to clear screen
def clearscreen():
    """This function uses the OS library to clear the screen"""
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
    # for windows platfrom
        _ = os.system('cls')
#end clearscreen

# START MAIN PROGRAM
# Set program to loop
loop = True

while loop:
    #Start Program Interaction

    #Get user input
    print('='.center(82,'='))
    print("Welcome to this program that awards scholarships to a Python Programming Bootcamp")
    print('='.center(82,'='))
    print("Please Enter Student's Details as follows:")
    fname = input("First Name: ") #First Name
    lname = input("Last Name: ") #Second Name
    fullnames = fname + " " + lname #Aggregate full names
    sid = input("ID Number: ") #ID Number
    gender = input("Gender [Input F for Female | M for Male]: ") #Enter gender
    phone = input("Phone Number: ") #Enter Phone Number
    email = input("Email Address: ") #Enter Email Address
    mail = input("Physical Address: ") #Enter Physical Address
    city = input("City: ") #Enter City
    zipcode = input("Zipcode: ") #Enter Zipcode
    country = input("Country: ") #Enter Country
    region = input("Region[Input A for Africa | O for Other]: ") #Enter Region
    
    #Set number of tests to loop through
    numQuiz = 3
    numTest = 2
    numAssigns = 10
    numZoom = 3

    #Set eligibility for Africa students for scholarship
    isAfrica = False
    if region.lower() == 'a':
        isAfrica = True
    
    #Quiz Scores
    print("============")
    print("Quiz Scores")
    print("============")
    #listQuiz = [int(quiz) for quiz in input(f"Enter {numQuiz} quiz scores each out of 100% separated by a space: ").split()]
    listQuiz = []
    for i in range (1, numQuiz+1, 1):
        quiz = int(input(f"Quiz {i} marks [max 100]:")) #get marks per quiz
        listQuiz.append(quiz) #append to list
    print(f"Quiz scores: {listQuiz}")
            
    #Test Scores
    print("============")
    print("Test Scores")
    print("============")
    #listTest = [int(test) for test in input(f"Enter {numTest} test scores each out of 100% separated by a space: ").split()]
    listTest = []
    for i in range (1, numTest+1, 1):
        test = int(input(f"Test {i} marks [max 100]:")) #get marks per test
        listTest.append(test) #append to list
    print(f"Exam Test scores: {listTest}")
    
    #Assignment Scores
    print("==================")
    print("Assignment Scores")
    print("==================")
    #listAssigns = [int(assign) for assign in input(f"Enter {numAssigns} assignment scores each out of 10  separated by a space: ").split()]
    listAssigns = []
    for i in range (1, numAssigns+1, 1):
        assign = int(input(f"Assignment {i} marks [max 10]:")) #get marks per assignment
        listAssigns.append(assign) #append to list
    print(f"Assignment scores: {listAssigns}")
    
    #Zoom Calls
    print("=====================")
    print("Zoom Call Attendance")
    print("=====================")
    #listZoom = [int(zoom) for zoom in input(f"Enter {numZoom} zoom attendace each out of 3 separated by a space: ").split()]
    listZoom = []
    for i in range (1, numZoom+1, 1):
        zoom = int(input(f"Zoom {i} attendance [max 3]:")) #get marks per assignment
        listZoom.append(zoom) #append to list
    print(f"Zoom scores: {listZoom}")
    
    #Calculate overal grade assuming a weighting formula where 30% test, 30% quizzes, 20% assignments and 20% zoom
    avgQuiz = listAverage(listQuiz)
    avgTest = listAverage(listTest)
    avgAssigns = listAverage(listAssigns)
    sumZoom = sum(listZoom)
    grade = ((avgTest/100*0.3) + (avgQuiz/100*0.3) + (avgAssigns/10*0.2) + (sumZoom/9*0.2))

    #Output the report on screen
    print('='.center(80,'='))
    print('Student Report'.center(80,'-')) #center heading filled with -
    print(f"Full Names: {fullnames}")
    print('Phone: {0}-{1}-{2} | Email: {3}'.format(phone[:4],phone[4:7],phone[7:],email))
    print(f"Address: {mail} | City:{city} | Zipcode:{zipcode} | Country:{country}")
    print(''.center(80,'-')) #center heading filled with -
    print(f"Quizzes: {avgQuiz/100:.2%}")
    print(f"Tests: {avgTest/100:.2%}")
    print(f"Assignments: {avgAssigns/10:.2%}")
    print(f"Zoom: {sumZoom:.0f}/9")
    print("======================")
    print(f"Overall Grade: {grade:.2%}")
    print('='.center(80,'='))

    # Determine whether to award scholarship
    isScholarship = awardScholarship(isAfrica,gender.lower(),grade)
    #print(f"isAfrica:{isAfrica}, Gender:{gender}, Grade:{grade}, isScholarship:{isScholarship}")

    if isScholarship:
        print(f"CONGRATULATIONS - {(fullnames.upper())} - YOU HAVE BEEN AWARDED A SCHOLARSHIP")
    else:
         print("UNFORTUNATELY YOU HAVE NOT BEEN AWARDED A SCHOLARSHIP")

    print('='.center(80,'='))

    # ask if user would like to run program again
    runAgain = input("Would you like to run program again?[y/n]: ")
    if runAgain.lower()=='n':
        loop = False
    else:
        loop = True
        clearscreen()
    
# end while loop

print('Thank you for using the program'.center(80,'-'))