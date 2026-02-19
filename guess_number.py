#Import random
import random

#Set the range of numbers to guess
list1 = range(1,100)


def guess_number():
#random number to guess
    number_to_guess = random.choice(list1)
    guess_amount = 0

    while True:
#Ask user to guess
        guess = int(input("Guess number 0-100\n"))
#If you guess it right end the loop
        if(guess == number_to_guess):
            print("You guessed it!")
            guess_amount+=1
            break
#If your guess was higher print lower
        elif(guess > number_to_guess):
            print("Lower")
            guess_amount+=1
#If your guess was lower print higher
        elif(guess < number_to_guess):
            print("Higher")
            guess_amount+=1
            
#Last print the random number
    print(f"The number was {number_to_guess}")
    print(f"You guessed {guess_amount} times")


#Call the func
guess_number()
