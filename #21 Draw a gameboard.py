#Time for some fake graphics! Let’s say we want to draw  game boards that look like this:

 #--- --- ---
#|   |   |   |
 #--- --- ---
#|   |   |   |
 #--- --- ---
#|   |   |   |
 #--- --- ---

#This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for  chess, 19x19 for Go, and many more).

#Ask the user what size  game board they want to draw, and draw it for them to the screen using Python’s print statement.

oneboard=(" ---")
oneboard_down=("   |")

print(oneboard)

dlugosc=int(input("Podaj dlugość: "))
szerokosc=int(input("Podaj szerokosc: "))

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
