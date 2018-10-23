#Spanish Practice
import random

spanishwords = []
englishwords = []
counter = 0
spanfile = open("Spanish.txt","r")
engfile = open("English.txt","r")

while counter <= 999:
    spanishwords.append(spanfile.readline())
    englishwords.append(engfile.readline())
    counter += 1

while True:
    switch = random.randint(1,2)
    ran = random.randint(0,1000)
    if switch == 1:
        answer = input(spanishwords[ran]+"In english is: ")
        if (answer+"\n") == englishwords[ran]:
            print ("correct \n")
        else:
            print ("In English is: "+englishwords[ran])
    else:
        answer = input(englishwords[ran]+"In spanish is: ")
        if (answer+"\n") == spanishwords[ran]:
            print ("correct \n")
        else:
            print ("In Spanish is: "+spanishwords[ran])
