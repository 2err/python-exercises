#One area of confusion for new coders is the concept of functions (which have been addressed on this blog in exercise 11 for example). So in this exercise, we will be stretching our functions muscle by refactoring an existing code snippet into using functions
import datetime

def rysowanie(dlugosc, szerokosc):

    oneboard=(" ---")
    oneboard_down=("   |")

    #print(oneboard)


    board=""
    board_low="|"
    board_martix=""
    b_m_low=""
    enter="\n"

    for x in range(szerokosc):
        board+=oneboard
        board_low+=oneboard_down

    board_martix=board+enter+board_low

    for y in range(dlugosc):
        b_m_low+= enter+ board_martix


    print(b_m_low+enter+board)


def sto_lat(x):
    now = datetime.datetime.now()
    rok=now.year
    ile_do_stu=100-x
    sto=rok+ile_do_stu


    print(f"Bedziesz miał 100 lat w roku {sto}.")



dl=int(input("Podaj dlugość: "))
sz=int(input("Podaj szerokosc: "))

rysowanie(dl, sz)

urodz=int(input("Ile masz lat? "))

sto_lat(urodz)


