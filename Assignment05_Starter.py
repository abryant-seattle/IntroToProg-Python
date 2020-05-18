# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# AlexanderBryant,5.15.2020,Added code to complete assignment 5
# AlexanderBryant,5.16.2020,Fixed file opening issues by stripping '\n' from text file
# AlexanderBryant,5.17.2020,Added counter to confirm to user task not found
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

# TODO: Add Code Here
# By opening the file for appending before reading it, it confirms the file exists and if not, creates it
# Without this line, opening to read could throw an error if the text file did not exist
activeFile = open(objFile, 'a')
activeFile.close()

# Opening the file for reading, adding any existing dictionary pairs to the task table
activeFile = open(objFile, 'r')
for row in activeFile:
    # This line strips carriage returns from the existing text file
    # Without this, errors result from empty lines within the text file if the file is opened multiple times
    row = row.strip('\n')
    # The following lines read the text file into dictionary rows and adds them to a list
    lstRow = row.split(',')
    dicRow = {'Task': lstRow[0], 'Priority': lstRow[1]}
    lstTable.append(dicRow)
# Closing the file so that it be reopened for reading or writing later
activeFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data.
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File.
    5) Exit Program.
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        # If the text file is empty and the user has not added any tasks yet, this line confirms it for the user
        if not lstTable:
            print('No tasks have been added yet.\n')
        else:
            print('Task | Priority\n')
            # This line uses a for loop to print the dictionary values
            for i in lstTable:
                print(i['Task'] + ' | ' + str(i['Priority']))
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        taskName = str(input('Task Name: ').lower())
        taskPriority = int(input('Task Priority [1-3]:  '))
        if taskPriority not in [1, 2, 3]:
            print('Invalid selection. Priority must be a 1,2, or 3. Task has not been added.')
        else:
            dicRow = {'Task': taskName, 'Priority': str(taskPriority)}
            lstTable.append(dicRow)
            print('Task "' + taskName + '" has been added.')
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        # This line confirms for the user that there are no tasks to remove
        if not lstTable:
            print('No tasks have been added yet.\n')
        else:
            removeRow = str(input('Remove which task?:  ').lower())
            # Using a counter to get around not being able to search dictionaries in lstTable by value
            counter = 0
            for i in lstTable:
                if i['Task'] == removeRow:
                    lstTable.remove(i)
                    counter += 1
                    print('Task "' + removeRow + '" has been removed.\n')
            if counter == 0:
                print('Task "' + removeRow + '" was not found\n')
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        # Confirming that the user is ready to save their tasks to the text file
        confirmInput = str(input('Save tasks to ' + objFile + '? [y or n]: '))
        if confirmInput.lower() == 'y':
            # Opening the file for overwriting, then using a for loop to write the table to the file
            # Overwriting is used instead of appending as existing contents were added to the table upon initialization
            activeFile = open(objFile, 'w')
            for i in lstTable:
                activeFile.write((i['Task'] + ',' + str(i['Priority']) + '\n'))
            activeFile.close()
            # Confirming the save was successful
            print(objFile + ' has been saved.')
        elif confirmInput.lower() == 'n':
            print('Tasks not saved')
        else:
            print('Invalid selection. Tasks have not been saved.')
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        confirmInput = str(input('Unsaved data will be lost. Exit without save? [y or n]: '))
        if confirmInput.lower() == 'y':
            break  # and Exit the program
        elif confirmInput.lower() == 'n':
            continue
        else:
            print('Invalid selection.')
            continue
