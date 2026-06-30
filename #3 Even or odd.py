#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.


liczba=int(input("Podaj liczbe całkowitą"))
dzielnik=int(input("Przez co mam ją podzielić?"))

if liczba%4==0:
    print("Liczba jest nie tylko parzysta, ale i dzieli sie przez 4... Podwójnie parzysta, hehehe")

elif liczba%2==0:
    print("Liczba jest parzysta")

else:
    print("Liczba jest nieparzysta")

if liczba%dzielnik==0:
    print(f"Liczba {liczba} jest podzielna przez {dzielnik}")

else:
    print(f"Liczba {liczba} nie jest podzielna przez {dzielnik}")

