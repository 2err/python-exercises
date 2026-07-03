#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
#Remember the rules:
#    Rock beats  scissors
#    Scissors beats paper
#    Paper beats rock

import numpy as np


schuffle=["rock", "paper", "scissors"]


end=False

while end==False:
    a=np.random.randint(len(schuffle))
    b=np.random.randint(len(schuffle))

    a_result=schuffle[a]
    b_result=schuffle[b]

    print(f"Wynik A: {a_result}; Wynik B: {b_result}.")

    if a_result=="rock":
        if b_result=="rock":
            print("Remis, gramy dalej")
        if b_result=="paper":
            print("Wygrana B")
            end=True
        if b_result=="scissors":
            print("Wygrana A")
            end = True

    if a_result=="paper":
        if b_result=="rock":
            print("Wygrana A")
            end = True
        if b_result=="paper":
            print("Remis, gramy dalej")
        if b_result=="scissors":
            print("Wygrana B")
            end = True

    if a_result=="scissors":
        if b_result=="rock":
            print("Wygrana B")
            end = True
        if b_result=="paper":
            print("Wygrana A")
            end = True
        if b_result=="scissors":
            print("Remis, gramy dalej")


    dalej=input("Czy chcesz grać dalej? T/N ")
    if dalej=="T":
        end=False
    else:
        break



