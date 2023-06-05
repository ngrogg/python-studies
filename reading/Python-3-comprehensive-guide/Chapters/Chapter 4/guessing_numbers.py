#!/usr/bin/python3

# Guessing Numbers
# By Nicholas Grogg

# Function to run program
def runProgram():
    print('Guessing Numbers')
    print('----------------------------------------------------')

    ## Initialize Variables
    secret  = 1337
    attempt = -1
    counter = 0

    while attempt != secret:
        attempt = int(input("Guess: "))

        if attempt < secret:
            print("Too Small!")

        if attempt > secret:
            print("Too Big!")

        counter += 1

    print("Great, you did it in", counter, "tries!")

# Run main function
runProgram()
