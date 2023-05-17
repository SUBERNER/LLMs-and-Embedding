#csvManager
#Class used to create and manage functions for csv files
#all current and future functions and systems working with csv should be held here for organization reasons


#imports
import csv #used to create csv files


#varibles


#used when creating the csv file
def AppendData(fileName:str, fileAccessMode:str, userData:list):
    try:
        with open(fileName, fileAccessMode, newline = "") as file:
            writer = csv.writer(file)
            writer.writerows(userData)
    except Exception as e: 
        print(e)
        