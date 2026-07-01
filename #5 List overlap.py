#Take two lists, say for example these two: and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
#    Randomly generate two lists to test this
#    Write this in one line of Python
import numpy as np

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

a_gen=[]
b_gen=[]

c_gen=[]

d=[]

a_ilosc=np.random.randint(0,20)
b_ilosc=np.random.randint(0,20)

for ilosc in range(a_ilosc):
    wartosc=np.random.randint(0,100)
    a_gen.append(wartosc)

for ilosc in range(b_ilosc):
    wartosc=np.random.randint(0,100)
    b_gen.append(wartosc)


#W jednej linijce
for i in a:
    for j in b:
        if i==j:
            if i not in c:
                c.append(i)

print(c)


#Generowane losowo
for i in a_gen:
    for j in b_gen:
        if i==j:
            if i not in c_gen:
                c_gen.append(i)

print(c_gen)


# W jednej linijce

d=list(dict.fromkeys(x for x in a if x in b))
print(d)