#Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal. Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.


board=[[0,0,0],
       [0,0,0],
       [0,0,0]]

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

czy_gramy=True

while czy_gramy==True:
	for player in range(1,3):
		podaj_polozenie(player)
		for row in board:
			print(row)

# Sprawdzanie czy w poziomie są takie same
		for row in board:
			if len(set(row)) <= 1:
				if row[1] == 1:
					print("Wygrał gracz 1")
					czy_gramy = False
					break
				if row[1] == 2:
					print("Wygrał gracz 2")
					czy_gramy = False
					break

# Sprawdzenie, czy w pionie są takie same
		for i in range(3):
			pion=[]
			for row in board:
				x=row[i]
				pion.append(x)
			if len(set(pion)) <= 1:
				if pion[1] == 1:
					print("Wygrał gracz 1")
					czy_gramy = False
					break
				if pion[1] == 2:
					print("Wygrał gracz 2")
					czy_gramy = False
					break

# Sprawdzenie, czy po przekątnej są takie same:
		przekatna = []
		for i in range(3):
			x=board[i][i]
			przekatna.append(x)
		if len(set(przekatna)) <= 1:
			if przekatna[1] == 1:
				print("Wygrał gracz 1")
				czy_gramy = False
				break
			if przekatna[1] == 2:
				print("Wygrał gracz 2")
				czy_gramy = False
				break

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
				czy_gramy = False
				break
			if przekatna_2[0] == 2:
				print("Wygrał gracz 2")
				czy_gramy = False
				break

		elif not any(0 in row for row in board):
			print("Remis")
			czy_gramy=False
			break

