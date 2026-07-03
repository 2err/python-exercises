#Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.


a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b=int(input("Podaj liczbę od 1 do 100. "))

in_list=False

if b in a:
    in_list=True
else:
    in_list=False

print(in_list)