#Import random and string
import random, string

#Set used in making password
LETTERS = string.ascii_letters
DIGITS = string.digits
SPECIAL = string.punctuation
COMB = LETTERS+DIGITS+SPECIAL

while True:
#Ask the user for psswd length
    psswd_length = int(input("Enter the length of the password (as a integer):\n"))
    if(psswd_length > 0):
        psswd = ""
#For as many times as psswd_length we add a random COMB to psswd 
        while psswd_length != 0:
            psswd = psswd+random.choice(COMB)
            psswd_length = psswd_length-1
#Print psswd 
        print(f"Generated password: {psswd}")
        break
#If the user has given negative number print this
    else:
        print("Password length must be a positive integer.")
