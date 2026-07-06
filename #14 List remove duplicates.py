#Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
#Write two different functions to do this - one using a loop and constructing a list, and another using sets.


list=["Kacper", "Ewelina", "Karolina", "Bartosz", "Nelka", "Martyna", "Martyna"]

imiona=True

while imiona==True:
    name = input("Podaj imię do listy (jak chcesz przerwać to wpisz <<stop>>): ")
    if name=="stop":
        imiona=False
    else:
        list.append(name)


no_rep=[]


for x in list:
    if x not in no_rep:
        no_rep.append(x)

print(f"Imiona bez powtarzania to: {no_rep}")


seti=set(list)

print(f"Imiona bez powtarzania to: {seti}")