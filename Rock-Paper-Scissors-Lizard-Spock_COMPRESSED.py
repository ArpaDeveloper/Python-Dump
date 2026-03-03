import random as r, sys as s
l=["ROCK","SPOCK","PAPER","LIZARD","SCISSORS"];o=print;
o(f"Welcome to ROCK-PAPER-{l[4]}-{l[3]}-SPOCK!");t1="Thank you for playing! Goodbye!";t2="Invalid input!"
while 1:
    p=input(f"Choose ROCK,PAPER,{l[4]},{l[3]} or SPOCK (type 'exit' to quit):\n").upper()
    if p=="EXIT":o(t1);s.exit()
    if p not in l:o(t2);continue
    c=r.choice(l)
    o(f"Computer chose: {c}")
    if p==c:o("Its a tie!");continue
    pI=l.index(p);cI=l.index(c)
    if((cI+1)%5==pI or (cI+2)%5==pI):o(f"You Won! {p} beats {c}.")
    else:o(f"You lost! {c} beats {p}.")
    while 1:
        i=input("Do you want to play again? (Y/N):\n").upper()
        if i=="Y":break
        elif i=="N":o(t1);s.exit()
        o(t2)
