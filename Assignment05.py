# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Deborah Yenubari, February 16, 2021, Added code to complete Assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt" # An object that represents a file
dicRow = {} # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = [] # A list that acts as a 'table' of rows
strChoice = "" # A Capture the user option selection
strMenu = """
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
""" # A menu of user options

# -- Processing -- #
# Step 1 - When the program starts, load the data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
dicRow = {"TASK": "Sort Personal Files on PC", "PRIORITY": "Urgent"}
lstTable.append(dicRow)
objFile = open("ToDoList.txt", "a")
objFile.write(dicRow["TASK"] + "," + dicRow["PRIORITY"] + "\n")
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print(strMenu)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    # Step 3 - Show the current items in the table
    if strChoice.strip() == "1":
        for dicRow in lstTable:
            print(dicRow)
        continue
    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == "2":
        strTask = input("ENTER A TASK: ").strip()
        strPriority = input("ENTER ITS PRIORITY LEVEL: ").strip()
        dicRow = {"TASK": strTask, "PRIORITY": strPriority}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove an item from the list/Table based on its name
    elif strChoice.strip() == "3":
        strTask = input("ENTER A TASK TO DELETE: ").strip()
        for dicRow in lstTable:
            if dicRow["TASK"] == strTask:
                lstTable.remove(dicRow)
                print(strTask, "HAS BEEN DELETED!")
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif strChoice.strip() == "4":
        dicRow = {"TASK": strTask, "PRIORITY": strPriority}
        objFile = open("ToDoList.txt", "a")
        objFile.write(dicRow["TASK"] + "," + dicRow["PRIORITY"] + "\n")
        # lstTable.append(dicRow)
        objFile.close()
        print("DATA SAVED TO FILE!")
        continue
    # Step 7 - Exit program
    else:
        print("You have exited the program")
        break
