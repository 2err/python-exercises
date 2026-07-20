#You, the user, will have in your head a number between 0 and 100. The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
#At the end of this exchange, your program should print out how many guesses it took to get your number.
#As the writer of this program, you will have to choose how your program will strategically guess. A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number. But that’s not an optimal guessing strategy. An alternate strategy might be to guess 50 (right in the middle of the range), and then increase / decrease by 1 as needed. After you’ve written the program, try to find the optimal strategy! (We’ll talk about what is the optimal one next week with the solution.)

import random



game=True

print("Pomyśl numer od 0 do 100, a ja postaram się go odgadnąć!")
x = random.randint(0, 100)
guess=0
wrong_guesses_much=[]
wrong_guesses_less=[]

x_min = 0
x_max = 100


while game==True:

    #if x in wrong_guesses:
    #    continue


    is_it=input(f"Czy ta liczba to {x}? tak, za mało, za dużo? ")
    if is_it=="tak":
        guess+=1
        print(f"Odpowiedziałem poprawnie po {guess} odpowiedziach!")
        game=False

    elif is_it=="za dużo":
        wrong_guesses_much.append(x)
        x_max=min(wrong_guesses_much)
        x=random.randint(x_min+1,x_max-1)

        guess+=1


    elif is_it=="za mało":
        wrong_guesses_less.append(x)
        x_min = max(wrong_guesses_less)
        x=random.randint(x_min+1,x_max-1)

        guess+=1

    else:
        continue

    #print(x_min)
    #print(x_max)













