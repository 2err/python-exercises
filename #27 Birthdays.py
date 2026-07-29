import json
from collections import Counter
from bokeh.plotting import figure, show, output_file


output_file("urodzinki.html")

urodziny = {
	"Kacper": "13.09.2002",
	"Ewelina": "3.01.1992",
	"Bartosz": "23.10.1994",
	"Nelka": "14.09.2019"
}

miesiace = {
    "01": "Styczeń",
    "02": "Luty",
    "03": "Marzec",
    "04": "Kwiecień",
    "05": "Maj",
    "06": "Czerwiec",
    "07": "Lipiec",
    "08": "Sierpień",
    "09": "Wrzesień",
    "10": "Październik",
    "11": "Listopad",
    "12": "Grudzień"
}


with open("uro.json", "w") as f:
    json.dump(urodziny, f)


with open("uro.json", "r") as f:
    uro = json.load(f)




print("Witamy w urodzinomacie! Znamy urodziny tych osób:")

dni_osoby=uro.keys()
lista="\n".join(dni_osoby)

print(lista)



osoba=input("Czyje urodziny chcesz sprawdzić? ")
data=urodziny[osoba]

print(data)


daty=[]

d_ur=list(uro.values())

for x in d_ur:
    text = x.split(".")
    miesiac = text[1]
    miesiac_nazwa = miesiace[miesiac]
    daty.append(miesiac_nazwa)

ile_kiedy = Counter(daty)


print(d_ur)
print(ile_kiedy)


x = list(ile_kiedy.keys())
y = list(ile_kiedy.values())

p = figure(
    x_range=x,   #Bo lista miesięcy jest w formie nazw a nie liczb
    title="Liczba urodzin w poszczególnych miesiącach",
    x_axis_label="Miesiąc",
    y_axis_label="Liczba osób"
)

# create a histogram
p.vbar(x=x, top=y, width=0.5)

# render (show) the plot
show(p)



