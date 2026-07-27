# In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS dictionary. Download this file and save it in the same directory as your Python code. This file is Peter Norvig’s compilation of the  dictionary of words used in professional Scrabble tournaments. Each line in the file contains a single wor

# Let’s say the word the player has to guess is “EVAPORATE”. For this exercise, write the logic that asks a player to guess a letter and displays letters in the clue word that were guessed correctly. For now, let the player guess an infinite number of times until they get the entire word. As a bonus, keep track of the letters the player guessed and display a different message if the player tries to guess that letter again. Remember to stop the game when all the letters have been guessed correctly! Don’t worry about choosing a word randomly or keeping track of the number of guesses the player has remaining - we will deal with those in a future exercise.


import random

words =[]

# Losowanie wyrazu

with open('sowpods.txt', 'r') as f:
  line = f.readline().strip()
  while line:

    words.append(line)
    #print(line)
    line = f.readline().strip()


word = random.choice(words)
print(word)

#Zgadywanie liter

guess= len(word)*"_"
guess_list=list(guess)

ilosc=0
wrong_guesses=6

while "_" in guess_list:
  if wrong_guesses==0:
    print("Przegrałeś")
    break
  else:
    litera = input("Zgadnij literkę z wyrazu: ").upper()
    #print(ilosc)

    if litera in guess_list:
      print("Ta litera już była")
    elif litera in word:
      print("Zgadza się")
      ilosc += 1
    else:
      print("To nie ta litera, spróbuj jeszcze raz")
      ilosc += 1
      wrong_guesses -=1
      print(f"Masz jeszcze {wrong_guesses} błędów")
    for i, x in enumerate(word):
      if x==litera:
        guess_list[i]=x
      else:
        continue

  guessed = "".join(guess_list)

  print(guessed)



    #print(guess)

