# Introduction to Python 2021 Training
# Assignment 8 - Sheng Translator
# Written by Paula Musuva
# Date: 15 May 2021

import os
import json
import requests #! pip install requests
import pickle

# Set filename
filename = 'sheng'

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

# Function to load data
def loadData():
    # Get data from the internet
    datauri = 'https://raw.githubusercontent.com/normansimonr/Dumb-Cogs/master/lolz/data/tranzlashun.json'
    resp = requests.get(datauri)

    # Load to a dictionary object
    dictionary = json.loads(resp.text)

    # Add Sheng words to dictionary
    shengDict = {
        'hi': 'niaje',
        'nairobi': 'kanairo',
        'two': 'Mbwegze',
        'ordinary': 'odi',
        'sausage': 'mutura',
        'pay': 'kanja',
        'morning': 'ngware',
        'work': 'mboka',
        'home': 'keja',
        'police': 'senke',
        'die': 'bugda',
        'friend': 'arif',
        'mother': 'mroko',
        'father': 'zing'
    }
    dictionary.update(shengDict)
    #print(dictionary)

    # Store to a binary file i.e. Pickle
    with open(filename,'wb') as outfile:
        pickle.dump(dictionary,outfile)
# End loadData()

# START MAIN PROGRAM
# Load data
loadData()

# Set program to loop
loop = True

while loop:
    # Welcome message
    print('='.center(40,'='))
    print("Welcome to the Sheng translator program")
    print('='.center(40,'='))

    # User interaction
    word = input('Input English word to translate to Sheng: ').lower()

    # Read and write back to binary file i.e. Unpickle 
    if (os.path.exists(filename)):
        with open(filename, 'rb') as infile:
            fileContent = pickle.load(infile)
            if word in fileContent:
                print ('The translation is: ', fileContent[word])
            else:
                print ('Sorry, that word has no translation in the dictionary')
    else:
        print ('Sorry could not load sheng dictionary')
    
    # Ask if user would like to run program again
    runAgain = input("Would you like to run program again?[y/n]: ")
    if runAgain.lower()=='n':
        loop = False
    else:
        loop = True
        clearscreen()
# END MAIN PROGRAM