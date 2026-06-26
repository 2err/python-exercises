# Wiedząc, że pierwiastek n-tego stopnia z x równa się x do potęgi 1/n, oblicz wartość pierwiastka n-tego stopnia z liczby liczba.
# Jeśli operacja jest niemożliwa do wykonania pojawia się właściwy komunikat.

liczba= float(input("Podaj dowolną liczbę: "))

stopien=int(input("Podaj stopien pierwiastka: "))


if stopien==0:
    print("Nie jest możliwe przeprowadzenie tej operacji, ponieważ nie da sie dzielić przez 0")

elif stopien%2==0 and liczba<0:
    print("Nie jest możliwe przeprowadzenie tej operacji na zbiorze liczb rzeczywistych")

else:
    pierwiastek = (liczba)**(1/stopien)
    print(f"Wartość pierwiastka stopnia {stopien} z liczby {liczba} wynosi {pierwiastek}")

