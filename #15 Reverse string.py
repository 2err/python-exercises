#Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string


zdanie=input("Podaj zdanie do odwrócenia: ")

wyrazy=zdanie.split(" ")
odwrocone=[]

print(len(wyrazy))

for x in reversed(range(len(wyrazy))):
    odwrocone.append(wyrazy[x])

result=" ".join(odwrocone)
print(result)