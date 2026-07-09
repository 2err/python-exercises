from random import choice

import numpy as np

list_of_letters=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "w", "z"]
list_of_numbers=["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
list_of_signs=["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "?"]
words = [
    "apple", "house", "water", "friend", "school",
    "book", "computer", "window", "garden", "street",
    "music", "movie", "phone", "table", "chair",
    "coffee", "tea", "bread", "butter", "cheese",
    "dog", "cat", "bird", "horse", "fish",
    "tree", "flower", "river", "mountain", "forest",
    "sun", "moon", "star", "cloud", "rain",
    "snow", "wind", "fire", "earth", "sky",
    "car", "train", "plane", "bicycle", "bus",
    "city", "village", "country", "island", "beach",
    "happy", "sad", "angry", "tired", "hungry",
    "strong", "weak", "fast", "slow", "young",
    "old", "big", "small", "long", "short",
    "red", "blue", "green", "yellow", "black",
    "white", "orange", "purple", "brown", "pink",
    "run", "walk", "jump", "swim", "read",
    "write", "speak", "listen", "learn", "teach",
    "open", "close", "start", "finish", "play",
    "work", "sleep", "eat", "drink", "think",
    "dream", "smile", "laugh", "cry", "help",
    "love", "find", "make", "choose", "remember"
]


hardness=input("Czy chcesz wygenerować trudne czy łatwe hasło? Wpisz <<trudne>> lub <<łatwe>>: ")



password_list=[]

if hardness=="łatwe":
    for x in range(4):
        if x%2==0:
            sign=np.random.choice(words)
            password_list.append(sign)
        else:
            sign=np.random.choice(list_of_signs)
            password_list.append(sign)


if hardness=="trudne":
    number_of_signs = int(input("Ile znaków ma mieć hasło? "))

    for x in range(number_of_signs):
        list=np.random.randint(3)
        znak=0

        if list==0:
            znak=np.random.randint(0, len(list_of_letters)-1)
            wielkosc = np.random.randint(2)

            if wielkosc==1:
                value=list_of_letters[znak]
            else:
                value=(list_of_letters[znak]).upper()
        elif list==1:
            znak=np.random.randint(0, len(list_of_numbers)-1)
            value = list_of_numbers[znak]
        else:
            znak = np.random.randint(0, len(list_of_signs) - 1)
            value = list_of_signs[znak]

        password_list.append(value)


print("".join(password_list))

