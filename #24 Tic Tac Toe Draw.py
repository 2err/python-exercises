#Draw Tic Tac Toe


board=[[0,0,0],
       [0,0,0],
       [0,0,0]]

#Rysowanie gameboardu


def draw_a_gameboard(tablica):
	szerokosc = len(tablica[0])
	oneboard = (" ---")
	linia=oneboard*szerokosc

	oneboard_down = ("   |")
	oneboard_down_x = (" x |")
	oneboard_down_o = (" o |")
	print(linia)


	for row in tablica:
		board_low = "|"

		for y in row:
			if y==0:
				board_low += oneboard_down
			elif y==1:
				board_low += oneboard_down_x
			elif y==2:
				board_low += oneboard_down_o

		print(board_low)
		print(linia)



def pytanie(x):
	pl_pio = int(input(f"Graczu {x}, podaj, w jakim miejscu chcesz postawić krzyżyk? Wiersz (1,3): "))
	pl_poz = int(input(f"Graczu {x}, podaj, w jakim miejscu chcesz postawić krzyżyk? Kolumna (1,3): "))

	return pl_pio, pl_poz

def podaj_polozenie(x):

	Player_pio, Player_poz= pytanie(x)

	if board[Player_pio-1][Player_poz-1] != 0:
		print(f"Miejsce jest zajęte. Wybierz inne")
		Player_pio, Player_poz=pytanie(x)
		board[Player_pio - 1][Player_poz - 1] = x

	else:
		board[Player_pio-1][Player_poz-1] = x


#Gra:


def gra():

	while True:

		for player in range(1,3):
			podaj_polozenie(player)
			#for row in board:
			#	print(row)
			draw_a_gameboard(board)

	# Sprawdzanie czy w poziomie są takie same
			for row in board:
				if len(set(row)) <= 1:
					if row[1] == 1:
						print("Wygrał gracz 1")
						#czy_gramy = False
						return
					if row[1] == 2:
						print("Wygrał gracz 2")
						# czy_gramy = False
						return

	# Sprawdzenie, czy w pionie są takie same
			for i in range(3):
				pion=[]
				for row in board:
					x=row[i]
					pion.append(x)
				if len(set(pion)) <= 1:
					if pion[1] == 1:
						print("Wygrał gracz 1")
						# czy_gramy = False
						return
					if pion[1] == 2:
						print("Wygrał gracz 2")
						# czy_gramy = False
						return

	# Sprawdzenie, czy po przekątnej są takie same:
			przekatna = []
			for i in range(3):
				x=board[i][i]
				przekatna.append(x)
			if len(set(przekatna)) <= 1:
				if przekatna[1] == 1:
					print("Wygrał gracz 1")
					# czy_gramy = False
					return
				if przekatna[1] == 2:
					print("Wygrał gracz 2")
					# czy_gramy = False
					return

			przekatna_2 = []
			for j in range(3):
				i=0
				if j==0:
					i=2
				elif j==1:
					i=1
				elif j==2:
					i=0
				x=board[j][i]
				przekatna_2.append(x)
			if len(set(przekatna_2)) <= 1:
				if przekatna_2[0] == 1:
					print("Wygrał gracz 1")
					# czy_gramy = False
					return
				if przekatna_2[0] == 2:
					print("Wygrał gracz 2")
					# czy_gramy = False
					return

			elif not any(0 in row for row in board):
				print("Remis")
				# czy_gramy = False
				return





while True:
		board = [[0, 0, 0],
				 [0, 0, 0],
				 [0, 0, 0]]

		gra()

		gramy=input("Czy chcesz grać dalej? T/N:")

		if gramy!="T":
			break


