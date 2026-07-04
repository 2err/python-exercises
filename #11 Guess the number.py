#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)
# Keep the  game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

y="0"


while y!="exit":
    guess = "no"
    x = random.randint(1, 9)
    print(x)
    count = 0

    if y=="exit":
        break
    while guess=="no":

        y = input("Guess the number form 1 to 9? ")
        z = int(y)
        if x==z:
            count += 1
            print(f"Zgadłeś! Wykonałeś {count} prób")
            guess="yes"
        elif x>z:
            print("Twoje liczba jest zbyt niska")
            count+=1
        else:
            print("Twoja liczba jest zbyt wysoka")
            count += 1