import random, sys
list1 = ["Scissors", "Paper", "Rock", "Lizard", "Spock"]
print("Welcome to Rock-Paper-Scissors-Lizard-Spock!")
while True:
    choice = input(str("Choose Rock, Paper, Scissors, Lizard, or Spock (type 'exit' to quit):\n"))
    if(choice not in list1 and choice != "exit"): print("Invalid choice");continue
    elif(choice == "exit"): print("Thank you for playing! Goodbye!");sys.exit()
    else:
        computer_choice = random.choice(list1)
        print(f"Computer chose: {computer_choice}")
        if(choice == computer_choice): print("Its a tie!")
        else:
            answer = (list1.index(choice)+list1.index(computer_choice)+2)
            if(answer == 3 and choice == "Scissors" or answer == 4 and choice == "Rock" or answer == 8 and choice == "Spock" or answer == 9 and choice == "Lizard" or answer == 5 and choice == "Scissors" or answer == 5 and choice == "Paper" or answer == 6 and choice == "Lizard" or answer == 6 and choice == "Spock" or answer == 7 and choice == "Rock" or answer == 7 and choice == "Paper"): print(f"You Won! {choice} beats {computer_choice}.")
            else: print(f"You lost! {computer_choice} beats {choice}.")
            answer=0
    while True:
        stop_choice = input(str("Do you want to play again? (yes/no):\n"))
        if(stop_choice == "yes"): break
        elif(stop_choice == "no"): print("Thank you for playing! Goodbye!");sys.exit()
        else: print("Invalid input!")
