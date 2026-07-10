#Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.

with open('primenumbers.txt', 'r') as open_file:
    prime = open_file.read()

prime_list=prime.split("\n")

with open('happynumbers.txt', 'r') as open_file:
    happy = open_file.read()

happy_list=happy.split("\n")

prime_happy=[]

for x in prime_list:
    if x in happy_list:
        prime_happy.append(x)

print(f"Oto lista liczb pierwszych, które są szczęśliwe {prime_happy}")

