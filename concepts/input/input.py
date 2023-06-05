#!/usr/bin/python3

# Input
# Demonstrates input methods in Python
# By Nicholas Grogg

# Import statements
import sys

# Function to run program
def runProgram():
    print('Input')
    print('----------------------------------------------------')

    ## If command line variable passed, assign value to variable
    if sys.argv[1:]:
        input_value = sys.argv[1]
    ## Else prompt user for input
    else:
        input_value = str(input("Please input a number: "))

    ## Output variable
    print(input_value)

# Run main function
runProgram()
