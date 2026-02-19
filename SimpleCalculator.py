#Let define the "UI"
ui = """
Select one of the following operations:
1) Enter integers
2) Sum
3) Subtract
4) Multiplication
5) Division
6) Power of
0) Stop
Select the function (0-5):
"""

#Variables
text=1
value1 = 0
value2 = 0

#Main func to handle choices
def main():

    while True:
#Call menu func to get choice and then depending on a choice call a func
            choice = menu()
            
            if(choice == 1):
                enter_integer(text)
                main()        
            elif(choice == 2):
                print(sum(value1, value2))
                main()       
            elif(choice == 3):
                print(subtract(value1,value2))
                main()   
            elif(choice == 4):
                print(multiplication(value1,value2))
                main()    
            elif(choice == 5):
                print(division(value1,value2))
                main()
            elif(choice == 6):
                 print(powerOf(value1,value2))
                 main()       
            elif(choice == 0):
                print("Bye.")
                break
            else:
                print("Unknown selection, try again.")
                main()
                
            return value1, value2




#menu func to print the menu and get the users choice
def menu():
    print(ui,end='')
    choice = int(input(""))
    return choice

#enter_integer func to get two integers from user
def enter_integer(text):
    global value1, value2
    value1 = int(input("Enter first integer: \n"))
    value2 = int(input("Enter second integer: \n"))
    print(f"You inputted integers {value1} and {value2}")
    return value1, value2

#func to get the integers sum
def sum(value1, value2):
    return f"Sum {value1} + {value2} = {value1+value2}"

#func to get the integers subtraction
def subtract(value1, value2):
    return f"Subtract {value1} - {value2} = {value1-value2}"

#func to get the integers multiplication
def multiplication(value1, value2):
    return f"Multiplication {value1} * {value2} = {value1*value2}"

#func to get the integers division
def division(value1, value2):
    if(value2 == 0):
        return "You cannot divide by zero."
    else:
        return f"Division {value1} / {value2} = {round(value1/value2, 2)}"

#func to get the first integer in the power of the second
def powerOf(value1, value2):
    return f"Power of {value1}**{value2}={value1**value2}"

#Call the main func to start the program     
main() 
