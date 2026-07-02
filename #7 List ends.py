#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

a = [5, 10, 15, 20, 25]
l=len(a)
new_a=[]

for x in range(l):
    if x==0:
        new_a.append(a[x])
    if x==l-1:
        new_a.append(a[x])

print(new_a)
