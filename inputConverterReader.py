#inputConverterReader
#Asks user to select a file
#Program takes the data and gives it to other program files to format and convert it correctly
#Finally, it will be send and stored inside a CSV file

#imports
import os
import string #holds many string related functions and constants
from transformers import GPT2Model, GPT2Tokenizer


#LMM model variables
model = GPT2Model.from_pretrained('gpt2') #loads the gpt2 model that have already been trained
tokenizer = GPT2Tokenizer.from_pretrained('gpt2') #loads gpt2 tokenizer, allowing the model to understand the input

#other varibles
textData = "" #holds the data the user puts in the input
literalStringList = [] #holds a list of the words from the input in string format
alteredStringList = [] #holds a list of the words from the input in string format but also removes punctuation
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
         
           
#splits text after each word from user input into, then stores words in list
#dose not remove punctuation
for word in textData.split():
    literalStringList.append(word)
print(literalStringList)

#removes punctuation
for word in textData.split():
    translator = word.maketrans("","",string.punctuation) #determines what is punctuation and needs to be removes
    alteredStringList.append(word.translate(translator)) #adds to list and removes punctuation for each word
print(alteredStringList)

#embedding user text input
for word in textData.split():
    #'pt' is being used, DUE NOT CHANGE unless you change the tensors being used with this program
    encodedText = tokenizer.encode(word, add_special_tokens = False, return_tensors = "pt")
    output = model(encodedText)
    
    word_embedding = output.last_hidden_state.mean(dim=1).squeeze(0)
    #"dim" specifies the deminsions along which a specific operation should be applied to
    #"squeeze" removes demensions/removes number of dimesnions from tensor
print(encodedText)


#the embeded list and the literal string lisr should both be simmeterical
#if the first value is apple in one list, the other list's first value sould be the embedded text of apple

#additionally, use another database to compare the accuracty of the emmbedding used by this program

#then the list is in another foreach loop
#with each word and corresponding embedding being added in a row in the CVS file

#user presses enter again once ready to end the program
input("Press ENTER to exit program")