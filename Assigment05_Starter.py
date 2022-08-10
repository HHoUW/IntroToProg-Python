# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# HHo, 2022-08-07, Added code to complete assignment 5
# HiHo, 2022-08-10, Added text to tell user to enter high, medium or low for priority
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = ""   # An object that represents a file
strFile = "ToDoList.txt"   # Data storage file name
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection
lstRow = []  # A list for a row of data from the file
strYesNo = ""  # A Capture the user option for yes or no
strMsg = ""  # A msg to the user

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
objFile = open(strFile, "r")
for row in objFile:
    lstRow = row.split(",")
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == "1"):
        # TODO: Add Code Here
        print("Your current Data is: \n")
        print("TASK" + " -- " + "PRIORITY")  # print header for displaying the data
        for row in lstTable:
            print(row["Task"] + " -- " + row["Priority"])  # print each item in the list with formatting
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == "2"):
        # TODO: Add Code Here
        dicRow = {"Task": input("Enter a task: "), "Priority": input("Enter the priority of the task (high/medium/low) : ")}
        lstTable.append(dicRow)
        print("New item added to list.")
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == "3"):
        # TODO: Add Code Here
        strData = input("Item to Remove: ")
        for row in lstTable:
            if row["Task"].lower() == strData.lower():
                lstTable.remove(row)
                strMsg = "Item removed from list."
            else:
                strMsg = "Item not found."
        print(strMsg)
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == "4"):
        # TODO: Add Code Here
        objFile = open(strFile, "w")
        for row in lstTable:
            objFile.write(row["Task"] + "," + row["Priority"] + "\n")
        objFile.close()
        print("Data saved to file.")
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == "5"):
        # TODO: Add Code Here
        strOption = input("Are you sure you want to exit the program?  ('y'/'n'): ")
        if strOption == "y":
            print('\nGoodbye!')
            break  # and Exit the program
        else:
            continue
