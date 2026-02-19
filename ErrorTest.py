#Imports
import sys
import math

ui = """What do you want to do:
1) Test for ValueError
2) Test for IndexError
3) Test for ZeroDivisionError
4) Test for TypeError
0) Stop
"""


def main():
    choice = menu()

    if(choice == 1):
        valueError()
    elif(choice == 2):
        indexError()
    elif(choice == 3):
        zeroDivisionError()
    elif(choice == 4):
        typeError()
    elif(choice == 0):
        print("See you again!")
        sys.exit()
    else:
        print("Unknown selection, please try again.")
        main()


def menu():
    print(ui, end="")
    while True:
        try:
            choice = int(input("Your choice:\n"))
            break
        except ValueError:
            print("ValueError happened. Enter the selection as an integer.")
        
   
    return choice

def valueError():
    integer = int(input("Give a non-negative integer: \n"))
    try:
        squared = math.sqrt(integer)
        print(f"Square root of {integer} is {round(squared,2)}.")
    except ValueError:
        print("ValueError happened. Non-negative number expected for square root.")
    main()


def indexError():
    indexNumber = int(input("Input index 0-4: \n"))
    list2 = [11, 22, 33, 44, 55]
    try:
        print(f"List value is {list2[indexNumber]} at index {indexNumber}.")
    except IndexError:
        print(f"Got an IndexError with index {indexNumber}.")
    main()
        
def zeroDivisionError():
    number = 4
    divider = int(input("Enter divider: \n"))
    try:
        result = number/divider
        print(f"{number}/{divider} = {round(result,2)}.")
    except ZeroDivisionError:
        print("ZeroDivisionError occurred, divider 0.")
    main()
    
def typeError():
    try:
        typeNumber = int(input("Enter number:\n"))
    except:
        typeNumber = "Maroon 5"
    try:
        test = typeNumber*typeNumber
    except TypeError:
        print("Got TypeError. Two strings cannot be multiplied together.")
    main()

main()
