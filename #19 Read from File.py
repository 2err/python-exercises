# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen. I have a .txt file for you, if you want to use it!

with open('nameslist.txt', 'r') as open_file:
    all_text = open_file.read()

imiona=all_text.split("\n")
lista_ilosc={}

for x in imiona:
    if x not in lista_ilosc:
        ilosc=imiona.count(x)
        lista_ilosc[x]=ilosc

print(lista_ilosc)



with open('Training_01.txt', 'r') as open_file:
    sun = open_file.read()

sun_list=sun.split("\n" and "/")
sun_list_new=[]
#print(sun_list)


for i in sun_list:
    if len(i)!=1 and not i.endswith("\n"):
        sun_list_new.append(i)


#print(sun_list_new)

sun_ilosc={}

for j in sun_list_new:
    if j not in sun_ilosc:
        kat=sun_list_new.count(j)
        sun_ilosc[j]=kat

print(sun_ilosc)
