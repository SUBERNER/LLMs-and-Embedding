#dataBaseManager.py
#Class used to create and manage functions for csv files
#all current and future functions and systems working with csv should be held here for organization reasons


#imports
try:
    import csv #used to create csv files
except ImportError as e:
    print(e)

#varibles

#used when creating the csv file
def AppendData(fileName:str, fileAccessMode:str, userData:list):
    try:
        with open(fileName, fileAccessMode, newline = "") as file:
            writer = csv.writer(file)
            writer.writerows(userData)
    except Exception as e: 
        print(e)
    

