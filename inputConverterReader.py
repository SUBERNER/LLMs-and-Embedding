#inputConverterReader
#Asks user to select a file
#Program takes the data and gives it to other program files to format and convert it correctly
#Finally, it will be send and stored inside a CSV file

textData = "" #holds the data the user puts in the input
literalStringList = [] #holds a list of the words from the input in string format
embeddingList = [] #holds a list of the words from the input in converted embedded format
retry = True #determines if user needs to redo or retree a step if they make a mistake
userInput = "0" #stores the input given by the user


#allow user to pick between selecting a file or typeing text directly
print("How would you like to enter the text data?")
print("Press [1] to use file")
print("Press [2] to use textinput\n")

#used to test the input and determine if its a valid input
while (retry == True):
    try:
        userInput = str(input()).strip()
        if (userInput == "1" or userInput == "2"):
            retry = False
        else:
            print("-Enter a valid input-\n")     
    except:
        print("-ERROR: Enter a valid input-\n")

#used for now to show what user selected (wont be in final version)
if (userInput == "1"):
    print("\nUSER SELECTED FILE")
if (userInput == "2"):
    print("\nUSER SELECTED TYPING")

    
    
#if user give invalid input, repeat question

#if user selects file input
    #file exploer is opened and user selects a file to use

#if user selects typing input
    #program asks user to type the text they want to be processed. Once done the user presses enter
    #after that the text file is sent to be used
    
    
#Text data from either one is then stored inside of a variable to temperarily hold it until converted correctly

#lists are then created, one sotring the literal string format of the word
#the other list holds the converted embedded version of the text

#use a foreach loop and convert each word into a embedded version
#the loop should then add the converted text into the second list

#the embeded list and the literal string lisr should both be simmeterical
#if the first value is apple in one list, the other list's first value sould be the embedded text of apple

#additionally, use another database to compare the accuracty of the emmbedding used by this program

#then the list is in another foreach loop
#with each word and corresponding embedding being added in a row in the CVS file

#user presses enter again once ready to end the program
input("Press ENTER to exit program")

