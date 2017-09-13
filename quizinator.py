#!/usr/bin/python3.5

import string
import random
from os import listdir
from os.path import isfile, join


usedList = []
numCorrect = 0
numIncorrect = 0
quizDict = dict()
bank_path = "quiz_bank"
bank_files = []

def getRandomChar():
    rndChar = random.choice(string.ascii_letters.upper())
    while rndChar in usedList:
        rndChar = random.choice(string.ascii_letters.upper())
    usedList.append(rndChar)
    return rndChar

def loadFile(filename):
    # read file
    with open(filename) as f:
        for line in f:
            splitline = line.split("|")
            quizDict[splitline[0]] = splitline[1].strip()

def load_quiz_bank():
    return [f for f in listdir(bank_path) if isfile(join(bank_path, f))]

def print_results():
    print("Correct: ", numCorrect)
    print("Incorrect: ", numIncorrect)
 

###################################
#              Main               #
###################################

bank_files = load_quiz_bank()

print("Welcome to the quizinator. Below is a list of available quizes.\n")
for quiz in bank_files:
    print("\t%s" % quiz.strip('.qz'))
selected_quiz = input("\nType in the name of the quiz to run: ")
try:
    loadFile("quiz_bank/%s.qz" % selected_quiz)
except FileNotFoundError:
    print("Quiz not found.  Exiting")
    exit(1)


while len(usedList) < len(quizDict):
    rndLetter = getRandomChar()
    playerGuess = input("%s: " % rndLetter)
    if playerGuess.lower() == "quit":
        break
    elif playerGuess.lower() == quizDict[rndLetter]:
        numCorrect += 1
        print("Correct!\n")
    else:
        numIncorrect += 1
        print("Incorrect! Correct response is: %s\n" % quizDict[rndLetter])

print_results()
