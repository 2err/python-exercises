#Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout the game and tell the user at the end.

import random

x=str(random.randint(1000,9999))
x_list=list(x)
print(x)

cow=0
bull=0
guesses=0
koniec=False


while koniec==False:
    y = input("Podaj liczbę czterocyfrową: ")
    guesses += 1
    for i in range(len(x_list)):
        if x==y:
            info=f"Wygrałeś! Miałeś {guesses} odpowiedzi i zebraliśmy {cow} krów i {bull} byków"
            print(info)
            with open('wygrana.txt', 'w', encoding="utf-8") as open_file:
                open_file.write(info)
            koniec=True
            break
        elif y[i] in x_list:
            if y[i] == x_list[i]:
                cow += 1
            else:
                bull+=1

    if koniec==False:
        print(f"Masz {cow} krów i {bull} byków")









