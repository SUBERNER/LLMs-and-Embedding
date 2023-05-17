#inputConverterReader
#Asks user to select a file
#Program takes the data and gives it to other program files to format and convert it correctly
#Finally, it will be send and stored inside a CSV file

print("-Please Wait-\n")

#imports
import os
import string #holds many string related functions and constants
from transformers import GPT2Model, GPT2Tokenizer
import dataBaseManager as dbm #used for everything involving csv


#LMM model variables
model = GPT2Model.from_pretrained('gpt2') #loads the gpt2 model that have already been trained
tokenizer = GPT2Tokenizer.from_pretrained('gpt2') #loads gpt2 tokenizer, allowing the model to understand the input

#other varibles
filePath = "" #Hold the name for the CSV file
textData = "" #holds the data the user puts in the input
temporaryList= [] #temporary holds the word and embedding of that same word until put into the main wordList
wordList = [] #holds a list of all the words and their embedded format
embeddingList = [] #holds a list of the words from the input in converted embedded format
userInput = "0" #stores the input given by the user


#allow user to pick between selecting a file or typeing text directly
print("How would you like to enter the text data?")
print("Press [1] to use file")
print("Press [2] to use text input")

#used to test the input and determine if its a valid input
while(True):
    try:
        userInput = str(input()).strip()
        if (userInput == "1" or userInput == "2"):
            break
        else:
            print("\n-Enter a valid input-\n")     
    except Exception as e: 
            print(e)
    
    
#if user selected file, file exploerer will open up 
#user then selects which file they want to be uses
if (userInput == "1"):
    print("\nEnter desired file location for embedding below:")
    while(True):
        try:
            filePath = input() #stores the path to user selected file
            
            if (os.path.exists(filePath) and os.path.isfile(filePath)): #makes sure selected file exists and is a file
                with open(filePath,"r") as file:
                    textData = file.read() #gets text from file
                    break
            else:
                print("\n-Enter valid file for embedding-\n")

        except Exception as e: 
            print(e)

#if user selects textinput, user types in the text they want to be
#user then selects which file they want to be uses
elif (userInput == "2"):
    print("\nEnter desired text for embedding below:")
    while(True):
        try:
            textData = input() #sotres user inputed text
            if (textData != ""):
                break 
            else:
                print("\n-Enter text for embedding-\n")
        except Exception as e: 
            print(e)
            
#asks user for location of the CSV file 
print("\nEnter CVS file location for appending below:")
while(True):
    try:
        filePath = input() #stores the path to user selected file
        
        if (os.path.exists(filePath) and os.path.isfile(filePath)): #makes sure selected file exists and is a file
            with open(filePath,"r") as file:
                break
        else:
            print("\n-Enter a valid CSV file-\n")

    except Exception as e: 
        print(e)    
         
#splits text after each word from user input into, then stores words in list
#creates the CSV file and stores all the data inside
print("\n-Creating CSV file-")
for word in textData.split():
    #being honest, these 2 lines are duck tape
    #to make sure the CVS file organizes and appends data properly
    temporaryList.clear()
    wordList.clear()
    
    #takes word in literal string form and stores in temporary list
    translator = word.maketrans("","",string.punctuation) #determines what is punctuation and needs to be removes
    temporaryList.append(word.translate(translator))

    encodedText = tokenizer.encode(word.translate(translator), add_special_tokens = False, return_tensors = "pt")
    #converts user input to embedded format and stores in temporary list
    #'pt' is being used, DUE NOT CHANGE unless you change the tensors being used with this program
    
    output = model(encodedText)
    embeddedText = output.last_hidden_state.mean(dim = 1).squeeze(0)
    #"dim" specifies the deminsions along which a specific operation should be applied to
    #"squeeze" removes demensions/removes number of dimesnions from tensor
    
    temporaryList.append(embeddedText)
    wordList.append(temporaryList) #storing value example: [word, embedded]
    dbm.AppendData(filePath, "a", wordList) #creates the CSV file
print("-Completed CSV file-\n")


#user presses enter again once ready to end the program
input("Press ENTER to exit program")