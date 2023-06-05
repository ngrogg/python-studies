#!/usr/bin/python3

# Loops
# Demonstrates for loops and while loops in Python
# By Nicholas Grogg

## Function to run program
def runProgram():
    ### Array of numbers
    numList = [1,2,3,4]

    ### Iterator object for list
    listIt  = iter(numList)

    ### Loop through list with iterator, add whitespace
    print("Using for loop")
    for i in listIt:
        print(i, end=" ")

    ### Print newline
    print("\n")

    ### Loop using while loop
    print("Using while loop")
    count   = 0
    while count < 4:
        print(numList[count])
        count += 1

## Run Program
runProgram()
