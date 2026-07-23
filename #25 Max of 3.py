#Implement a function that takes as  input three variables, and returns the largest of the three. Do this without using the Python max() function!

lista=[]

for x in range(3):
    y=input("Podaj dowolną liczbę: ")
    lista.append(y)

print(lista)

z=max(lista)

print(f"Największa liczba z listy to {z}")