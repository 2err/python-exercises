# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

slowo=input("Podaj słowo do sprawdzenia ")

x=len(slowo)

s=slowo[x-1::-1]

print(s)

if slowo==s:
    print("To jest palindrom")
else:
    print("To nie jest palindrom")

